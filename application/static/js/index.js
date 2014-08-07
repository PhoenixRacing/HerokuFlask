$(document).ready(function(){
	$('.banner-caption').fadeIn(1700);
	$('.tryinstuff').fadeIn(600);
	$('.bottom-slide').fadeIn(500);
	$('.frontpage-container').fadeIn(800);
	$('.frontpage-caption').fadeIn('slow');
	$('.bottom-wrap').fadeIn(800);
	$('.container').fadeIn('slow').slick({
		autoplay: true,
		dots: false,
		draggable: false,
		pauseOnHover: true,
		arrows: true,
		speed: 600,
		autoplaySpeed: 6000,
  		infinite: true,
  		fade: true,
	});
});