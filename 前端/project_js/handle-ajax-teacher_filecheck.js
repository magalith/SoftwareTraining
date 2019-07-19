var data = [
    
    {
        "id": "D_001",
        "text": "第一次作业.......",
        "file": "http://0.0.0.0/a.txt",
        "student_name": "aaaaaaa",
        "score": ''
    },
    {
        "id": "D_002",
        "text": "第二次作业.......",
        "file": "http://0.0.0.0/b.txt",
        "student_name": "bbbbbbb",
        "score": 90
    },
    {
    "id": "D_001",
        "text": "第一次作业.......",
        "file": "http://0.0.0.0/a.txt",
        "student_name": "aaaaaaa",
        "score": 85
    },
    {
        "id": "D_002",
        "text": "第二次作业.......",
        "file": "http://0.0.0.0/b.txt",
        "student_name": "bbbbbbb",
        "score": 90
    }
    ]


function showScore(){
    var html = '';
    for ( var i = 0; i < data.length; i++) {//循环json对象，拼接tr,td的html
        html += '<tr>';
        html += '<td>' + data[i].id + '</td>';
        html += '<td>' + data[i].student_name + '</td>';
        html += '<td>' + data[i].text + '</td>';
        html += '<td><span class="label label-success">' + data[i].file + '</span></td>';
        html += '<td>' + data[i].score + '</td>';
        html += '<td><form action="#" method="post">'
        html += '<input type="text" name="message" placeholder="score" class="form-control" style="width: 60px" onchange="handleScoreChange(this)">'
        html += '</form></td>';
        html += '</tr>';
    }
    $('#table_filecheck').append(html);
}

function handleScoreChange(obj){
    const value = obj.value;
    console.log(value);
    $(obj).parent().parent().prev().text(value);
    console.log($(obj).parent().parent().prev().text())
}

$(document).ready(showScore())

