document.getElementById("scriptForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const username = document.getElementById("username").value.trim();
  const webhook = document.getElementById("webhook").value.trim();
  const output = document.getElementById("scriptOutput");

  if (!username || !webhook) {
    output.textContent = "Please fill in both fields.";
    return;
  }

  output.textContent = "Fetching script...";

  try {
    const res = await fetch(`/api/generate_script?username=${encodeURIComponent(username)}&webhook=${encodeURIComponent(webhook)}`);
    if (!res.ok) throw new Error(`HTTP error ${res.status}`);

    const data = await res.json();
    output.textContent = data.script || "-- No script returned --";
  } catch (err) {
    output.textContent = `Error: ${err.message}`;
  }
});
