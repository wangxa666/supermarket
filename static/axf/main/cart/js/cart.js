//attr方法可以获取自带的属性值  也可以获取自定义的属性值
        //prop方法可以获取自带的属性值  不可以获取自定义的属性值

        // alert($button.attr('class'));
        // alert($button.prop('class'));

        // var $goodsid = $button.attr('goodsid');
        // var $goodsid1 = $button.prop('goodsid');



$(function () {
    $('.addShopping').click(function () {

        var $button = $(this);

        var $goodsid = $button.attr('goodsid');

        $.get('/axfcart/addToCart/',
              {'goodsid':$goodsid},
              function (data) {
                  if(data['status'] == 200){
                      $button.prev().html(data['c_goods_num']);
                  }else{
                      window.location.href='/axfuser/login/';
                  }
              })
    })


    $('.subShopping').click(function () {
        var $button = $(this);
        var $div = $button.parent().parent();
        var cartid = $div.attr('cartid');

        $.post('/axfcart/subCart/',
               {'cartid':cartid},
                function (data) {
                    if(data['status'] == 200){
                            $button.next().html(data['c_goods_num']);
                            $('#total_price').html(data['total_price']);
                        }else{
                            $div.remove();
                            $('#total_price').html(data['total_price']);
                        }if(data['is_all_select']){
                            $('#all_select').find('span').find('span').html('✔');
                        }else{
                            $('#all_select').find('span').find('span').html('');
                        }

                }
            )
    })


    $('.confirm').click(function () {
        var $div = $(this);

        var cartid = $div.parent().attr('cartid');

        $.ajax({
            url:'/axfcart/changeStatus/',
            data:{'cartid':cartid},
            type:'get',
            dataType:'json',
            success:function (data) {
                if(data['c_is_select']){
                    $div.find('span').find('span').html('✔');
                    $('#total_price').html(data['total_price']);
                }else{
                    $div.find('span').find('span').html('');
                    $('#total_price').html(data['total_price']);
                }if(data['is_all_select']){
                    $('#all_select').find('span').find('span').html('✔');
                }else{
                    $('#all_select').find('span').find('span').html('');
                }
            }
        })

    })


    $('#all_select').click(function () {
        var $confirm = $('.confirm');

        var select_list = [];
        var unselect_list = [];
        
        $confirm.each(function () {
            var $con = $(this);

            var cartid = $con.parent().attr('cartid');


            if($con.find('span').find('span').html()){
                select_list.push(cartid);
            }else{
                unselect_list.push(cartid);
            }
        })


        if(unselect_list.length > 0){
            $.getJSON('/axfcart/allSelect/',
                      {'cartlist':unselect_list.join('#')},
                      function (data) {
                          if(data['status'] == 200){
                              $confirm.find('span').find('span').html('✔');
                              $('#all_select').find('span').find('span').html('✔');
                              $('#total_price').html(data['total_price']);
                          }
                      })

        }else{
            $.get('/axfcart/allSelect/',
                      {'cartlist':select_list.join('#')},
                      function (data) {
                          if(data['status'] == 200){
                                $confirm.find('span').find('span').html('');
                              $('#all_select').find('span').find('span').html('');
                              $('#total_price').html(data['total_price']);
                          }
                      })
        }




    })



    $('#make_order').click(function () {
        //把购物车中的选中的商品放到了一个列表中
        //把购物车中的未选中的商品放到了一个列表中
        var $confirm = $('.confirm');

        var select_list = [];
        var unselect_list = [];

        $confirm.each(function () {
            var $con = $(this);

            var cartid = $con.parent().attr('cartid');


            if($con.find('span').find('span').html()){
                select_list.push(cartid);
            }else{
                unselect_list.push(cartid);
            }
        })


        if(select_list.length == 0){
            return
        }

        $.get('/axforder/makeOrder/',
               function (data) {
                   if(data['status'] == 200){
                       window.location.href='/axforder/orderDetail/?order_id='+data['order_id']
                   }
               })


    })




})