# antigen
Scraper pro zjišťování skutečně volné kapacity antigenních testů v reálném čase

## Krok první (volitelný): stažení seznamu poskytovatelů

Protože ÚZIS neposkytuje podle nejlepšího vědomí seznam poskytovatelů jako otevřená data,
musíme si je z přehledu vylámat sami.

Navíc nejsou jednoduše získatelné ani souřadnice odběrných míst, proto se ptáme Nominatimu OSM
a zbytek je opravený ručně za pomoci skriptu `manual_fill_coords.py` (z Mapy.cz).

Seznam aktuální k 20. prosinci 2020 je součástí repozitáře v souboru `providers.json`

Pro aktualizaci seznamu stačí spustit `./scrape_providers.py`
(a doplnit souřadnice tam kde se nepodařily přeložit automaticky).
