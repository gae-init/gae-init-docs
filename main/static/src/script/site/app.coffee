$ ->
  init_common()
  setTimeout ->
    ($ '.social').css('opacity', '1')
  , 2000

$ -> ($ 'html.welcome').each ->
  ($ 'abbr').tooltip()
  ($ '.tip').tooltip()
  github_init()

$ -> ($ 'html.profile').each ->
  init_profile()

$ -> ($ 'html.feedback').each ->

$ -> ($ 'html.admin-config').each ->
  init_admin_config()
