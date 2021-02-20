$(function() {
    var blw=$("body").width();
    if(blw>1280){
    // 点击导航下拉菜单
    $(".header_left .sub_nav").mouseover(function() {
        $(this).addClass("nav_focus");
        // if()
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
    }else if(blw<1281) {
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

    // $(this).css('color');

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


    $(".dt_btn button").click(function(){
        $(".dt_content_item").removeClass("hide");
        $(".dt_btn").hide();
    });

   


    // 751顶部下拉
    $(".header_left-751").click(function () {
        // $(".header_left-751").css("background-image","url(../../atImg/headerNavBtn2.png)");
        $(".header_left-751").toggleClass("header_left2-751");
        if($(this).hasClass("header_left2-751")){
            $(".header_nav_751").show();
            $(".submenu_751" ).hide();
        }else {
            $(".header_nav_751").hide();
            $(".submenu_751" ).hide();
        }
    });
    // 751点击二级菜单
    $(".header_nav_751 .sub_nav").click(function () {
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

        $(".download_hover_content ").hide();
        $(this).find(".download_hover_content ").show();
    });
    // 751dwonload导航切换
    $(".ui_nav_751 li").click(function () {
        var ctext = $($(this).find("a")).text();
        $(".ui_page_header751 h3").html(ctext + "<span class=\"arrow_down-icon751\"></span>");
    })




//751下拉菜单
    $(".ui_page_header751 h3").click(function () {
        $(this).find('span').toggleClass('rotate');
        $(".ui_nav_751 ").toggle();
    })




   

});







