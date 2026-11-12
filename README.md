# mpv_config

[![Validate](https://github.com/baros4294/mpv_config/actions/workflows/validate.yml/badge.svg)](https://github.com/baros4294/mpv_config/actions/workflows/validate.yml) [![Latest release](https://img.shields.io/github/v/release/baros4294/mpv_config?sort=semver)](https://github.com/baros4294/mpv_config/releases/latest) [![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Clean, quality-first [mpv](https://mpv.io) config for Windows 11 on Intel Iris Xe with an 8-bit SDR display, using the [uosc](https://github.com/tomasklaen/uosc) interface and [thumbfast](https://github.com/po5/thumbfast) seek previews.

## Install

Download `mpv_config-<version>.zip` from the [latest release](https://github.com/baros4294/mpv_config/releases/latest) (or clone this repository) and extract it into mpv's config folder:

- Windows: `%APPDATA%\mpv\` (or `portable_config\` next to `mpv.exe`)
- Linux / macOS: `~/.config/mpv/`

`mpv.conf` targets Direct3D 11 (`gpu-api=d3d11`, `hwdec=d3d11va`, `ao=wasapi`). On another OS, change those lines.

## Layout

| Path | What it is |
| :--- | :--- |
| `mpv.conf` | Renderer, scaling, HDR tone mapping, debanding, subtitles, audio, cache |
| `input.conf` | Key bindings (playback, uosc menus, stats) |
| `script-opts/` | Options for uosc and thumbfast |
| `scripts/uosc/`, `fonts/` | uosc, vendored from its releases |
| `scripts/thumbfast.lua` | thumbfast, vendored |
| `shaders/` | FSRCNNX x2 upscaling shader |

## Upkeep

- **Validate** (`.github/workflows/validate.yml`) runs on every push and pull request. It checks that each `uosc/...` binding in `input.conf` and each option in `script-opts/` still exists in the bundled scripts, and that every Lua file compiles under LuaJIT. Run `python3 .github/scripts/check.py` locally for the same check without the Lua compile.
- **Update upstream scripts** (`.github/workflows/update-upstream.yml`) runs weekly. When uosc has a new release or thumbfast has new commits, it validates them and opens a pull request with the change and the SHA-256 of the bundled binaries, then runs Validate on it. If the checks pass and uosc keeps its major version, the pull request merges itself; a new uosc major version waits for you.
- **Release** (`.github/workflows/release.yml`): pushing a `vMAJOR.MINOR.PATCH` tag publishes a release with a ready-to-extract zip and its SHA-256.
- **Dependabot** keeps the workflows' pinned actions current; its updates merge themselves when Validate passes and the major version is unchanged, and **CodeQL** scans the workflows.

## License

This repository's own files (the `*.conf` files and the automation under `.github/`) are [MIT](LICENSE) © 2026 Baros. The bundled third-party files keep their own licenses:

- [uosc](https://github.com/tomasklaen/uosc) (`scripts/uosc/`, `fonts/uosc_*`), by Tomas Klaen and contributors: LGPL-2.1
- [thumbfast](https://github.com/po5/thumbfast) (`scripts/thumbfast.lua`), by po5: MPL-2.0
- [FSRCNNX](https://github.com/igv/FSRCNN-TensorFlow) (`shaders/FSRCNNX_x2_16-0-4-1.glsl`), by igv: LGPL-3.0-or-later

Their full license texts are in [LICENSES/](LICENSES/).

See [CONTRIBUTING.md](CONTRIBUTING.md) to propose changes and [SECURITY.md](SECURITY.md) for private reports.
