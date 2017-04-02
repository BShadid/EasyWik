var wikiUrl = window.location.href;
var APIurl = wikiUrl.replace("https://en.wikipedia.org/wiki","https://localhost:5000").replace(/_/g,"%20");

var xhr = new XMLHttpRequest();

var handleResponse = function (status, response) {
	if(status == 200)
		document.write(response);
}

xhr.onreadystatechange = function() {
	switch (this.readyState) {
		case 0:
		case 1:
		case 2:
		case 3:
			break;
		case 4:
			handleResponse(this.status,this.responseText);
			break;
		default:
			alert("error");
	}
}

xhr.open('GET', APIurl, true);
xhr.send(null);
