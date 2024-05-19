import requests

#cast 1:

ico = input("Zadejte IČO subjektu: ")
path = 'https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/ICO'
path = path.replace("ICO",ico)

response = requests.get(path)
rejstrik = response.json()

print(rejstrik["obchodniJmeno"])
print(rejstrik["sidlo"]["textovaAdresa"])

#cast 2:

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}

data = '{"obchodniJmeno": "nazev_subjektu"}'
nazev = input("Zadejte název subjektu: ")
data = data.replace("nazev_subjektu", nazev)

res = requests.post("https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat", headers=headers, data=data)

odpoved=res.json()
pocet = odpoved["pocetCelkem"]

print(f"Nalezeno subjektů: {pocet}")

for i in range(int(pocet)):
    jmeno = odpoved["ekonomickeSubjekty"][i]["obchodniJmeno"]
    ico = odpoved["ekonomickeSubjekty"][i]["ico"]
    print(f"{jmeno}, {ico}") 

