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
    html = html + '</h5>   </div>   <div class="box-footer no-padding">        <ul class="nav nav-stacked">            <li class="dropdown notifications-menu"><a href="#" class="dropdown-toggle" data-toggle="dropdown" aria-expanded="false">学生人数 <span class="pull-right badge bg-blue">';
    html = html + data[i].students.length + '</span></a> <ul class="dropdown-menu" style = "width:400px">              <li class="header">学生名单</li>              <li>                <ul class="menu">                             ';
    for (var j = 0; j < data.length; j++) { html = html + '<li> ' + data[j].teacher +' </li>'};
    html = html + '                </ul>              </li>              <li class="footer"></li>            </ul></li>            <li><a href="#">负责老师 <span class="pull-right badge bg-aqua">';
    
    
    
    // <li class="dropdown notifications-menu">
    //         <a href="#" class="dropdown-toggle" data-toggle="dropdown" aria-expanded="false">
    //           <i class="fa fa-bell-o"></i>
    //           <span class="label label-warning">10</span>
    //         </a>
    //         <ul class="dropdown-menu" >              <li class="header">You have 10 notifications</li>              <li>                <ul class="menu">                  <li>                    <a href="#">                      <i class="fa fa-users text-aqua"></i> 5 new members joined today                    </a>                  </li>                </ul>              </li>              <li class="footer"><a href="#">View all</a></li>            </ul>
    //       </li>
    html = html + data[i].teacher + '</span></a></li>            <!--<li><a href="#">Completed Projects <span class="pull-right badge bg-green">12</span></a></li>            <li><a href="#">Followers <span class="pull-right badge bg-red">842</span></a></li>-->        </ul>    </div></div><!-- /.widget-user --></div>';
    $('#class_name_tag').append(html);
    html = ''
}

function deleteItem(e){
    console.log(e)
}