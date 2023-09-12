"""Tämä scripti yhdistää Maptionnaire-karttakyselystä saatuihin pistemuotoisiin vastauksiin vastaajien kaikki taustatiedot.
Scriptin lopputulos on haluttuun paikkaan tallennettu csv-tiedosto. Absoluuttiset polut on poistettu."""

# Tuodaan pandas-kirjasto
import pandas as pd
#import tkinter as tk

# Tuodaan Maptionnairesta saadut ja erotellut datat dataframeiksi 
polku1 = r'polku/Vastaajat.xlsx'
polku2 = r'polku/Pistevastaukset.xlsx'
vastaajat = pd.read_excel(polku1)
pistevastaukset = pd.read_excel(polku2)

# Yhdistetään vastaajakohtaiset datat pistevastauksiin
vastaukset_yhdistetty = pd.merge(pistevastaukset, vastaajat, on='Respondent ID')

# Tallennetaan vastaukset uuteen csv-taulukkoon
vastaukset_yhdistetty.to_csv(r'polku\tulos_print.csv', sep=';', index=False, encoding='utf-8')

# Alla kuvailuun käytettyjä käskyjä
"""
print(vastaukset_yhdistetty)

print('Vastaajat-taulukko: ',vastaajat)
print('')
print('Pistevastaukset-taulukko: ',pistevastaukset)
"""