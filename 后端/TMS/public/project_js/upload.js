$(document).ready(function(){

	var inputCover = $(".inputCover");
	var processNum = $(".processNum");
	var processBar = $(".processBar");

	//上传准备信息
	$("#file").change(function(){
		var file = document.getElementById('file');
		var fileName = file.files[0].name;
		var fileSize = file.files[0].size;
        processBar.css("width",0); 
		if(fileSize > 1024*2*1024*1024*1024){
			inputCover.html("<font>文件过大，请重新选择</font>");
			processNum.html('未选择文件');
			document.getElementById('file').value = '';
			return false;
		}else{
			inputCover.html(fileName+' / '+parseInt(fileSize/1024)+'K');
			processNum.html('等待上传');
		}
	})

	//提交验证
	$(".submit").click(function(){
		if($("#file").val() == ''){
			alert('请先选择文件！');
		}else{
			upload();
		}
	})

	//创建ajax对象，发送上传请求
	function upload(){
		var file = document.getElementById('file').files[0];
		var csrf = $("[name='csrfmiddlewaretoken']").val();
		console.log(csrf)
		var form = new FormData();
		form.append('myfile',file);
		form.append('csrfmiddlewaretoken',csrf);
		$.ajax({
			url: '../upload_ajax/',
			async: true,
			type: 'post',
			data: form,
			processData: false,
 			contentType: false,
 			xhr:function(){                        
                myXhr = $.ajaxSettings.xhr();
                if(myXhr.upload){
                    myXhr.upload.addEventListener('progress',function(e){                            
                        var loaded = e.loaded;
                        var total = e.total;
                        var percent = Math.floor(100*loaded/total);
                        processNum.text(percent+"%");       
                        processBar.css("width",percent+"px");                                                                
                    }, false);
                }
                return myXhr;
            },
 			success: function(data){
 				console.log("文档当前位置是："+data);
 				document.cookie = "url="+data;
 				$(".submit").text('上传成功');
 				$(".upagain").css("display","block");
 				$(".show").html('文件上传成功，地址是：<a href="'+data+'" target="_blank">'+data+'</a>');
 			}
		})
	}

	//继续上传
	$(".upagain").click(function(){
		$("#file").click();
		processNum.html('未选择文件');
        processBar.css("width",0); 
        $(".submit").text('上传');
		document.getElementById('file').value = '';
		$(this).css("display","none");
	})
})