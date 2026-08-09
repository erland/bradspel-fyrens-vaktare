# [REGLERV3] Fyrens väktare

> Observera: detta dokument är äldre. Aktuell rekommenderad balans finns i `docs/rulebook.md` och `docs/recommended-balance-REGLERV4.md`.

**Version:** REGLERV3  
**Status:** Arbetsregler för nästa provspelning, uppdaterad spelarbalans  
**Spelare:** 2–4  
**Rekommenderad första test:** 2 spelare  
**Speltid:** ca 20–30 minuter  
**Typ:** Kooperativt äventyrs- och byggspel

---

## Ändringar från [REGLERV2] till [REGLERV3]

Den här versionen ändrar bara rekommenderad startmat för fler spelarantal:

- **3 spelare:** startmat ändras till **2 mat**, Mörkerspår är fortsatt **9 steg**.
- **4 spelare:** startmat ändras till **1 mat**, Mörkerspår är fortsatt **8 steg**.
- **2 spelare:** oförändrat: **4 mat** och **10 steg**.

Syftet är att kompensera för att fler spelare har fler handlingar per dag och därför får större nytta av varje stoppad natt.

---

## 1. Spelets mål

Spelarna samarbetar för att bygga **Fyren** innan Mörkret hinner ta över Kubriket.

Spelarna vinner när de bygger den sista Fyrdelen:

1. **Grund**
2. **Torn**
3. **Ljuskärna**

Spelarna förlorar om **Mörkermarkören** når sista rutan på Mörkerspåret.

---

## 2. Innehåll

För en första prototyp behövs:

- 1 spelbräde
- 2–4 spelarpjäser
- 1 Mörkermarkör
- resursmarkörer: trä, sten, mat och kristall
- 12 fyndkort
- 12 hotkort
- 1 A6-referenskort eller regelöversikt

Låna gärna kuber, mynt, pärlor eller papperslappar som resurser i första testet.

---

## 3. Rekommenderad balans för Mörkerspår

Använd olika längd på Mörkerspåret beroende på antal spelare.

| Antal spelare | Startmat i Basförrådet | Mörkerspår |
|---:|---:|---:|
| 2 spelare | 4 mat | 10 steg |
| 3 spelare | 2 mat | 9 steg |
| 4 spelare | 1 mat | 8 steg |

**Första rekommenderade test:** 2 spelare, 4 startmat och 10-stegs Mörkerspår.

---

## 4. Förberedelser

1. Lägg spelbrädet mitt på bordet.
2. Placera alla spelarpjäser på **Bas**.
3. Placera Mörkermarkören på första rutan på Mörkerspåret.
4. Lägg **4 mat** i Basförrådet.
5. Lägg övriga resursmarkörer bredvid spelbrädet.
6. Blanda fyndkorten och lägg dem i en hög.
7. Blanda hotkorten och lägg dem i en hög.
8. Bestäm fast turordning, till exempel medurs.

---

## 5. Spelplan

Spelplanen består av rutor. Rörelse sker ortogonalt, alltså upp, ned, vänster eller höger. Diagonal rörelse är inte tillåten.

Faktisk karta i nuvarande prototyp:

```text
Rad 1: Skog | Skog | Ruin     | Berg | Grotta
Rad 2: Bas  | Stig | Fyrplats | Stig | Grotta
Rad 3: Stig | Äng  | Stig     | Berg | Stig
Rad 4: Äng  | Ruin | Äng      | Stig | Skog
```

---

## 6. Turordning

Spelet spelas i **fast turordning**.

På din tur har du normalt **2 handlingar**.

När alla spelare har haft varsin tur sker **Nattfasen**.

Sedan börjar nästa dag med samma fasta turordning.

---

## 7. Handlingar

På din tur får du göra upp till 2 handlingar.

Du kan välja samma handling flera gånger om inget annat sägs.

### 7.1 Flytta

Flytta din spelarpjäs 1 steg till en angränsande ruta.

Du får inte flytta diagonalt.

### 7.2 Samla

Få 1 resurs från rutan du står på, om rutan ger resurser.

