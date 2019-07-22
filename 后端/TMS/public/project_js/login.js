$(function () {
  $('input').iCheck({
    checkboxClass: 'icheckbox_square-blue',
    radioClass: 'iradio_square-blue',
    increaseArea: '20%' /* optional */
  });

  $('#signIn').on("click", log_in)
});

function log_in() {
    var username = $('#username').val();
    var password = $('#password').val();
    var timestamp = 'dasd';
    // var href = $(window).attr("href").slice(0, 22);
    // console.log($(window).attr("href").slice(0, 22));
    if(username != "" && username != null && password != "" && password != null){
        // 执行post指令，向服务器传递用户账号
        $.post("../login", { "user_name": username, "password":password, "timestamp":timestamp }, function(data){
            // console.log(href + data);
            window.location.replace("http://127.0.0.1:8000" + data)
        })

        // function(data){
        //   alert(data.name); // John
        //   console.log(data.time); //  2pm
        
        console.log(username);
        console.log(password);
    }else {
        alert("请填写完整")
    }
}



