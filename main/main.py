# -*- coding: utf-8 -*-

from google.appengine.api import mail
from flaskext import wtf
import flask
import config
import model
import util

app = flask.Flask(__name__)
app.config.from_object(config)
app.jinja_env.line_statement_prefix = '#'
app.jinja_env.line_comment_prefix = '##'
app.jinja_env.globals.update(slugify=util.slugify)

import auth
import admin


################################################################################
# Main page
################################################################################
@app.route('/')
def welcome():
  return flask.render_template('welcome.html', html_class='welcome')


################################################################################
# Sitemap stuff
################################################################################
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


@app.route('/example/')
def example():
  return flask.render_template(
      'example/example.html',
      html_class='example',
      title='Examples',
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
      'coming_soon.html',
      html_class='guide',
      title="Developer's Guide",
    )


@app.route('/features/')
def features():
  return flask.render_template(
      'doc/features.html',
      html_class='features',
      title='Features',
    )


@app.route('/reference/')
def reference():
  return flask.render_template(
      'reference/reference.html',
      html_class='reference',
      title='Reference',
    )


@app.route('/tutorial/')
def tutorial():
  return flask.render_template(
      'coming_soon.html',
      html_class='tutorial',
      title='Tutorial',
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


################################################################################
# Profile stuff
################################################################################
class ProfileUpdateForm(wtf.Form):
  name = wtf.TextField('Name',
      [wtf.validators.required()], filters=[util.strip_filter],
    )
  email = wtf.TextField('Email',
      [wtf.validators.optional(), wtf.validators.email()],
      filters=[util.strip_filter],
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
      title='Profile',
      html_class='profile',
      form=form,
      user_db=user_db,
    )


################################################################################
# Feedback
################################################################################
class FeedbackForm(wtf.Form):
  subject = wtf.TextField('Subject',
      [wtf.validators.required()], filters=[util.strip_filter],
    )
  message = wtf.TextAreaField('Message',
      [wtf.validators.required()], filters=[util.strip_filter],
    )
  email = wtf.TextField('Email (optional)',
      [wtf.validators.optional(), wtf.validators.email()],
      filters=[util.strip_filter],
    )


@app.route('/feedback/', methods=['GET', 'POST'])
def feedback():
  if not config.CONFIG_DB.feedback_email:
    return flask.abort(418)

  form = FeedbackForm()
  if form.validate_on_submit():
    mail.send_mail(
        sender=config.CONFIG_DB.feedback_email,
        to=config.CONFIG_DB.feedback_email,
        subject='[%s] %s' % (
            config.CONFIG_DB.brand_name,
            form.subject.data,
          ),
        reply_to=form.email.data or config.CONFIG_DB.feedback_email,
        body='%s\n\n%s' % (form.message.data, form.email.data)
      )
    flask.flash('Thank you for your feedback!', category='success')
    return flask.redirect(flask.url_for('welcome'))
  if not form.errors and auth.current_user_id() > 0:
    form.email.data = auth.current_user_db().email

  return flask.render_template(
      'feedback.html',
      title='Feedback',
      html_class='feedback',
      form=form,
    )


################################################################################
# User Stuff
################################################################################
@app.route('/_s/user/', endpoint='user_list_service')
@app.route('/user/')
def user_list():
  user_dbs, more_cursor = util.retrieve_dbs(
      model.User.query(),
      limit=util.param('limit', int),
      cursor=util.param('cursor'),
      order=util.param('order') or '-created',
      name=util.param('name'),
      admin=util.param('admin', bool),
    )

  if flask.request.path.startswith('/_s/'):
    return util.jsonify_model_dbs(user_dbs, more_cursor)

  return flask.render_template(
      'user_list.html',
      html_class='user',
      title='User List',
      user_dbs=user_dbs,
      more_url=util.generate_more_url(more_cursor),
    )


################################################################################
# Error Handling
################################################################################
@app.errorhandler(400)  # Bad Request
@app.errorhandler(401)  # Unauthorized
@app.errorhandler(403)  # Forbidden
@app.errorhandler(404)  # Not Found
@app.errorhandler(405)  # Method Not Allowed
@app.errorhandler(410)  # Gone
@app.errorhandler(418)  # I'm a Teapot
@app.errorhandler(500)  # Internal Server Error
def error_handler(e):
  try:
    e.code
  except:
    class e(object):
      code = 500
      name = 'Internal Server Error'

  if flask.request.path.startswith('/_s/'):
    return util.jsonpify({
        'status': 'error',
        'error_code': e.code,
        'error_name': e.name.lower().replace(' ', '_'),
        'error_message': e.name,
      }), e.code

  return flask.render_template(
      'error.html',
      title='Error %d (%s)!!1' % (e.code, e.name),
      html_class='error-page',
      error=e,
    ), e.code