### 7.3 Utforska

På **Ruin** får du dra 1 fyndkort.

Lös kortet direkt om kortet inte säger något annat.

### 7.4 Bygga

På **Basen** eller **Fyrplatsen** får du bygga nästa Fyrdel om ni har rätt resurser.

Fyrdelarna måste byggas i ordning:

1. Grund
2. Torn
3. Ljuskärna

### 7.5 Vila

På **Basen** får du ta 1 mat.

Lägg maten i Basförrådet eller låt spelaren bära den, enligt vad gruppen beslutar när handlingen görs.

---

## 8. Gratis saker på Basen

När du är på **Basen** får du göra följande gratis, utan att använda handling:

- lämna valfritt antal resurser till Basförrådet
- ta valfritt antal mat från Basförrådet och bära med dig
- lämna mat till Basförrådet

Detta kan göras under din tur när du befinner dig på Basen.

---

## 9. Stig

**Stig är en snabb väg.**

När du står på **Stig** och din nästa handling är **Flytta**, får du flytta upp till **2 steg** i stället för 1.

Du får stanna efter 1 steg.

Du får inte samla resurser på Stig.

Viktigt:

```text
Stig ger inte extra rörelse när du går in på en Stig.
Stig förbättrar bara en Flytta-handling som börjar på Stig.
```

Exempel:

```text
Handling 1: Bas → Stig
Handling 2: Från Stig får du flytta upp till 2 steg
```

Detta är två separata Flytta-handlingar.

---

## 10. Mat

Mat är en tempo- och trygghetsresurs.

Mat kan användas på två sätt:

1. som extra handling för en spelare
2. som Nattvakt från Basförrådet

### 10.1 Äta mat för extra handling

En gång per tur får du betala 1 **medtagen mat** för att få **1 extra handling** den turen.

Det betyder att du normalt har 2 handlingar, men kan få 3 handlingar om du betalar 1 medtagen mat.

Att betala mat är inte en handling.

Exempel:

```text
Spelaren bär 1 mat.

Handling 1: Flytta
Betala 1 mat för +1 handling
Handling 2: Samla
Handling 3: Flytta
```

### 10.2 Nattvakt

I början av Nattfasen får spelarna betala 1 mat från **Basförrådet**.

Om de gör det flyttas inte Mörkermarkören sitt vanliga steg denna natt.

Dra och lös fortfarande 1 hotkort.

Nattvakt kan användas högst 1 gång per natt.

---

## 11. Platser och resurser

### Bas

På Basen kan du:

- lämna resurser gratis
- ta eller lämna mat gratis
- bygga Fyrdelar

### Skog

Utforska:

```text
Få 1 trä.
```

### Berg

Utforska:

```text
Få 1 sten.
```

### Äng

Utforska:

```text
Få 1 mat.
```

### Grotta

Utforska:

```text
Få 1 sten eller 1 kristall.
```

Om du tar 1 kristall:

```text
Dra 1 hotkort och lös det direkt.
```

### Ruin

Utforska:

```text
Dra 1 fyndkort.
```

### Fyrplats

På Fyrplatsen kan du bygga Fyrens delar.

### Stig

Stig ger ingen resurs.

När du står på Stig och din nästa handling är Flytta får du flytta upp till 2 steg.

---

## 12. Bygga Fyren

Fyren byggs i tre delar.

Delarna måste byggas i ordning.

| Fyrdel | Kostnad |
|---|---:|
| Grund | 3 sten |
| Torn | 3 trä + 2 sten |
| Ljuskärna | 3 kristaller |

När **Ljuskärnan** byggs vinner spelarna direkt.

---

## 13. Resurser vid bygge

När en spelare bygger får spelarna använda:

- resurser i Basförrådet, om bygget sker på Basen
- resurser som byggande spelare bär
- resurser som andra spelare på samma ruta bär

För första testet rekommenderas enkel kooperativ tolkning:

```text
Om flera spelare står på samma ruta får deras resurser användas tillsammans för bygge.
```

---

## 14. Nattfas

När alla spelare har haft varsin tur sker Nattfasen.

Gör i ordning:

