$(function () {
  $('input').iCheck({
    checkboxClass: 'icheckbox_square-blue',
    radioClass: 'iradio_square-blue',
    increaseArea: '20%' /* optional */
  });

  $('#signIn').on("click", log_in)
});

function log_in() {
    const username = $('#username').val();
    const password = $('#password').val();

    if(username != "" && username != null && password != "" && password != null){
        // 执行post指令，向服务器传递用户账号
        $.post("test.php", { "user_name": username, "password":password, "timestamp":timestamp } )
        // function(data){
        //   alert(data.name); // John
        //   console.log(data.time); //  2pm
        
        console.log(username);
        console.log(password);
    }else {
        alert("请填写完整")
    }
}



