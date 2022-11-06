namespace = '/graphingService';

var socket = io(namespace);

socket.on('dateTime', function(data) {
    document.getElementById("server-time").innerHTML = data;
});

function GetDatabases() {
    socket.emit('getDatabases');
}

socket.on('onDatabaseNames', function(data) {
    console.log(data);   
    var list = document.getElementById("database");
    list.innerHTML='';
    data.forEach((item)=>{
        var li = document.createElement("a");
        li.innerText = item;
        li.setAttribute('href', "/graphingService/" + item)
        list.appendChild(li);
      })
      document.getElementById("databaseDiscovery").innerHTML = "Databases:";
});

function myPeriodicMethod() {
    socket.emit('dateTimeRequest', {data: '?'});
    setTimeout(myPeriodicMethod, 1000);
}
// schedule the first invocation:
setTimeout(myPeriodicMethod, 1000);