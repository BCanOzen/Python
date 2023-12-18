import requests as rq
import json as js

#https://www.exchangerate-api.com üzerinden bir requests denemesidir. 


api_key = "cc6de6a2e0f66de897000498"
api_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

bozulan_doviz = input("Bozulan döviz turu: ") # USD
alinan_doviz = input("Alınan döviz türü: ") # TRY
miktar = int(input(f"Bozmak istediğiniz {bozulan_doviz} miktarını giriniz: ")) # miktar

sonuc = rq.get(api_url + bozulan_doviz)
sonuc_json = js.loads(sonuc.text)

print("1 {0} = {1} {2}".format(bozulan_doviz,sonuc_json["conversion_rates"][alinan_doviz],alinan_doviz))
print("{0} {1} = {2} {3}".format(miktar, bozulan_doviz, miktar * sonuc_json["conversion_rates"][alinan_doviz],alinan_doviz))
 
