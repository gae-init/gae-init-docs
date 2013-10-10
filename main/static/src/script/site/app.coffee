$ ->
  init_common()
  setTimeout ->
    ($ '.social').css('opacity', '1')
  , 2000

$ -> ($ 'html.welcome').each ->
  ($ 'abbr').tooltip()
  ($ '.tip').tooltip()

$ -> ($ 'html.profile').each ->
  init_profile()

$ -> ($ 'html.feedback').each ->

$ -> ($ 'html.admin-config').each ->
  init_admin_config()

$ -> ($ 'html.reference').each ->
  init_doc()

$ -> ($ 'html.tutorial').each ->
  init_doc()

$ -> ($ 'html.requirement').each ->
  init_doc()

$ -> ($ 'html.tree').each ->
  init_tree()
