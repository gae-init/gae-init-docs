window.github_init = () ->
  repo = $('.github').data('repo')
  $(".btn[data-repo=#{repo}]").removeAttr('href')
  $(".btn[data-repo=#{repo}]").addClass('disabled')

  return
  $('head').append $('<script>').attr('src',  "https://api.github.com/repos/gae-init/#{repo}?callback=github")

add_commas = (n) ->
  String(n).replace /(\d)(?=(\d{3})+$)/g, "$1,"

window.github = (obj) ->
  $(".watchers").append(add_commas(obj.data.watchers_count))
  $(".forks").append(add_commas(obj.data.forks_count))
