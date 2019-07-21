
$(function(){
    $.post("/api/get_teachers", {"timestamp": 123}, function(data){
        loadTeacherList(data);
    }, "json");
    $('#addlist').on("click", addtext_to_list)
})

function loadTeacherList(data){
    data = data.data;
    var html = '';
    for ( var i = 0; i < data.length; i++) {//循环json对象，拼接tr,td的html
        html = html + '<tr>';
        html = html + '<td>' + data[i].id + '</td>';
        html = html + '<td>' + data[i].name + '</td>';
        html = html + '<td>' + data[i].class + '</td>';
        html = html + '<td><span class="glyphicon glyphicon-trash" onclick="deleteItem(this)"></span></td>';
        html = html + '</tr>';
    }
    $('#table_tch_list').append(html);

}

function deleteItem(obj){
    $(obj).parent().parent().remove();
}

function addtext_to_list(){
    var username = $('#username').val();
    var guanliclass = $('#guanliclass').val();
    if(username != "" && username != null && guanliclass != "" && guanliclass != null ){
        console.log(username);
        html = '';
        html = html + '<tr>';
        html = html + '<td></td>';
        html = html + '<td>' + username + '</td>';
        html = html + '<td>' + guanliclass + '</td>';
        html = html + '<td><span class="glyphicon glyphicon-trash" onclick="deleteItem(this)"></span></td>';
        html = html + '</tr>';
        $('#table_tch_list').append(html);
        $('#username').val("")
        $('#guanliclass').val("")
    } else {
        alert("请输入完整添加内容")
        $('#username').val("")
        $('#guanliclass').val("")
    }
}