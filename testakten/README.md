# Testakten-Zentrale

Die Testakten-Zentrale bündelt 25 vollständig fiktive Arbeitszeugnisse aus
allgemeinen Branchen, Jura und Wissenschaft sowie Leitungsfunktionen. Sie dient
dem realistischen Blindtest des [`Arbeitszeugnis-Prüfers`](../skill/SKILL.md):
PDF zuerst ohne Lösungshinweise analysieren, danach Notenkorridor,
Mindestbefund und Überinterpretationsschutz in der
[`TESTFALL-MATRIX.md`](TESTFALL-MATRIX.md) vergleichen.

Alle Personen, Organisationen, Registerdaten, Anschriften und Vorgänge sind
frei erfunden. Die Fälle sind Trainings- und Demonstrationsmaterial, keine
echten Personalunterlagen und keine Rechtsberatung.

**Navigation:** [Hauptübersicht](../README.md) ·
[Downloadseite](https://klotzkette.github.io/arbeitszeugnispruefer-skill/) ·
[neuester Release](https://github.com/Klotzkette/arbeitszeugnispruefer-skill/releases/latest) ·
[Prüfsummen](https://github.com/Klotzkette/arbeitszeugnispruefer-skill/releases/latest/download/SHA256SUMS.txt)

## Schnellzugriff

| Umfang | Fälle | Schwerpunkt | Dateien und Downloads |
| --- | ---: | --- | --- |
| [Allgemeine Branchen](arbeitszeugnis-analyse-bluehendes-leben/README.md) | 01–10 | Apotheke, Kanzlei, Medizin, Logistik, Pflege, Handel und Industrie | [Einzel-PDF-ZIP](https://github.com/Klotzkette/arbeitszeugnispruefer-skill/releases/latest/download/arbeitszeugnis-testakten-einzel-pdfs.zip) · [Gesamt-PDF](https://github.com/Klotzkette/arbeitszeugnispruefer-skill/releases/latest/download/arbeitszeugnis-analyse-bluehendes-leben_gesamt.pdf) · [Erwartungshorizont](arbeitszeugnis-analyse-bluehendes-leben/90-erwartungshorizont-und-pruefpunkte.md) |
| [Jura und Wissenschaft](arbeitszeugnisse-jura-und-wissenschaft/README.md) | 11–20 | Lehrstuhl, Forschung, Kanzleibetrieb und Associate-Rollen | [Einzel-PDF-ZIP](https://github.com/Klotzkette/arbeitszeugnispruefer-skill/releases/latest/download/arbeitszeugnisse-jura-und-wissenschaft-einzel-pdfs.zip) · [Gesamt-PDF](https://github.com/Klotzkette/arbeitszeugnispruefer-skill/releases/latest/download/arbeitszeugnisse-jura-und-wissenschaft_gesamt.pdf) |
| [Leitungsfunktionen](arbeitszeugnisse-leitungsfunktionen/README.md) | 21–25 | Recht, Finanzen, Personal, Compliance und Werkleitung | [Einzel-PDF-ZIP](https://github.com/Klotzkette/arbeitszeugnispruefer-skill/releases/latest/download/arbeitszeugnisse-leitungsfunktionen-einzel-pdfs.zip) · [Gesamt-PDF](https://github.com/Klotzkette/arbeitszeugnispruefer-skill/releases/latest/download/arbeitszeugnisse-leitungsfunktionen_gesamt.pdf) |
| Komplettpaket | 01–25 | Alle PDFs, READMEs und Erwartungshorizonte | [Komplett-ZIP herunterladen](https://github.com/Klotzkette/arbeitszeugnispruefer-skill/releases/latest/download/arbeitszeugnis-testpaket-komplett.zip) |
| [Zentrale Fallmatrix](TESTFALL-MATRIX.md) | 01–25 | Sollkorridore, Kernbefunde und Guardrails | [`TESTFALL-MATRIX.md`](TESTFALL-MATRIX.md) |
| [Bonusakte „Blühendes Leben“](arbeitszeugnis-analyse-bluehendes-leben/90-ergaenzende-korrespondenz-und-vollvermerke.md) | Zusatzfall | Tatsachenblatt, Matrix, Mandantenerklärung und Arbeitgeberanschreiben | [Akte öffnen](arbeitszeugnis-analyse-bluehendes-leben/90-ergaenzende-korrespondenz-und-vollvermerke.md) |

## Empfohlener Testablauf

1. **Blindlauf:** Nur ein Einzel-PDF oder ein Gesamt-PDF an das Modell geben.
   Erwartungshorizont und Matrix noch nicht mitliefern.
2. **Mindestoutput prüfen:** Rolle, Zeugnisart, Kurzbefund, Satzmatrix,
   Gesamtnotenspanne und rollenrichtige Schreiben müssen vollständig vorliegen.
3. **Kalibrieren:** Ergebnis mit Sollkorridor, Kernbefund und Guardrail in der
   Fallmatrix sowie dem jeweiligen Erwartungshorizont vergleichen.
4. **Überinterpretation suchen:** Neutrale Befristung, Reorganisation,
   Schlussformel oder nicht belegte Auslassung dürfen nicht als sichere
   Negativtatsache ausgegeben werden.
5. **Batchlauf:** Mehrere PDFs gemeinsam prüfen; Dokumentgrenzen, Fallnummern
   und Befunde müssen getrennt bleiben.

## Bewertungslogik

- Der **Sollkorridor** bezeichnet die erwartbare sprachliche Gesamttendenz,
  keine gerichtliche Feststellung.
- Die **Ampel** bewertet Handlungsbedarf und Risiko, nicht automatisch die Note.
- Der **Kernbefund** muss erkannt und am Originalwortlaut begründet werden.
- Der **Guardrail** nennt eine typische Überdehnung, die gerade nicht als
  gesicherter Mangel ausgegeben werden darf.
- Ein Berichtigungsverlangen setzt einen belastbaren Berichtigungspunkt und die
  erforderliche Tatsachen- beziehungsweise Beleggrundlage voraus.

## Technische Qualität

Alle 25 Fälle verwenden ein gemeinsames adaptives A4-Layout mit
Briefkopf, Fortsetzungszeile, Seitenfuß, Signaturblock und sichtbarer
Kennzeichnung als fiktive Testakte. Der Release-Build erzeugt sämtliche PDFs
und ZIP-Dateien aus versionierten Quellen deterministisch, prüft Seitenzahl, Textgehalt, Schriften,
Dokumentgrenzen, ZIP-Struktur und SHA-256-Prüfsummen und baut das Komplettpaket
zweimal byte-identisch.

[Zur Hauptübersicht](../README.md) ·
[Zur Fallmatrix](TESTFALL-MATRIX.md) ·
[Vollversion herunterladen](https://github.com/Klotzkette/arbeitszeugnispruefer-skill/releases/latest/download/SKILL.md) ·
[Mini-Version herunterladen](https://github.com/Klotzkette/arbeitszeugnispruefer-skill/releases/latest/download/SKILL-mini.md)
