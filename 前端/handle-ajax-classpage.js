var data = [{
    "class_name": "01",
    "teacher": "teacher_a",
    "students": [1001, 1002, 1003, 244]
    },
    {
    "class_name": "02",
    "teacher": "teacher_a",
    "students": [1001, 1002, 1003]
    },
    {
    "class_name": "03",
    "teacher": "teacher_a",
    "students": [1001, 1002, 1003]
    }]



for (var i = 0; i < data.length; i++) {//将班级名称加入列表中
    var html = '	<div class="col-md-4"> <!-- Widget: user widget style 1 --><div class="box box-widget widget-user-2">    <!-- Add the bg color to the header using any of the bg-* classes -->    <div class="widget-user-header bg-blue">        <!--<div class="widget-user-image">            <img class="img-circle" src="../dist/img/user7-128x128.jpg" alt="User Avatar">        </div>-->        <!-- /.widget-user-image -->        <h5 class="widget-user-username class_name_tag">';
    html = html + data[i].class_name + '班';
    html = html + '</h5>   </div>   <div class="box-footer no-padding">        <ul class="nav nav-stacked">            <li><a href="#">学生人数 <span class="pull-right badge bg-blue">';
    html = html + data[i].students.length + '</span></a></li>            <li><a href="#">负责老师 <span class="pull-right badge bg-aqua">';
    html = html + data[i].teacher + '李老师</span></a></li>            <!--<li><a href="#">Completed Projects <span class="pull-right badge bg-green">12</span></a></li>            <li><a href="#">Followers <span class="pull-right badge bg-red">842</span></a></li>-->        </ul>    </div></div><!-- /.widget-user --></div>';
    $('#class_name_tag').append(html);
    html = ''
}

function deleteItem(e){
    console.log(e)
}