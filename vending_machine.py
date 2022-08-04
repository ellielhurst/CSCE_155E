class VendingMachine:
    def __init__(self):
        self.bottles = 20
        
    def purchase(self, amount):
        self.bottles = self.bottles - amount
      
    def restock(self, amount):
        self.bottles = self.bottles + amount
    
    def get_inventory(self):
        return self.bottles
        
    def report(self):
        print(f'Inventory: {self.bottles} bottles')

if __name__ == "__main__":
    drink_machine = VendingMachine()
    drinks_to_buy = int(input("Drinks to buy?"))
    bottles_to_stock = int(input("Bottles to stock?"))
    drink_machine.purchase(drinks_to_buy)
    drink_machine.restock(bottles_to_stock)
    drink_machine.report()
