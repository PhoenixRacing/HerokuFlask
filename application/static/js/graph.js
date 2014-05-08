$(function () {

    if (data.data.length > 0){
        initialize_chart(data);
    }else{
        $('#container').append('<p>Sorry, there is no data available at this time.</p>');
    }

});

var max_data_points = 50;

function initialize_chart(data){
    $('#container').empty()

    // populate the chart with initial data
    chart = $('#container').highcharts({
        title: { text: 'Placeholder Graph'},
        // xAxis: { categories: t},
        series: [{
            data: getSpeedSeries(data),
            name: 'Speed'
        }]
    });
}

function getSpeedSeries(data){
    data_tuples = data.data.map(function(d){
        if (d.speed != undefined){
            dt = d.time.$date - data.start_time.$date;
            return [dt/60000, d.speed];
        }
    });
    return data_tuples.slice(-max_data_points)
}