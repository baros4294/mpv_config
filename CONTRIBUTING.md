# Contributing

Issues and pull requests are welcome.

- Change only this repository's own files: `mpv.conf`, `input.conf` and `script-opts/`. Files under `scripts/`, `fonts/` and `shaders/` come from upstream; the weekly **Update upstream scripts** workflow replaces them, so local edits there would be lost.
- Say what hardware and OS a change targets; the defaults are tuned for Windows 11 and Intel Iris Xe.
- Run `python3 .github/scripts/check.py` before opening a pull request; CI runs it plus a LuaJIT compile of every script.
- Commit messages follow [Conventional Commits](https://www.conventionalcommits.org/) (`feat:`, `fix:`, `docs:`, `ci:`).
