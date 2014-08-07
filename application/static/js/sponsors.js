//TODO: Make this shit look better on mobile!
$(document).ready(function(){
	$('.donate_banner_container').fadeIn('slow');
	$('.frontpage-caption').fadeIn(500);
	$('.sponsor-banner-cap').fadeIn('slow');
	$('.frontpage-container').fadeIn('slow');
	$('.gold-container').slick({
		autoplay: true,
		dots: true,
		swipe: true,
		arrows: false,
		infinite: true,
		slidesToShow: 3,
		slidesToScroll: 3
	})
	$('.silver-container').slick({
		autoplay: true,
		dots: true,
		swipe: true,
		arrows: false,
		infinite: true,
		slidesToShow: 5,
		slidesToScroll: 5
	})
});