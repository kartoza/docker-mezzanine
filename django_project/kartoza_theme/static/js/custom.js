(function($) {

	var isSearch = false;

	// prettyPhoto
	jQuery(document).ready(function(){
		jQuery('a[data-gal]').each(function() {
			jQuery(this).attr('rel', jQuery(this).data('gal'));
		});  	
		jQuery("a[data-rel^='prettyPhoto']").prettyPhoto({animationSpeed:'slow',theme:'light_square',slideshow:false,overlay_gallery: false,social_tools:false,deeplinking:false});
	}); 

	$('#search-box').click(function(){
		if(!isSearch) {
			$('.menu-bar').hide();
			$('#search-bar').show();
			$($('#search-box').children()[0]).hide();
			$($('#search-box').children()[1]).show();
			isSearch = true;
		} else {
			$('.menu-bar').show();
			$('#search-bar').hide();
			$($('#search-box').children()[0]).show();
			$($('#search-box').children()[1]).hide();
			isSearch = false;
		}
	});
		
})(jQuery);