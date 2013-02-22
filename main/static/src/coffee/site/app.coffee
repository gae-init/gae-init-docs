$ ->

$ -> $('html.welcome').each ->
  $('abbr').tooltip()
  $('.tip').tooltip()

$ -> $('html.profile').each ->
  init_profile()

$ -> $('html.feedback').each ->
  init_loading_button()

$ -> $('html.admin-config').each ->
  init_admin_config()
