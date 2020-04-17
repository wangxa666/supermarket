function changeCode(){
    var i = document.getElementById('icode');
    i.src = '/axfuser/get_code/?'+Math.random();
}



function parse() {

    alert(1);

    var password = document.getElementById('exampleInputPassword1').value;


    var password1 = md5(password);

    document.getElementById('exampleInputPassword1').value=password1

    return true;
}