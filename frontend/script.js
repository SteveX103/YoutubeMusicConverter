async function convert(){
    const url = document.getElementById("url").value;
    fetch("http://localhost:8000/convert",{
        method : "POST",
        headers: {
            "content-type" : "application/json"
        },
        body: JSON.stringify({url})
    });
    document.getElementById("status").innerText = data.status;
}