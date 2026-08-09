# Fyrens väktare – Kortlista v0.1

## Kortstruktur

Första versionen använder två kortlekar:

- 12 fyndkort
- 12 hotkort

Alla kort är enkelsidiga prototypkort.

## Printbeslut

Korten skrivs ut 4 × 4 per A4. Originaltexterna behålls i v0.1, men layouten ska sakna illustrationer och använda kompakt men läsbar text.

---

# Fyndkort

## FYN-001 – Glittrande kristall

**Typ:** Fynd  
**Antal:** 1  
**Effekt:** Få 1 kristall.

## FYN-002 – Gammal kista

**Typ:** Fynd  
**Antal:** 1  
**Effekt:** Välj: få 2 trä eller 1 valfri resurs.

## FYN-003 – Djupt stenlager

**Typ:** Fynd  
**Antal:** 1  
**Effekt:** Få 2 sten.

## FYN-004 – Bärbuskar

**Typ:** Fynd  
**Antal:** 1  
**Effekt:** Få 2 mat.

## FYN-005 – Torrt virke

**Typ:** Fynd  
**Antal:** 1  
**Effekt:** Få 2 trä.

## FYN-006 – Genväg under marken

**Typ:** Fynd  
**Antal:** 1  
**Effekt:** Flytta upp till 2 steg direkt.

## FYN-007 – Ljuslykta

**Typ:** Fynd  
**Antal:** 1  
**Effekt:** Ignorera nästa hotkort som dras på din tur.

## FYN-008 – Starka verktyg

**Typ:** Fynd  
**Antal:** 1  
**Effekt:** Nästa gång du utforskar den här turen får du 1 extra resurs av samma typ.

## FYN-009 – Byggplan

**Typ:** Fynd  
**Antal:** 1  
**Effekt:** Nästa Fyrdel eller basbygge kostar 1 valfri resurs mindre.

## FYN-010 – Gammal karta

**Typ:** Fynd  
**Antal:** 1  
**Effekt:** Titta på de 2 översta hotkorten. Lägg tillbaka dem i valfri ordning.

## FYN-011 – Vänlig vandrare

**Typ:** Fynd  
**Antal:** 1  
**Effekt:** Lägg 1 valfri resurs direkt i Basens förråd.

## FYN-012 – Morgonljus

**Typ:** Fynd  
**Antal:** 1  
**Effekt:** Sänk Mörker 1 steg bakåt. Den kan inte flyttas bakom start.

---

# Hotkort

## HOT-001 – Skuggor i skogen

**Typ:** Hot  
**Antal:** 1  
**Effekt:** Alla spelare på Skog tappar 1 resurs om möjligt.

## HOT-002 – Ras i grottan

**Typ:** Hot  
**Antal:** 1  
**Effekt:** Nästa spelare som utforskar i Grotta får ingen resurs.

## HOT-003 – Kall natt

**Typ:** Hot  
**Antal:** 1  
**Effekt:** Betala 1 mat från Basens förråd. Om ni inte kan, sänk Mörker 1 extra steg.

## HOT-004 – Vilsen i dimman

**Typ:** Hot  
**Antal:** 1  
**Effekt:** Alla spelare utanför Basen får inte flytta på sin nästa handling.

## HOT-005 – Sprickor i berget

**Typ:** Hot  
**Antal:** 1  
**Effekt:** Alla spelare på Berg tappar 1 sten om möjligt.

## HOT-006 – Mörkret tätnar

**Typ:** Hot  
**Antal:** 1  
**Effekt:** Sänk Mörker 1 extra steg.

## HOT-007 – Hungriga skuggor

**Typ:** Hot  
**Antal:** 1  
**Effekt:** Varje spelare utanför Basen måste betala 1 mat eller tappa 1 valfri resurs.

## HOT-008 – Förlorade verktyg

**Typ:** Hot  
**Antal:** 1  
**Effekt:** Nästa Utforska-handling ger 1 resurs mindre, minst 0.

## HOT-009 – Blockerad stig

**Typ:** Hot  
**Antal:** 1  
**Effekt:** Nästa Flytta-handling kostar 2 handlingar i stället för 1.

## HOT-010 – Skugga över fyren

**Typ:** Hot  
**Antal:** 1  
**Effekt:** Om minst en Fyrdel är byggd, betala 1 kristall eller sänk Mörker 1 extra steg.

## HOT-011 – Oroligt läger

**Typ:** Hot  
**Antal:** 1  
**Effekt:** Spelare på Basen kan inte Nattvakt förrän efter nästa nattfas.

## HOT-012 – Mörkervåg

**Typ:** Hot  
**Antal:** 1  
**Effekt:** Dra ytterligare 1 hotkort och lös det. Flytta inte Mörkermarkören extra för detta kort.

---

# Balansanteckning för v0.1

Kortleken är avsiktligt enkel. Första speltestet ska visa:

- om hoten är för hårda
- om fyndkorten ger tillräckligt hopp
- om kristaller är för lätta eller för svåra att få
- om spelarna bygger Fyren för snabbt
- om valfria basbyggen används alls

## Kortsynkning v0.7.0

Kortlistan har synkats med REGLERV3:

- `Samla` heter nu `Utforska`.
- `Vila` är borttaget.
- `HOT-011 Oroligt läger` påverkar nu Nattvakt.
- `FYN-012 Morgonljus` är anpassat till nedräknande Mörker.
- `FYN-008 Starka verktyg` gäller bara när Utforska ger en resurs.
