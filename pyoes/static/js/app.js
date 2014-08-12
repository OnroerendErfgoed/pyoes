// Foundation JavaScript
// Documentation can be found at: http://foundation.zurb.com/docs
$(document).foundation();

// Function that makes the mobile menu work.
$('#mobile-menu-select').change(function() {
	window.location = $(this).val();
});
