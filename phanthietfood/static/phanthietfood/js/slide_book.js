(function($) {

  $(function() {  
     $(window).on("load resize", function(){
      if ($(window).width() <= 767) {

    $("#bnr_book").carouFredSel({
      circular: false,
      infinite: false,
      auto    : false,
      height  : false,
 
      prev    : {
      button  : "#ico_prev",
      key     : "left"
      },

      next    : {
        button  : "#ico_next",
        key     : "right"
      }
    });

          }  
    });

  });
})(jQuery);