async function ask() {
  const question = document.getElementById("q").value;
  const resDiv = document.getElementById("result");
  resDiv.innerHTML = "Thinking...";

  const response = await fetch("/ask", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({question: question})
  });

  const data = await response.json();
  if (data.error) {
    resDiv.innerHTML = "Error: " + data.error;
  } else {
    resDiv.innerHTML = "<b>Answer:</b> " + data.answer;
  }
}
