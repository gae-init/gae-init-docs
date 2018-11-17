window.init_hash_header_highlight = ->
  update_hash_header()
  ($ window).on 'hashchange', ->
    update_hash_header()


window.update_hash_header = ->
  id = location.hash.substr(1)
  id = id.replace('.', '\\.').replace('@', '\\@')
  ($ '.hash').removeClass 'hash'
  if id.length > 0
    ($ "##{id}").first().addClass('hash')
