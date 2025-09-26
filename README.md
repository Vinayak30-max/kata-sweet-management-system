SweetShop 🛍🍬

A simple Python class to manage sweets in a shop. You can add, update, delete, and list sweets easily.

How to Use

shop = SweetShop()
shop.add_sweet('Ladoo', 20, 10)
shop.add_sweet('Barfi', 10, 15)
shop.update_sweet('Ladoo', quantity=25)
print(shop.list_sweets())
shop.delete_sweet('Barfi')
print(shop.list_sweets())

Error Handling ⚠

Invalid inputs (empty name, quantity ≤ 0, price ≤ 0) raise a ValueError

Updating or deleting a non-existent sweet returns None

License 📄

MIT License
