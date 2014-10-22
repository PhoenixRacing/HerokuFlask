$(document).ready(function(){
	$('.banner-caption').fadeIn(1700);
	$('.tryinstuff').fadeIn(600);
	$('.bottom-slide').fadeIn(500);
	$('.frontpage-container').fadeIn(800);
	$('.frontpage-caption').fadeIn('slow');
	$('.bottom-wrap').fadeIn(800);
	$('.container').fadeIn('slow');
});

var ie = (function(){
 
    var undef,
        v = 3,
        div = document.createElement('div'),
        all = div.getElementsByTagName('i');
 
    while (
        div.innerHTML = '<!--[if gt IE ' + (++v) + ']><i></i><![endif]-->',
        all[0]
    );
 
    return v > 4 ? v : undef;
 
}());
if (ie<9){
	document.write('<FONT SIZE="20">');
	document.write('<a href="http://whatbrowser.org/">I&#39;m sorry! It appears that your browser is not compatible with our website! Please click HERE to get information about updating your software!</a>')
	document.write('</FONT>')
	document.execCommand('Stop');
	}