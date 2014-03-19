window.init_global = () ->
  init_markdown_header_links()
  $('.self-link > a:first-child').attr('title', 'Permenant link')
  $('a').each (index) ->
    $this = $($('a')[index])
    if $this.attr('href')?.substr(0, 4) == 'http'
      $this.attr('target', "gae-#{$this.attr('href')}")


window.init_markdown_header_links = ->
  $('div.markdown :header[id]')
    .addClass('self-link')
    .each (i, el) ->
      e = $(el)
      e.append(" <a href=\"##{e.attr('id')}\"></a>")


window.init_doc = ->
  hljs.initHighlightingOnLoad()
