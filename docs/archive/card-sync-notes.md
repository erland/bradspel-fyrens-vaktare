# Kortsynkning – Fyrens väktare v0.7.0

## Syfte

Hot- och fyndkorten har synkats med nuvarande REGLERV3-regler.

Det här steget gör korten relevanta efter ändringarna:

- `Samla` har bytt namn till `Utforska`.
- `Vila` är borttaget.
- Mörker räknar ned mot 0.
- Bygga sker på Fyrplatsen.
- A6-kortet används som primär platsreferens.

## Viktiga ändringar

### FYN-008 – Starka verktyg

Ny effekt:

```text
Få 1 valfri resurs utom kristall.
```

Motiv:

- fungerar med `Utforska`
- gäller inte Ruin, eftersom Ruin ger fyndkort och inte resurs
- fungerar med Skog, Berg, Äng och Grotta när Grotta ger sten/kristall

### FYN-012 – Morgonljus

Ny effekt:

```text
Flytta Mörker 1 steg bort från 0. Den kan inte gå över startvärdet.
```

Motiv:

- passar nedräknande Mörkerspår
- undviker den gamla formuleringen `flytta bakåt`
- begränsar effekten så att Mörker inte kan gå över startvärdet

### HOT-011 – Oroligt läger

Ny effekt:

```text
Nästa gång spelarna använder Nattvakt kostar det 2 mat i stället för 1.
```

Motiv:

- ersätter den gamla `Vila`-kopplingen
- gör Basens matval mer intressant
- skiljer sig från `Kall natt`, som kräver omedelbar matbetalning

## Kvar att kontrollera

Kortark i `output/print/cards/` kan fortfarande vara äldre output om de inte regenererats.

Inför nästa utskrift bör nya kortark genereras från `data/cards.yaml`.


## Kortsynkning rev1 – FYN-008

`FYN-008 Starka verktyg` har ändrats eftersom fyndkort löses direkt när de dras.

Ny effekt:

```text
Få 1 valfri resurs utom kristall.
```

Motiv:

- den tidigare effekten var för smal eftersom den bara gällde samma tur
- fyndkort dras oftast genom Ruin, och då har spelaren redan använt en Utforska-handling
- ny effekt är direkt, enkel och ger inte kristall
