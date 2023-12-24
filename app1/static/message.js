function scroll() {
  logTa = document.getElementById("textarea_id")
  logTa.scrollTop = logTa.scrollHeight;
}
scroll()


function text_message_update(){ 
  var currentUrl = window.location.href;
  var id=currentUrl.split('/')[4]
  console.log(id)
  $.ajax({ 
    url: '/text_message_update/'+id,
    type: 'GET', 
  })
  
  .done(function(res){
    $('#textarea_id').html(res); 
    function scrollLogToBottom() {
      logTa = document.getElementById("textarea_id")
      logTa.scrollTop = logTa.scrollHeight;
    }
    scrollLogToBottom()
      // manipulate the dom when the response comes back
})

} 


function fetchdata(){ 
  
  $.ajax({ 
    url: '/message_continuos_update', 
    type: 'GET', 
  })
  
  .done(function(res){
     $('.notifications_ajax').html(res);  // manipulate the dom when the response comes back
})
console.log('repeating')
} 
$(document).ready(function(){ 
  setInterval(fetchdata,5000); 
  setInterval(text_message_update,5000);
});


