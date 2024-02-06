const headerElement = document.querySelector('header');
const toggleElement = document.getElementById('toggle_header');

toggleElement.addEventListener("click", updateColor);

function updateColor() {
if (headerElement.classList.contains('green')) {
  headerElement.classList.remove("green");
  headerElement.classList.add("red");
} else {
  headerElement.classList.remove("red");
  headerElement.classList.add("green");
  }
}
