const API = "aiven-ai-production.up.railway.app";

async function send() {
  const input = document.getElementById("message");
  const chat = document.getElementById("chat");

  if (!input.value.trim()) return;

  chat.innerHTML += `<div class="message user">You → ${input.value}</div>`;

  const res = await fetch(API, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: input.value })
  });

  const data = await res.json();

  chat.innerHTML += `<div class="message ai">AIVEN → ${data.reply}</div>`;

  input.value = "";
  chat.scrollTop = chat.scrollHeight;
                                                       }
