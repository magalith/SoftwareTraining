
$(function() {
    $.post("/api/get_students", {"timestamp": 123}, function(data){
        loadStuList(data)
    }, "json");
})

function loadStuList(data){
    data = data.data;
    var html = '';
    for ( var i = 0; i < data.length; i++) {//循环json对象，拼接tr,td的html
        html = html + '<tr>';
        html = html + '<td>' + data[i].id + '</td>';
        html = html + '<td>' + data[i].stuname + '</td>';
        html = html + '<td>' + data[i].class + '</td>';
        html = html + '<td><span class="label label-success">' + data[i].teacher + '</span></td>';
        html = html + '<td>' + data[i].note + '</td>';
        html = html + '<td><span class="glyphicon glyphicon-trash" onclick="deleteItem(this)"></span></td>';
        html = html + '</tr>';
    }
    $('#table_test').append(html);
}

function deleteItem(obj){
    $(obj).parent().parent().remove();
    $.post("/api")
}