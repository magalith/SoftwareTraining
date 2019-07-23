
$(function(){
    $.post("/api/get_stage", {"timestamp": 1}, function(data){
        data = data.data;

        load_missionlist(data)
        // addtext_to_list(data)
    }, "json")

    $('.addlist').on("click", addtext_to_list)

})


function load_missionlist(data){
    
    for (var i=0; i<data.length; i++){
        title = '<h4 class="title_hidden">' + data[i].id + '</h4>'
        $('.missionlist').eq(data[i].stage_number).append(title)
        // console.log(data[i].missions)
        if (data[i].missions.length !== 0) {
            for (var j=0; j<data[i].missions.length; j++) {
                task_name = data[i].missions[j].text.split(";;;")[0];
                task_detail = data[i].missions[j].text.split(";;;")[1];
                task_ddl = data[i].missions[j].deadline;
                var html = '';
                html += '<li style="font-size: 20px"><a href="/tch_check_studoc"><h3>任务名称：' + task_name + '</h3></a></li>';
                html += '<li>详细描述：' + task_detail + '</li>';
                html += '<li>截止日期：' + task_ddl + '</li>';
                $('.missionlist').eq(data[i].stage_number).append(html)
            }
        }
    }
    
}


function addtext_to_list(){
    stage_id = $('.addlist').index(this)
    // id = data[stage_id].id;
    id = $('.title_hidden').eq(stage_id).text();
    console.log(id)
    $('.addlist').on("click", addtext_to_list)

    var title = $('.title').eq(stage_id).val();
    var discription = $('.discription').eq(stage_id).val();
    var deadline = $('.deadline').eq(stage_id).val();
    if(title != "" && title != null && discription != "" && discription != null && deadline != "" && deadline != null) {
        datap = {"timestamp": 1, "stage_id": id, "mission": '{"text":"' + title+';;;'+discription + '", "file": "", "deadline": "30"}'}
        console.log(datap)
        $.post("/api/push_mission", datap)
        var html = '';
        html += '<li style="font-size: 20px"><a href="/tch_check_studoc"><h3>任务名称：' + title +'</h3></a></li>';
        html += '<li>详细描述：' + discription + '</li>';
        html += '<li>截止日期：' + deadline + '</li>';
        $('.missionlist').eq(stage_id).append(html)
        $('.title').val("");
        $('.discription').val("");
        $('.deadline').val("");
    } else{
        alert("请输入完整添加内容")
        $('.title').val("")
        $('.discription').val("")
        $('.deadline').val("");
    }
}