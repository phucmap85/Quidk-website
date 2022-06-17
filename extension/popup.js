var language = new String("en");
var checkb = document.getElementById("checkbox");
var checksubmit = document.getElementById("submit");

if (checkb) {
	document.getElementById("checkbox").addEventListener("change", (event) => {
		const cb = document.querySelector('#checkbox');
		console.log(cb.checked);
		language = new String("en");
		if (cb.checked) {
			language = new String("vi");
		}
		document.getElementById("output").innerHTML = language;
	});
}

if (checksubmit) {
	document.getElementById("submit").addEventListener('click', () => {
		// console.log("test");
		// document.getElementById("output").innerHTML = "Loading...";
		var x = document.getElementById("text1").value;
		jQuery.ajax({
			type: "POST",
			url: 'http://localhost/quidk/summarization.php',
			dataType: 'json',
			data: { text: x, lang: language },
			
			success: function (obj) {
				document.getElementById("output").innerHTML = "";
				for( var name in obj) {
					// console.log( obj[ name ] + ' ');
					// str = str + " \n\n" + obj[name];
					var tag = document.createElement("p"); // <p></p>
					var text = document.createTextNode(obj[name]); 
					tag.appendChild(text); // <p>TEST TEXT</p>
					var element = document.getElementById("output");
					// console.log(element);
					element.appendChild(tag); // <body> <p>TEST TEXT</p> </body>
				}
				// console.log(str);
				// document.getElementById('output').innerHTML = str;
			}
		});
	});
}