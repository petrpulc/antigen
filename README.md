# antigen
Scraper pro zjišťování skutečně volné kapacity PCR a antigenních testů v reálném čase

## Krok první: stažení seznamu poskytovatelů

Přístup k datům o poskytovatatelích sice není nikde zdokumentovaný, ale je možné použít podkladová data z ArcGISu ÚZIS kde je úplně to samé jako na webu crs.uzis.cz.

Stačí tedy spustit `./get_providers.sh`

## Krok druhý: najít poskytovatele v okolí

Aneb: nemá smysl kontrolovat kapacitu u poskytovatelů na druhé straně republiky.

`./find.py --lat <zem. šířka> --lon <zem. délka> --range <okolí v km>`
