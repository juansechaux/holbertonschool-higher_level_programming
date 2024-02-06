const getHeader = document.querySelector('#update_header');
const headerData = document.querySelector('header');

getHeader.addEventListener('click', updateHeader);

function updateHeader() {
  headerData.textContent = 'New Header!!!';
}
