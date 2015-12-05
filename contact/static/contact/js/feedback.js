;(function($, win) {
  "use strict";

  $(function() {
    helpTxt();
    validateForm();
  });

 function helpTxt() {
  $(".help_txt").hide();

  $('#alert_help').on({

    "mouseover":function(){
       $(".help_txt").fadeIn(); 
    },

    "mouseleave" : function(){
      $(".help_txt").fadeOut();
    }
  });
  
  
  };

function validateForm() {

console.log("llo")
  //Name cant be blank
  $('#contact_name').on('input', function() {
    var input=$(this);
    var is_name=input.val();
    if(is_name){input.removeClass("invalid").addClass("valid");}
    else{input.removeClass("valid").addClass("invalid");}
  });
  
  //Email must be an email 
  $('#contact_email').on('input', function() {
    var input=$(this);
    var re = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
    var is_email=re.test(input.val());
    if(is_email){input.removeClass("invalid").addClass("valid");}
    else{input.removeClass("valid").addClass("invalid");}
  });
  
  //Website must be a website 
  $('#contact_tel').on('input', function() {
    var input=$(this);
    var re = /^(0|([\+][8][4]))[0-9]{2}[-\s\.]{0,1}[0-9]{3}[-\s\.]{0,1}[0-9]{4,5}$/;
    var is_tel=re.test(input.val());
    if(is_tel){input.removeClass("invalid").addClass("valid");}
    else{input.removeClass("valid").addClass("invalid");}
  });
  
  //Message cant be blank 
  $('#contact_comment').keyup(function(event) {
    var input=$(this);
    var message=$(this).val();
    console.log(message);
    if(message){input.removeClass("invalid").addClass("valid");}
    else{input.removeClass("valid").addClass("invalid");} 
  });

// After Form Submitted Validation
$("#contact_submit button").click(function(event){
  var form_data=$("#the_form").serializeArray();
  var error_free=true;
  for (var input in form_data){
    var element=$("#contact_"+form_data[input]['name']);
    var valid=element.hasClass("valid");
    var error_element=$("span", element.parent());
    if (!valid){error_element.removeClass("error").addClass("error_show"); error_free=false;}
    else{error_element.removeClass("error_show").addClass("error");}
  }
  if (!error_free){
    event.preventDefault(); 
  }
  else{
    alert('Bạn đã gửi email thành công, chúng tối sẽ cập nhập thông tin của bạn. Xin chân thành cảm ơn!');
  }
});
};


})(jQuery, window);