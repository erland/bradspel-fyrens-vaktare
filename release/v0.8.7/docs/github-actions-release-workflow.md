# GitHub Actions – validering, preview och release

Projektet har tre GitHub Actions-workflows i `.github/workflows/`.

`.github` ska ligga i projektroten, på samma nivå som `README.md`.

## 01-validate.yml

Körs vid pull request och push till `main` när relevanta projektfiler ändras.

Valideringen kontrollerar bland annat:

- att viktiga källfiler finns
- att senaste release har förväntade SVG- och PDF-filer
- att release-manifestet pekar på filer som finns
- att regelboken inte innehåller versionsrad, utskriftsavsnitt eller prototypformulering
- att kort-id:n är unika
- att fynd-/hotkort har rätt antal kort
- att spelplanens rutnät och mörkerspår är rimliga
- att viktiga begrepp finns i regelboken
- att interna Markdown-länkar inte är trasiga

Lokal körning:

```bash
python scripts/ci_validate_project.py .
```

## 02-build-preview.yml

Kan köras manuellt och körs även vid pull request som ändrar print-/regelmaterial.

Den skapar en preview-artifact med PDF:er för allt som ska kunna skrivas ut:

- spelplan
- A6-referenskort
- A4 4-up referenskort
- fyndkort
- hotkort
- regelbok

Workflowen regenererar print-PDF:er från release-SVG:er och bygger regelboks-PDF från `docs/rulebook.md`.

Lokal körning:

```bash
python scripts/ci_build_print_preview.py --output-dir /tmp/fyrens-vaktare-preview
```

## 03-release.yml

Körs när en tagg som börjar med `v` pushas, till exempel:

```bash
git tag v0.8.6
git push origin v0.8.6
```

Workflowen:

1. validerar projektet
2. bygger print-preview
3. paketerar en print-and-play-zip
4. laddar upp zipen och separata PDF-filer som GitHub Release-assets

Lokal körning:

```bash
python scripts/ci_package_release.py --output-dir /tmp/fyrens-vaktare-release --release-name v0.8.6
```

## Designprincip

Källor ligger i `data/`, `docs/`, `scripts/`, `templates/` och `assets/`.

`release/vX.Y.Z/` är det som används för färdiga utskriftsfiler och releasepaket.

PDF:er ska kunna byggas om deterministiskt i CI.


## GitHub-runner: LaTeX-beroenden

Pandocs standardmall kan kräva `lmodern.sty` även när PDF:en byggs med XeLaTeX.
Därför installerar preview- och release-workflowen paketet `lmodern` explicit
tillsammans med XeLaTeX-paketen.

Om felet `LaTeX Error: File 'lmodern.sty' not found` uppstår saknas detta paket
i runner-miljön.
