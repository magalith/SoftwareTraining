$(function () {

});


function get_username() {
$.post("/api/get_self_info", {"timestamp":1}, function(data){
$("#user_name").html("管理员"+ data[0]  +"<small>Member since Nov. 2012</small>+)
})
}

