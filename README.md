# mpv_config

Clean, quality-first [mpv](https://mpv.io) config for Windows 11 on Intel Iris Xe with an 8-bit SDR display, using the [uosc](https://github.com/tomasklaen/uosc) interface and [thumbfast](https://github.com/po5/thumbfast) seek previews.

## Install

Copy the contents of this repository into mpv's config folder:

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
- **Update upstream scripts** (`.github/workflows/update-upstream.yml`) runs weekly. When uosc has a new release or thumbfast has new commits, it validates them and opens a pull request with the change and the SHA-256 of the bundled binaries. Review and merge it; nothing changes on `main` until you do.
- **Dependabot** keeps the workflows' pinned actions current, and **CodeQL** scans the workflows.

## Credits and licenses

This repository's own files are the config (`*.conf`) and the automation under `.github/`. The bundled third-party files keep their own licenses:

- [uosc](https://github.com/tomasklaen/uosc) (`scripts/uosc/`, `fonts/uosc_*`), by Tomas Klaen and contributors: LGPL-2.1
- [thumbfast](https://github.com/po5/thumbfast) (`scripts/thumbfast.lua`), by po5: MPL-2.0
- [FSRCNNX](https://github.com/igv/FSRCNN-TensorFlow) (`shaders/FSRCNNX_x2_16-0-4-1.glsl`), by igv: LGPL-3.0-or-later
