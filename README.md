# antigen
Scraper pro zjišťování skutečně volné kapacity PCR a antigenních testů v reálném čase

## Krok první: stažení seznamu poskytovatelů

Přístup k datům o poskytovatatelích sice není nikde zdokumentovaný, ale je možné použít podkladová data z ArcGISu ÚZIS kde je úplně to samé jako na webu crs.uzis.cz.

Stačí tedy spustit `./get_providers.sh`

## Krok druhý: najít poskytovatele v okolí

Aneb: nemá smysl kontrolovat kapacitu u poskytovatelů na druhé straně republiky.

`./find.py --lat <zem. šířka> --lon <zem. délka> --range <okolí v km>`

## Krok třetí [WIP]: zpracovat data z rezervačního formuláře

Závisí na poskytovateli rezervační služby, veřejné API je snem, ale nevím o žádném a všude rozhodně nebude existovat. Parsery je potřeba napsat pro: (SLD seřazené podle počtu poskytovatelů)

- [x] reservatic.com (78)
- [ ] reservio.com (16)
- [ ] reservio.cz (11)
- [ ] aeskulab.cz (10)
- [ ] spadia.cz (10)
- [ ] prevedig.cz (8)
- [ ] medicalc.cz (8)
- [ ] kzcr.eu (7)
- [ ] euclaboratore.cz (7)
- [ ] labin.cz (6)
- [ ] citylab.cz (6)
- [ ] kr-vysocina.cz (6)
- [ ] rezervace-synlab.cz (6)
- [ ] vidia-diagnostika.cz (5)
- [ ] msk.cz (4)
- [ ] ifcor.cz (4)
- [ ] fnkv.cz (3)
- [ ] reenio.cz (3)
- [ ] synlab.cz (3)
- [ ] vysetri.me (2)
- [ ] nemzatec.eu (2)
- [ ] staynegative.cz (2)
- [ ] zuusti.cz (2)
- [ ] nemjil.cz (2)
- [ ] nempt.cz (2)
- [ ] nemocnice-st.cz (2)
- [ ] nemocnice-horovice.cz (2)
- [ ] nemorako.cz (2)
- [ ] nemocnicepk.cz (2)
- [ ] fnol.cz (2)
- [ ] jihnem.cz (2)
- [ ] nemocnice-beroun.cz (2)
- [ ] gendet.cz (2)
- [ ] fnmotol.cz (2)
- [ ] nemocnicekolin.cz (2)
- [ ] biopticka.cz (2)
- [ ] nemzn.cz (2)
- [ ] fnusa.cz (2)
- [ ] cuni.cz (2)
- [ ] covid-ghc.com (2)
- [ ] nemuh.cz (2)
- [ ] prahamp.cz (2)
- [ ] nemobk.cz (2)
- [ ] anygence.com (2)
- [ ] nnm.cz (1)
- [ ] hospital-bn.cz (1)
- [ ] nem-km.cz (1)
- [ ] nemcb.cz (1)
- [ ] elitemedical.eu (1)
- [ ] fnplzen.cz (1)
- [ ] klaudianovanemocnice.cz (1)
- [ ] covidtest24.cz (1)
- [ ] nemlib.cz (1)
- [ ] covidtestbrno.cz (1)
- [ ] nemjbc.cz (1)
- [ ] fno.cz (1)
- [ ] bulovka.cz (1)
- [ ] nemocnice-vs.cz (1)
- [ ] nemocnicepribram.cz (1)
- [ ] rostiapp.cz (1)
- [ ] nemsl.cz (1)
- [ ] kkn.cz (1)
- [ ] e-gene.cz (1)
- [ ] nembv.cz (1)
- [ ] nemocnice-lt.cz (1)
- [ ] nemtisnov.cz (1)
- [ ] onjc.cz (1)
- [ ] euc.cz (1)
- [ ] ml-software.cz (1)
- [ ] nemocnicenachod.cz (1)
- [ ] agellab.cz (1)
- [ ] vfn.cz (1)
- [ ] nemcl.cz (1)
- [ ] testymost.cz (1)
- [ ] dia-gon.cz (1)
- [ ] covidtestpraha.cz (1)
- [ ] nemckr.cz (1)
- [ ] zuova.cz (1)
- [ ] mnof.cz (1)
- [ ] nemocnicesumperk.cz (1)
- [ ] covidpoint.cz (1)
- [ ] interclinic.cz (1)
- [ ] antigen.cz (1)
- [ ] nazadanku.cz (1)
- [ ] sapacovid.cz (1)
- [ ] snopava.cz (1)
- [ ] nemocnicekutnahora.cz (1)
- [ ] hola-biolabs.com (1)
- [ ] nemcaslav.cz (1)
- [ ] kntb.cz (1)
