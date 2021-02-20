// $(function(){
//     //点赞加1
//     $('.iconthumb-up-line').on('click',function(){
//         $('.item-right addone').removeClass('none');
//     });
// });
var page = 1
var last = false
var toloading = false;
var faqs_title = $('#fqas_keyword').val();
if(!$('#fqas_keyword').val()){
	faqs_title='';
}

function FaqsSearch(id){
	page = 1;
	last = false;
	toloading = false;
	if(!toloading){
		toloading = true
		$('#upLoading').text('加载中...')
		api.GET('/content/page',{
			"contentId": "",
			// "channelIds": "2273,2274,2275,2276",
            "channelIds": "2286,2287,2288,2289",
            "tagIds": "",
			"channelPaths": "",
			"siteIds": "",
			"typeIds": "",
			"title": $('#fqas_keyword').val(),
			"isNew": "",
			"isTop": "",
			"timeBegin": "",
			"timeEnd": "",
			"excludeId": "",
			"orderBy": "",
			"page": page,
			"size": 50,
			"releaseTarget": ""
		},function(res){
            if(res.code===200){

                if(res.data.content.length==0){
                    myMessage.add("Search for no results,try another word", 'error');
                    return;
                }else {
                    if($("body").width() > 768){
                        $(".faqs_btm_right ").hide();
                    }else{
                        $(".faqs_btm_right_box_751").remove();
                        $(".faqs_btm_right_box_751_shearch").show();
                    }
                    // $(".faqs_btm_left").hide()
                    $("#faqs_search_list").show();
                    var data = res.data.content
                    var html=[];
                    if($("body").width() > 768){
                        for(var i=0;i<data.length;i++){
                            // if(data[i].contentTxts.length>0){
                                var faqs_result = '<li id="index_'+ data[i].channelName +'" class="faqs_search"><p class=""><a href="javascript:;"><span class="fqas-icon"></span>Q:'+ data[i].title +'</a></p> </li><div class="faqs_btm_right_content hide">'+ data[i].txt +'</div>'
                                html.push(faqs_result);
                                $('#faqs_search_list ul').html(html.join(""));
                            // }
                        }
                    }else {
                        for (var i = 0; i < data.length; i++) {
                            var faqs_result = '<li><p class=""> <a href="javascript:;"><span class="fqas-icon"></span>Q:' + data[i].title + '</a></p></li><div class="faqs_btm_right_content hide">' + data[i].txt + '</div>'
                            html.push(faqs_result);
                            $('.faqs_btm_right_box_751_shearch ul').html(html.join(""));
                        }
                    }
                    toloading = false
                    last = res.data.last
                    if(last){
                        $("#faqs_view_more").hide();
                    }else{
                        $("#faqs_view_more").show();
                    }
                }


			}else{
				myMessage.add(result.message, 'error');
			}
		})
	}
}

function loading(){
	if(!last && !toloading){
		page+=1
		toloading = true
		$('#upLoading').text('loading...')
		api.GET('/content/faqs/page',{
			"contentId": "",
			"channelIds": "2273,2274,2275,2276",
			"tagIds": "",
			"channelPaths": "",
			"siteIds": "",
			"typeIds": "",
			"title": $('#fqas_keyword').val(),
			"isNew": "",
			"isTop": "",
			"timeBegin": "",
			"timeEnd": "",
			"excludeId": "",
			"orderBy": "",
			"page": page,
			"size": 6,
			"releaseTarget": ""
		},function(res){
			if(res.code===200){
				var data = res.data.content
				last=res.data.last
				for(var i=0;i<data.length;i++){
					var faqs_result = $('<li class="faqs_search"><p class=""><a href="javascript:;"><span class="fqas-icon"></span>Q:'+ data[i].title +'</a></p> </li><div class="faqs_btm_right_content hide">'+ data[i].contentTxts[0].attrTxt +'</div>')
					faqs_result.appendTo($('#faqs_search_list ul'));
				}
				toloading = false
				if(last){
					$('#upLoading').text('no more');
					$('#upLoading').css({'background-color':'#fff','margin-top':'-9px'});
					$('#upLoading').removeClass('loading').addClass('none-loading');
				}else{
					$('#upLoading').text('read more')
					// page+=1
				}
			}else{
				myMessage.add(result.message, 'error');
			}
		})
	}else if(last){
		myMessage.add('no more', 'warning');
	}
}


