// Variales
const sign = document.querySelector('.sign');
const signU = document.querySelector('.signUp');
const toggle = document.querySelector('.toggle');
const signUp = document.querySelector('.sign-up');
const signIn = document.querySelector('.sign-in');
const form01 = document.querySelector('.form-01');
const form02 = document.querySelector('.form-02');

sign.addEventListener('click', () => {
    signUp.style.display = 'flex';
    signIn.style.display = 'none';
});

signU.addEventListener('click', () => {
    signUp.style.display = 'none';
    signIn.style.display = 'flex';
});

toggle.addEventListener('click', () => {
    signUp.classList.toggle('sign-in-out');
    signIn.classList.toggle('sign-in-in');
    toggle.classList.toggle('display');
});

form01.addEventListener('submit', (e) => {
    const input = document.getElementsByTagName('input');
    input.value = '';
    for (let i = 0; i < input.length; ++i) {
        if (input[i].value == '') {
            input[i].style.borderBottom = 'solid 1px red';
        } else {
            input[i].style.borderBottom = 'solid 1px gray';
        }
    }
});
form02.addEventListener('submit', (e) => {
    // Regular Expression (regex)
    const mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    const regex = new RegExp(mailformat);
    const input = document.getElementsByTagName('input');
    input.value = '';
    for (let i = 0; i < input.length; ++i) {
        if (input[i].value == '' && !input[i].match(regex)) {
            input[i].style.borderBottom = 'solid 1px red';
        } else {
            input[i].style.borderBottom = 'solid 1px gray';
        }
    }
});