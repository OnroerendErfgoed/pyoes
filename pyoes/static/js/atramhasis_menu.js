

function showlist(item) {
  var list = document.getElementById(item);
  $(list).toggle(500);
  $('#item2').toggle(500);

}

function showsubList(item, elem) {
  var list = document.getElementById(item);
  $("ul#item1list > li:not(:first)").toggle(500);
  $(list).toggle(500);
}