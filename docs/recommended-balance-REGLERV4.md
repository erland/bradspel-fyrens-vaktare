# Rekommenderad balans – [REGLERV4-STARTBALANS]

Detta är den balans som förts in i regelkällorna efter scriptade sanity-simuleringar.

## Startvärden

| Antal spelare | Startmat i Basförrådet | Mörker startar på |
|---:|---:|---:|
| 2 spelare | 6 mat | 10 |
| 3 spelare | 4 mat | 10 |
| 4 spelare | 4 mat | 10 |

## Fyrdelar

| Fyrdel | Kostnad |
|---|---:|
| Grund | 3 sten |
| Torn | 3 trä + 2 sten |
| Ljuskärna | 2 kristaller |

## Inte infört som standard

- Basbygge är inte infört.
- Billigare Torn, till exempel `1 trä + 2 sten`, är inte infört.
- Tornets standardkostnad är fortfarande `3 trä + 2 sten`.

## Simuleringsbakgrund

Scriptade direktrutter gav ungefär följande vinstgrader när maten sparades till Nattvakt:

| Spelare | Testad setup | Vinstgrad |
|---:|---|---:|
| 2 | Mörker 10, 6 mat, Ljuskärna 2 | ca 30 % |
| 3 | Mörker 10, 4 mat, Ljuskärna 2 | ca 36 % |
| 4 | Mörker 10, 4 mat, Ljuskärna 2 | ca 40 % |

Detta är beslutsstöd, inte ersättning för fysiskt speltest. Första bordstestet bör observera om spelarna sparar mat till Nattvakt eller använder mat som tempo.

## Regeltydlighet införd

Spelare som står på samma plats får fritt ge resurser till varandra. Det kostar ingen handling.
