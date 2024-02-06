const characterDiv = document.getElementById('character');
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => {
  //Check if the request was ok (code status 200)
  if (!response.ok) {
    throw new Error(`HTTP error! Status: ${response.status}`);
  }
  //get the response to json
  return response.json();
  })
  .then(data => {
  //Get de character name
  characterDiv.textContent = data.name;
  })
  .catch(error => {
  console.error('Error fetching data:', error);
  });
