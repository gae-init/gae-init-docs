# -*- coding: utf-8 -*-

import os
try:
  # This part is surrounded in try/except because the this config.py file is
  # also used in the run.py script which is used to compile/minify the client
  # side files (*.less, *.coffee, *.js) and is not aware of the GAE
  import model
  from datetime import datetime
  CONFIG_DB = model.Config.get_master_db()
  SECRET_KEY = CONFIG_DB.flask_secret_key.encode('ascii')
  CURRENT_VERSION_ID = os.environ.get('CURRENT_VERSION_ID')
  CURRENT_VERSION_NAME = CURRENT_VERSION_ID.split('.')[0]
  CURRENT_VERSION_TIMESTAMP = long(CURRENT_VERSION_ID.split('.')[1]) >> 28
  CURRENT_VERSION_DATE = datetime.fromtimestamp(CURRENT_VERSION_TIMESTAMP)
except:
  pass

PRODUCTION = os.environ.get('SERVER_SOFTWARE', '').startswith('Google App Engine')
DEVELOPMENT = not PRODUCTION
DEBUG = DEVELOPMENT

DEFAULT_DB_LIMIT = 64

################################################################################
# SITE
################################################################################
REQUIREMENT = [
  ('gae', 'Google App Engine', 'Required'),
  ('nodejs', 'node.js', 'Required'),
  ('sublime', 'Sublime', 'Optional'),
]

REFERENCE = [
  ('util', 'Utilities', 'util.py'),
  ('auth', 'User related', 'auth.py'),
  ('decorator', 'Decorators', 'auth.py'),
  ('config', 'Config', 'config.py'),
]

REFERENCE_DEF = {
    'util': [
        ('param', 'name, cast=None'),
        ('get_next_url', ''),
        ('retrieve_dbs', 'query, order=None, limit=None, cursor=None, **filters'),
        ('jsonify_model_dbs', 'model_dbs, more_cursor=None'),
        ('jsonify_model_db', 'model_db'),
        ('model_db_to_object', 'model_db'),
        ('json_value', 'value'),
        ('generate_more_url', 'more_cursor, base_url=None'),
        ('uuid', ''),
        ('format_datetime_utc', 'timestamp'),
        ('format_datetime_ago', 'timestamp'),
      ],
    'auth': [
        ('current_user_id', ''),
        ('current_user_key', ''),
        ('current_user_db', ''),
        ('is_logged_in', ''),
      ],
    'decorator': [
        ('login_required', ''),
        ('admin_required', ''),
      ],
    'config': [
        ('config_db', ''),
        ('secret_key', ''),
        ('current_version_id', ''),
        ('development', ''),
        ('production', ''),
        ('debug', ''),
        ('default_db_limit', ''),
        ('styles', ''),
        ('scripts_modules', ''),
        ('scripts', ''),
      ],
  }

TUTORIAL = [
  ('introduction', 'Introduction'),
  ('code', 'Getting the code'),
  ('compile', 'Compile the files'),
  ('run', 'Run the application'),
  ('model', 'Modifying the model'),
  ('create', 'Adding contacts'),
  ('list', 'Listing contacts'),
  ('view', 'Viewing contacts'),
  ('update', 'Updating contacts'),
  ('delete', 'Deleting contacts'),
  ('theme', 'Changing theme'),
  ('deploy', 'Deploy!!!'),
]

################################################################################
# Client modules, also used by the run.py script.
################################################################################
STYLES = [
    'src/style/style.less',
  ]

SCRIPTS_MODULES = [
    'libs',
    'scripts',
  ]

SCRIPTS = {
    'libs': [
        'src/lib/jquery.js',
        'src/lib/nprogress.js',
        'src/lib/moment.js',
        'src/lib/prettify.js',
        'src/lib/bootstrap/js/alert.js',
        'src/lib/bootstrap/js/button.js',
        'src/lib/bootstrap/js/collapse.js',
        'src/lib/bootstrap/js/dropdown.js',
        'src/lib/bootstrap/js/tooltip.js',
        'src/lib/bootstrap/js/affix.js',
        'src/lib/bootstrap/js/popover.js',
      ],
    'scripts': [
        'src/script/common/util.coffee',
        'src/script/common/service.coffee',
        'src/script/site/app.coffee',
        'src/script/site/profile.coffee',
        'src/script/site/admin.coffee',
        'src/script/site/main.coffee',
        'src/script/site/tree.coffee',
      ],
  }
