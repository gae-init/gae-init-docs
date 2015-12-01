# coding: utf-8

import os


PRODUCTION = os.environ.get('SERVER_SOFTWARE', '').startswith('Google App Eng')
DEBUG = DEVELOPMENT = not PRODUCTION

try:
  # This part is surrounded in try/except because the config.py file is
  # also used in the run.py script which is used to compile/minify the client
  # side files (*.less, *.coffee, *.js) and is not aware of the GAE
  from google.appengine.api import app_identity
  APPLICATION_ID = app_identity.get_application_id()
except (ImportError, AttributeError):
  pass
else:
  from datetime import datetime
  CURRENT_VERSION_ID = os.environ.get('CURRENT_VERSION_ID')
  CURRENT_VERSION_NAME = CURRENT_VERSION_ID.split('.')[0]
  CURRENT_VERSION_TIMESTAMP = long(CURRENT_VERSION_ID.split('.')[1]) >> 28
  if DEVELOPMENT:
    import calendar
    CURRENT_VERSION_TIMESTAMP = calendar.timegm(datetime.utcnow().timetuple())
  CURRENT_VERSION_DATE = datetime.utcfromtimestamp(CURRENT_VERSION_TIMESTAMP)
  USER_AGENT = '%s/%s' % (APPLICATION_ID, CURRENT_VERSION_ID)

  import model
  CONFIG_DB = model.Config.get_master_db()
  SECRET_KEY = CONFIG_DB.flask_secret_key.encode('ascii')
  RECAPTCHA_PUBLIC_KEY = CONFIG_DB.recaptcha_public_key
  RECAPTCHA_PRIVATE_KEY = CONFIG_DB.recaptcha_private_key
  RECAPTCHA_LIMIT = 8


DEFAULT_DB_LIMIT = 64
SIGNIN_RETRY_LIMIT = 4
TAG_SEPARATOR = ' '

################################################################################
# SITE
################################################################################
REQUIREMENT = [
    ('gae', 'Google App Engine', 'Required'),
    ('nodejs', 'Node.js', 'Required'),
    ('gulp', 'Gulp', 'Required'),
    ('pip', 'pip', 'Required'),
    ('virtualenv', 'virtualenv', 'Required'),
    ('git', 'Git', 'Required'),
  ]

HOWTO = [
  ('start', 'Start'),
  ('add_frontend', 'Add Frontend Library'),
  ('add_backend', 'Add Backend Library'),
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
        ('param', '(name, cast=None)'),
        ('get_next_url', "(next_url='')"),
        ('get_dbs', '(query, order=None, limit=None, cursor=None, prev_cursor=False, keys_only=None, **filters)'),
        ('get_keys', '(*args, **kwargs)'),
        ('jsonpify', '(*args, **kwargs)'),
        ('is_iterable', '(value)'),
        ('check_form_fields', '(*fields)'),
        ('generate_next_url', '(next_cursor, base_url=None)'),
        ('uuid', '()'),
        ('slugify', '(text)'),
        ('is_valid_username', '(username)'),
        ('create_name_from_email', '(email)'),
        ('password_hash', '(user_db, password)'),
        ('update_query_argument', '(name, value=None, ignore=[])'),
        ('parse_tags', '(tags, separator=None)'),
        ('strip_filter', '()'),
        ('email_filter', '()'),
        ('sort_filter', '()'),
      ],
    'task': [
        ('send_mail_notification', '(subject, body, **kwargs)'),
        ('new_user_notification', '(user_db)'),
        ('verify_email_notification', '(user_db)'),
        ('reset_password_notification', '(user_db)'),
        ('email_conflict_notification', '(email)'),
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
        ('permission_required', '(permission=None, methods=None)')
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
      ],
    'utils': [
        ('order_by_link', "(property, title, ignore=['cursor'])"),
        ('filter_by_link', "(property, value, icon=None, ignore=['cursor'])"),
        ('next_link', "(next_url, caption='Next Page')"),
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
    ('introduction', 'Introduction'),
    ('code', 'Get the code'),
    ('run', 'Run the application'),
    ('model', 'Add the new model'),
    ('create', 'Add contacts'),
    ('list', 'List contacts'),
    ('view', 'View contacts'),
    ('update', 'Update contacts'),
#    ('delete', 'Deleting contacts'),
#    ('theme', 'Change theme'),
    ('deploy', 'Deploy'),
  ]

CONVENTION = [
    ('global', 'Global', ''),
    ('python', 'Python', ''),
    ('html', 'HTML / Jinja2', ''),
    ('less', 'Less / CSS', ''),
    ('coffee', 'CoffeeScript', ''),
    ('markdown', 'Markdown', 'for gae-init documentation'),
  ]
