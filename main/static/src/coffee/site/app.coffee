$ ->
  init_time()

$ -> $('html.welcome').each ->
  $('abbr').tooltip()
  $('.tip').tooltip()
  github_init()

$ -> $('html.profile').each ->
  init_profile()

$ -> $('html.feedback').each ->
  init_loading_button()

$ -> $('html.admin-config').each ->
  init_admin_config()
