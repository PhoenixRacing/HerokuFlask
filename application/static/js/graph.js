$(function () {
	console.log(tach);
	console.log(speed);
	// var speed = data[0].speed

	// $("#yeebox").text(data["speed"]);
	var Xdata = [1,1,2,2,3,4,4,5,6]
	var Ydata = [1,1,2,2,3,4,4,5,6]
    $('#container').highcharts({
        title: { text: 'Placeholder Graph'},
        xAxis: { categories: Xdata},
        series: [{
            data: Ydata,
            name: 'Speed'
        }]
    });
});