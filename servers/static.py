from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.static import File

# ex.1 Static content serve
# resource = File('./')
# factory = Site(resource)

ex. 2 Static content serve multiple urls
root = File('./')
root.putChild("doc", File("./doc"))
root.putChild("logs", File("./logs"))
factory = Site(root)

reactor.listenTCP(8000, factory)
reactor.run()