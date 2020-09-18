

var ctx1 = document.getElementById('chart1').getContext('2d');
var myChart = new Chart(ctx1, {
    type: 'doughnut',
    data: {
        labels: ['Fixed', 'Not Fixed'],
        datasets: [{
           // data: [20, 9],
            data:data11,
            backgroundColor: [
                'rgba(0,255,127, 0.8)',
                'rgba(255, 99, 132, 0.8)',

            ],
            borderColor: [
                'rgb(8,122,55)',
                'rgb(125,50,60)',

            ],
            borderWidth: 1
        }]
    },
    options: {
        responsive:true,
        maintainAspectRatio: false,

    }
});




var ctx2 = document.getElementById('chart2').getContext('2d');
var myChart = new Chart(ctx2, {
    type: 'bar',
    data: {
        labels:labels22,
        datasets: [{
            label: 'my policies',
            // data: [3, 4, 80, 0, 105, 40, 50,10],
            data: data22,
            backgroundColor: 'rgb(73,180,192)',
            borderColor: 'rgb(54,99,146)',
            borderWidth: 1
        }]
    },
options: {
    responsive:true,
    maintainAspectRatio: false,
    scales: {
        yAxes: [{
            ticks: {
                beginAtZero: true
            }
        }]
    }
}
});

var ctx3 = document.getElementById('chart3').getContext('2d');
var myChart = new Chart(ctx3, {
    type: 'line',
    data: {
        labels: labels33,
        datasets: [{
            label: 'violations',
            data:data33,
            backgroundColor: 'rgba(76,194,194,0.6)',
            borderColor: 'rgb(47,120,120)',
            borderWidth: 2,
            fill: false
        }]
    },
    options: {
        responsive:true,
        maintainAspectRatio: false,
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});


var ctx4 = document.getElementById('chart4').getContext('2d');
var myChart = new Chart(ctx4, {
    type: 'pie',
    data: {
        labels: labels44,
        datasets: [{
            label: 'Resources',
            data: data44,
            backgroundColor: [
                'rgba(255,99,132,0.8)',
                'rgba(54, 162, 235, 0.8)',
                'rgba(255, 206, 86, 0.8)',
                'rgba(255, 159, 64, 0.8)'
            ],
            borderColor: [
                'rgb(156,55,88)',
                'rgb(37,112,156)',
                'rgb(156,126,53)',
                'rgb(156,98,38)'
            ],
            borderWidth: 1,
            fill: false
        }]
    },
    options: {
        responsive:true,
        maintainAspectRatio: false,

    }
});