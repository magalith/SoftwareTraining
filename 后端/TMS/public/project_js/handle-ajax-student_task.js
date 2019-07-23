
$(function(){
    $.post("/api/get_missions", {"timestamp": 1}, function(data){
        getStuMission(data)
    }, "json")
})

function getStuMission(data) {
    data = data.data;
    var html = ''
    for (i=0; i<data.length; i++) {
        if (data[i].stage_number === 0) {
            html += '<li><a><h3>' + data[i].text + '</h3></a></li><li>' + data[i].deadline + '</li>';
            $('.missionlist').eq(0).append(html);
            html = ''
        } else if (data[i].stage_number === 1) {
            html += '<li><a><h3>' + data[i].text + '</h3></a></li><li>' + data[i].deadline + '</li>';
            $('.missionlist').eq(1).append(html);
            html = ''
        } else {
            html += '<li><a><h3>' + data[i].text + '</h3></a></li><li>' + data[i].deadline + '</li>';
            $('.missionlist').eq(2).append(html);
            html = ''
        }
    }
}