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