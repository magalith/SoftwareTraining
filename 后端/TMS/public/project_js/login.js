$(function () {
  $('input').iCheck({
    checkboxClass: 'icheckbox_square-blue',
    radioClass: 'iradio_square-blue',
    increaseArea: '20%' /* optional */
  });
  $('.tab-item').click(function(){
    $(this).addClass("active").siblings("li").removeClass("active");
    $(".noshow").eq($(this).index()).addClass("selected").siblings("form").removeClass("selected");
  })
  $('#userSignIn').on("click", log_in);
  $('#getCaptcha').click(getCaptcha);
  $('#captchaSignIn').click(captchaLogin);
});

function log_in() {
    var username = $('#username').val().slice(-3);
    var password = $('#password').val();
    console.log(username.slice(-3))
    var timestamp = 'dasd';
    if(username != "" && username != null && password != "" && password != null){
        // 执行post指令，向服务器传递用户账号
        $.post("../login", { "user_name": username, "password":password, "timestamp":timestamp }, function(data){
            // console.log(href + data);
            window.location.replace(data)
        })
    }else {
        alert("请填写完整")
    }
}

function getCaptcha() {
  var phone_num = $('#phone_num').val();
  $.post("/api/send_sms", {"timestamp": 123, "phone": phone_num})
}

function captchaLogin(){
  var phone_num = $('#phone_num').val();
  var code = $('#captcha').val();
  $.post("/api/login_phone", {"timestamp": 123, "phone": phone_num, "code": code}, function(data){
    console.log(data);
    window.location.replace(data)
  })
}