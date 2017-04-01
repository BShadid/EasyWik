/* request_server.json :: requests the python server for info on the current wikipedia page */

chrome.browserAction.onClicked.addListener(function(tab) {
	chrome.tabs.executeScript(null, {code: 'alert("not working yet")'});
});
