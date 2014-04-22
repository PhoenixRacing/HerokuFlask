$(function () {

    // unpack the time and speed variables
    t = data.data.map(function(d){
        if (d.speed != undefined){
            return d.time.$date;
        }
    });
    speed = data.data.map(function(d){
        if (d.speed != undefined){
            return d.speed;
        }
    });

    // populate the chart with initial data
    $('#container').highcharts({
        title: { text: 'Placeholder Graph'},
        xAxis: { categories: t},
        series: [{
            data: speed,
            name: 'Speed'
        }]
    });
});