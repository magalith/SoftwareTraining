
$(function() {
    $.post("/api/get_project_pool", {"timestamp": 1}, function(data){
        selectProject(data.data);
        // chooseProject(data_choose);
        
    }, "json")
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
        data = $.parseJSON( data );
        // console.log(data.data)
        html = ' <h2>已选项目</h2> <div class="col-md-4">        <div class="box box-warning box-solid ">            <div class="box-header with-border">                <h3 class="boxtitle pro_title" >'+data.data.project.id + data.data.project.name +' </h3>';
        html = html + '     </div>            <div class="box-body pro_detail" style> <h4>  '+ data.data.project.detail +'   </h4>   </div>        </div>    </div>';
        $("#showProject").html(html)
       
        // $(".pro_title").eq(0).html(data[0].id + data[0].name);
        // $(".pro_detail").eq(0).append('<h4>' + data[0].detail + '</h4>')
        // console.log(proj_id)
    })

}

