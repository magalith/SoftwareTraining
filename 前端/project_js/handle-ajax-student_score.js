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
for ( var i = 0; i < data.length; i++) {//循环json对象，拼接tr,td的html
    if (data[i].file === ''){

    
    html = html + '<tr>';
    html = html + '<td>' + data[i].id + '</td>';
    // html = html + '<td>' + data[i].student_name + '</td>';
    html = html + '<td>' + data[i].text + '</td>';
    html = html + '<td><span class="label label-success">点击上传</span></td>';
    html = html + '<td>' + data[i].score + '</td>';
    // html = html + '<td>								<form action="#" method="post">								  <div class="input-group">									<input type="text" name="message" placeholder="总分" class="form-control" style="width: 80px">																			  <button type="submit" class="btn btn-primary btn-flat">评分</button>																		  </div>								</form>							 </td>';
    html = html + '</tr>';
}
}
$('#table_filecheck1').append(html);

var html = '';
for ( var i = 0; i < data.length; i++) {//循环json对象，拼接tr,td的html
    if (data[i].file === ''){}

    else{
    html = html + '<tr>';
    html = html + '<td>' + data[i].id + '</td>';
    // html = html + '<td>' + data[i].student_name + '</td>';
    html = html + '<td>' + data[i].text + '</td>';
    html = html + '<td><span class="label label-success">' + data[i].file + '</span></td>';
    html = html + '<td>' + data[i].score + '</td>';
    // html = html + '<td>								<form action="#" method="post">								  <div class="input-group">									<input type="text" name="message" placeholder="总分" class="form-control" style="width: 80px">																			  <button type="submit" class="btn btn-primary btn-flat">评分</button>																		  </div>								</form>							 </td>';
    html = html + '</tr>';
}
}
$('#table_filecheck').append(html);

function deleteItem(e){
    console.log(e)
}
