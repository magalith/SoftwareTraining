var data = [{
    "id": 1,
    "stuname": "aa",
    "class": '',
    "teacher": "aa",
    "note": ""
},
{
    "id": 1,
    "stuname": "aa",
    "class": 2,
    "teacher": "aa",
    "note": ""
},
{
    "id": 1,
    "stuname": "aa",
    "class": 2,
    "teacher": "aa",
    "note": ""
},
{
    "id": 1,
    "stuname": "aa",
    "class": 2,
    "teacher": "aa",
    "note": ""
},
{
    "id": 1,
    "stuname": "aa",
    "class": 2,
    "teacher": "aa",
    "note": ""
},
{
    "id": 1,
    "stuname": "aa",
    "class": 2,
    "teacher": "aa",
    "note": ""
},
{
    "id": 1,
    "stuname": "aa",
    "class": 2,
    "teacher": "aa",
    "note": ""
},
{
    "id": 1,
    "stuname": "aa",
    "class": 2,
    "teacher": "aa",
    "note": ""
},
{
    "id": 1,
    "stuname": "aa",
    "class": 2,
    "teacher": "aa",
    "note": ""
},
{
    "id": 1,
    "stuname": "aa",
    "class": 2,
    "teacher": "aa",
    "note": ""
},
{
    "id": 1,
    "stuname": "aa",
    "class": 2,
    "teacher": "aa",
    "note": ""
},
{
    "id": 1,
    "stuname": "aa",
    "class": 2,
    "teacher": "aa",
    "note": ""
},
{
    "id": 1,
    "stuname": "aa",
    "class": 2,
    "teacher": "aa",
    "note": ""
},
{
    "id": 1,
    "stuname": "aa",
    "class": 2,
    "teacher": "aa",
    "note": ""
},
{
    "id": 1,
    "stuname": "aa",
    "class": 2,
    "teacher": "aa",
    "note": ""
}
,{
    "id": 1,
    "stuname": "aa",
    "class": 2,
    "teacher": "aa",
    "note": ""
},
{
    "id": 1,
    "stuname": "aa",
    "class": 2,
    "teacher": "aa",
    "note": ""
},
{
    "id": 1,
    "stuname": "aa",
    "class": 2,
    "teacher": "aa",
    "note": ""
},
{
    "id": 1,
    "stuname": "aa",
    "class": 2,
    "teacher": "aa",
    "note": ""
},
{
    "id": 1,
    "stuname": "aa",
    "class": 2,
    "teacher": "aa",
    "note": ""
},
{
    "id": 1,
    "stuname": "aa",
    "class": 2,
    "teacher": "aa",
    "note": ""
},
{
    "id": 1,
    "stuname": "aa",
    "class": 2,
    "teacher": "aa",
    "note": ""
},
{
    "id": 1,
    "stuname": "aa",
    "class": 2,
    "teacher": "aa",
    "note": ""
},
{
    "id": 1,
    "stuname": "aa",
    "class": 2,
    "teacher": "aa",
    "note": ""
},
{
    "id": 1,
    "stuname": "aa",
    "class": 2,
    "teacher": "aa",
    "note": ""
},
{
    "id": 1,
    "stuname": "aa",
    "class": 2,
    "teacher": "aa",
    "note": ""
},
{
    "id": 1,
    "stuname": "aa",
    "class": 2,
    "teacher": "aa",
    "note": ""
}]

$(function(){
    loadStudentList();
    $('#addList').on("click", addDataToList);
    $('#divide_class').find("a").on("click", divideClass)
})

function loadStudentList(){
    var html = '';
    for ( var i = 0; i < data.length; i++) {//循环json对象，拼接tr,td的html
        html = html + '<tr>';
        html = html + '<td>' + data[i].id + '</td>';
        html = html + '<td>' + data[i].stuname + '</td>';
        html = html + '<td>' + data[i].class + '</td>';
        html = html + '<td><span class="label label-success">' + data[i].teacher + '</span></td>';
        html = html + '<td>' + data[i].note + '</td>';
        html = html + '<td><span class="glyphicon glyphicon-trash" onclick="deleteItem(this)"></span></td>';
        html = html + '</tr>';
    }
    $('#table_test').append(html);
}

function deleteItem(obj){
    $(obj).parent().parent().remove();
}

function addDataToList(){
    var username = $('#username').val();
    var congshuclass = $('#congshuclass').val();
    var teacher = $('#teacher').val();
    var note = $('#note').val();
    if(username != "" && username != null && congshuclass != "" && congshuclass != null && teacher != "" && teacher != null){
        console.log(username);
        var html = "";
        html += '<tr><td></td><td>' + username +'</td><td>' + congshuclass + '</td><td>';
        html += '<span class="label label-success">' + teacher + '</span></td>';
        html += '<td>' + note + '</td>';
        html += '<td><span class="glyphicon glyphicon-trash" onclick="deleteItem(this)"></span></td></tr>';
        $('#table_test').append(html);
        $('#username').val("");
        $('#congshuclass').val("");
        $('#teacher').val("");
        $('#note').val("");
    } else {
        alert("请输入完整添加内容");
        $('#username').val("");
        $('#congshuclass').val("");
        $('#teacher').val("");
        $('#note').val("");
    }
}

function divideClass() {
    if(data[0].class === ''){
        var nClass = $(this).text();
        console.log(nClass);
        var nPerClass = parseInt(data.length/nClass);
        var html = '<p>将所有学生划分为<b>' + nClass + '</b>个班级, 每个班级大致包含<b>' + nPerClass;
        html += '</b>名同学，请注意班级数不可修改，请谨慎确认!</p>';
        $(".modal-body").eq(0).append(html);
        $('#cancel_class_divide').on("click", function(){
            $('.modal-body').eq(0).html('');
            return ;
        })
        $('#confirm_class_divide').on("click", function(){
            data[0].class = 1;
        $('#table_test').html('<tbody><tr><th>序号</th><th>姓名</th><th>从属班级</th><th>老师</th><th>备注</th></tr></tbody>');
        loadStudentList();
        $('#divide_class').css("display", "none");
        })
    } else {
        $('#divide_class').css("display", "none");
    }
}