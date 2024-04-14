class Book:
    def __init__(self,title,pages,price,sold,costs):
        self.title = title
        self.pages = pages
        self.price = price
        self.sold = sold
        self.costs = costs
        
    def get_info(self):
        return f"Kniha s názvem {self.title} má {self.pages} stran a stojí {self.price} Kč."
    
    
    def get_time_to_read(self,time=4):
        time_to_read = int(time * self.pages/60)
        return f"Přečíst knihu s názvem {self.title} potrvá cca {time_to_read} hodin."
    def profit(self):
        zisk = self.sold *(self.price - self.costs)
        return zisk
    
    def rating(self):
        if self.profit() < 50000:
            rating = "Propadák"
        elif self.profit() < 500000:
            rating = "Priemer"
        else:
            rating = "Bestseller"
        return rating
    

kniha = Book("Hlava XXII",255,349,95000,250)

print(kniha.get_info(), kniha.get_time_to_read(),kniha.rating())

