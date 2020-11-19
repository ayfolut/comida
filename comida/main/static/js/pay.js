const select = document.querySelector('.filter-select');
const mastercard = document.querySelector('.mastercard');
const visa = document.querySelector('.visa');
const verve = document.querySelector('.verve');

// Select
select.addEventListener('change', changeValue);

function changeValue() {
    if (select.value == 'mastercard') {
        mastercard.classList.add('current');
        visa.classList.remove('current');
        verve.classList.remove('current');
    } else if (select.value == 'visa') {
        mastercard.classList.remove('current');
        visa.classList.add('current');
    } else if (select.value == 'verve') {
        mastercard.classList.remove('current');
        visa.classList.remove('current');
        verve.classList.add('current');
    }
}