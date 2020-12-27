$(function() {
    var blw=$("body").width();
    if(blw>1280 && blw != 1366){
        $(document).mousemove(function(e){
            var $target = $(e.target);
            var nav_classlist = $target[0].classList;
            if( ($target.parents().hasClass("header_left_item") || ($target).hasClass("header_left_item") || $target.parents().hasClass("home_submenu") || ($target).hasClass("home_submenu"))  == false ){
                $(".home_submenu").slideUp(200);
            }

        });
        // 点击导航下拉菜单
    $(".header_left .sub_nav").mouseover(function() {
        $(this).addClass("nav_focus");
        var i = $(this).index() / 2;
        $($(".home_submenu")[i]).stop().slideDown(200);
        $($(".home_submenu")[i]).siblings().stop().slideUp(200);

        $($(".home_submenu")[i]).mouseleave(function() {
            $($(".home_submenu")[i]).stop().slideUp(200);
        });
        $(this).stop().siblings().mouseover(function() {
            $($(".home_submenu")[i]).stop().slideUp(200);
        });
        // 导航成选中状态
        $(".header_left li").mouseover(function() {
            $(this).addClass("nav_focus");
        });
        $(".header_left li").mouseleave(function() {
            $(this).removeClass("nav_focus");
        });


        $(".home_submenu").mouseover(function() {
            var i = $(this).index()*2;
            $($(".header_left .sub_nav")[i]).addClass("nav_focus");
        });
        $(".home_submenu").mouseleave(function() {
            var i = $(this).index()*2;
            $($(".header_left .sub_nav")[i]).removeClass("nav_focus");
        });

    });
    }else if( blw == 1366 || blw<1281 ) {
        $(".header_left_item a").css("text-decoration","none")
        //平板隐藏下拉框
        $(".header_left .sub_nav").click(function() {
            $($(this).siblings()).removeClass("nav_focus");
            $(this).toggleClass("nav_focus");
            var i = $(this).index() / 2;
            $($(".home_submenu")[i]).stop().slideToggle(200);
            $($(".home_submenu")[i]).siblings().stop().slideUp(200);
        });
    }



    //导航语言
    $('.laguage_box #btnSelect').on('click', function() {
        $(".laguage_box .language-icon").toggleClass("rotate");
        $(this).siblings('.laguage_div').toggleClass('ulShow');
    });
    $('.laguage_box .laguage_div ul li').on('click', function() {
        var selTxt = $(this).text();
        $('.laguage_box #btnSelect').text(selTxt);
        $('.laguage_div').removeClass('ulShow');
    });
    //AD国家选择
    $('.country-icon').click(function () {
        $('.country_box #btnSelect').click()
    });
    $('.country_box #btnSelect').on('click', function() {
        $(this).siblings('.laguage_div').toggleClass('ulShow');
    });
    $('.country_box .laguage_div ul li').on('click', function() {
        var selTxt = $(this).text();
        var i =$(this).index();
        $('.country_box #btnSelect').text(selTxt);
        $('.laguage_div').removeClass('ulShow');

        $('.AD_section').addClass('hide');
        $($('.AD_section')[i]).removeClass('hide');
    });


    // products切换
    $(".dt_title_box li").click(function() {
        $(this).addClass("red_button");
        $(this).removeClass("grey_button");

        $(this).siblings().removeClass("red_button");
        $(this).siblings().addClass("grey_button");

		var dt_i = $(this).index();
		$($(".dt_content")[dt_i]).removeClass("hide");
		$($(".dt_content")[dt_i]).siblings().addClass("hide");
        var dt_btn = $($(".dt_content")[dt_i]).find(".dt_btn");
        dt_btn.fadeIn();
        var hide_ele = $(".dt_content").eq(dt_i).find(".dt_content_item")[7];
        $(hide_ele).nextAll().addClass("hide");
	});
	
	// products more
	/*var pds_ele = $(".dt_content_item").eq(8);
	var pds_eles = $($(pds_ele).nextAll()).addClass("hide");*/

    $(".dt_btn button").click(function(){
        $(".dt_content_item").removeClass("hide");
        $(".dt_btn").hide();
    });

    // 产品详情模块
    $(".pi_content_nav li").click(function() {
        $(this).addClass("red_button");
        $(this).removeClass("grey_button");
        $(this).siblings().removeClass("red_button");
        $(this).siblings().addClass("grey_button");

        var i = $(this).index();
        $($(".pi_content_item")[i]).siblings().addClass("hide");
        $($(".pi_content_item ")[i]).removeClass("hide");
    });


    // download模块
    $(".downl_header .dt_title_item ").click(function () {

        var i = $(this).index();
        $($(".download_content_box")[i]).siblings(".download_content_box").addClass("hide");
        $($(".download_content_box")[i]).removeClass("hide");
    })

    // download更多
    dl_leng = 3;
    for(i=0;i<dl_leng;i++){
        var dol_li_len =  $($(".download_content_ul")[i]).children("li").length;
        if(blw>768){
            var dol_ele = $($(".download_content_ul")[i]).children("li").eq(7);
            $($(dol_ele).nextAll("li")).addClass("hide");
        }else {
            var dol_ele = $($(".download_content_ul")[i]).children("li").eq(3);
            $($(dol_ele).nextAll("li")).addClass("hide");
            if(dol_li_len<4){
                $($(".download_content_ul")[i]).next(".view_more_btn").hide();
            }
        }
    }

    $(".download_content_title .red_text").click(function(){
        var dol_ele = $($(this).parents(".download_content")).find(".download_content_ul").children("li").eq(7);
        $($(dol_ele).nextAll("li")).toggle();
    });

    // 产品详情模块751
    $(".product_title_751").click(function() {
        var i = ($(this).index()+12)/2;
        // $($(".pi_content_item")).addClass("hide");
        $($(".pi_content_item ")[i]).toggle();
        $($(this).find("span")).toggleClass("rotate");
    });

    //产品详情切图
    $(".pi_imgs li").click(function(){
        var img_src = $(this).find("img").attr("src");
        $(".pi_header_left img").attr("src",img_src);
    });

    // Feedback隐藏表单按钮
    $(".ts_header_title a").click(function () {
        $(this).toggleClass("rotate");
        $(".ts_header_content").slideToggle(500);
    });

    // faqs问题隐藏
    //

if(blw<769){
    $(".faqs_btm_right_box_751 .faqs_btm_right li").click(function () {
        $($(this).next(".faqs_btm_right_content")).slideToggle(200);
        $(this).find('span').toggleClass("rotate");
        $(this).find("p").toggleClass("faqs_bl_red");
    });

    $(".faqs_btm").on('click', ".faqs_btm_right_box_751_shearch .faqs_btm_right li" ,function () {
        $($(this).next(".faqs_btm_right_content")).slideToggle(200);
        $(this).find('span').toggleClass("rotate");
        $(this).find("p").toggleClass("faqs_bl_red");
    });

}else {
    $(".faqs_btm").on('click', ".faqs_btm_right li" ,function () {
        $($(this).next(".faqs_btm_right_content")).slideToggle(200);
        $(this).find('span').toggleClass("rotate");
        $(this).find("p").toggleClass("faqs_bl_red");
    });
}


    // faqs模块切换
    $(".page_header_nav li").click(function() {
        $(".page_header_nav .red_button").removeClass("red_button");
        $(this).addClass("red_button");

        var i = $(this).index();
        $("#faqs_search_list").hide();
        $(".faqs_btm_left").show()
        $(".faqs_btm_right_box .faqs_btm_right").hide();
        $($(".faqs_btm_right_box .faqs_btm_right ")[i]).show();
        $(".faqs_btm_left h3").hide();
        $($(".faqs_btm_left h3")[i]).show();


        //UPDATA INFO
        // var z = $(this).index();
        // $($(".ui_content")[i]).siblings().addClass("hide");
        // $($(".ui_content")[i]).removeClass("hide");
    });

    $(".faqs_btm").on('click',".faqs_search",function () {
    $(".page_header_nav li").removeClass("red_button");
    $(".faqs_btm .faqs_btm_left h3").hide();
        switch ($(this).attr('id')) {
            case "index_DiagnosticTool":
                $($(".page_header_nav li")[0]).addClass("red_button");
                $($(".faqs_btm .faqs_btm_left h3")[0]).show();
                break;
            case "index_TPMS":
                $($(".page_header_nav li")[1]).addClass("red_button");
                $($(".faqs_btm .faqs_btm_left h3")[1]).show();
                break;
            case "index_ADAS":
                $($(".page_header_nav li")[2]).addClass("red_button");
                $($(".faqs_btm .faqs_btm_left h3")[2]).show();
                break;
            case "index_IMMOTool":
                $($(".page_header_nav li")[3]).addClass("red_button");
                $($(".faqs_btm .faqs_btm_left h3")[3]).show();
                break;
        }
    })



    //faqs viewmore
    if( $($(".faqs_btm_right .view_more_btn").prev("ul")).find("li").length < 7){
        $(this).addClass("hide");
    }

    $(".faqs_btm_right .view_more_btn").click(function () {
        var faqs_li = $($(this).prev("ul")).find("li");

        if ($(this).hasClass("pack_up")){
            $(this).removeClass("pack_up");
            $(faqs_li).addClass("hide");
            $(".faqs_btm_right_content").hide();
            $(".faqs_btm_right li > p .fqas-icon").addClass("rotate");
            $(".faqs_btm_right li > p" ).removeClass("faqs_bl_red");

            var faqs_ele = $(faqs_li).eq(7);
            $($(faqs_ele).prevAll("li")).removeClass("hide");
        }else{
            $(faqs_li).removeClass("hide");
            $(this).addClass("pack_up");
        }

    })
    //faqs字体
    $(".faqs_btm_right p").css("font-family","Helvetica, Regular, Verdana, Arial");
    $(".faqs_btm_right span").css("font-family","Helvetica, Regular, Verdana, Arial");

    //UPDATA INFO 隐藏按钮
    uic_len = $(".ui_content li").length;
    var pds_ele = $(".ui_content li").eq(3);
    var pds_eles = $($(pds_ele).nextAll()).hide();
    if( uic_len<4 ){
        $(".ui_btn_box .view_more_btn").hide();
        $(".ui_content ul").css("margin-bottom","100px")
    }
    $(".ui_btn_box .view_more_btn").click(function () {
        $(".ui_content li").show();
    })

    // 751faqs模块切换

    $($(".fqas-icon_751")[0]).addClass("rotate");
    $($(".faqs_btm_right_title")[0]).addClass("noneborder");
    $(".faqs_btm_right_title").click(function() {
        $($(this).find("span")).toggleClass("rotate");
        $($(this).next("ul")).slideToggle(200);
    });

    if($(this).hasClass("noneborder" )== false){
        $(this).css("border-bottom","none");
        $(this).addClass("noneborder")
    }else if($(this).hasClass("noneborder") ) {
        $(this).css("border-bottom","solid 1px #cccccc");
        $(this).removeClass("noneborder");
    }


    // 首页products边框变长
    // $(".home_scroll_content_item").mouseenter(function () {
    //     var i =$(this).index();
    //     $($(".products_box")[i]).css("height","401px");
    //     $($(".products_box")[i-1]).css("height","401px");
    // });
    //
    // $(".home_scroll_content_item").mouseleave(function () {
    //     var i =$(this).index();
    //     $($(".products_box")[i]).css("height","315px");
    //     $($(".products_box")[i-1]).css("height","315px");
    // });
    //news新闻集合按钮
    // if($(".ln_box li").length < 4 ){
    //     $(".new_button").hide();
    // }
    // $(".new_button").click(function () {
    //     $(".ln_box li").css("display","flex");
    //     $(this).hide();
    // });




    // 首页products点图片跳转
$("#js_dt_content .dt_content_item").click(function () {
    var a_src = $($(this).find("a")[0]).attr("href");
    window.location.href = a_src;
})

    // where to buy 地区切换
    $(".wtb_div .area_btn").click(function () {
        var i = $(this).index();
    $(".wtb_area_box .wtb_area").addClass("hide");
    $($(".wtb_area_box .wtb_area")[i]).removeClass("hide");
    })
//搜索回车功能
    var isFocus=$(".header_serch_input").focus(function () {
        $(document).keydown(function(event){
            if (event.keyCode == 13){
                upSearch();
            }
        })
    });

    //751signout
    $(".header_right-751").click(function (){
            $(".sign_submenu_751").toggle();
    })

//751languae
    $(".lan_box751div").hide()
    $(".foot_lan_box").click(function () {
        $(".lan_box751div").toggle()
    })

    // 751顶部下拉
    $(".header_left-751").click(function () {
        $(".header_left-751").toggleClass("header_left2-751");
        if($(this).hasClass("header_left2-751")){
            $(".header_nav_751").show();
            $(".submenu_751" ).hide();
        }else {
            $(".header_nav_751").hide();
            $(".submenu_751" ).hide();
        }
    });
//751搜索

    $('.header_serch_input').on('keyup',function(){
        var search_input = $(".header_serch_input");
        for(i=0;i<search_input.length;i++){
            $(search_input[i]).val($(this).val());
        }
    });


    // 751点击二级菜单
    $(".header_nav_751 .sub_nav").click(function () {
        var search_input = $(".submenu_751 .header_serch_input");

        $(".home_submenu").unbind();
        var i = ($(this).index()-1)/2;
        $($(".submenu_751_box .submenu_751")[i]).toggle();
        $(".header_nav_751").toggle();
    });
    //菜单退回
    $(".submenu_751_header").click(function () {
        $($(this).parents(".submenu_751")).toggle();
        $(".header_nav_751").toggle();
    });
    //751dwonload点击显示
    $(".download_content_ul li").click(function () {
        $(".download_hover_content ").not($(this).find(".download_hover_content ")).hide();
        $(this).find(".download_hover_content ").toggle();
    });
    //751dwonload viewmoew
    for(i=0;i<dl_leng;i++) {
        var dol_ele = $($(".download_content")[i]).children(".download_content_ul").children("li").length;
        if(dol_ele<3){
            $($(".download_content")[i]).find(".view_more_btn").hide();
        }
    }

    $(".download_content .view_more_btn").click(function () {
        var dol_ele = $($(this).parents(".download_content")).children(".download_content_ul").children("li").eq(3);
        $($(dol_ele).nextAll("li")).toggle();
        if( $(this).text() == "VIEW MORE"){
            $(this).text("Put more");
        }else{
            $(this).text("VIEW MORE");
        }

    })

    // 751dwonload导航切换
    $(".ui_nav_751 li").click(function () {
        var ctext = $($(this).find("a")).text();
        $(".ui_page_header751 h3").html(ctext + "<span class=\"arrow_down-icon751\"></span>");
    })

//about autel新闻点more
    var stitle_len = $(".abus_mid_frist_item p").length;
    for(i=0;i<=stitle_len;i++){
        var sTitle = $($(".abus_mid_frist_item p")[i]).text();
        var ab_span = $("<span class='hide'></span>");
        ab_span.html(sTitle);

        if(sTitle.length>140 ){
            sTitle = sTitle .substring(0,140)+"<a class=\"red_text\">…more<span class=\"db_arrow-icon\"></span></a>";
            $($(".abus_mid_frist_item p")[i]).html(sTitle);
            $($(".abus_mid_frist_item")[i]).append(ab_span);
        }
    }

    // $(".abus_mid_frist_item .red_text").click(function () {
    //     var allText = $(this).next("span").text();
    //     $(this).parent("p").html(allText+"<a class=\"short_content\">more<span class=\"db_arrow-icon\"></span></a>");
    // })

    $(".abus_mid_frist_item").on('click',".red_text", function() {
        var allText = $(this).parent("p").next("span").text();
        $(this).parent("p").html(allText+"<a class=\"short_content\">more<span class=\"db_arrow-icon\"></span></a>");
    });

    $(".abus_mid_frist_item").on('click',".short_content", function() {
        var sTitle = $(this).parent("p").text();
        sTitle = sTitle .substring(0,140)+"<a class=\"red_text\">…more<span class=\"db_arrow-icon\"></span></a>";
        $($(this).parent("p")).html(sTitle);
    });



//751下拉菜单
    $(".ui_page_header751 h3").click(function () {
        $(this).find('span').toggleClass('rotate');
        $(".ui_nav_751 ").toggle();
    })




    // 751download模块
    $(".ui_nav_751 li").click(function () {
        var i = $(this).index();
        var oldtext = $(this).innerText;
        $(".download_content_box").addClass("hide");
        $($(".download_content_box")[i]).removeClass("hide");
        $(".ui_nav_751 ").toggle();
    })


    // 轮播图
    if($(".swiper-slide").length>1){
        var mySwiper = new Swiper('.swiper-container', {
            direction: 'horizontal', // 垂直切换选项
            loop: true, // 循环模式选项
            autoplay:{
                delay:7000
            },
            // 如果需要分页器
            pagination: {
                el: '.swiper-pagination',
                clickable :true
            }
        });
    }


    if(blw<769) {

    }else if(769<blw && blw<1280){
        var mySwiper2 = new Swiper('.swiper-container2', {
            slidesPerView: 3,
            spaceBetween: 0,
            slidesPerGroup: 1,
            navigation: {
                nextEl: '.swiper-button-next2',
                prevEl: '.swiper-button-prev2'
            }
        })
    }else{
        var mySwiper2 = new Swiper('.swiper-container2', {
            slidesPerView: 5,
            spaceBetween: 0,
            slidesPerGroup: 1,
            navigation: {
                nextEl: '.swiper-button-next2',
                prevEl: '.swiper-button-prev2'
            }
        })
    }

    var mySwiper3 = new Swiper('.swiper-container3', {
        slidesPerView: 3,
        spaceBetween: 0,
        slidesPerGroup: 1,
        navigation: {
            nextEl: '.swiper-button-next2',
            prevEl: '.swiper-button-prev2'
        }
    });





//751轮播

//富文本bug修复
    $(".bug").find("a").addClass("red_button bd_btn");
    $(".swiper-container4 li").addClass("swiper-slide");
//UPDATA INFO li加class
    $($(".ui_page_header .page_header_nav li")[0]).addClass("red_button");
    $(".ui_page_header .page_header_nav li").addClass("grey_button");


    if(blw<769) {

    }else if(blw>769){
        var mySwiper2 = new Swiper('.swiper-container4', {
            slidesPerView: 4,
            spaceBetween: 0,
            slidesPerGroup: 1,
            navigation: {
                nextEl: '.swiper-button-next2',
                prevEl: '.swiper-button-prev2'
            }
        })
    }else if(blw>1280){
        var mySwiper4 = new Swiper('.swiper-container4', {
            slidesPerView: 3,
            spaceBetween: 0,
            slidesPerGroup: 1,
            navigation: {
                nextEl: '.swiper-button-next2',
                prevEl: '.swiper-button-prev2'
            }
        })
    }





    function getBrowserInfo()
    {
        var agent = navigator.userAgent.toLowerCase() ;

        var regStr_ie = /msie [\d.]+;/gi ;
        var regStr_ff = /firefox\/[\d.]+/gi
        var regStr_chrome = /chrome\/[\d.]+/gi ;
        var regStr_saf = /safari\/[\d.]+/gi ;
//IE
        if(agent.indexOf("msie") > 0)
        {
            return agent.match(regStr_ie) ;
        }

//firefox
        if(agent.indexOf("firefox") > 0)
        {
            return agent.match(regStr_ff) ;
        }

//Chrome
        if(agent.indexOf("chrome") > 0)
        {
            return agent.match(regStr_chrome) ;
        }

//Safari
        if(agent.indexOf("safari") > 0 && agent.indexOf("chrome") < 0)
        {
            $(".red_button").css("appearance","none")
            return agent.match(regStr_saf) ;
        }

    }
    var browser = getBrowserInfo() ;
    // alert(browser[0]);

    if(browser[0] == "chrome/30.0.0.0"){
        $(".header_left-751").css("marginTop","27px");
        $(".header_logo-751").css("marginTop","27px");
        $(".header_right-751").css("marginTop","27px");
        $(".ln_box img").css("display","block");
        $(".ln_box img").css("width","100%");
        if(blw<769){
            $(".page_banner h2").css("paddingTop","120px");
            $(".home_scroll_banner_content_bgimg").css("height","116vw");
        }
    }else if(browser[0] == "safari/537.36"){
        if(blw<769){
            $(".email_box input").css("height","100%");
            $(".email_box input").css("box-sizing","border-box");
            $(".products_banner_content").css("height","auto");
        }
    }




















});







