fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error, Status: ${response.status}`)
    }
    return response.json();
  })
  .then(data => {
    const divHello = document.getElementById('hello');
    const newP = document.createElement('p');
    newP.textContent = data.hello;
    divHello.appendChild(newP);
  })
  .catch(error => {
    console.error(`Error fetching data: ${error}`);
  });
