var data = 
[
        {
            "id": "M_001",
            "text": "作业一",
            "file": "http://0.0.0.0/a.txt", 
            "deadline": "截止日期:19.19273.2"
        }, 
        {
            "id": "M_002",
            "text": "作业二",
            "file": "http://0.0.0.0/b.txt", 
            "deadline": "截止日期:19.19273.2"
        }, 
        {
            "id": "M_002",
            "text": "作业二",
            "file": "http://0.0.0.0/b.txt", 
            "deadline": "截止日期:19.19273.2"
        }, 
        {
            "id": "M_002",
            "text": "作业二",
            "file": "http://0.0.0.0/b.txt", 
            "deadline": "截止日期:19.19273.2"
        }
]



$(function(){
    load_missionlist();
    $('.addlist').on("click", addtext_to_list)
})


function load_missionlist(){
    var html = '';
    for ( var i = 0; i < data.length; i++) {
        html += '<li style="font-size: 20px"><a href="teacher_file_check.html"><h3>' + data[i].text +'</h3></a></li>';
        html += '<li>' + data[i].deadline + '</li> <br/>';
        html += ''
        $('.missionlist').eq(i).append(html);
        html = ''
}
}


function addtext_to_list(){
    // var tit = $(this).parent().prev().find("input").eq(0).val();
    console.log($(this).index())
    var title = $('.title').val();
    var discription = $('.discription').val();
    if(title != "" && title != null && discription != "" && discription != null )
    {
        // console.log(tit);
        html = '';
        html += '<li style="font-size: 20px"><a href="teacher_file_check.html"><h3>' + title +'</h3></a></li>';
        html += '<li>' + discription + '</li> <br/>';

        $(this).parent().parent().parent().parent().prev().find(".missionlist").append(html)
        // $('.missionlist').append(html);
        $('.title').val("");
        $('.discription').val("");

    } 
    else 
    {
        alert("请输入完整添加内容")
        $('.title').val("")
        $('.discription').val("")

    }


}