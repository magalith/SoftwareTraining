
$(function(){
    $.post("/api/get_docs", {'timestamp': 1}, function(data){
        loadDocumentList(data);
    }, "json")
})

function loadDocumentList(data) {
    data = data.data;
    var html = '';
    for (var i=0; i<data.length; i++){
        if(data[i].file === '') {
            html += '<tr>';
            html += '<td>' + data[i].id + '</td>';
            html += '<td>' + data[i].text + '</td>';
            html += '<form id="uploadForm" enctype="multipart/form-data"><td><input id="file" type="file" name="file"/></td>'
            html += '<td><button id="upload" type="button" class="btn btn-default btn-sm" onclick="submitFile()">上传文件</button></td></form>'
            html += '</tr>';
            $('#check_untask').append(html);
            html = ''
        }else{
            html += '<tr>';
            html += '<td>' + data[i].id + '</td>';
            html += '<td>' + data[i].text + '</td>';
            html += '<td><a href="' + data[i].file + '" download="">下载附件</a></td>';
            html += '<td>' + data[i].score + '</td>';
            html += '</tr>';
            $('#check_task').append(html);
            html = ''
        }
    }
}
//未完成
function submitFile() {
    $.ajax({
        url: '/api/push_doc',
        type: 'POST',
        cache: false,
        data: new FormData($('#uploadForm')[0]),
        processData: false,
        contentType: false
    }).done(function(res){
        console.log(res)
    })
    // var file=$("#submit_file").files()
    // $.post("/api/push_doc", {"timestamp": 1, "mission_id": "mi_01", "text": "", "file": file})
}




