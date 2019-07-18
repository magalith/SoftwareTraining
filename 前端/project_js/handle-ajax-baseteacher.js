var data = [{
    "id": 1,
    "teacher_name": "aa",
    "class": 2,
    "note": ""
},
{
    "id": 1,
    "teacher_name": "aa",
    "class": 2,
    "note": ""
},
{
    "id": 1,
    "teacher_name": "aa",
    "class": 2,
},
{
    "id": 1,
    "teacher_name": "aa",
    "class": 2,
},
{
    "id": 1,
    "teacher_name": "aa",
    "class": 2,
}]

var html = '';
for ( var i = 0; i < data.length; i++) {//循环json对象，拼接tr,td的html
    html = html + '<tr>';
    html = html + '<td>' + data[i].id + '</td>';
    html = html + '<td>' + data[i].teacher_name + '</td>';
    html = html + '<td>' + data[i].class + '</td>';
    html = html + '<td><span class="glyphicon glyphicon-trash" onclick="deleteItem(this)"></span></td>';
    html = html + '</tr>';
}
$('#table_test').append(html);

function deleteItem(obj){
    $(obj).parent().parent().remove();
}
