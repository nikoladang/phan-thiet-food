(function($) {
  $(function(scroll) {
    var scroller = (/safari/i.test(navigator.userAgent)) ? $("body") : $("html");
    $("#home").on("click tap", function() {
      scroller.animate({scrollTop: $("#header").offset().top},800);
      return false;
    });
  });  
})(jQuery);