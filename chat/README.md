# Chat
This chat exercise I learned the following things.

1. The `del` keyword which is used to remove an element from a list or dict; also it can be used to remove the binding of a variable.
2. _Persistent State_ is expressed in the `protocol.factory()`
3. The structural similarity between the echo, chat, and quote services
  * Define a protocol class
  * Define a factory class
  * Use `reactor.connectTCP` to initiate a connection to the server. 
  * Use `reactor.listenTCP` to listen for and respond to client connections
  * NOTE: communication doesnt start until `reactor.run()` is called. 
4. Discovered the _"Twisted from Scratch"_ how-to guide
5. Discovered the _"AutobahnPython"_ project