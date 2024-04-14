class Package:
    def __init__(self,address,weight,state):
        self.address = address
        self.weight = weight
        self.state = state
    
    def get_info(self):
        return f"Balík na adresu {self.address} má hmotnost {self.weight} kg je ve stavu {self.state}."
    def delivery_price(self):
        if self.weight < 10:
            price = 129
        elif self.weight <20:
            price = 159
        else: 
            price = 359
        return f"Cena přepravy je {price} Kč."

""" Zkus si vytvořit alespoň dva objekty ze třídy Balik. 
U address uvažujeme typ řetězec (str), 
u weight desetinné číslo. 
U atributu state zadávej pro zjednodušení pouze dva stavy: doručen a nedoručen. """

balik_1 = Package("Radlická 150, Praha",3.55, "nedoručen")
balik_2 = Package("Plzeňská 35, Praha",15.48,"doručen")


print(balik_1.get_info())
print(balik_1.delivery_price())
print(balik_2.get_info())
print(balik_2.delivery_price())

""" Vytvoř metodu delivery_price(), která vypočítá cenu přepravy balíku. 
Cena přepravy je daná hmotností balíku. Cena přepravy balíku do 10 kg je 129 Kč, 
cena přepravy balíku od 10 kg do 20 kg je 159 Kč a cena přepravy balíků těžších než 20 kg je 359 Kč. 
Metoda spočítá cenu a vrátí ji jako číslo. """

