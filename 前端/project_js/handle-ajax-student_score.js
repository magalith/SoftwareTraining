var data = [
    
    {
        "id": "D_001",
        "text": "第一次作业.......",
        "file": "http://0.0.0.0/a.txt",
        // "student_name": "aaaaaaa",
        "score": 85
    },
    {
        "id": "D_002",
        "text": "第二次作业.......",
        "file": "http://0.0.0.0/b.txt",
        // "student_name": "bbbbbbb",
        "score": 90
    },
    {
    "id": "D_001",
        "text": "第一次作业.......",
        "file": "",
        // "student_name": "aaaaaaa",
        "score": ""
    },
    {
        "id": "D_002",
        "text": "第二次作业.......",
        "file": "http://0.0.0.0/b.txt",
        // "student_name": "bbbbbbb",
        "score": 90
    }
    ]

var html = '';
for (var i=0; i<data.length; i++){
    if(data[i].file === '') {
        html += '<tr>';
        html += '<td>' + data[i].id + '</td>';
        html += '<td>' + data[i].text + '</td>';
        html += '<td><span class="label label-success">点击上传</span></td>';
        html += '<td>' + data[i].score + '</td>';
        html += '</tr>';
        $('#check_untask').append(html)
        html = ''
    }else{
        html += '<tr>';
        html += '<td>' + data[i].id + '</td>';
        html += '<td>' + data[i].text + '</td>';
        html += '<td><span class="label label-success">' + data[i].file + '</span></td>';
        html += '<td>' + data[i].score + '</td>';
        html += '</tr>';
        $('#check_task').append(html)
        html = ''
    }
}
function deleteItem(e){
    console.log(e)
}
