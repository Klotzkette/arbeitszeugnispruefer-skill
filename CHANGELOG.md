# Changelog

Alle nennenswerten Änderungen an diesem Skill werden hier festgehalten.
Das Format orientiert sich an [Keep a Changelog](https://keepachangelog.com/de/1.1.0/);
die Versionierung folgt [Semantic Versioning](https://semver.org/lang/de/).
Die Versionsnummer steht zugleich im Frontmatter von `skill/SKILL.md` und `skill/SKILL-mini.md`.

## [3.0.10] — 2026-07-06

### Hinzugefügt
- Dritte Testakte `arbeitszeugnisse-leitungsfunktionen` mit fünf
  ausführlichen fiktiven Arbeitszeugnissen für obere Führungsrollen:
  Leiter Rechtsabteilung eines mitteldeutschen Mischkonzerns,
  kaufmännische Leitung/CFO, Leitung Personal und Arbeitsrecht,
  Compliance/Datenschutz sowie Werk- und Standortleitung.
- Reproduzierbares Build-Skript
  `scripts/build_leitungsfunktionen_testakten.py` für Einzel-PDFs,
  Gesamt-PDF, ZIP und öffentliche `docs/testakten`-Downloads.
- Erwartungshorizont und Prüfpunkte zur neuen Leitungsakte.

### Geändert
- README und Download-Seite verlinken nun alle drei Testakten-Sätze.
- Release-Integritätscheck prüft zusätzlich die neue Leitungsakte.
- Versionsbump auf 3.0.10 in Voll- und Mini-Skill; README und Download-Seite
  aktualisiert.

### Geprüft
- Leitungsfunktionen-ZIP enthält genau 5 Einzel-PDFs; Gesamt-PDF ist A4,
  nicht verschlüsselt und enthält 5 Zeugnisüberschriften.
- Voller Integritätscheck läuft erfolgreich; Mini-Fassung bleibt unter
  7.500 Zeichen; `skill/` und `docs/` sind byte-identisch.

## [3.0.9] — 2026-07-04

### Hinzugefügt
- Neues Skript `scripts/check_release_integrity.py` für den wiederholbaren
  Release-Check: Versionsgleichlauf, `skill/`-/`docs/`-Spiegel,
  Mini-Zeichenlimit, Markdown-Anker, lokale HTML-Links, öffentliche
  Testakten-Artefakte sowie PDF-/ZIP-Sanity.
- README-Abschnitt „Qualitätssicherung und Release-Check" mit dem zentralen
  Prüfkommando vor neuen Versionen.

### Geändert
- Versionsbump auf 3.0.9 in Voll- und Mini-Skill; README und Download-Seite
  aktualisiert.

### Geprüft
- Neuer Integritätscheck läuft erfolgreich auf dem Release-Stand.
- Mini-Fassung bleibt unter 7.500 Zeichen; `skill/` und `docs/` sind
  byte-identisch; interne Anker, lokale Download-Links und Testakten-Artefakte
  wurden durch das neue Skript geprüft.

## [3.0.8] — 2026-07-04

### Geändert
- Die zehn Jura-/Wissenschafts-Testzeugnisse wurden fachlich und formal
  vertieft: ausführlichere Briefköpfe, Personalzeichen, Projekt- und
  Registerbezüge, HR-/Ausstellerrollen, Dienstsiegel und Kanzleistempel.
- Aufgabenprofile und Bewertungsstellen wurden expliziter gefasst, insbesondere
  für juristische Lehrstühle, Postdoc-/Drittmittelkontext, Kanzleileitung ohne
  Anwaltszulassung, Probezeit-Associate, ReNo-/beA-/RVG-Arbeit und
  Senior-Associate-Konstellationen.
- Erwartungshorizont und README der Testakte betonen nun Briefkopf/Formalia,
  Ausstellerkompetenz, Rollenabgrenzung und typische Auslassungen.
- Versionsbump auf 3.0.8 in Voll- und Mini-Skill; README und Download-Seite
  aktualisiert.

### Geprüft
- Build-Skript erzeugt die Jura-/Wissenschafts-Artefakte zentral aus den
  hinterlegten Falltexten neu.
- Jura/Wissenschaft-ZIP enthält genau 10 Einzel-PDFs; Gesamt-PDF ist A4,
  nicht verschlüsselt und enthält 10 Zeugnisüberschriften.
- Mini-Fassung bleibt unter 7.500 Zeichen; `skill/` und `docs/` sind
  byte-identisch; interne Markdown-Anker und lokale HTML-Links wurden geprüft.

## [3.0.7] — 2026-07-04

### Hinzugefügt
- Zweite Testakte `arbeitszeugnisse-jura-und-wissenschaft` mit zehn
  fiktiven Arbeitszeugnissen aus juristisch-akademischen Rollen:
  wissenschaftliche Mitarbeit an juristischen Lehrstühlen, Kanzleileitung ohne
  Anwaltszulassung, Junior Associate in der Probezeit, ReNo-Fachkraft und
  Senior Associates in Boutique und Großkanzlei.
- Reproduzierbares Build-Skript
  `scripts/build_jura_und_wissenschaft_testakten.py` für Einzel-PDFs,
  Gesamt-PDF, ZIP und öffentliche `docs/testakten`-Downloads.
- Erwartungshorizont und Prüfpunkte zur neuen Testakte.

### Geändert
- README und Download-Seite verlinken nun beide Testakten-Sätze.
- Versionsbump auf 3.0.7 in Voll- und Mini-Skill; README-Versionssatz
  aktualisiert.

### Geprüft
- Neue Einzel-PDFs und Gesamt-PDF werden in A4 erzeugt.
- Jura/Wissenschaft-ZIP enthält genau 10 Einzel-PDFs; Gesamt-PDF enthält
  genau 10 Seiten.
- Download-Artefakte liegen zusätzlich unter `docs/testakten/`.

## [3.0.6] — 2026-07-01

### Hinzugefügt
- Fortsetzungs- und Abbruchprotokoll in der Vollversion: Statuskopf,
  Fortsetzungsmarke und feste Blockreihenfolge für lange One-Shot-Ausgaben.
- Komprimierte Fortsetzungsregel in der Mini-Fassung, damit kleine Modelle nach
  „weiter" am nächsten offenen Block fortfahren statt neu anzusetzen.
- Eigene GitHub-Pages-Downloadstarts für `SKILL.md` und `SKILL-mini.md` mit
  automatischem Downloadversuch und sichtbarem Fallback-Button.
- Ausgabe-Kompass in README und Download-Seite: erster Blick, One-Shot,
  HR-/Arbeitgeberprüfung und Fortsetzung nach Abbruch.

### Geändert
- Download-Seite mit Versionsstand 3.0.6, klarerer Ausgabeerwartung und
  neutralerem Layout.
- Versionsbump auf 3.0.6 in Voll- und Mini-Skill; README-Versionssatz
  aktualisiert.

### Geprüft
- Mini-Fassung bleibt unter 7.500 Zeichen.
- `docs/`-Kopien bleiben mit den Quelldateien in `skill/` byte-identisch.
- Interne Markdown-Sprungmarken und Versionsangaben wurden erneut geprüft.

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

[3.0.10]: https://github.com/Klotzkette/arbeitszeugnispruefer-skill/releases/tag/v3.0.10
[3.0.9]: https://github.com/Klotzkette/arbeitszeugnispruefer-skill/releases/tag/v3.0.9
[3.0.8]: https://github.com/Klotzkette/arbeitszeugnispruefer-skill/releases/tag/v3.0.8
[3.0.7]: https://github.com/Klotzkette/arbeitszeugnispruefer-skill/releases/tag/v3.0.7
[3.0.6]: https://github.com/Klotzkette/arbeitszeugnispruefer-skill/releases/tag/v3.0.6
[3.0.5]: https://github.com/Klotzkette/arbeitszeugnispruefer-skill/releases/tag/v3.0.5
[3.0.4]: https://github.com/Klotzkette/arbeitszeugnispruefer-skill/releases/tag/v3.0.4
