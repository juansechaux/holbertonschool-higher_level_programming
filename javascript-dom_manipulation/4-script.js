const ulElement = document.querySelector('.my_list');
const addElement = document.getElementById('add_item');


function createLi() {
  const liElement = document.createElement('li');
  liElement.textContent = 'Item';
  ulElement.appendChild(liElement);
}

addElement.addEventListener("click", createLi);
