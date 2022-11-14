"use strict";

// Class definition
var KTPortletAside = function () {
	// Base elements
	var offcanvas;

	// Private functions
	var initAside = function () {
		// Mobile offcanvas for mobile mode
        offcanvas = new KTOffcanvas('kt_portlet_aside', {
            overlay: true,
            baseClass: 'kt-app__aside',
            closeBy: 'kt_portlet_aside_close',
            toggleBy: 'kt_subheader_mobile_toggle'
        });
	}

	return {
		// public functions
		init: function() {
			initAside();
		}
	};
}();

KTUtil.ready(function() {
  KTPortletAside.init();
});
