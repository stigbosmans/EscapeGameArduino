var server = require('http').createServer();
var io = require('socket.io')(server);
io.on('connection', function(client){
	console.log("connected")
	client.on('msg', function(data){
		io.emit('msg', data);
	});
	client.on('disconnect', function(){});
});
server.listen(3000);