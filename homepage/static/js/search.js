const searchButton = document.getElementById('search-button');
const searchInput = document.getElementById('search-input');
searchButton.addEventListener('click', () => {
  const inputValue = searchInput.value;
  const theUrl=`http://127.0.0.1:8000/?q=${inputValue}`
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.open( "GET", theUrl,false ); // false for synchronous request
  xmlHttp.send( );
  return xmlHttp.responseText;
});