var language = new String("en");

document.getElementById("checkbox").addEventListener("change", (event)=>{
	const cb = document.querySelector('#checkbox');
	console.log(cb.checked);
	language = new String("en");
	if (cb.checked) {
		language = new String("vi");
	}
	document.getElementById("output").innerHTML = language;
});

function clicked() {
	chrome.tabs.query({active: true, lastFocusedWindow: true}, tabs => {
		let url = tabs[0].url;
		// use `url` here inside the callback because it's asynchronous!
	});
}