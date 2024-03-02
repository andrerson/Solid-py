class PaymentGateway:
    def process_payment(self, amount):
        print('Making payment on Stripe')
        pass

class Item: 
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self, order_id, items, payment_gateway):
        self.order_id = order_id
        self.items = items
        self.payment_gateway = payment_gateway

    def calculate_total(self):
        total = sum(item.price for item in self.items)
        return total
    
    def place_order(self):
        total = self.calculate_total()
        #Perform order placement logic
        self.payment_gateway.process_payment(total)
    
# High-level module
class OrderManager:
    def place_order(self, order):
        order.place_order()

payment_gateway = PaymentGateway()
order_items = [
    Item("Product 1", 10),
    Item("Product 2", 20),
    Item("Product 3", 15)
]

order = Order(123, order_items, payment_gateway)
order_manager = OrderManager()
order_manager.place_order(order)