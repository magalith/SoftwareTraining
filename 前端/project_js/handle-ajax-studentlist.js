var data = [{
    "id": 1,
    "stuname": "aa",
    "class": 2,
    "teacher": "aa",
    "note": "实训管理系统blablablabla实训管理系统blablablabla"
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

var html = '';
for ( var i = 0; i < data.length; i++) {//循环json对象，拼接tr,td的html
    html = html + '<tr>';
    html = html + '<td>' + data[i].id + '</td>';
    html = html + '<td>' + data[i].stuname + '</td>';
    html = html + '<td>' + data[i].class + '</td>';
    html = html + '<td><span class="label label-success">' + data[i].teacher + '</span></td>';
    html = html + '<td>' + data[i].note + '</td>';
    html = html + '<td style="width: 160px"><form action="#" method="post"><div class="input-group"><input type="text" name="message" placeholder="总分" class="form-control" style="width: 60px"><button type="submit" class="btn btn-primary btn-flat">评分</button></div></form></td>';
    html = html + '</tr>';
}
$('#table_studentlist').append(html);

