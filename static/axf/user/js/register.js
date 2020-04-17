$(function(){

    var flag = false;
    var flag1 = false

    $('#exampleInputName').blur(function () {
        //前端验证
        // var name = $(this).val();
        //
        // var reg = /^[a-zA-Z]{3,6}$/;
        //
        // var b = reg.test(name);
        //
        // if(b){
        //     // $('#nameinfo').html('用户名字正确✔').css({'color':'green','font-size':'15px'});
        //
        //
        //
        // }else {
        //     $('#nameinfo').html('用户名字格式不正确❌').css({'color':'red','font-size':'15px'});
        // }
        //



        //后端验证
        // var name  = $(this).val();
        //
        //
        // //$.getJSON(请求资源路径，请求参数，返回值)
        // //'/axfuser/checkName/' 是请求资源路径
        // // {'name':name} 是参数   ‘name’是变量名字   name  变量值
        // //data就是视图函数的返回值
        //
        // $.getJSON('/axfuser/checkName/',
        //           {'name':name},
        //           function (data) {
        //               if(data['status']==200){
        //                     $('#nameinfo').html(data['msg']).css({'color':'green','font-size':'15px'})
        //               }else{
        //                     $('#nameinfo').html(data['msg']).css({'color':'red','font-size':'15px'})
        //               }
        //           })


        var name = $(this).val();

        var reg = /^[a-zA-Z]{3,6}$/;

        var b = reg.test(name);

        if(b){
                $.getJSON('/axfuser/checkName/',
                  {'name':name},
                  function (data) {
                      if(data['status']==200){
                            $('#nameinfo').html(data['msg']).css({'color':'green','font-size':'15px'})
                            flag1 = true;
                      }else{
                            $('#nameinfo').html(data['msg']).css({'color':'red','font-size':'15px'})

                      }
                  })

        }else {
            $('#nameinfo').html('用户名字格式不正确❌').css({'color':'red','font-size':'15px'});


        }


    })

    $('#exampleInputPassword2').blur(function () {
            var password = $('#exampleInputPassword1').val();
            var confirmpassword = $(this).val();

            if(password == confirmpassword){
                $('#passwordinfo').html('密码一致').css({'color':'green','font-size':'15px'});
                flag = true;
            }else{
                $('#passwordinfo').html('密码不一致，请重新输入').css({'color':'red','font-size':'15px'});
            }


        })


    $('form').submit(function () {
        var b = flag & flag1;

        if(b==1){
            var password = $('#exampleInputPassword1').val();
            password = md5(password);
            alert(password);
            $('#exampleInputPassword1').val(password);

            return true;
        }else{
           $('#nameinfo').html('用户名字格式不正确❌').css({'color':'red','font-size':'15px'});
           $('#passwordinfo').html('密码不一致，请重新输入').css({'color':'red','font-size':'15px'});
           return false;
        }

    })


})