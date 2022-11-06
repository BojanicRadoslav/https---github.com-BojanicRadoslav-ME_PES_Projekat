namespace = '/relayCtrl';

var socket = io(namespace);
var relay1Connection = 0
var relay1Connection = 0

socket.on('dateTime', function(data) {
    document.getElementById("server-time").innerHTML = data;
});

socket.on('onRelay1', function(data) {
    // extract data
    if(data == "connect")
    {
        relay1Connection = 1;
    }

    if(relay1Connection == 1)
    {
        var stateText = "";
        if(data == 1)
        {
            stateText = "Relay 1: on"
        }
        else
        {
            stateText = "Relay 1: off"
        }
        document.getElementById("relay_1").innerHTML = stateText;
    }
});

socket.on('onRelay2', function(data) {
    if(data == "connect")
    {
        relay2Connection = 1;
    }

    if(relay2Connection == 1)
    {
        var stateText = "";
        if(data == 1)
        {
            stateText = "Relay 2: on"
        }
        else
        {
            stateText = "Relay 2: off"
        }
        document.getElementById("relay_2").innerHTML = stateText;
    }
});

function ConnectRelays() {
    socket.emit('ConnectRelays');
}

function relay1Ctrl()
{
    if(document.getElementById("relay_1").innerHTML.includes("click to connect"))
    {
        ConnectRelays();
    }
    else
    {
        socket.emit('relay1Ctrl');
    }
}

function relay2Ctrl()
{
    if(document.getElementById("relay_2").innerHTML.includes("click to connect"))
    {
        ConnectRelays();
    }
    else
    {
        socket.emit('relay2Ctrl');
    }
}

function myPeriodicMethod() {
    socket.emit('dateTimeRequest', {data: '?'});
    setTimeout(myPeriodicMethod, 1000);
}
// schedule the first invocation:
setTimeout(myPeriodicMethod, 1000);