
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
            html += '<td><input type="file" name="file" id="file_submit"></input></td>';
            html += '<td><button type="submit" class="btn btn-primary btn-flat btn-sm" id="submit_file" onclick="file_submit">submit</button></td>';
            html += '</tr>';
            $('#check_untask').append(html)
            html = ''
        }else{
            html += '<tr>';
            html += '<td>' + data[i].id + '</td>';
            html += '<td>' + data[i].text + '</td>';
            html += '<td><a href="' + data[i].file + '">下载附件</a></td>';
            html += '<td>' + data[i].score + '</td>';
            html += '</tr>';
            $('#check_task').append(html)
            html = ''
        }
    }
}

function deleteItem(e){
    console.log(e)
}


function file_submit() {
    var file=$("#submit_file").files()
    $.post("/api/push_doc", {"timestamp": 1, "mission_id": "mi_01", "text": "", "file": file})
    // console.log($(this).index())

}




