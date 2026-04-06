#Поведенчкские патторны
#Strategy
class StandartDelivery:
    def calculate(self, weight):
        return 200 + weight * 10

class ExpresDelivery:
    def calculate(self, weight):
        return 500 + weight * 20
    
class PinkupDelivery:
    def calculate(self, weight):
        return 0

class DeliveryCalc: 
    def __init__(self, strategy):
        self.strategy = strategy

    def get_price(self, weight):
        return self.strategy.calculate(weight)
    
print(DeliveryCalc(PinkupDelivery()).get_price(10))


#Status
class DrafState:
    def publish(self, document):
        document.state = ReviewState()
        return "Ch"
    
class ReviewState:
    def publish(self, document):
        document.state = PublishedState()
        return "pablish"
    
class PublishedState:
    def publish(self, document):
        return "Good"
    
class Document:
    def __init__(self):
        self.state = DrafState()

    def publish(self):
        return

#Observer
class Order:
    def __init__(self):
        self.subscribers = []

    def subscriders(self, listner):
        self.subscribers.append(listner)

    def set_status(self, status):
        for subscribers in self.subscribers:
            self.subscribers(status)

def email_listner(status):
    print({status})

def sms_listner(status):
    print({status})

order = Order()
order.subscribers(email_listner)



#Momento
class Editor:
    def __init__(self):
        self.text = ""

    def write(self, text):
        self.text += text

    def save(self):
        return self.text
    
    def restore(self, snapshot):
        self.text = snapshot

editor = Editor()
editor.write("Hello")
snapshot = editor.save()
editor.write(", world")
print(editor.text)
editor.restore(snapshot)
print(editor.text)

#Mediator
class ChatMediator:
    def send(self, message, user):
        for c in user.colleagues:
            if c is not user:
                c.receive(message)



class User:
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator
        self.colleagues = []

    def send(self, message):
        self.mediator.send(f"{self.name}: {message}", self)

    def receive(self, message):
        print(message)

mediator = ChatMediator()
alice = User("Alice", mediator)





#Command
class Light:
    def on(self):
        print("Light is on")

class TurnOnCommand:
    def __init__(self, light):
        self.light = light
    
    def execute(self):
        self.light.on()

class Button:
    def __init__(self, command):
        self.command = command

    def press(self):
        self.command.execute()
Button(TurnOnCommand(Light())).press



#Chain of Responsibility
class Handler:
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def handle(self, request):
        if self.next_handler:
            return self.next_handler(request)
        return "Unhandler"

class AuthHandler(Handler):
    def handle(self, request):
        if not request.get("user"):
            return "401 U"
        return super().handle(request)

class RoleHandler(Handler):
    def handle(self, request):
        if request.get("role") != "admin":
            return "401 F"
        return super().handle(request)

chain = AuthHandler(RoleHandler())
print(chain.handle({"user": "alice", "role": "admin"}))


#Proxy
class Image:
    def __init__(self, path):
        print("Загрузка")
        self.path = path
    def show(self):
        print(f"Show {self.path}")

class ImageProxy:
    def __init__(self, path):
        self.path = path
        self._real = None
    def show(self):
        if self._real is None:
            self._real = Image(self.path)
        self._real.show()

img = Image("photo.png")
img.show()#загрустка
img.show()#пусто


#Flyweight
class Flyweight:
    def __init__(self, color):
        self.color = color
    def draw(self, x, y):
        print(self.color, x, y)

class Factory:
    __cached = {}


    @classmethod
    def get(cls, color):
        if color not in cls.__cached:
            cls.__cached[color] = Flyweight(color)
        return cls.__cached[color]
    
red1 = Factory.get("red")
red2 = Factory.get("red")

print(red1 is red2)
        



#Facade
class Paymentservice:
    def pay(self, amount):
        print(f"Оплата {amount} подтверждения")

class WarehouseService:
    def reserve(self, item):
        print(f"Njdfh {item} pfhtu")

class DeliveryServise:
    def create(self, item):
        print(f"")

class OrderFacade:
    def __init__(self):
        self.pay
        



#Decorator
class Coffee:
    def price(self):
        return 20
    
    def description(self):
        return "Кофе"

class MilkDecorator:
    def __init__(self, drink):
        self.drink = drink

    def price(self):
        return self.drink.price() + 30
    
    def description(self):
        return self.drink.description() + ", молоко"
    
class SypupDecorator:
    def __init__(self, drink):
        self.drink = drink

    def price(self):
        return self.drink.price() + 25
    
    def description(self):
        return self.drink.description() + ", сироп"
    
drink = SypupDecorator(MilkDecorator(Coffee()))
print()

#Composite
class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def det_size(self):
        return self.size
    
class Folder:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, child):
        self.children.append(child)
    
    def get_size(self):
        return sum(child.get_size() for child in self.children)
    
docs = Folder("docs")
docs.add(File("text_1.txt", 10))
docs.add(File("text_2.txt", 20))
print(docs.get_size())

#Prototype
import copy
template_order = {
    "delivery": "standard",
    "promo": False,
    "items":["book"]
}
fast_order = copy.deepcopy(template_order)
fast_order["delivery"] = "express"

print(template_order, fast_order)

#Builder
class LaptopBuilder:
    def __init__(self):
        self.laptop = {
            "cup": "Intel i5",
            "ram": "8",
            "ssd": 256,
            "gru": "intergrated"
        }

    def for_study(self):
        self.laptop["ram"] = 16
        self.laptop["ssd"] = 512
        return self
    
    def for_gaming(self):
        self.laptop["ram"] = 32
        self.laptop["ssd"] = 1024
        self.laptop["gpu"] = "RTX 4070"
        return self
    
    def with_cup(self, cpu):
        self.laptop["cpu"] = cpu
        
    def build(self):
        return self.laptop.copy()
    
print(LaptopBuilder().for_study().with_cup("Intel i7").build())

#Abstract Factory
class LightButton:
    def  render(self):
        return "LightButton"
    
class LightInput:
    def  render(self):
        return "LightInput"
    
class DarkButton:
    def  render(self):
        return "DarkButton"
    
class DarkInput:
    def  render(self):
        return "DarkInput"

class LightThemeFactory:
    def create_button(self):
        return LightButton()
    
    def input_button(self):
        return LightInput()
    
class DarkThemeFactory:
    def create_button(self):
        return DarkButton
    
    def input_button(self):
        return DarkInput()

def build_from(factory):
    button = factory.create_button()
    field = factory.create_input()
    print(button.render(), field.render())

build_from(LightThemeFactory)


# Factory Method
class EmailSender:
    def send(self, messange):
        return f"Email: {messange}"
    
class SmsSender:
    def send(self, messange):
        return f"SMS: {messange}"
    
class NotificationFactory:
    @staticmethod
    def create(channel):
        if channel == "email":
            return EmailSender
        if channel == "sms":
            return SmsSender
        raise ValueError("Unknown channel")

sender = NotificationFactory.create("sms")
sender.send("Ваш код подтверждения 1234")

# Singleton

class AppConfig: 
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.mode = "prod"
        return cls._instance