
$(function(){
    $.post("/api/get_teachers", {"timestamp": 123}, function(data){
        loadTeacherList(data);
    }, "json");
    $('#add_tch').on("click", addTchList)
})

function loadTeacherList(data){
    data = data.data;
    var html = '';
    for ( var i = 0; i < data.length; i++) {//循环json对象，拼接tr,td的html
        html = html + '<tr>';
        html = html + '<td>' + data[i].id + '</td>';
        html = html + '<td>' + data[i].name + '</td>';
        html = html + '<td>' + data[i].class + '</td>';
        html = html + '<td>' + data[i].gender + '</td>';
        html = html + '<td><span class="glyphicon glyphicon-trash" onclick="deleteItem(this)"></span></td>';
        html = html + '</tr>';
    }
    $('#table_tch_list').append(html);

}

function deleteItem(obj){
    $(obj).parent().parent().remove();
    tch_id = parseInt($(obj).parent().parent().find('td').eq(0).text());
    $.post("/api/update_user_list", {"timestamp": 123, "method": "del", "user_list": "[" + tch_id + "]"})
}

user_list = []
function addTchList(){
    var name = $('#tch_name').val();
    console.log(typeof(name));
    var password = $('#tch_password').val();
    var gender = $('#tch_gender').val();
    var phone_num = $('#phone_num').val();
    if (name!="" && name!=null && password!="" && password!=null) {
        user_list.push('{"name": "' + name + '","password": "' + password + '","gender": "' + gender + '","group":"T", "phone": "' + phone_num + '"}')
        console.log(user_list)
        $('#tch_name').val("");
        $('#tch_password').val("");
        $('#tch_gender').val("");
        $('#phone_num').val("");
    } else {
        alert("请输入完整内容！")
        $('#tch_name').val("");
        $('#tch_password').val("");
        $('#tch_gender').val("");
        $('#phone_num').val("");
    }
    $('#confirm_tchlist').click(confirmTchList)
}

function confirmTchList(){
    console.log(user_list.toString())
    $.post("/api/update_user_list", {"timestamp": 123, "method": "add", "user_list": '['+ user_list + ']'});
    window.location.replace("/admin_teacher")
}