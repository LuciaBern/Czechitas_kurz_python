class Package:
    def __init__(self,address,weight,state):
        self.address = address
        self.weight = weight
        self.state = state
    
    def __str__(self):
        return f"Balík na adresu {self.address} má hmotnost {self.weight} kg je ve stavu {self.state}."
    def delivery_price(self):
        if self.weight < 10:
            price = 129
        elif self.weight <20:
            price = 159
        else: 
            price = 359
        return f"Cena přepravy je {price} Kč."
    def deliver(self):
        if self.state == "doručen":
            vysledok = "Balík již byl doručen."
        else: 
            self.state = "doručen"
            vysledok = "Doručení uloženo."
        return vysledok

""" Zkus si vytvořit alespoň dva objekty ze třídy Balik. 
U address uvažujeme typ řetězec (str), 
u weight desetinné číslo. 
U atributu state zadávej pro zjednodušení pouze dva stavy: doručen a nedoručen. """

balik_1 = Package("Radlická 150, Praha",3.55, "nedoručen")
balik_2 = Package("Plzeňská 35, Praha",15.48,"doručen")


print(balik_1)
print(balik_1.delivery_price())
print(balik_1.deliver())
print(balik_1.deliver())
""" print(balik_2)
print(balik_2.delivery_price()) """

