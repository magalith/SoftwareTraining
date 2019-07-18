var data = 
[
        {
            "id": "M_001",
            "text": "作业一",
            "file": "http://0.0.0.0/a.txt", 
            "deadline": "截止日期:19.19273.2 作业要求"
        }, 
        {
            "id": "M_002",
            "text": "作业二",
            "file": "http://0.0.0.0/b.txt", 
            "deadline": "截止日期:19.19273.2 作业要求"
        }, 
        {
            "id": "M_002",
            "text": "作业二",
            "file": "http://0.0.0.0/b.txt", 
            "deadline": "截止日期:19.19273.2 作业要求"
        }, 
        {
            "id": "M_002",
            "text": "作业二",
            "file": "http://0.0.0.0/b.txt", 
            "deadline": 1563346789
        }
]


var html = '';
for ( var i = 0; i < data.length; i++) {
    html = html + '<li style="font-size: 20px">' + data[i].text +'</li>';
    html = html + '<li>' + data[i].deadline + '</li> <br/>';
    $('.missionlist').eq(i).append(html);
    html = ''
}


function deleteItem(obj){
    $(obj).parent().parent().remove();
}
