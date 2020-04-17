$(function(){
    init_wheel();
    init_mustbuy();
})



function init_wheel() {
    var mySwiper = new Swiper('#topSwiper',{
                              loop:true,
                              autoplay:3000,
                              pagination:'.swiper-pagination',
                              autoplayDisableOnInteraction:false
    });
}


function init_mustbuy() {
    var mySwiper1 = new Swiper('#swiperMenu',{
                                slidesPerView:3
    })
}

