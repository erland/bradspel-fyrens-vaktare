# Brädanteckningar – Fyrens väktare

## Version

v0.7.0 – [PLAN2] Steg 3.1

## Syfte

Det här brädet är ett spelbart A4-bräde för REGLERV3.

Fokus är tydlighet vid bordet och låg ändringskostnad om reglerna justeras senare.

## Viktiga beslut

- Spelet heter nu **Fyrens väktare**.
- Brädet har ett generiskt Mörkerspår från **9 till 0**.
- Startvärden för Mörker står på A6-referenskortet, inte på brädet.
- Mörkerspåret är vertikalt längst till höger.
- Platsrutorna visar bara **typ av ruta**, inte regeltext eller effekter.
- A6-kortet används för påminnelser om vad platserna gör.
- SVG-filen är flat och använder inte filter eller drop shadow.

## Karta

```text
Rad 1: Skog | Skog | Ruin     | Berg | Grotta
Rad 2: Bas  | Stig | Fyrplats | Stig | Grotta
Rad 3: Stig | Äng  | Stig     | Berg | Stig
Rad 4: Äng  | Ruin | Äng      | Stig | Skog
```

## Mörkerspår

```text
MÖRKER
9
8
7
6
5
4
3
2
1
0
```

Spåret räknar ned mot 0.

Startposition:

- 2 spelare: 9
- 3 spelare: 8
- 4 spelare: 7

Startpositionerna står på A6-kortet för att brädet ska vara generiskt och lättare att återanvända.

## Output

- `output/print/board/board-a4-REGLERV3-v0.7.0-rev2.svg`
- `output/preview/board-a4-REGLERV3-v0.7.0-rev2.svg`
