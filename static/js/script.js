let chart;

function predict() {
    const input = document.getElementById("energyInput").value
        .split(",")
        .map(Number);

    fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ input: input })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("result").innerText =
            "Predicted Consumption: " + data.prediction + " kWh";

        const list = document.getElementById("suggestions");
        list.innerHTML = "";
        data.suggestions.forEach(tip => {
            const li = document.createElement("li");
            li.textContent = tip;
            list.appendChild(li);
        });

        drawChart(input);
    });
}

function drawChart(values) {
    const ctx = document.getElementById("energyChart").getContext("2d");

    if (chart) chart.destroy();

    chart = new Chart(ctx, {
        type: "line",
        data: {
            labels: values.map((_, i) => "T" + (i + 1)),
            datasets: [{
                label: "Energy Consumption",
                data: values,
                borderColor: "#00e6e6",
                fill: false,
                tension: 0.4
            }]
        },
        options: {
            animation: {
                duration: 2000
            }
        }
    });
}
