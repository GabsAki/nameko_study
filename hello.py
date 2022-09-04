# Reference: 
# https://medium.com/nerd-for-tech/introduction-to-python-microservices-with-nameko-435efed35dd5

from nameko.rpc import rpc

class GreetingService:
    name = "greeting_service"

    @rpc
    def hello(self, name):
        return "Hello, {}!".format(name)
