# Release-policy

Projektets Git-repo ska i normalfallet bara innehålla källor och byggscript.

## Källor som ska versioneras

- `data/`
- `docs/`
- `scripts/`
- `assets/`
- `templates/`
- `.github/`
- projektets översiktsfiler i roten

## Genererat material som inte ska versioneras

- `output/`
- `release/`
- `dist/`
- `build/`

De katalogerna kan skapas lokalt, men ska kunna raderas utan informationsförlust.

## Lokal byggning

Bygg komplett print-and-play-paket:

```bash
python scripts/build_print_and_play.py --output-dir dist/print-and-play --release-name local
```

Bygg bara regelboks-PDF:

```bash
python scripts/build_rulebook_pdf.py --output dist/docs/rulebook.pdf
```

Bygg samma preview som GitHub Actions:

```bash
python scripts/ci_build_print_preview.py --output-dir dist/preview --release-name local-preview
```

Paketera release-assets lokalt:

```bash
python scripts/ci_package_release.py --output-dir dist/release --release-name vX.Y.Z
```

## GitHub Actions

- `01-validate.yml` validerar källor och byggscript.
- `02-build-preview.yml` bygger en preview-artifact från källorna.
- `03-release.yml` bygger och laddar upp release-assets när en tagg `v*` pushas.

GitHub Release-assets är den officiella platsen för färdiga print-and-play-filer.
