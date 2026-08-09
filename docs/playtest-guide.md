# Playtestguide – Fyrens väktare

## Aktuell version

v0.7.0 – [PLAN2] Steg 4

## Syfte med nästa test

Nästa test ska kontrollera om REGLERV3 är spelbar som helhet.

Det viktigaste är inte exakt balans, utan att se om spelarna kan genomföra spelets grundloop:

```text
Flytta → Utforska → samla/bära resurser → bygga på Fyrplatsen → överleva Nattfasen
```

## Rekommenderad testtyp

Börja med **intern testomgång**.

Designern får förklara reglerna, men bör anteckna varje gång en spelare behöver hjälp.

Efter 1–2 interna tester kan spelet gå vidare till observerat test.

## Testa särskilt

- om `Utforska (se plats)` är tydligt nog
- om spelarna förstår att platsrutornas effekter står på A6-kortet
- om `Bygga (på Fyrplatsen)` är tillräckligt tydligt
- om vertikalt Mörkerspår fungerar vid bordet
- om startvärdena 9/8/7 känns rimliga för 2/3/4 spelare
- om matvalet mellan extra handling och Nattvakt är meningsfullt
- om Grotta känns lockande men riskfylld
- om Stig-regeln används utan missförstånd

## Testa inte ännu

Vänta med:

- grafisk puts
- nya kort
- nya resurser
- roller eller specialförmågor
- fler platstyper
- större bräde
- finbalans av alla kort

## Mätvärden

Anteckna:

- antal spelare
- speltid
- vinst/förlust
- vilken dag/natt spelet slutade
- Mörker vid slutet
- hur många Fyrdelar som byggdes
- om spelarna ofta saknade en viss resurs
- om någon regel behövde förklaras flera gånger

## Efter testet

Välj högst 1–3 ändringar.

Bra ändringar efter första testet är till exempel:

- förtydliga en regel
- ändra ett startvärde
- ändra en kostnad
- justera ett kort som skapade problem

Undvik att ändra allt samtidigt.
