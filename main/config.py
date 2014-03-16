# -*- coding: utf-8 -*-

import os

try:
  # This part is surrounded in try/except because the config.py file is
  # also used in the run.py script which is used to compile/minify the client
  # side files (*.less, *.coffee, *.js) and is not aware of the GAE
  from datetime import datetime
  from google.appengine.api import app_identity
  import model

  CONFIG_DB = model.Config.get_master_db()
  SECRET_KEY = CONFIG_DB.flask_secret_key.encode('ascii')
  CURRENT_VERSION_ID = os.environ.get('CURRENT_VERSION_ID')
  CURRENT_VERSION_NAME = CURRENT_VERSION_ID.split('.')[0]
  CURRENT_VERSION_TIMESTAMP = long(CURRENT_VERSION_ID.split('.')[1]) >> 28
  CURRENT_VERSION_DATE = datetime.fromtimestamp(CURRENT_VERSION_TIMESTAMP)
  APPLICATION_ID = app_identity.get_application_id()
except:
  pass

PRODUCTION = os.environ.get('SERVER_SOFTWARE', '').startswith('Google App Eng')
DEVELOPMENT = not PRODUCTION
DEBUG = DEVELOPMENT

DEFAULT_DB_LIMIT = 64

################################################################################
# SITE
################################################################################
REQUIREMENT = [
    ('gae', 'Google App Engine', 'Required'),
    ('nodejs', 'node.js', 'Required'),
  ]

REFERENCE = [
    ('util', 'Utilities', 'util.py'),
    ('task', 'Tasks', 'task.py'),
    ('auth', 'User related', 'auth.py'),
    ('decorator', 'Decorators', 'auth.py'),
    ('config', 'Config', 'config.py'),
    ('utils', 'Utilities (HTML)', 'utils.html'),
    ('forms', 'Forms (HTML)', 'forms.html'),
  ]

REFERENCE_DEF = {
    'util': [
        ('param.md.md', '(name, cast=None)'),
        ('get_next_url.md', '()'),
        ('retrieve_dbs.md', '(query, order=None, limit=None, cursor=None, keys_only=None, **filters)'),
        ('jsonify_model_dbs.md', '(model_dbs, more_cursor=None)'),
        ('jsonify_model_db.md', '(model_db)'),
        ('model_db_to_object.md', '(model_db)'),
        ('json_value.md', '(value)'),
        ('jsonpify.md', '(*args, **kwargs)'),
        ('generate_more_url.md', '(more_cursor, base_url=None)'),
        ('uuid.md', '()'),
        ('slugify.md', '(text)'),
        ('is_valid_username.md', '(username)'),
        ('update_query_argument.md', '(name, value=None, ignore=[])'),
        ('strip_filter.md', '()'),
        ('email_filter.md', '()'),
      ],
    'task': [
        ('send_mail_notification.md', '(subject, body, **kwargs)'),
        ('new_user_notification.md', '(user_db)'),
      ],
    'auth': [
        ('current_user_id.md', '()'),
        ('current_user_key.md', '()'),
        ('current_user_db.md', '()'),
        ('is_logged_in.md', '()'),
      ],
    'decorator': [
        ('login_required.md', ''),
        ('admin_required.md', ''),
        ('permission_required.md', '(permission=None, methods=None)')
      ],
    'config': [
        ('config_db.md', ''),
        ('secret_key.md', ''),
        ('current_version_id.md', ''),
        ('current_version_name.md', ''),
        ('current_version_timestamp.md', ''),
        ('current_version_date.md', ''),
        ('application_id.md', ''),
        ('development.md', ''),
        ('production.md', ''),
        ('debug.md', ''),
        ('default_db_limit.md', ''),
        ('styles.md', ''),
        ('scripts.md', ''),
      ],
    'utils': [
        ('order_by_link', "(property, title, ignore=['cursor'])"),
        ('filter_by_link', "(property, value, icon=None, ignore=['cursor'])"),
        ('next_link', "(more_url, caption='Next Page')"),
        ('prefetch_link', '(url)'),
        ('auth_icon', '(auth_id)'),
        ('auth_icons', '(auth_ids)'),
        ('html_element', '(name, content)'),
      ],
    'forms': [
        ('field_errors.md', '(field)'),
        ('field_description.md', '(field)'),
        ('input_field.md', "(field, type='text')"),
        ('text_field.md', '(field)'),
        ('password_field.md', '(field)'),
        ('number_field.md', '(field)'),
        ('date_field.md', '(field)'),
        ('email_field.md', '(field)'),
        ('select_field.md', '(field)'),
        ('hidden_field.md', '(field)'),
        ('textarea_field.md', '(field, rows=4)'),
        ('checkbox_field.md', '(field)'),
        ('multiple_checkbox_field.md', '(field)'),
        ('oauth_fields.md', '(name, fields, checkmark, help)'),
      ],
  }

TUTORIAL = [
    ('introduction', 'Introduction'),
    ('code', 'Get the code'),
    ('run', 'Run the application'),
    ('model', 'Modify the model'),
    ('create', 'Add contacts'),
    ('list', 'List contacts'),
    ('view', 'View contacts'),
    ('update', 'Update contacts'),
#    ('delete', 'Deleting contacts'),
#    ('theme', 'Change theme'),
    ('deploy', 'Deploy'),
  ]

CONVENTION = [
    ('global', 'Global'),
    ('python', 'Python'),
    ('html', 'HTML'),
    ('less', 'LESS'),
    ('coffee', 'CoffeeScript'),
  ]

###############################################################################
# Client modules, also used by the run.py script.
###############################################################################
STYLES = [
    'src/style/style.less',
  ]

SCRIPTS = [
    ('libs', [
        'ext/js/jquery/jquery.js',
        'ext/js/momentjs/moment.js',
        'ext/js/nprogress/nprogress.js',
        'ext/js/bootstrap/alert.js',
        'ext/js/bootstrap/button.js',
        'ext/js/bootstrap/transition.js',
        'ext/js/bootstrap/collapse.js',
        'ext/js/bootstrap/dropdown.js',
        'ext/js/bootstrap/tooltip.js',
        'ext/js/bootstrap/affix.js',
        'ext/js/bootstrap/popover.js',
        'src/lib/prettify.js',
      ]),
    ('scripts', [
        'src/script/common/service.coffee',
        'src/script/common/util.coffee',
        'src/script/site/app.coffee',
        'src/script/site/admin.coffee',
        'src/script/site/profile.coffee',
        'src/script/site/user.coffee',
        'src/script/site/main.coffee',
        'src/script/site/tree.coffee',
      ]),
  ]