1. Spelarna får välja om de vill använda **Nattvakt**.
2. Om Nattvakt inte används, flytta Mörkermarkören 1 steg framåt.
3. Dra 1 hotkort och lös det.
4. Om Mörkermarkören når sista rutan förlorar spelarna.

### 14.1 Nattvakt och hotkort

Nattvakt stoppar bara Mörkermarkörens vanliga steg.

Hotkort kan fortfarande flytta Mörkermarkören.

Exempel:

```text
Spelarna betalar 1 mat för Nattvakt.
Mörkermarkören flyttas inte sitt vanliga steg.
Sedan dras hotkortet Mörkret tätnar.
Mörkermarkören flyttas ändå 1 extra steg av hotkortet.
```

---

## 15. Kall natt

Hotkortet **Kall natt** behålls oförändrat i REGLERV3.

```text
Betala 1 mat från Basförrådet.
Om ni inte kan, flytta Mörkermarkören 1 extra steg.
```

Det betyder att mat i Basförrådet kan behövas både till Nattvakt och till Kall natt.

Om både Nattvakt och Kall natt sker samma natt:

1. Spelarna får först välja om de vill betala 1 mat för Nattvakt.
2. Sedan dras och löses hotkortet.
3. Om hotkortet är Kall natt behöver spelarna betala 1 mat till från Basförrådet.
4. Om de inte kan betala för Kall natt flyttas Mörkermarkören 1 extra steg.

---

## 16. Vinst och förlust

### Vinst

Spelarna vinner direkt när **Ljuskärnan** byggs.

### Förlust

Spelarna förlorar om Mörkermarkören når sista rutan på Mörkerspåret.

---

## 17. Exempel på Stig

Spelare A står på Bas.

```text
Handling 1: A flyttar från Bas till Stig.
Handling 2: A gör en ny Flytta-handling från Stig.
Eftersom A börjar handlingen på Stig får A flytta upp till 2 steg.
```

Stigbonusen var alltså inte en gratis fortsättning på handling 1.

---

## 18. Exempel på mat

Spelare B står på Bas och tar 1 mat från Basförrådet gratis.

```text
Handling 1: B flyttar Bas → Skog.
B betalar 1 mat för att få +1 handling denna tur.
Handling 2: B samlar 1 trä.
Handling 3: B flyttar Skog → Bas.
```

När B kommer till Basen lämnar B träet gratis i Basförrådet.

---

## 19. Exempel på Nattfas

Basförrådet innehåller 2 mat.

Spelarna använder Nattvakt:

```text
Betala 1 mat från Basförrådet.
Mörkermarkören flyttas inte sitt vanliga steg.
```

Sedan dras hotkortet **Kall natt**.

```text
Betala 1 mat från Basförrådet.
Ingen extra Mörkerflytt.
```

Basförrådet har nu 0 mat kvar.

---

## 20. Saker att observera i nästa provspelning

Skriv gärna ned:

- Användes Stig ofta?
- Var Stig-regeln tydlig?
- Glömde spelarna att Stig bara gäller när man börjar på Stig?
- Användes mat både för extra handling och Nattvakt?
- Blev Kall natt för hårt tillsammans med Nattvakt?
- Var 4 startmat lagom?
- Var 10-stegs Mörkerspår lagom för 2 spelare?
- Hann spelarna bygga Grund, Torn och Ljuskärna?
- Kändes kristallerna spännande eller för farliga?
- Blev det för mycket administration kring Basförrådet?

---

## 21. Regler som fortfarande är testregler

Följande regler är inte slutgiltiga och bör testas:

- Startmat: 4 mat
- Mörkerspår per spelarantal
- Mat ger +1 handling
- Nattvakt
- Stig som 2-stegs Flytta från Stig
- Kall natt tillsammans med Nattvakt
- Kristall drar hotkort

Gör helst bara 1–3 ändringar efter nästa riktiga provspelning.


## Bygga på Fyrplatsen

Du får bara välja handlingen **Bygga** om du står på **Fyrplatsen**.

Bygg Fyren innan Mörker når 0 för att vinna.
