class Item:
    def __init__(self, name, price):
        self.name = str(name)
        self.price = float(price)

    def __str__(self):
        return f"{self.name}: {self.price} Kč."


class Pizza(Item):
    def __init__(self, name, price, ingredients):
        super().__init__(name, price)
        self.ingredients = dict(ingredients)

    def add_extra(self, ingredient, quantity, price_per_ingredient):
        self.ingredient = ingredient
        self.quantity = quantity
        self.price_per_ingredient = price_per_ingredient
        self.price += price_per_ingredient
        self.ingredients[ingredient] = quantity

    def __str__(self):
        return f"Pizza {self.name} se skládá z ingrediencí: {', '.join(self.ingredients)} a stojí {self.price} Kč."


class Drink(Item):
    def __init__(self, name, price, volume):
        super().__init__(name, price)
        self.volume = int(volume)

    def __str__(self):
        return f"Nápoj {self.name} o objemu {self.volume} ml stojí {self.price} Kč."


class Order:
    def __init__(self, customer_name, delivery_address, items, status):
        self.customer_name = str(customer_name)
        self.delivery_address = str(delivery_address)
        self.items = list(items)
        self.status = str(status)

    def mark_delivered(self):
        if self.status:
            self.status = "Doručeno"

    def __str__(self):
        return f"Objednávka na jméno {self.customer_name}, adresu {self.delivery_address}, která obsahuje položky: {", ".join(self.items)} je ve stavu {self.status}."


class DeliveryPerson:
    def __init__(self, name, phone_number, available=True, current_order=None):
        self.name = str(name)
        self.phone_number = str(phone_number)
        self.available = bool(available)
        self.current_order = current_order

    def assign_order(self, objednavka):
        self.current_order = objednavka
        self.available = False
        objednavka.status = "Na cestě"

    def complete_delivery(self, objednavka):
        self.available = True
        objednavka.status = "Doručeno"

    def __str__(self):
        if self.current_order == None:
            return f"Doručovatel {self.name} je k dispozici."
        else:
            if self.available == True:
                stav = "k dispozici"
            else:
                stav = "nedostupný"
            return f"Doručovatel {self.name}, tel. {self.phone_number} je {stav}."


# ------PROGRAM--------------------
# sortiment
pizza1 = Pizza("Margherita", 200, {"passata": 30, "mozzarella": 70})
pizza2 = Pizza("Capricciosa", 228, {
               "passata": 30, "mozzarella": 70, "olivy": 50, "šunka": 70, "žampiony": 60})
pizza3 = Pizza("Marinara", 180, {"passata": 30, "česnek": 40, "bazalka": 30})
pizza4 = Pizza("Prosciutto", 228, {
               "passata": 30, "mozzarella": 70, "šunka": 70, })
napoj1 = Drink("Coca Cola", 45, 330)
napoj2 = Drink("Fanta", 45, 330)
napoj3 = Drink("Sprite", 45, 330)
napoj4 = Drink("Soda", 25, 500)

# objednavky
obj1 = Order("Vincent Pruhovaný", "Kocourkova 13, 15800, Praha",
             [pizza1.name, napoj1.name], "Nová")
obj2 = Order("Agnes Černá", "Kočičkova 13, 15800, Praha",
             [pizza3.name, napoj2.name], "Nová")
obj3 = Order("Štepán Skvrnitý","Lesní 5, 15800, Praha", [pizza4.name,napoj3.name],"Nová")

# doručovatelé
dorucovatel1 = DeliveryPerson("Martin B.", "775453201")
dorucovatel2 = DeliveryPerson("Lucia B.", "775920433")
dorucovatel3 = DeliveryPerson("Vincent B.", "775340111")

# -------CODE-INITIALIZATION--------
print(pizza1, napoj1) # základní pizza a nápoj z nabídky
pizza1.add_extra("bazalka", 50, 10); print(pizza1) # něco navíc
print(dorucovatel1) # je dostupný, nemá přiřazenou objednávku
print(obj1) # nová objednávka
dorucovatel1.assign_order(obj1) # přiřazení obj.
print(dorucovatel1) # je nedostupný, má obj.
print(obj1) # stav obj. "na cestě"
dorucovatel1.complete_delivery(obj1) # doručení obj.
print(dorucovatel1, f"\n{obj1}") # kontrola
# ------CODE-END--------------------
