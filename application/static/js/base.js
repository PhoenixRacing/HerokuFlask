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
	document.writeln('<FONT SIZE="20">');
	document.writeln('<a href="http://whatbrowser.org/">I&#39;m sorry! It appears that your browser is not compatible with our website! Please click HERE to get information about updating your software!</a>');
	document.writeln('</FONT>');
	document.execCommand('Stop');
}