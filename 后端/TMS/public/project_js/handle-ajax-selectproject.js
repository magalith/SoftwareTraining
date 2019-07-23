
$(function() {
    $.post("/api/get_self_info", {"timestamp": 123}, function(data){
        data = JSON.parse(data);
        console.log(data.data.project);
        if(data.data.project.id == 0){
            $.post("/api/get_project_pool", {"timestamp": 1}, function(data){
                selectProject(data.data);
            }, "json")
        } else{
            html = ' <h2>已选项目</h2><div class="col-md-4"><div class="box box-warning box-solid"><div class="box-header with-border"><h3 class="boxtitle pro_title">' + data.data.project.id + data.data.project.name + '</h3>';
            html = html + '</div><div class="box-body pro_detail" style><h4>' + data.data.project.content +'   </h4>   </div>        </div>    </div>';
            $("#showProject").html(html)
        }
    })
})

function selectProject(data) {
    for (var i = 0; i<data.length; i++) {
        $(".pro_title").eq(i).html(data[i].id + data[i].name);
        $(".pro_detail").eq(i).append('<h4>' + data[i].detail + '</h4>')
    }
    var html = '<button type="button" class="btn btn-block btn-default" onclick="submitPro(this)">Confirm</button>'
    $('.pro_detail').append(html)
}

function submitPro(obj) {
    var proj_id = $(obj).parent().parent().find(".pro_title").text()[0]
    $.post("/api/set_studentproj", {"proj_id":proj_id, "timestamp":1}, function(data){
        $.post("/api/get_self_info", {"timestamp": 123}, function(data){
            data = JSON.parse(data);
            console.log(data)
            html = ' <h2>已选项目</h2><div class="col-md-4"><div class="box box-warning box-solid"><div class="box-header with-border"><h3 class="boxtitle pro_title">' + data.data.project.id + data.data.project.name + '</h3>';
            html = html + '</div><div class="box-body pro_detail" style><h4>' + data.data.project.content +'</h4></div></div></div>';
            $("#showProject").html(html)
        }) 
    })
}

