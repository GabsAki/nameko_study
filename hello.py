# Reference: 
# https://medium.com/nerd-for-tech/introduction-to-python-microservices-with-nameko-435efed35dd5

from nameko.rpc import rpc
from time import sleep

class GreetingService:
    name = "greeting_service"

    @rpc
    def hello(self, name):
        sleep(5)
        return "Hello, {}! (version 2)".format(name)
