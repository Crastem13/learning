var browser={    
		versions:function(){            
		var u = navigator.userAgent, app = navigator.appVersion; 
		/*if(u.indexOf("Android")>0){
			removejscssfile('themes/autel/css/css.css','css');
			addCSS('themes/autel/css/tpcss.css');
		} else{
			removejscssfile('themes/autel/css/tpcss.css','css');
			addCSS('themes/autel/css/css.css');
		} 2016-9-3，由于没有找到tpcss.css，先去掉*/
		addCSS('themes/autel/css/css.css');
		}()
	} 
function addCSS(url) {
    var link = document.createElement('link');
    link.type = 'text/css';
    link.rel = 'stylesheet';
    link.href =url ;
    document.getElementsByTagName("head")[0].appendChild(link);
}
function removejscssfile(filename, filetype){
	var targetelement=(filetype=="js")? "script" : (filetype=="css")? "link" : "none"
	var targetattr=(filetype=="js")? "src" : (filetype=="css")? "href" : "none"
	var allsuspects=document.getElementsByTagName(targetelement)
	for (var i=allsuspects.length; i>=0; i--){
	if (allsuspects[i] && allsuspects[i].getAttribute(targetattr)!=null && allsuspects[i].getAttribute(targetattr).indexOf(filename)!=-1)
	   allsuspects[i].parentNode.removeChild(allsuspects[i])
	}
}