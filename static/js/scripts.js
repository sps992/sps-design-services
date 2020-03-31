var contact = $("form#contact");
contact.submit(function(event){
	event.preventDefault();
 
    (function(){
      emailjs.init("user_GXxEk5JXUi6PanXg50NK5");
   })();
  // Change to your service ID, or keep using the default service
  var service_id = "gmail";
  var template_id = "contact_form";

 contact.find("button").text("Sending...");
  emailjs.sendForm(service_id,template_id,contact[0])
  	.then(function(){ 
        $('#form-message').removeClass('hide').addClass('alert alert-success alert-dismissible').slideDown().show();
        $('#messages_content').html('<p>Thank you for your message, I will be in touch ASAP!</p>');
       contact.find("button").text("Send");
    }, function(err) {
        $('#messages').removeClass('hide').addClass('alert alert-success alert-dismissible').slideDown().show();
        $('#messages_content').html('<p>Sorry, something has gone wrong. Please try again later or contact us on <span><a href="mailto:support@samsedgeman.co.uk">support@samsedgeman.co.uk</a></span></p>');
       contact.find("button").text("Send");
    });
  return false;
  
});


