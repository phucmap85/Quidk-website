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

function clicked(){
	document.getElementById("output").innerHTML = "Loading...";
	var x = document.getElementById("text1").value;
	jQuery.ajax({
		type: "POST",
		url: 'summarization.php',
		dataType: 'json',
		data: {text: x, lang: language},

		success: function (obj, textstatus) {
			console.log(obj);
		}
	});
}