$(() => {
  initCommon();
  init_global();

  setTimeout(() => {
    $('.social').css('opacity', '1');
  }, 2000);

  $('html.auth').each(() => {
    initAuth();
  });

  $('html.user-list').each(() => {
    initUserList();
  });

  $('html.user-merge').each(() => {
    initUserMerge();
  });

  $('html.welcome').each(() => {
    $('abbr').tooltip()
    $('.tip').tooltip()
  }

  $('html.reference').each(() => {
    init_doc()
}
  $('html.quickstart').each(() => {
    init_doc()
}
  $('html.tutorial').each(() => {
    init_doc()
}
  $('html.requirement').each(() => {
    init_doc()
}
  $('html.howto').each(() => {
    init_doc()
}
  $('html.tree').each(() => {
    init_tree()
}
  $('html.convention').each(() => {
    init_doc()
}
});
