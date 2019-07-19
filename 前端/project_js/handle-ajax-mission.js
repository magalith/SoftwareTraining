var data = 
[
        {
            "id": "M_001",
            "text": "作业一",
            "file": "http://0.0.0.0/a.txt", 
            "deadline": "截止日期:19.19273.2"
        }, 
        {
            "id": "M_002",
            "text": "作业二",
            "file": "http://0.0.0.0/b.txt", 
            "deadline": "截止日期:19.19273.2"
        }, 
        {
            "id": "M_002",
            "text": "作业二",
            "file": "http://0.0.0.0/b.txt", 
            "deadline": "截止日期:19.19273.2"
        }, 
        {
            "id": "M_002",
            "text": "作业二",
            "file": "http://0.0.0.0/b.txt", 
            "deadline": "截止日期:19.19273.2"
        }
]


var html = '';
for ( var i = 0; i < data.length; i++) {
    html += '<li style="font-size: 20px"><a href="teacher_file_check.html">' + data[i].text +'</a></li>';
    html += '<li>' + data[i].deadline + '</li> <br/>';
    html += ''
    $('.missionlist').eq(i).append(html);
    html = ''
}


function deleteItem(obj){
    $(obj).parent().parent().remove();
}
