class SweetShop:
    def __init__(self):
        self.inventory = []

    def add_sweet(self, name, quantity, price):
        if not name or quantity <= 0 or price <= 0:
            raise ValueError('Invalid input')
        sweet = {'name': name, 'quantity': quantity, 'price': price}
        self.inventory.append(sweet)
        return sweet

    def get_sweet(self, name):
        for sweet in self.inventory:
            if sweet['name'] == name:
                return sweet
        return None

    def update_sweet(self, name, quantity=None, price=None):
        sweet = self.get_sweet(name)
        if sweet is None:
            return None
        if quantity is not None:
            sweet['quantity'] = quantity
        if price is not None:
            sweet['price'] = price
        return sweet

    def delete_sweet(self, name):
        for i, sweet in enumerate(self.inventory):
            if sweet['name'] == name:
                return self.inventory.pop(i)
        return None

    def list_sweets(self):
        return self.inventory

# Usage example
shop = SweetShop()
shop.add_sweet('Ladoo', 20, 10)
shop.add_sweet('Barfi', 10, 15)
shop.update_sweet('Ladoo', quantity=25)
print(shop.list_sweets())
shop.delete_sweet('Barfi')
print(shop.list_sweets())
