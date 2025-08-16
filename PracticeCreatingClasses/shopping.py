class Item:
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
       
class ShoppingCart:

    def __init__(self):
        self.items = []
        self.total_cost = 0

    def add_item(self, newitem):
        self.items.append(newitem)
        self.total_cost += newitem.price

    def rem_item(self, newitem): 
        self.items.remove(newitem)
        self.total_cost -= newitem.price

    def empty_cart(self):
        self.items = []
        self.total_cost = 0  

    def print_cart_info(self):
        for item in self.items:
            print(f"{item.name} ${item.price}")
        print(f"totalcost=${self.total_cost}")

item1 = Item("MacBookM55", 150000000000000.25)
item2 = Item("iPhone24 Steve Jobs idgaf its the same phone!!!!!", 100000000.25)        
item3 = Item("iPhone25 Steve Jobs idgaf its still the same damn phone!!!!! Same same but different (added few jailbreak tweaks from 2015 and new chip + 4% better performance)", 1000039393939)

cart = ShoppingCart()
cart.add_item(item1) 
cart.add_item(item2)
cart.empty_cart()
cart.add_item(item3)
cart.print_cart_info()


        







