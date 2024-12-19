//2024-12-19 16:53

var http = require('http');

//create server object 

http.createServer(function (request, response) {

    response.write('2024-12-19 16:56');
    response.end();

  
}).listen(8080)

