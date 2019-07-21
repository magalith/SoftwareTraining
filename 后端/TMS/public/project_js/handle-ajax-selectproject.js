
$(function() {
    $.post("/api/get_project_pool", {"timestamp": 1}, function(data){
        selectProject(data);
    }, "json")
})

function selectProject(data) {
    data = data.data;
    for (var i = 0; i<data.length; i++) {
        $(".pro_title").eq(i).html(data[i].id + data[i].name);
        $(".pro_detail").eq(i).append('<h4>' + data[i].detail + '</h4>')
    }
    var html = '<button type="button" class="btn btn-block btn-default" onclick="submitPro(this)">Confirm</button>'
    $('.pro_detail').append(html)
}

function submitPro(obj) {
    var proj_id = $(obj).parent().parent().find(".pro_title").text()[0]
    console.log(proj_id)
}
