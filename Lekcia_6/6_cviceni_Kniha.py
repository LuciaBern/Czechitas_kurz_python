""" Zkus pro nakladatelství vytvořit software s využitím tříd a objektů.
Vytvoř tedy třídu Book, která reprezentuje knihu. Každá kniha bude mít atributy title, 
pages a price. Hodnoty nastav ve funkci __init__.

Přidej knize funkci get_info(), která vypíše informace o knize v nějakém pěkném formátu.
Přidej metodu get_time_to_read(). Metoda vrátí čas potřebný na přečtení knihy v hodinách. 
S využitím atributu pages vypočítej čas na přečtení knihy. 
Metoda bude mít nepovinný parametr, který udává počet minut potřebných pro přečtení jedné stránky knihy. 
Dobu potřebnou na přečtení knihy získáš jako násobek doby potřebné na přečtení jedné stránky knihy a počet stránek knihy. 
Výchozí hodnota nepovinného parametru je 4. """

class Book:
    def __init__(self,title,pages,price):
        self.title = title
        self.pages = pages
        self.price = price

    def get_info(self):
        return f"Kniha s názvem {self.title} má {self.pages} stran a stojí {self.price} Kč."
    
    def get_time_to_read(self,time=4):
        time_to_read = int(time * self.pages/60)
        return f"Přečíst knihu s názvem {self.title} potrvá cca {time_to_read} hodin."

kniha = Book("Hlava XXII",255,349)

print(kniha.get_info(), kniha.get_time_to_read())

