# coding: utf-8

import logging

from flask.ext import wtf
import flask

import config
import util

app = flask.Flask(__name__)
app.config.from_object(config)
app.jinja_env.line_statement_prefix = '#'
app.jinja_env.line_comment_prefix = '##'
app.jinja_env.globals.update(slugify=util.slugify)
app.jinja_env.globals.update(update_query_argument=util.update_query_argument)
app.jinja_env.add_extension('jinja2_markdown.MarkdownExtension')
app.jinja_env.markdowner.set_output_format('html5')


import admin
import auth
import task
import user
import model


if config.DEVELOPMENT:
  from werkzeug import debug
  app.wsgi_app = debug.DebuggedApplication(app.wsgi_app, evalex=True)


###############################################################################
# Main page
###############################################################################
@app.route('/')
def welcome():
  return flask.render_template('welcome.html', html_class='welcome')


###############################################################################
# Sitemap stuff
###############################################################################
@app.route('/sitemap.xml')
def sitemap():
  response = flask.make_response(flask.render_template(
      'sitemap.xml',
      host_url=flask.request.host_url[:-1],
      lastmod=config.CURRENT_VERSION_DATE.strftime('%Y-%m-%d'),
    ))
  response.headers['Content-Type'] = 'application/xml'
  return response


@app.route('/what/')
def what():
  return flask.render_template(
      'doc/what.html',
      html_class='what',
      title='What is gae-init?',
    )


@app.route('/tree/')
def tree():
  return flask.render_template(
      'tree/tree.html',
      html_class='tree',
      title='Source Tree',
    )


@app.route('/source/')
def source():
  return flask.render_template(
      'coming_soon.html',
      html_class='source',
      title='Source Code',
    )


@app.route('/run/')
def run():
  return flask.render_template(
      'run.html',
      html_class='run',
      title='Run script',
    )


@app.route('/requirement/')
def requirement():
  return flask.render_template(
      'requirement/requirement.html',
      html_class='requirement',
      title='Requirements',
    )


@app.route('/guide/')
def guide():
  return flask.render_template(
      'guide/guide.html',
      html_class='guide',
      title="Guide",
    )


@app.route('/features/')
def features():
  return flask.render_template(
      'feature/feature.html',
      html_class='features',
      title='Features',
    )


@app.route('/reference/')
def reference():
  return flask.render_template(
      'reference/reference.html',
      html_class='reference',
      title='API Reference',
    )


@app.route('/tutorial/')
def tutorial():
  return flask.render_template(
      'tutorial/tutorial.html',
      html_class='tutorial',
      title='Tutorial',
    )


@app.route('/convention/')
def convention():
  return flask.render_template(
      'convention/convention.html',
      html_class='convention',
      title='Code Conventions',
    )


@app.route('/faq/')
def faq():
  return flask.render_template(
      'faq/faq.html',
      html_class='faq',
      title='FAQ',
    )


@app.route('/contact/')
def contact():
  return flask.render_template(
      'coming_soon.html',
      html_class='contact',
      title='Contact',
    )


###############################################################################
# Profile stuff
###############################################################################
class ProfileUpdateForm(wtf.Form):
  name = wtf.StringField('Name',
      [wtf.validators.required()], filters=[util.strip_filter],
    )
  email = wtf.StringField('Email',
      [wtf.validators.optional(), wtf.validators.email()],
      filters=[util.email_filter],
    )


@app.route('/_s/profile/', endpoint='profile_service')
@app.route('/profile/', methods=['GET', 'POST'])
@auth.login_required
def profile():
  user_db = auth.current_user_db()
  form = ProfileUpdateForm(obj=user_db)

  if form.validate_on_submit():
    form.populate_obj(user_db)
    user_db.put()
    return flask.redirect(flask.url_for('welcome'))

  if flask.request.path.startswith('/_s/'):
    return util.jsonify_model_db(user_db)

  return flask.render_template(
      'profile.html',
      title=user_db.name,
      html_class='profile',
      form=form,
      user_db=user_db,
      has_json=True,
    )


###############################################################################
# Feedback
###############################################################################
class FeedbackForm(wtf.Form):
  subject = wtf.StringField('Subject',
      [wtf.validators.required()], filters=[util.strip_filter],
    )
  message = wtf.TextAreaField('Message',
      [wtf.validators.required()], filters=[util.strip_filter],
    )
  email = wtf.StringField('Email (optional)',
      [wtf.validators.optional(), wtf.validators.email()],
      filters=[util.email_filter],
    )


@app.route('/feedback/', methods=['GET', 'POST'])
def feedback():
  if not config.CONFIG_DB.feedback_email:
    return flask.abort(418)

  form = FeedbackForm(obj=auth.current_user_db())
  if form.validate_on_submit():
    body = '%s\n\n%s' % (form.message.data, form.email.data)
    kwargs = {'reply_to': form.email.data} if form.email.data else {}
    task.send_mail_notification(form.subject.data, body, **kwargs)
    flask.flash('Thank you for your feedback!', category='success')
    return flask.redirect(flask.url_for('welcome'))

  return flask.render_template(
      'feedback.html',
      title='Feedback',
      html_class='feedback',
      form=form,
    )


###############################################################################
# Warmup request
###############################################################################
@app.route('/_ah/warmup')
def warmup():
  # TODO: put your warmup code here
  return 'success'


###############################################################################
# Error Handling
###############################################################################
@app.errorhandler(400)  # Bad Request
@app.errorhandler(401)  # Unauthorized
@app.errorhandler(403)  # Forbidden
@app.errorhandler(404)  # Not Found
@app.errorhandler(405)  # Method Not Allowed
@app.errorhandler(410)  # Gone
@app.errorhandler(418)  # I'm a Teapot
@app.errorhandler(500)  # Internal Server Error
def error_handler(e):
  logging.exception(e)
  try:
    e.code
  except AttributeError:
    e.code = 500
    e.name = 'Internal Server Error'

  if flask.request.path.startswith('/_s/'):
    return util.jsonpify({
        'status': 'error',
        'error_code': e.code,
        'error_name': util.slugify(e.name),
        'error_message': e.name,
        'error_class': e.__class__.__name__,
      }), e.code

  return flask.render_template(
      'error.html',
      title='Error %d (%s)!!1' % (e.code, e.name),
      html_class='error-page',
      error=e,
    ), e.code


if config.PRODUCTION:
  @app.errorhandler(Exception)
  def production_error_handler(e):
    return error_handler(e)
