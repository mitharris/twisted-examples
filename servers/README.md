# Servers
This lesson is about gaining an understanding of TCP Servers and HTTP Servers. I learned how to accept a connection, process the request, and send back an HTTP-formatted response. Heres some of the highlights from my learning:

1. Discovered *Telnet*; I'm interested to if there are applications for Telnet for the purpose of the bot as Foreman.

2. The _App_ should be built using the *TCP transport layer protocol* _because_ HTTP uses it.
3. Specify how HTTP requests are process using the `web.http.Request()` class overriding the process method. 
4. There are 6 other HTTP content-type header types, including: multipart, message, image, audio, video, and application. The `message` content-type seems sort of interesting.
5. I think that a `web.resource.Resource()` class may represent the same concept as a controller in traditional _MVC_ architectures.


