
$(function(){
    $.post("/api/get_missions", {'timestamp': 1}, function(data){
        loadDocumentList(data);
    }, "json")
})

function loadDocumentList(data) {
    data = data.data;
    var html = '';
    for (var i=0; i<data.length; i++){
        if(data[i].docs.length === 0) {
            html += '<tr>';
            html += '<td>' + data[i].id + '</td>';
            html += '<td>' + data[i].text.split(";;;")[0] + '</td>';
            html += '<td>' + data[i].text.split(";;;")[1] + '</td>';
            html += '<form id="uploadForm" enctype="multipart/form-data"><td><input class="my_file" type="file" multiple="multiple"/></td>'
            html += '<td><button id="file_upload" type="button" class="btn btn-default btn-sm submit file_upload" onclick="upload(this)">上传文件</button></td></form>'
            html += '</tr>';
            $('#check_untask').append(html);
            html = ''
        }else{
            html += '<tr>';
            html += '<td>' + data[i].id + '</td>';
            html += '<td>' + data[i].text.split(";;;")[0] + '</td>';
            html += '<td>' + data[i].text.split(";;;")[1] + '</td>';
            html += '<td><a href="' + data[i].file + '" download="">下载附件</a></td>';
            html += '<td>' + data[i].score + '</td>';
            html += '</tr>';
            $('#check_task').append(html);
            html = ''
        }
    }
}

//创建ajax对象，发送上传请求
function upload(obj){
    // var file = document.getElementById('file_submit').files[0];
    var index = $('.file_upload').index(obj);
    console.log(index);
    var my_file = document.getElementsByClassName('my_file')[index].files[0];
    m_id = $(obj).parent().parent().find('td').eq(0).text();
    console.log($(obj).parent().parent().find('td').eq(0).text());
    // console.log(file)
    var my_form = new FormData();
    my_form.append('file', my_file);
    my_form.append('timestamp', 6666666);
    my_form.append('mission_id', m_id);
    my_form.append('text', "texttexttext");
    $.ajax({
        url: '/api/push_doc',
        // async: true,
        type: 'post',
        // data: {"timestamp":1, "mission_id":1, "text":"text", "file": my_file},
        data: my_form,
        // processData: false,
        //  contentType: false
        async: true,
        processData: false,
        contentType: false,
    })
    window.location.replace("/stu_doc_check")
}