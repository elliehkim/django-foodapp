$('.plus-cart').click(function(){
    var id = $(this).attr("pid").toString();
    $.ajax({
        type:"GET",
        url:"/pluscart",
        data:{
            item_id:id
        },
        success:function(html){
            location.reload();
        }
    })
})

$('.minus-cart').click(function(){
    var id = $(this).attr("pid").toString();
    $.ajax({
        type:"GET",
        url:"/minuscart",
        data:{
            item_id:id
        },
        success:function(html){
            location.reload()
        }
    })
})


$('.remove-btn').click(function(){
    var id=$(this).attr('pid').toString();
    $.ajax({
        type:"GET",
        url:"/removecart",
        data:{
            item_id:id
        },
        success:function(data){
            location.reload()
        }
    })
})
