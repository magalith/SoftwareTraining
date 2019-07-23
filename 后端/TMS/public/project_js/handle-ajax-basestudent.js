
$(function() {
    $.post("/api/get_students", {"timestamp": 123}, function(data){
        loadStuList(data)
        $('.divide_class').click(data, divideClass);
    }, "json");
    $('#add_stu').click(addStuList);
})

// 加载学生列表
function loadStuList(data){
    data = data.data;
    var html = '';
    for ( var i = 0; i < data.length; i++) {//循环json对象，拼接tr,td的html
        html = html + '<tr>';
        html = html + '<td>' + data[i].id + '</td>';
        html = html + '<td>' + data[i].stuname + '</td>';
        html += '<td>' + data[i].gender + '</td>';
        html = html + '<td>' + data[i].class + '</td>';
        html = html + '<td><span class="label label-success">' + data[i].teacher + '</span></td>';
        html = html + '<td>' + data[i].note + '</td>';
        html = html + '<td><span class="glyphicon glyphicon-trash delete_stulist" onclick="deleteItem(this)"></span></td>';
        html = html + '</tr>';
    }
    $('#table_test').append(html);
}

// 删除学生功能
function deleteItem(obj){
    $(obj).parent().parent().remove();
    stu_id = parseInt($(obj).parent().parent().find('td').eq(0).text());
    $.post("/api/update_user_list", {"timestamp": 123, "method": "del", "user_list": "[" + stu_id + "]"})
}

// 增加学生名单功能，由于删除与增加不可同时进行，故将删除按钮禁用
// 定义全局变量user_list，两个函数进行调用
user_list = []
function addStuList(){
    $('.delete_stulist').removeAttr("onclick");
    var name = $('#stu_name').val();
    var password = $('#stu_password').val();
    var gender = $('#stu_gender').val();
    var phone_num = $('#phone_num').val();
    if (name!="" && name!=null && password!="" && password!=null) {
        user_list.push('{"name": "' + name + '","password": "' + password + '","gender": "' + gender + '","group":"S", "phone": "' + phone_num + '"}')
        console.log(user_list)
        $('#stu_name').val("");
        $('#stu_password').val("");
        $('#stu_gender').val("");
        $('#phone_num').val("");
    } else {
        alert("请输入完整内容!")
        $('#stu_name').val("");
        $('#stu_password').val("");
        $('#stu_gender').val("");
        $('#phone_num').val("");
    }
    $('#confirm_stulist').click(confirmStuList)
}

// 向数据库提交增加名单，并刷新界面，重新渲染学生名单
function confirmStuList(){
    console.log(user_list.toString())
    $.post("/api/update_user_list", {"timestamp": 123, "method": "add", "user_list": '['+ user_list + ']'});
    window.location.replace("/admin_student")
}

// 分班功能
function divideClass(event){
    var data = event.data.data;
    var index = $('.divide_class').index(this);
    var n_class = $('.divide_class').eq(index).text();
    console.log(n_class)
    var per_class_n = parseInt(data.length/n_class);
    var content = "";
    content += '将班级划分为' + n_class + '个，每班约含' + per_class_n + '个学生，班级不可修改，请谨慎确认！';
    $('#divide_class_info').html(content);
    // 为划分班级绑定方法
    var obj = {stulist: data, classnum: n_class, n_stu: per_class_n}
    $('#confirm_class').click(obj, submitClass);
}

// 创建班级并完成班级信息更新
function submitClass(event){
    $('#divide_n_class').css("display", "none");
    var classNum = event.data.classnum;
    var stuList = event.data.stulist;
    var n_stu = event.data.n_stu;
    var confirm_time = 0;
    for(var i=0; i<classNum; i++){
        $.post("/api/operate_class", {"method": "add", "timestamp": 1, "class": '[{"name": "CLASS_' + i + '","room": "10' + i + '"}]'}, function(data){
            confirm_time += 1
            console.log(confirm_time)
        })
    }
    console.log(classNum);
    console.log(stuList);
}
