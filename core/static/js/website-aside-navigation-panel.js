"use strict";

var WIHNavPanel = function() {
    var panel;

    var initOffcanvas = function() {
        const a = new KTOffcanvas(panel, {
            overlay: true,
            baseClass: 'kt-quick-panel',
            closeBy: 'wih_nav_panel_close_btn',
            toggleBy: 'wih_nav_panel_toggler_btn'
        });
        var menu_wrapper = KTUtil.get('kt_aside_menu_wrapper');

        // needed to provide scroll for initial menu
        KTUtil.scrollInit(menu_wrapper, {
            // mobileNativeScroll: true,
            resetHeightOnDestroy: true,
            handleWindowResize: true,
            //rememberPosition: true,
            height: function() {
                return KTUtil.getViewPort().height;
            }
        });

        /*a.on('beforeHide', function(){
            const open_menus = KTUtil.findAll(panel, '.kt-menu__item--open-dropdown')
            if (open_menus.length > 0){
                for (let i in open_menus){
                    const el = open_menus[i];
                    KTUtil.removeClass(el, 'kt-menu__item--open-dropdown kt-menu__item--hover' );

                }
            }

        })*/

        /*const asideMenu = new KTMenu('wih_aside_menu', {
            // Vertical scroll
            scroll: scroll,

            // Submenu setup
            submenu: {
                desktop: 'dropdown',
                tablet: 'accordion', // menu set to accordion in tablet mode
                mobile: 'accordion' // menu set to accordion in mobile mode
            },

            // Accordion setup
            accordion: {
                autoScroll: false, // enable auto scrolling(focus) to the clicked menu item
                expandAll: false   // allow having multiple expanded accordions in the menu
            }
        });

        var menu_wrapper = KTUtil.get('kt_aside_menu_wrapper');

        // needed to provide scroll for initial menu
        KTUtil.scrollInit(menu_wrapper, {
            // mobileNativeScroll: true,
            resetHeightOnDestroy: true,
            handleWindowResize: true,
            //rememberPosition: true,
            height: function() {
                return KTUtil.getViewPort().height;
            }
        });

        // Handle full height dropdowns
        if (KTUtil.isInResponsiveRange('desktop')) {
            // remove > wrapper to provide directly to submenus to work properly with the scroll above
            var query = KTUtil.findAll(panel, '.kt-menu__item--submenu-fullheight .kt-menu__submenu');

            for (var i = 0, j = query.length; i < j; i++) {
                var item = query[i];

                if (item) {
                    KTUtil.scrollInit(item, {
                        mobileNativeScroll: true,
                        resetHeightOnDestroy: true,
                        handleWindowResize: true,
                        rememberPosition: true,
                        height: function() {
                            return KTUtil.getViewPort().height;
                        }
                    });

                    // Update scroller on submenu toggle
                    asideMenu.on('submenuToggle', function(submenuEl) {
                        if (submenuEl && item.contains(submenuEl)) {
                            KTUtil.scrollUpdate(item);
                        }
                    });
                }
            }
        }*/

    }

    return {
        init: function() {
            panel = KTUtil.get('wih_nav_panel');
            initOffcanvas();

        }
    };
}();

$(document).ready(function() {
    WIHNavPanel.init();

    // to allow click from multiple buttons
    KTUtil.addEvent(KTUtil.get('wih_nav_panel_header_toggler_btn'), 'click', function(e){
        e.preventDefault()
        KTUtil.get('wih_nav_panel_toggler_btn').click()
    })
});
