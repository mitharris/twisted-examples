# Deferreds
Deferreds are important because we use them when writing HTTP servers and clients. 
This time around I learned some pretty important distinctions about Deferreds, including:

1. The method `addCallbacks()` on the `internet.defer.Deferred` class registers a callback with the callback chain and an errback with the errback chain *at the same level*

2. The method `addCallback()` on the `internet.defer.Deferred` class registers a callback with the callback chain and a _pass-through_ with the errback chain, which simply returns the result passed to it.

3. The method `addErrback()` on the `internet.defer.Deferred` class registers an errback with the errback chain and a _pass-through_ with the callback chain.

The important difference is that callbacks and errbacks registered together using `Deferred.addCallbacks()` _do not interact_ or cannot handle exceptions raised by that callback. Another way of saying is that an `exception` raised on level 3 could be handled by the errback on level 4. 