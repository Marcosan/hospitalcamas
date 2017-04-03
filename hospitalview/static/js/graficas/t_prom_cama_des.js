var MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
var randomScalingFactor = function() {
    return Math.round(Math.random() * 100 * (Math.random() > 0.5 ? -1 : 1));
};
var randomColorFactor = function() {
    return Math.round(Math.random() * 255);
};
var randomColor = function(opacity) {
    return 'rgba(' + randomColorFactor() + ',' + randomColorFactor() + ',' + randomColorFactor() + ',' + (opacity || '.3') + ')';
};

var config = {
    type: 'line',
    data: {
        labels: ["January", "February", "March", "April", "May", "June", "July"],
        datasets: [{
            label: "Por días",
            data: [],
            lineTension: 0,
            fill: false,
        }]
    },
    options: {
        responsive: true,
        legend: {
            position: 'bottom',
        },
        hover: {
            mode: 'label'
        },
        scales: {
            xAxes: [{
                display: true,
                scaleLabel: {
                    display: true,
                    labelString: 'Día'
                }
            }],
            yAxes: [{
                display: true,
                scaleLabel: {
                    display: true,
                    labelString: 'Tiempo'
                }
            }]
        },
        title: {
            display: true,
            text: 'Tiempo promedio de cama desocupada'
        }
    }
};

function crearLabel(ini, fin){
	/*mes = 1;
	for(var a = ini, a <= fin, a++){
		config.data.labels[a] = a + "/" + mes;
	}*/

	for (var i = 0; i <= 7; i++) {
		config.data.datasets[0].data[i] = 1;
	}
}

$.each(config.data.datasets, function(i, dataset) {
    var background = randomColor(0.5);
    dataset.borderColor = background;
    dataset.backgroundColor = background;
    dataset.pointBorderColor = background;
    dataset.pointBackgroundColor = background;
    dataset.pointBorderWidth = 1;
});

function graficar_tpcd(){
	crearLabel(1,1);
    var ctx = document.getElementById("c_desocupada").getContext("2d");
    myLine = new Chart(ctx, config);
}

$('#randomizeData').click(function() {
    $.each(config.data.datasets, function(i, dataset) {
        dataset.data = dataset.data.map(function() {
            return randomScalingFactor();
        });

    });

    window.myLine.update();
});

$('#addDataset').click(function() {
    var background = randomColor(0.5);
    var newDataset = {
        label: 'Dataset ' + config.data.datasets.length,
        borderColor: background,
        backgroundColor: background,
        pointBorderColor: background,
        pointBackgroundColor: background,
        pointBorderWidth: 1,
        fill: false,
        data: [],
    };

    for (var index = 0; index < config.data.labels.length; ++index) {
        newDataset.data.push(randomScalingFactor());
    }

    config.data.datasets.push(newDataset);
    window.myLine.update();
});

function addData() {
    if (config.data.datasets.length > 0) {
        var month = MONTHS[config.data.labels.length % MONTHS.length];
        config.data.labels.push(month);

        $.each(config.data.datasets, function(i, dataset) {
            dataset.data.push(randomScalingFactor());
        });

        window.myLine.update();
    }
}

$('#removeDataset').click(function() {
    config.data.datasets.splice(0, 1);
    window.myLine.update();
});

$('#removeData').click(function() {
    config.data.labels.splice(-1, 1); // remove the label first

    config.data.datasets.forEach(function(dataset, datasetIndex) {
        dataset.data.pop();
    });

    window.myLine.update();
});