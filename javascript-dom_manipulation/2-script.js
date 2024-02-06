const headerElement = document.querySelector('header');
const redHeader = document.querySelector('#red_header');

redHeader.addEventListener("click", updateColor);

function updateColor() {
  headerElement.classList.add("red");
}
