# coding: utf-8

import flask

from main import app


###############################################################################
# Redirects
###############################################################################
@app.route('/guide/')
def guide():
  return flask.redirect(flask.url_for('howto'))


###############################################################################
# Main pages
###############################################################################
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


@app.route('/quickstart/')
def quickstart():
  return flask.render_template(
    'quickstart/quickstart.html',
    html_class='quickstart',
    title='Quickstart',
  )


@app.route('/howto/')
def howto():
  return flask.render_template(
    'howto/howto.html',
    html_class='howto',
    title='How To',
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
