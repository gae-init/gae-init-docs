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
    ('auth', 'User related', 'auth.py'),
    ('decorator', 'Decorators', 'auth.py'),
    ('config', 'Config', 'config.py'),
    ('utils', 'Utilities (HTML)', 'utils.html'),
    ('forms', 'Forms (HTML)', 'forms.html'),
  ]

REFERENCE_DEF = {
    'util': [
        ('param', '(name, cast=None)'),
        ('get_next_url', '()'),
        ('retrieve_dbs', '(query, order=None, limit=None, cursor=None, keys_only=None, **filters)'),
        ('jsonify_model_dbs', '(model_dbs, more_cursor=None)'),
        ('jsonify_model_db', '(model_db)'),
        ('model_db_to_object', '(model_db)'),
        ('json_value', '(value)'),
        ('jsonpify', '(*args, **kwargs)'),
        ('generate_more_url', '(more_cursor, base_url=None)'),
        ('uuid', '()'),
        ('slugify', '(text)'),
        ('is_valid_username', '(username)'),
        ('update_query_argument', '(name, value=None, ignore=[])'),
        ('strip_filter', '()'),
        ('email_filter', '()'),
      ],
    'auth': [
        ('current_user_id', '()'),
        ('current_user_key', '()'),
        ('current_user_db', '()'),
        ('is_logged_in', '()'),
      ],
    'decorator': [
        ('login_required', ''),
        ('admin_required', ''),
        ('permission_required', '(permission=None)')
      ],
    'config': [
        ('config_db', ''),
        ('secret_key', ''),
        ('current_version_id', ''),
        ('current_version_name', ''),
        ('current_version_timestamp', ''),
        ('current_version_date', ''),
        ('application_id', ''),
        ('development', ''),
        ('production', ''),
        ('debug', ''),
        ('default_db_limit', ''),
        ('styles', ''),
        ('scripts', ''),
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
        ('field_errors', '(field)'),
        ('field_description', '(field)'),
        ('input_field', "(field, type='text')"),
        ('text_field', '(field)'),
        ('password_field', '(field)'),
        ('number_field', '(field)'),
        ('date_field', '(field)'),
        ('email_field', '(field)'),
        ('select_field', '(field)'),
        ('hidden_field', '(field)'),
        ('textarea_field', '(field, rows=4)'),
        ('checkbox_field', '(field)'),
        ('multiple_checkbox_field', '(field)'),
        ('oauth_fields', '(name, fields, checkmark, help)'),
      ],
  }

TUTORIAL = [
    ('introduction.md', 'Introduction'),
    ('code.md', 'Get the code'),
    ('run.md', 'Run the application'),
    ('model.md', 'Modify the model'),
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
