
$(function(){
    $.post("/api/get_class_info", {"timestamp": 12}, function(data){
        loadClassInfo(data)
    }, "json")
})

function loadClassInfo(data) {
    data = data.data;
    html = ''
    for (var i = 0; i < data.length; i++) {//将班级名称加入列表中
        if (data[i].students_id.length != 0){
            html += '<div class="col-md-4"><div class="box box-widget widget-user-2"><div class="widget-user-header bg-blue"><h5 class="widget-user-username class_name_tag">';
            html += data[i].cid + '|班';
            html += '</h5></div><div class="box-footer no-padding"><ul class="nav nav-stacked"><li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown" aria-expanded="false">学生人数<span class="pull-right badge bg-blue">';
            html += data[i].students_id.length + '</span></a>';
            html += '<ul class="dropdown-menu" style = "width:310px"><li><b>学生名单</b></li>';
            for (var j = 0; j < data[i].students_id.length; j++) {
                html += '<li><a>' + data[i].students_id[j].id + data[i].students_id[j].name + '</a></li>'
            };
            html += '</ul><li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown" aria-expanded="false">负责老师 <span class="pull-right badge bg-aqua teacher_name">';
            tch_name = data[i].teacher_id;
            if (data[i].teacher_id.length != 0){
                html += data[i].teacher_id[0].name;
            }
            html += '</span></a><ul class="dropdown-menu tch_list" style="width: 310px">';
            html += '</ul></li></ul></div>';
            $('#class_name_tag').append(html);
            html = ''
        }
    }
    addTchToList();
}


function addTchToList(){
    $.post("/api/get_teachers", {"timestamp": 123}, function(obj){
        console.log(JSON.parse(obj));
        data = JSON.parse(obj).data;
        console.log(data);
        tch_list = ''
        for( var j=0; j<data.length; j++){
            tch_list += '<li><a onclick="getTeacher(this)">' + data[j].id + '|' + data[j].name + '</a></li>'
        }
        $('.tch_list').append(tch_list)
    })
}

function getTeacher(obj) {
    index = $(obj).parent().index();
    c_index = $()
    console.log(index)
    $(obj).parent().parent().siblings().find("span").html(obj.text);
    c_id = $(obj).parent().parent().parent().parent().parent().parent().find('.class_name_tag').text().split("|")[0];
    console.log(c_id);
    tch_id = $(obj).text().split("|")[0];
    console.log(tch_id);
    classes = '[{"class_id": ' + c_id + ', "teacher_id": [' + tch_id + '], "students_id": []}]';
    $.post("/api/update_class_member_bak", {"timestamp": 123, "class": classes});
}
