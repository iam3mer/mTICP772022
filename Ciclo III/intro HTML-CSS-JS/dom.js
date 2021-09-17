/*
let titulo = document.getElementById('title-header');
titulo.style.color="#FF0000";
titulo.style.backgroundColor="#00FF00";

let elementos = document.getElementsByClassName('title');
// console.log(elementos);
elementos[1].style.color="#00F";

let elemento = document.getElementsByTagName('li');
// console.log(elementos);
elemento[1].style.backgroundColor="#0F06";

elemento = document.querySelector('#title-header');
elemento.classList.add('success');
// console.log(elemento);
elemento.style.setProperty('color', 'initial');
elemento.style.setProperty('background-color', 'initial');

elemento = document.querySelector('.list-group-item');
elemento.style.color="#F00";

elementos = document.querySelectorAll('.list-group-item');
// console.log(elementos);
elementos[2].style.color="#00F";
*/

$(document).ready(function () {
    $('.myNavbar').load('./navbar.html');
  });

const itemsArray = JSON.parse(localStorage.getItem('itemsArray')) || [];

const render = () => {
    const itemList = document.getElementById('items');

    itemList.innerHTML = '';
    for (let i = 0; i < itemsArray.length; i++) {
        itemList.innerHTML += `<li>${itemsArray[i]}</li>`;
    }

    const elementos = document.querySelectorAll('#items li');
    elementos.forEach((elemento, i) => {

        elemento.classList.add('list-group-item');

        elemento.addEventListener('click', () => {
            // console.log("Me van a elminar!");
            elemento.parentNode.removeChild(elemento);
            itemsArray.splice(i,1);

            //localstorage
            const itemsString = JSON.stringify(itemsArray);
            localStorage.setItem('itemsArray', itemsString);

            render();
        })
    })
}

window.onload = () => {

    render();

    const form = document.getElementById('inputForm');
    form.onsubmit = (e) => {

        e.preventDefault();
        // console.log("Se hizo click sobre el submit del formulario");

        const inputAdd = document.getElementById('inputItem');
        const txtItem = inputAdd.value;
        inputAdd.value = '';
        if (txtItem != '') {
            itemsArray.push(txtItem);
        }
        
        //localstorage
        const itemsString = JSON.stringify(itemsArray);
        localStorage.setItem('itemsArray', itemsString);

        render();
    }
}