document.addEventListener("DOMContentLoaded", function () {
    // Bar Chart
    const barCtx = document.getElementById("barChart").getContext("2d");
    const barChart = new Chart(barCtx, {
        type: "bar",
        data: {
            labels: JSON.parse(document.getElementById("financeLabels").textContent), // Labels from template
            datasets: [{
                label: "Transaction Amounts",
                data: JSON.parse(document.getElementById("financeAmounts").textContent), // Data from template
                backgroundColor: "rgba(75, 192, 192, 0.6)",
                borderColor: "rgba(75, 192, 192, 1)",
                borderWidth: 1,
            }],
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                },
            },
        },
    });

    // Pie Chart
    const pieCtx = document.getElementById("pieChart").getContext("2d");
    const pieChart = new Chart(pieCtx, {
        type: "pie",
        data: {
            labels: JSON.parse(document.getElementById("financeLabels").textContent), // Labels from template
            datasets: [{
                label: "Transaction Distribution",
                data: JSON.parse(document.getElementById("financeAmounts").textContent), // Data from template
                backgroundColor: [
                    "#FF6384",
                    "#36A2EB",
                    "#FFCE56",
                    "#4BC0C0",
                    "#9966FF",
                    "#FF9F40",
                ],
            }],
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: "top",
                },
            },
        },
    });
});
