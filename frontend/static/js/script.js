let selectedLocation = null;


// ============================
// LOCATION SEARCH
// ============================

function searchLocation() {

    let query = document.getElementById("locationInput").value;

    if (query.length < 3) return;

    fetch(`/search/${query}`)
        .then(res => res.json())
        .then(data => {

            let box = document.getElementById("suggestions");
            box.innerHTML = "";

            data.forEach(loc => {

                let div = document.createElement("div");

                div.innerHTML = `${loc.name}, ${loc.state}, ${loc.country}`;

                div.onclick = () => {
                    selectedLocation = loc;
                    document.getElementById("locationInput").value =
                        `${loc.name}, ${loc.state}`;
                    box.innerHTML = "";
                };

                box.appendChild(div);
            });
        });
}


// ============================
// CROP PREDICTION
// ============================

function predictCrop() {

    if (!selectedLocation) {
        alert("Please select a location");
        return;
    }

    fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(selectedLocation)
    })
        .then(res => res.json())
        .then(data => {

            let html = "<h3>Top Recommended Crops</h3>";

            data.recommended_crops.forEach(item => {
                html += `<p>${item.crop} — ${item.confidence}%</p>`;
            });

            html += `
                <br>
                <b>Weather Info</b><br>
                Temperature: ${data.weather.temperature} °C<br>
                Rainfall: ${data.weather.rainfall} mm
            `;

            document.getElementById("result").innerHTML = html;
        });
}
