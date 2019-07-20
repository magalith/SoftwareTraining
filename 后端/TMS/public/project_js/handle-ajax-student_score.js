
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
            html += '<td><input type="file"></input></td>';
            html += '<td>' + data[i].score + '</td>';
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
