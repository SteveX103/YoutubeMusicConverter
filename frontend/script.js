const convertBtn = document.getElementById("convertBtn");
const downloadBtn = document.getElementById("downloadBtn");
const status = document.getElementById("status");
const urlInput = document.getElementById("url");

let lastFilename = null;

convertBtn.addEventListener("click", async () => {
  status.innerText = "⏳ Converting...";
  downloadBtn.style.display = "none";
  lastFilename = null;

  try {
    const res = await fetch("http://localhost:8000/convert", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ url: urlInput.value })
    });

    const data = await res.json();
    console.log("Backend:", data);

    if (res.ok && data.filename) {
      status.innerText = " Ready to download";
      lastFilename = data.filename;
      downloadBtn.style.display = "inline-block";
    } else {
      status.innerText = " Conversion failed";
    }

  } catch (e) {
    console.error(e);
    status.innerText = " Server error";
  }
});

downloadBtn.addEventListener("click", () => {
  if (!lastFilename) return;

  
  window.location.href =
    `http://localhost:8000/download/${encodeURIComponent(lastFilename)}`;
});
