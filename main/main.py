# coding: utf-8

import logging

from flask.ext import wtf
import flask
import wtforms

import config
import util

app = flask.Flask(__name__)
app.config.from_object(config)
app.jinja_env.line_statement_prefix = '#'
app.jinja_env.line_comment_prefix = '##'
app.jinja_env.add_extension('jinja2_markdown.MarkdownExtension')
app.jinja_env.markdowner.set_output_format('html5')
app.jinja_env.globals.update(
    check_form_fields=util.check_form_fields,
    is_iterable=util.is_iterable,
    slugify=util.slugify,
    update_query_argument=util.update_query_argument,
  )

import user
import admin
import auth
import model
import profile
import task

if config.DEVELOPMENT:
  from werkzeug import debug
  app.wsgi_app = debug.DebuggedApplication(app.wsgi_app, evalex=True)
  app.testing = True


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
# Feedback
###############################################################################
class FeedbackForm(wtf.Form):
  message = wtforms.TextAreaField(
      'Message',
      [wtforms.validators.required()], filters=[util.strip_filter],
    )
  email = wtforms.StringField(
      'Your email (optional)',
      [wtforms.validators.optional(), wtforms.validators.email()],
      filters=[util.email_filter],
    )
  recaptcha = wtf.RecaptchaField('Are you human?')


@app.route('/feedback/', methods=['GET', 'POST'])
def feedback():
  if not config.CONFIG_DB.feedback_email:
    return flask.abort(418)

  form = FeedbackForm(obj=auth.current_user_db())
  if not config.CONFIG_DB.has_anonymous_recaptcha or auth.is_logged_in():
    del form.recaptcha
  if form.validate_on_submit():
    body = '%s\n\n%s' % (form.message.data, form.email.data)
    kwargs = {'reply_to': form.email.data} if form.email.data else {}
    task.send_mail_notification('%s...' % body[:48].strip(), body, **kwargs)
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
