window.init_global = () ->
  $('a', '.self-link').attr('title', 'Permenant link')
  $('a').each (index) ->
    $this = $($('a')[index])
    if $this.attr('href')?.substr(0, 4) == 'http'
      $this.attr('target', "gae-#{$this.attr('href')}")


window.init_doc = () ->
  prettyPrint()
  init_affix()
