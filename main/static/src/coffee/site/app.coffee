$ ->

$ -> $('html.welcome').each ->
  $('abbr').tooltip()

$ -> $('html.profile').each ->
  init_profile()

$ -> $('html.feedback').each ->
  init_loading_button()

$ -> $('html.admin-config').each ->
  init_admin_config()
