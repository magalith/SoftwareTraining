$(function () {
  $.post("/api/get_self_info", {"timestamp":1}, function(data){
    data = JSON.parse(data);
    data = data.data
    get_username(data)
})
})


function get_username(data) {
console.log(data)
$(".user_name").append(":"+ data.name )

}