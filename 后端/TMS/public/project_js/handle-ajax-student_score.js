
$(function(){
    $.post("/api/get_missions", {'timestamp': 1}, function(data){
        loadDocumentList(data);
    }, "json")

// $("#file_upload").click(upload);
})

function loadDocumentList(data) {
    data = data.data;
    var html = '';
    for (var i=0; i<data.length; i++){
        if(data[i].file === "" || data[i].file === null) {
            html += '<tr>';
            html += '<td>' + data[i].id + '</td>';
            html += '<td>' + data[i].text + '</td>';
            html += '<form id="uploadForm" enctype="multipart/form-data"><td><input id="my_file" type="file" multiple="multiple"/></td>'
          
            html += '<td><button id="file_upload" type="button" class="btn btn-default btn-sm submit" onclick="upload()">上传文件</button></td></form>'
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





	function uploadFormData(){
		if($("#my_file").val() == ''){
			alert('请先选择文件！');
		}else{
			upload();
		}
    }


	//创建ajax对象，发送上传请求
	function upload(){
		// var file = document.getElementById('file_submit').files[0];
        var my_file = document.getElementById('my_file').files[0];
        // console.log(file)
        var my_form = new FormData();
		my_form.append('file', my_file);
		my_form.append('timestamp', 6666666);
		my_form.append('mission_id', 1);
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

        // $.post('/api/push_doc', {"timestamp":1, "mission_id":1, "text":"text", "file":file}, function(data){
            // console.log("文档当前位置是："+data);
            // document.cookie = "url="+data;/
            // console.log('文件上传成功，地址是：<a href="'+data+'" target="_blank">'+data+'</a>');
        // })
   
    }