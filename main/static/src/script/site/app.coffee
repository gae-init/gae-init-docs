$ ->
  init_global()
  init_common()
  setTimeout ->
      $('.social').css('opacity', '1')
    , 2000


$ -> $('html.welcome').each ->
  $('abbr').tooltip()
  $('.tip').tooltip()

$ -> $('html.auth').each ->
  init_auth()

$ -> $('html.feedback').each ->

$ -> $('html.user-list').each ->
  init_user_list()

$ -> $('html.user-merge').each ->
  init_user_merge()

$ -> $('html.admin-config').each ->
  init_admin_config()

$ -> $('html.reference').each ->
  init_doc()

$ -> $('html.quickstart').each ->
  init_doc()

$ -> $('html.tutorial').each ->
  init_doc()

$ -> $('html.requirement').each ->
  init_doc()

$ -> $('html.howto').each ->
  init_doc()

$ -> $('html.tree').each ->
  init_tree()

$ -> $('html.convention').each ->
  init_doc()
