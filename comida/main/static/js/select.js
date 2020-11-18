const select = document.querySelector('.filter-select');
const vegetables = document.querySelector('.veg');
const fishes = document.querySelector('.fish');
const fruits = document.querySelector('.fruits');

// Select
select.addEventListener('change', changeValue);

function changeValue() {
    if (select.value == 'vegetable') {
        vegetables.classList.add('current');
        fishes.classList.remove('current');
        fruits.classList.remove('current');
    } else if (select.value == 'fish') {
        vegetables.classList.remove('current');
        fishes.classList.add('current');
    } else if (select.value == 'fruit') {
        vegetables.classList.remove('current');
        fishes.classList.remove('current');
        fruits.classList.add('current');
    }
}

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