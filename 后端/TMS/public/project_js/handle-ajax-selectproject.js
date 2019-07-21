data =  [
    {
        "id": "P_001",
        "name": "电商网站",
        "detail": "做一个小阿里巴巴"
    },
    {
        "id": "P_002",
        "name": "实训管理系统",
        "detail": "做一个给领导看的虚伪web系统"
    },
    {
        "id": "P_003",
        "name": "毕业设计管理系统",
        "detail": "让系统,搅乱你的毕设"
    }
]

$(function() {
    $.post("/api/get_project_pool", {"timestamp": 1}, function(data){
        selectProject(data);
    }, "json")
})

function selectProject(data) {
    data = data.data;
    var html = ''
    for (i = 0; i<data.length; i++) {
        html += '<div class="col-md-4"><div class="box box-warning box-solid collapsed-box">'
        html += '<div class="box-header with-border"><h3 class="boxtitle" data-widget="collapse">'
        html += data[i].name + '</h3></div>'
        html += '<div class="box-body" style="display: none;">'
        html += '<p>' + data[i].id + '</p>' + '<p>' + data[i].detail + '</p>'
        html += '<button type="button" class="btn btn-block btn-default">'
        html += '<b>Confirm</b></button></div></div></div>'
        $('#showProject').append(html)
        html = ''
    }
}