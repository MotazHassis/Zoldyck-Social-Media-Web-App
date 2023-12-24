
function fetch_messages(){ 
  
  $.ajax({ 
    url: '/message_continuos_update', 
    type: 'GET', 
  })
  
  .done(function(res){
     $('.notifications_ajax').html(res);  // manipulate the dom when the response comes back
})
console.log('repeating')
} 


// -----------------------
function fetch_friends_request(){ 
  
  $.ajax({ 
    url: '/friend_request_update', 
    type: 'GET', 
  })
  
  .done(function(res){
     $('.notifications_friend').html(res);  // manipulate the dom when the response comes back
})
console.log('repeating')
} 

function hide_button(elem){
  elem.style.display = 'none';
}
add_emoji = document.getElementById("emoji_to_add")
function copypaste(elem){
  emo=elem.innerText;
  add_emoji.value+= emo;
}

function onClick(element) {
  document.getElementById("img01").src = element.src;
  document.getElementById("modal01").style.display = "block";
}



// -----------------------

$(document).ready(function(){
  setInterval(fetch_messages,5000);
  setInterval(fetch_friends_request,5000);



// -------------------------

  $('.addcomment').click(function(){
    var data = $("#regForm-"+$(this)[0].id).serialize()   // capture all the data in the form in the variable data
    $.ajax({
        method: "POST",   // we are using a post request here, but this could also be done with a get
        url: "/comment/"+$(this)[0].id,
        data: data
    })

    .done(function(res){
        console.log($('#like-'+$(this)[0].url.split('/')[2]))
        
        
          $('.allcomment-'+$(this)[0].url.split('/')[2]).html(res)// manipulate the dom when the response comes back
          // console.log($('.clear_comment').length)
          for (var i=0;i<$('.clear_comment').length;i++){
            $('.clear_comment')[i].value = ""
            console.log($('.clear_comment').value)
          }


          
    })
    })
    $('.addcomment').click(function(){
    $.ajax({
      method: "GET",   // we are using a post request here, but this could also be done with a get
      url: "/count_comment/"+$(this)[0].id,
      
    })

    .done(function(res){
      console.log($('.comment_count_no-'+$(this)[0].url.split('/')[2]))
       $('#comment_count_no-'+$(this)[0].url.split('/')[2]).html(res)  // manipulate the dom when the response comes back
    })
  })






  $('.like_link').click(function(){
    console.log($(this))
    $.ajax({
          method: "GET",   
          url:$(this)[0].name,
      })
      .done(function(res){
        // console.log($('#like-'+$(this)[0].url.split('/')[2])[0])
        $('#like-'+$(this)[0].url.split('/')[2]).html(res)
      })
})
})

// --------------------
// popover
var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
  return new bootstrap.Popover(popoverTriggerEl);
});
