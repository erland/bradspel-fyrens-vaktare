# Projektstatus – Fyrens väktare

**Aktuell arbetsversion:** v0.7.0 – [REGLERV4-STARTBALANS]  
**Status:** Rekommenderad startbalans införd i källfiler, regler och ny A6-/brädesoutput.

## Aktuell rekommenderad balans

| Antal spelare | Startmat i Basförrådet | Mörker startar på |
|---:|---:|---:|
| 2 spelare | 6 mat | 10 |
| 3 spelare | 4 mat | 10 |
| 4 spelare | 4 mat | 10 |

## Fyrdelar

- Grund: 3 sten
- Torn: 3 trä + 2 sten
- Ljuskärna: 2 kristaller

## Inte infört

- Basbygge är inte infört.
- Billigare Torn är inte infört som standard.
- Tornets kostnad är fortsatt 3 trä + 2 sten.

## Uppdaterade källor

- `docs/rulebook.md`
- `docs/quickstart.md`
- `docs/reference-card.md`
- `docs/recommended-balance-REGLERV4.md`
- `data/game.yaml`
- `data/rules.yaml`
- `data/buildings.yaml`
- `data/board.yaml`
- `data/reference-card.yaml`
- `docs/rules-sync-validation.md`

## Ny genererad output

- `output/print/reference/reference-card-a6-REGLERV4-STARTBALANS-v0.7.0.svg`
- `output/print/reference/reference-card-a4-4up-REGLERV4-STARTBALANS-v0.7.0.svg`
- `output/preview/reference-card-a6-REGLERV4-STARTBALANS-v0.7.0.svg`
- `output/print/board/board-a4-REGLERV4-STARTBALANS-v0.7.0.svg`
- `output/preview/board-a4-REGLERV4-STARTBALANS-v0.7.0.svg`

## Speltestnotering

Mat bör i första fysiska test främst sparas till Nattvakt. Simuleringarna visar att tempo-mat ofta sänker vinstchansen.

## Regeltydlighet – byta resurser

Spelare som står på samma plats får fritt ge resurser till varandra utan handling. Regeln är införd i regelbok, snabbstart, strukturerade regler och A6-referenskort.

## v0.7.6 – överlämning till ny chat

Tillagt:
- `docs/NEW_CHAT_HANDOFF.md`
- `PROJECT_HANDOFF.json`

Syfte: göra projektet lättare att fortsätta i en ny chat utan att tappa balansbeslut, simulatorstandard eller style-system.

## v0.7.7 – output-städning

Genomfört:
- Rensat bort äldre genererade filer i `output/`.
- Behållit endast nuvarande rekommenderade printfiler och en preview av aktuell spelplan.
- Förtydligat i `output/README.md` att äldre output ska regenereras vid behov.

## v0.7.8 – docs-arkiv och release-struktur

Genomfört:
- Flyttat äldre dokument och gamla simuleringsanalyser till `docs/archive/`.
- Lagt till `docs/README.md` och `docs/archive/README.md`.
- Skapat `release/v0.8.6/` med aktuella printfiler och centrala speldokument.
- Lagt till `PROJECT_STRUCTURE.md`.

## v0.7.9 – PDF-versioner i release

Genomfört:
- Genererat PDF-versioner av aktuell spelplan, referenskort och kortark.
- Strukturerat release-printfiler i `release/v0.8.6/print/svg/` och `release/v0.8.6/print/pdf/`.
- Uppdaterat release-dokumentation och manifest.


## v0.8.0 – Ink-friendly kort

- Uppdaterade fynd- och hotkort till en mer toner-snål styled layout.
- Tog bort dekorativa cirklar längst ned på korten.
- Regenererade release-SVG och PDF för båda kortarken.

## v0.8.1 – Ink-friendly reference and board

- Färdigställd ink-friendly styled variant av A6-referenskortet.
- Färdigställd ink-friendly light-variant av spelplanen.
- Regenererad release `release/v0.8.6/` med uppdaterade SVG- och PDF-filer.

## v0.8.2 – regelboks-PDF

Genomfört:
- Uppdaterat `docs/rulebook.md` med aktuell releaseinformation.
- Skapat professionellt formaterad regelboks-PDF med Pandoc/XeLaTeX.
- Lagt PDF och uppdaterad markdown-källa i `release/v0.8.6/docs/`.
- Lagt till `scripts/build_rulebook_pdf.py` för framtida regenerering.

## v0.8.3 – regelboksgenomgång

Genomfört:
- Tog bort innehållsförteckning och kapitelnumrering från regelboks-PDF.
- Gjorde en förståelseanalys av regeltexten.
- Uppdaterade `docs/rulebook.md` för tydligare berättelse, begrepp och nattfas.
- Lade till `docs/rulebook-clarity-analysis-v0.8.3.md`.
- Regenererade `release/v0.8.6/docs/rulebook.pdf`.

## v0.8.4 – regelboksrensning

Genomfört:
- Tog bort prototypformuleringar från regelboken.
- Tog bort avsnitten `Första speltest` och `Utskrift` från regelboken.
- Uppdaterade regelboksanalysen med v0.8.4-notering.
- Regenererade `release/v0.8.6/docs/rulebook.pdf`.

## v0.8.5 – regelbok utan synlig versionsrad

Genomfört:
- Tog bort `Version`-raden i början av `docs/rulebook.md`.
- Tog bort synlig release-/versionsinformation från regelboks-PDF.
- Regenererade `release/v0.8.6/docs/rulebook.pdf`.

## v0.8.6 – GitHub Actions

Genomfört:
- Lade till `.github/workflows/01-validate.yml`.
- Lade till `.github/workflows/02-build-preview.yml`.
- Lade till `.github/workflows/03-release.yml`.
- Lade till `scripts/ci_validate_project.py`.
- Lade till `scripts/ci_build_print_preview.py`.
- Lade till `scripts/ci_package_release.py`.
- Lade till `docs/github-actions-release-workflow.md`.
- Uppdaterade release v0.8.6 och manifest.
