var checksubmit = document.getElementById("submit");

if(checksubmit) {
	checksubmit.addEventListener('click', () => {
		document.getElementById("output").innerHTML = "Loading...";
		chrome.tabs.query({'active': true, 'windowId': chrome.windows.WINDOW_ID_CURRENT},
			function(tabs) {
				console.log(tabs[0].url);
				jQuery.ajax({
					type: "POST",
					url: 'http://localhost/quidk/summarization.php',
					dataType: 'json',
					data: {text: tabs[0].url},
		
					success: function (obj) {
						document.getElementById("output").innerHTML = "";
						for(var name in obj) {
							var tag = document.createElement("p");
							var text = document.createTextNode(obj[name]); 
							tag.appendChild(text);
							document.getElementById("output").appendChild(tag);
						}
					}
				});
			}
		);
	});
}