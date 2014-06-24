//need to install flask-socketio for any of this shit to work

//Opens a socket with the server.
//Updates the speed, previous time, current time,
//throttle percentage and brake percentage. 

$(document).ready(function(){
    var socket = io.connect();
    socket.on('updateSpeed', function(msg) {
    	console.log("Boo!");
    });
   	//dummy socket speed
    //socket.on('updateSpeed', function(msg) {
    $('#speed').html('<p>' + 5 + ' mph</p>');
    //});
    //setInterval(getSpeed, 180);
    //function getSpeed() {
        //socket.emit('update', {data : {}});    
    //}
});

