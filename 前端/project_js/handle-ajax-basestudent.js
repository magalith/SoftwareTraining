var data = [{
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
    $('#addList').on("click", addDataToList)
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
    const username = $('#username').val();
    const congshuclass = $('#congshuclass').val();
    const teacher = $('#teacher').val();
    const note = $('#note').val();
    if(username != "" && username != null && congshuclass != "" && congshuclass != null && teacher != "" && teacher != null){
        console.log(username);
    } else {
        alert("请输入完整添加内容")
    }
}