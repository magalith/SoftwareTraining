data = [
    {
        "period_id": 1,
        "id": "M_001",
        "text": "作业一",
        "file": "http://0.0.0.0/a.txt",
        "deadline": 1563349746
    },
    {
        "period_id": 2,
        "id": "M_002",
        "text": "作业二",
        "file": "http://0.0.0.0/b.txt",
        "deadline": 1563346789
    },
    {
        "period_id": 3,
        "id": "M_002",
        "text": "作业二",
        "file": "http://0.0.0.0/b.txt",
        "deadline": 1563346789
    },
    {
        "period_id": 1,
        "id": "M_001",
        "text": "作业一",
        "file": "http://0.0.0.0/a.txt",
        "deadline": 1563349746
    },
    {
        "period_id": 2,
        "id": "M_002",
        "text": "作业二",
        "file": "http://0.0.0.0/b.txt",
        "deadline": 1563346789
    },
    {
        "period_id": 3,
        "id": "M_002",
        "text": "作业二",
        "file": "http://0.0.0.0/b.txt",
        "deadline": 1563346789
    }
]

var html = ''
for (i=0; i<data.length; i++) {
    if (data[i].period_id === 1) {
        html += '<li><a><h3>' + data[i].text + '</h3></a></li><li>' + data[i].deadline + '</li>';
        $('.missionlist').eq(0).append(html);
        html = ''
    } else if (data[i].period_id === 2) {
        html += '<li><a><h3>' + data[i].text + '</h3></a></li><li>' + data[i].deadline + '</li>';
        $('.missionlist').eq(1).append(html);
        html = ''
    } else {
        html += '<li><a><h3>' + data[i].text + '</h3></a></li><li>' + data[i].deadline + '</li>';
        $('.missionlist').eq(2).append(html);
        html = ''
    }
}