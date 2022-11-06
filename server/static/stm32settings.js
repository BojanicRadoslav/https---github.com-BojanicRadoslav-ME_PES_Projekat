namespace = '/stmCommander';

var socket = io(namespace);

socket.on('dateTime', function(data) {
    document.getElementById("server-time").innerHTML = data;
});

function myPeriodicMethod() {
    socket.emit('dateTimeRequest', {data: '?'});
    setTimeout(myPeriodicMethod, 1000);
}
// schedule the first invocation:
setTimeout(myPeriodicMethod, 1000);