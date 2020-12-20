# antigen
Scraper pro zjišťování skutečně volné kapacity antigenních testů v reálném čase

## Krok první (volitelný): stažení seznamu poskytovatelů

Protože ÚZIS neposkytuje podle nejlepšího vědomí seznam poskytovatelů jako otevřená data,
musíme si je z přehledu vylámat sami.

Seznam aktuální k 20. prosinci 2020 je součástí repozitáře v souboru `providers.json`

Pro občerstvení seznamu stačí spustit `./scrape_providers.py`
