
$(function() {
    $.post("/api/get_project_pool", {"timestamp": 1}, function(data){
        selectProject(data);
    }, "json")
})

function selectProject(data) {
    data = data.data;
    for (var i = 0; i<data.length; i++) {
        $(".pro_title").eq(i).html(data[i].name);
        $(".pro_detail").eq(i).append(data[i].detail)
    }
}
