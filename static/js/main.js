// Sidenav
const sideNav = document.querySelector('.sidenav');
M.Sidenav.init(sideNav, {});

// Slider
$(document).ready(function() {
    $('.slider').slider({
        indicators: false,
        interval: 3000,
    });
});

// Material Boxed
const mb = document.querySelectorAll('.materialboxed');
M.Materialbox.init(mb, {});

// ScrollSpy
const ss = document.querySelectorAll('.scrollspy');
M.ScrollSpy.init(ss, {});

// Select
$(document).ready(function() {
    $('select').formSelect();
});