window.LOG = ->
  console?.log? arguments...


window.init_common = ->
  init_loading_button()
  init_time()
  init_announcement()
  init_hash_header_highlight()


window.init_loading_button = ->
  $('body').on 'click', '.btn-loading', ->
    $(this).button 'loading'


window.init_time = ->
  if $('time').length > 0
    recalculate = ->
      $('time[datetime]').each ->
        date = moment.utc $(this).attr 'datetime'
        diff = moment().diff date , 'days'
        if diff > 25
          $(this).text date.local().format 'YYYY-MM-DD'
        else
          $(this).text date.fromNow()
        $(this).attr 'title', date.local().format 'dddd, MMMM Do YYYY, HH:mm:ss Z'
      setTimeout arguments.callee, 1000 * 45
    recalculate()


window.init_announcement = ->
  $('.alert-announcement button.close').click ->
    sessionStorage?.setItem 'closedAnnouncement', $('.alert-announcement').html()

  if sessionStorage?.getItem('closedAnnouncement') != $('.alert-announcement').html()
    $('.alert-announcement').show()


window.clear_notifications = ->
  $('#notifications').empty()


window.show_notification = (message, category='warning') ->
  clear_notifications()
  return if not message

  $('#notifications').append """
      <div class="alert alert-dismissable alert-#{category}">
        <button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>
        #{message}
      </div>
    """


window.init_hash_header_highlight = ->
  update_hash_header()
  ($ window).on 'hashchange', ->
    update_hash_header()


window.update_hash_header = ->
  id = location.hash.substr(1)
  id = id.replace('.', '\\.').replace('@', '\\@')
  ($ '.hash').removeClass 'hash'
  if id.length > 0
    ($ "##{id}.self-link, ##{id} .self-link").first().addClass('hash')
