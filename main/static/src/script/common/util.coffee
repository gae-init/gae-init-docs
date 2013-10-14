window.LOG = ->
  console?.log? arguments...


window.init_common = ->
  init_loading_button()
  init_time()


window.init_loading_button = ->
  ($ 'body').on 'click', '.btn-loading', ->
    ($ this).button 'loading'


window.init_time = () ->
  if ($ 'time').length > 0
    recalculate = ->
      ($ 'time[datetime]').each ->
        date = moment.utc ($ this).attr 'datetime'
        diff = moment().diff date , 'days'
        if diff > 25
          ($ this).text date.local().format 'YYYY-MM-DD'
        else
          ($ this).text date.fromNow()
        ($ this).attr 'title', date.local().format 'dddd, MMMM Do YYYY, HH:mm:ss Z'
    recalculate()
    setInterval ->
        recalculate()
      , 1000 * 60


window.init_smooth_scrolling = () ->
  $('body').on 'click', '.smooth-scroll', ->
    $('html, body').animate({
        scrollTop: $($(this).attr('href')).offset().top
     }, 256);

window.init_affix = () ->
  $(".docs-sidenav").affix offset:
    top: ->
      if $(window).width() <= 980 then 180 else 170
    bottom: 270
