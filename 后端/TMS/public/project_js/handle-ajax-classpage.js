var data = [{
    "class_name": "01",
    "teacher": "teacher_a",
    "students": [1001, 1002, 1003, 244]
    },
    {
    "class_name": "02",
    "teacher": "teacher_b",
    "students": [1001, 1002, 1003]
    },
    {
    "class_name": "03",
    "teacher": "teacher_c",
    "students": [1001, 1002, 1003]
    }]


html = ''
for (var i = 0; i < data.length; i++) {//将班级名称加入列表中
    html += '<div class="col-md-4"><div class="box box-widget widget-user-2"><div class="widget-user-header bg-blue"><h5 class="widget-user-username class_name_tag">';
    html += data[i].class_name + '班';
    html += '</h5></div><div class="box-footer no-padding"><ul class="nav nav-stacked"><li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown" aria-expanded="false">学生人数<span class="pull-right badge bg-blue">';
    html += data[i].students.length + '</span></a>';
    html += '<ul class="dropdown-menu" style = "width:310px"><li><b>学生名单</b></li>';
    for (var j = 0; j < data[i].students.length; j++) {
        html += '<li><a>' + data[i].students[j] +'</a></li>'
    };
    html += '</ul><li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown" aria-expanded="false">负责老师 <span class="pull-right badge bg-aqua teacher_name">';
    html += data[i].teacher + '</span></a>';
    html += '<ul class="dropdown-menu" style="width: 310px">';
    for (var j = 0; j < data.length; j++) {
        html += '<li><a onclick="getTeacher(this)">' + data[j].teacher + '</a></li>';
    }
    html += '</ul></li></ul></div>';
    $('#class_name_tag').append(html);
    html = ''
}

function getTeacher(obj) {
    index = $(obj).parent().index();
    $(obj).parent().parent().siblings().find("span").html(obj.text);
}
