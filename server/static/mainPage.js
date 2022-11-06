namespace = '/mainPage';

var socket = io(namespace);

socket.on('connect', function() {
    socket.emit('my_event', {data: 'Client connection deluxe'});
});

socket.on('dateTime', function(data) {
    document.getElementById("server-time").innerHTML = data;
});

socket.on('onStmData', function(data) {
    // extract data
    var temp = -99.9;
    var hum = -99.9;
    document.getElementById("temp-value").innerHTML = temp;
    document.getElementById("hum-value").innerHTML = hum;
});

function myFunction() {
    socket.emit('buttonClick', {data: 'Button is clicket at client side'});
}

function myPeriodicMethod() {
    socket.emit('dateTimeRequest', {data: '?'});
    setTimeout(myPeriodicMethod, 1000);
}
// schedule the first invocation:
setTimeout(myPeriodicMethod, 1000);