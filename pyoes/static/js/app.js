// Foundation JavaScript
// Documentation can be found at: http://foundation.zurb.com/docs
$(document).foundation();

// Function that makes the mobile menu work.
$('#mobile-menu-select').change(function() {
	window.location = $(this).val();
});

/*
// Function to stick footer to the bottom of page
// -- not working 100% becauce of 'vlaanderen' banners
*/
$(document).ready(function() {
    var footer = $("#footer-bottom");
    var pos = footer.position();
    var height = $(window).height();
    height = height - pos.top;
    height = height - footer.height();
    height = height - 45 * 2; // Vlaanderen banners
    if (height > 0) {
        footer.css({
            'margin-top': height + 'px'
        });
    }
});