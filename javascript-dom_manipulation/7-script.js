const ulElement = document.getElementById('list_movies');
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => {
  //Check if the request was ok (code status 200)
  if (!response.ok) {
    throw new Error(`HTTP error, Status: ${response.status}`);
  }
  //get the response to json
  return response.json();
  })
  .then(data => {
  for (const i in data.results) {
    const newLi = document.createElement('li');
    ulElement.appendChild(newLi);
    newLi.textContent = data.results[i].title;
  }
  })
  .catch(error => {
  console.error('Error fetching data:', error);
  });
