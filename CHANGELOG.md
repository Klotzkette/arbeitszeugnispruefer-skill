# Changelog

Alle nennenswerten Änderungen an diesem Skill werden hier festgehalten.
Das Format orientiert sich an [Keep a Changelog](https://keepachangelog.com/de/1.1.0/);
die Versionierung folgt [Semantic Versioning](https://semver.org/lang/de/).
Die Versionsnummer steht zugleich im Frontmatter von `skill/SKILL.md` und `skill/SKILL-mini.md`.

## [3.0.5] — 2026-06-29

### Hinzugefügt
- Dieses `CHANGELOG.md` als durchgehende Release-Historie.
- Direkt kopierbarer Begleitsatz (Starter-Prompt) im README-Abschnitt „Anwendung".
- Kurzer Einführungstext und sichtbarer Haftungshinweis auf der Download-Seite (`docs/index.html`).

### Geändert
- Versionsbump auf 3.0.5 in Voll- und Mini-Skill; README-Versionssatz aktualisiert.

### Geprüft (ohne inhaltliche Änderung)
- Sanity- und Kohärenz-Sweep: alle internen Sprungmarken lösen auf; jedes
  BAG-/LAG-Aktenzeichen ist durchgängig identisch datiert; Mini- und
  Vollversion sind in den Notenstufen deckungsgleich.
- `docs/`-Kopien sind mit den Quelldateien in `skill/` byte-identisch
  (Auto-Sync via GitHub-Actions-Workflow).

## [3.0.4]
- Kohärenz-Sweep Mini/Voll: Notenstufen der Mini-Fassung mit der Vollversion
  in Deckung gebracht (Trennung „zu unserer Zufriedenheit" = Note 4 und
  „im Großen und Ganzen …" = Note 5), fehlerhafte tabellarische Form mit
  Negativbeispiel veranschaulicht, doppelte Beweislast-Passage entschlackt,
  Testakten-Downloads (ZIP + Gesamt-PDF) auf der Download-Seite verlinkt.

## [3.0.3]
- BAG-Anker und One-Shot-Ausgabe gehärtet.

## [3.0.2]
- Code-Lesarten gehärtet.

## [3.0.1]
- BAG-Zitatanker korrigiert.

## [3.0.0]
- Release-Bump der konsolidierten Skill-Fassung.

## [2.2.0] — [2.2.17]
- Mini-Version und rollenabhängige Ausgaben eingeführt (2.2.0); danach
  iterative Feinarbeit: Beweislast, Anwaltskosten (§ 12a ArbGG), Verjährung
  und Ausschlussfristen, elektronische Form (§ 109 Abs. 3 GewO, § 16 BBiG),
  § 109 Abs. 2 Klarheit und BAG-Anker präzisiert.

## [2.1.0]
- Im nicht-interaktiven Einsatz wird die Arbeit immer rollenrichtig
  fertiggeliefert.

## [2.0.0]
- Sofortstart, grafische Ampeln, Einschätzungsmatrix mit Rechtsprechungsstütze,
  Rechtsprechungsanker (BAG 1995–2026 + LAG), Vollstreckungsmodul und
  HR-Gegenprüfung. Konsolidierung der ursprünglich 50-teiligen
  Plugin-Sammlung in eine einzige `SKILL.md`.

[3.0.5]: https://github.com/Klotzkette/arbeitszeugnispruefer-skill/releases/tag/v3.0.5
[3.0.4]: https://github.com/Klotzkette/arbeitszeugnispruefer-skill/releases/tag/v3.0.4
