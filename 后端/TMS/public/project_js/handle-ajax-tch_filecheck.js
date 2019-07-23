$(function(){
    mission_id = window.location.search.slice(-1);
    $.post("/api/check_mission", {"timestamp": 123, "mission_id": mission_id}, function(data){
        data = JSON.parse(data);
        data = data.data;
        showScore(data);
        obj = {M_id: mission_id, data: data}
        $('#submit_score').click(obj, submitScore);
    })
})


function showScore(data){
    var html = '';
    for ( var i = 0; i < data.length; i++) {//循环json对象，拼接tr,td的html
        html += '<tr class="stu_score">';
        html += '<td>' + data[i].id + '</td>';
        html += '<td>' + data[i].user.name + '</td>';
        html += '<td>' + data[i].text + '</td>';
        html += '<td><span class="label label-success">' + data[i].file + '</span></td>';
        html += '<td class="score">' + data[i].score + '</td>';
        html += '<td><input type="text" name="message" placeholder="score" class="form-control" style="width: 60px" onchange="handleScoreChange(this)">'
        html += '</td></tr>';
    }
    $('#table_filecheck').append(html);
}

function handleScoreChange(obj){
    const value = obj.value;
    $(obj).parent().prev().text(value);
}

function submitScore(event){
    data = event.data.data;
    M_id = event.data.M_id;
    console.log(data);
    console.log(M_id);
    score = []
    for(var i=0; i<data.length; i++){
        stu_score = $('.stu_score').eq(i).find('.score').text();
        score.push('{"did": ' + data[i].id + ',"score":' + stu_score + '}')
    }
    score = score.toString();
    console.log(score.toString())
    trans_data = '{"timestamp": 123, "mission_id": ' + M_id + ', "score": [' + score + ']}';
    $.post("/api/set_score", {"timestamp": 123, "mission_id": M_id , "score": '[' + score + ']'}, function(data){
        console.log(data);
    })
}

