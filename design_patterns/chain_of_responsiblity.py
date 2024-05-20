"""
Chain of Responsibility

Chain of Responsibility is a behavioral design pattern that lets
you pass requests along a chain of handlers. Upon receiving a
request, each handler decides either to process the request or
to pass it to the next handler in the chain.
"""


from abc import ABC, abstractmethod


# Handler interface
class Handler(ABC):
    @abstractmethod
    def handle_request(self, request):
        pass


# Concrete Handler 1
class ConcreteHandler1(Handler):
    def __init__(self, successor=None):
        self.successor = successor

    def handle_request(self, request):
        if request >= 0 and request < 10:
            print(f"Request {request} handled by ConcreteHandler1")
        elif self.successor:
            self.successor.handle_request(request)


# Concrete Handler 2
class ConcreteHandler2(Handler):
    def __init__(self, successor=None):
        self.successor = successor

    def handle_request(self, request):
        if (request >= 10 and request < 20):
            print(f"Request {request} handled by ConcreteHandler2")
        elif self.successor:
            self.successor.handle_request(request)


# Concrete Handler 3
class ConcreteHandler3(Handler):
    def __init__(self, successor=None):
        self.successor = successor

    def handle_request(self, request):
        if request >= 20 and request < 30:
            print(f"Request {request} handled by ConcreteHandler3")
        elif self.successor:
            self.successor.handle_request(request)


# Client code
def main():
    handler_chain = ConcreteHandler1(ConcreteHandler2(ConcreteHandler3()))

    requests = [5, 12, 25, 30]

    for request in requests:
        handler_chain.handle_request(request)


if __name__ == "__main__":
    main()


