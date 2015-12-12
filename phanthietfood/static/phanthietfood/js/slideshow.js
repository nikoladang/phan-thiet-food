;(function($){

var currentImage;
var currentIndex = -1;
var interval = 3000;
var myTimer;

var showImage = function(index){
  if(index < $("#slide_img img").length){
    var indexImage = $("#slide_img img")[index]
    if(currentImage){   
      if(currentImage != indexImage ){
      $(currentImage).css("z-index",2);
        clearTimeout(myTimer);
        $(currentImage).fadeOut(250, function() {
          myTimer = setTimeout(showNext, interval);
          $(this).css({"display":"none","z-index":1})
        });
      }
    }
    $(indexImage).css({"display":"block"});
    currentImage = indexImage;
    currentIndex = index;
    $("#number li").removeClass("current_slide_on");
    $($("#number li")[index]).addClass("current_slide_on");
    $("#nav_item li").removeClass("current");
    $($("#nav_item li")[index]).addClass("current");
  }
};

var showNext = function(){
  var len = $("#slide_img img").length;
  var next = currentIndex < (len-1) ? currentIndex + 1 : 0;
  showImage(next);
};
$(function() { 
  myTimer = setTimeout(showNext, interval);
  showNext(); //loads first image
    $("#number li a").bind("click",function(e){
      var count = $(this).attr("rel");
      showImage(parseInt(count)-1);
      return false;      
    });
    $("#nav_item li a").bind("click",function(e){
      var count = $(this).attr("rel");
      showImage(parseInt(count)-1);
      return false;      
    });
}); 

}(jQuery));