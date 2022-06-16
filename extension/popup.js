var language = new String("en");
var checkb = document.getElementById("checkbox");
var checksubmit = document.getElementById("submit");

if(checkb) {
	document.getElementById("checkbox").addEventListener("change", (event)=>{
		const cb = document.querySelector('#checkbox');
		console.log(cb.checked);
		language = new String("en");
		if (cb.checked) {
			language = new String("vi");
		}
		document.getElementById("output").innerHTML = language;
	});
}

if(checksubmit) {
	document.getElementById("submit").addEventListener('click', () => {
		console.log("test");
		document.getElementById("output").innerHTML = "Loading...";
		var x = document.getElementById("text1").value;
		jQuery.ajax({
			type: "POST",
			url: 'quidk/summarization.php',
			dataType: 'json',
			data: {text: x, lang: language},
	
			success: function (obj) {
				// json
				console.log("test");
				const myJSON = JSON.stringify(obj);
				console.log(myJSON);
				document.getElementById("text1").innerHTML = myJSON;
			}
		});
	});
}