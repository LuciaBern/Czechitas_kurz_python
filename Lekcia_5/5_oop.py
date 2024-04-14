class Employee:
    def __init__(self,name, position, holiday_entitlement):
        self.name = name
        self.position = position
        self.holiday_entitlement = holiday_entitlement

    def get_info(self):
        return f"Zamestnanec {self.name} pracuje na pozici {self.position}."
    
frantisek = Employee("Frantisek", "prodavac", 9)
print(frantisek.get_info())

jitka = Employee("Jitka","administrator",25)
print(jitka.get_info())