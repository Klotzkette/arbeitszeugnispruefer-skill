# Arbeitszeugnis-Prüfer Skill

> Experimenteller Agent-Skill für die anwaltliche Prüfung deutscher Arbeitszeugnisse — als Anregung für Kanzlei-Arbeitsabläufe. Orientiert sich an der deutschen Rechtspraxis, an Gesetzestexten, amtlichen Materialien und frei überprüfbarer Rechtsprechung. Enthält keinerlei Fachgutachten oder Rechtsberatung, alle Angaben ohne Gewähr — jede Nutzerin und jeder Nutzer kalibriert den Skill selbst für die eigene Praxis.

> Transparenz: Dieser Skill ist strukturierter Markdown-Text — ein umfangreicher, sorgfältig gegliederter Prompt, den ein Sprachmodell bei der Analyse eines Arbeitszeugnisses als Arbeitsanweisung lädt. Kein eigenes Modell, keine Blackbox, keine versteckte Logik. Der gesamte Inhalt ist offen einsehbar, nachvollziehbar, anpassbar und forkbar.
>
> Eine einzige Datei, modellunabhängig einsetzbar. Der vollständige Workflow steckt in einer einzigen Markdown-Datei: [`skill/SKILL.md`](skill/SKILL.md) — ohne Pflichtanhänge oder zusätzliche Promptdateien. Er funktioniert in jedem leistungsfähigen KI-Chatbot bzw. Sprachmodell: Claude, ChatGPT, Gemini, Mistral, Perplexity, lokal betriebene Modelle. Es ist keine Installation und kein Konto erforderlich; tragende Rechtsquellen sind vor Schriftsatznutzung gleichwohl live zu prüfen — siehe [Anwendung](#anwendung-so-einfach-gehts).

Konsolidierter Skill (Version 3.0.20) für die Prüfung deutscher Arbeits-, Dienst- und Ausbildungszeugnisse nach dem Ampelsystem — Befunde werden als farbige Ampelsymbole 🔴/🟠/🟢 ausgegeben, nicht als Farbwörter. Der Skill bündelt eine ursprünglich 50-teilige Plugin-Sammlung in eine einzige `SKILL.md` und deckt den vollständigen Bogen ab — vom Mandanten-Intake über die satzweise Notenmatrix bis zur Klagestrategie auf Zeugnisberichtigung. Version 3.0.20 macht die Testakten-Builds byte-reproduzierbar, schützt kuratierte READMEs vor Überschreiben und sichert die drei bisherigen Codex-Review-Hinweise durch Regressionstests ab.

## Navigation

[Direktdownloads](#direktdownloads) · [Testakten](#testakten-im-überblick) · [Anwendung](#anwendung-so-einfach-gehts) · [Repository-Landkarte](#repository-landkarte) · [Qualitätssicherung](#qualitätssicherung-und-release-check) · [Workflow](#workflow-in-acht-stufen) · [Rechtsanker](#rechtlicher-anker) · [Nutzungshinweise](#-keine-aussage-über-berufsrecht-datenschutz-ki-vo-oder-beschlagnahmeverbote)

## Direktdownloads

Die Links in der Spalte **Herunterladen** liefern unmittelbar eine Datei statt einer GitHub-Vorschauseite: Skills und Prüfsummen aus dem neuesten Release, das Gesamtprojekt als aktuelles `main`-Archiv. Die Spalte **Ansehen** ist zum Lesen, Prüfen oder Kopieren im Browser gedacht.

| Inhalt | Herunterladen | Ansehen |
| --- | --- | --- |
| Vollversion `SKILL.md` | [Datei herunterladen](https://github.com/Klotzkette/arbeitszeugnispruefer-skill/releases/latest/download/SKILL.md) | [`skill/SKILL.md`](skill/SKILL.md) |
| Mini-Version `SKILL-mini.md` | [Datei herunterladen](https://github.com/Klotzkette/arbeitszeugnispruefer-skill/releases/latest/download/SKILL-mini.md) | [`skill/SKILL-mini.md`](skill/SKILL-mini.md) |
| Prüfsummen `SHA256SUMS.txt` | [Datei herunterladen](https://github.com/Klotzkette/arbeitszeugnispruefer-skill/releases/latest/download/SHA256SUMS.txt) | [Pages-Ansicht](https://klotzkette.github.io/arbeitszeugnispruefer-skill/SHA256SUMS.txt) |
| Gesamtes Repository | [ZIP von `main` herunterladen](https://github.com/Klotzkette/arbeitszeugnispruefer-skill/archive/refs/heads/main.zip) | [Dateibaum öffnen](https://github.com/Klotzkette/arbeitszeugnispruefer-skill) |

Weitere Einstiege: [komfortable Downloadseite](https://klotzkette.github.io/arbeitszeugnispruefer-skill/) · [Downloadhilfe Vollversion](https://klotzkette.github.io/arbeitszeugnispruefer-skill/download-skill.html) · [Downloadhilfe Mini-Version](https://klotzkette.github.io/arbeitszeugnispruefer-skill/download-mini.html) · [alle versionierten Release-Assets](https://github.com/Klotzkette/arbeitszeugnispruefer-skill/releases/latest) · [`CHANGELOG.md`](CHANGELOG.md)

Kurzversion für kleine Assistenten: Wenn Claude, ChatGPT, Gemini, ein Agent-Harness oder ein kleines Skillset die große Datei nicht sauber annimmt, nimm die kompakte Sparversion. Sie bleibt unter 7.500 Zeichen inklusive Leerzeichen, ist weniger tief als die Vollversion, bildet aber den Kernworkflow mit Ampel, Rollenlogik, tabellarischer Satzmatrix, Notenspanne, Mandantenerklärung in normaler Sprache und Gegenseitenschreiben ab. Beide Dateien sind freistehend nutzbar: herunterladen oder kopieren, in ein KI-System geben, Zeugnis nachreichen.

Falls ein In-App-Browser den Direktdownload blockiert, die passende Downloadhilfe öffnen und dort den sichtbaren Button verwenden. Die Release-Seite bleibt der versionsfeste Fallback für Vollversion, Mini-Version, Prüfsummen und sämtliche PDF-/ZIP-Testakten.

Downloads selbst prüfen: `SHA256SUMS.txt` und die gewünschten Release-Assets in denselben Ordner laden und dort einen der folgenden Befehle ausführen. Nicht mitgeladene Assets werden vom Sammelcheck als fehlend gemeldet; die vorhandenen Dateien werden trotzdem einzeln geprüft.

```bash
# Linux
sha256sum -c SHA256SUMS.txt

# macOS
shasum -a 256 -c SHA256SUMS.txt
```

Wer den Inhalt lieber direkt sehen und kopieren will, öffnet [`skill/SKILL.md`](skill/SKILL.md) oder die Kurzfassung [`skill/SKILL-mini.md`](skill/SKILL-mini.md) — das sind die formatierten Ansichten hier im Repository. Der gesamte Text lässt sich dort mit `Strg+A` / `Cmd+A` markieren und kopieren.

## Testakten im Überblick

Fünfundzwanzig fiktive Arbeitszeugnisse zum Durchtesten des Skills. Alle Akten sind frei erfunden, als Einzel-PDFs und Gesamt-PDF verfügbar und zusätzlich mit Erwartungshorizont beziehungsweise Prüfpunkten im Repository dokumentiert.

| Akte | Inhalt | Direktdownloads | Details im Repository |
| --- | --- | --- | --- |
| Allgemeine Branchen | 10 Zeugnisse: PTA, Rechtsanwalt, MTA-R, Lagermeister, ZFA, Sparkassen-Filialleitung, Spedition, Hotel-Empfang, Altenpflege, Industriemechanik. | [ZIP mit 10 Einzel-PDFs](https://github.com/Klotzkette/arbeitszeugnispruefer-skill/releases/latest/download/arbeitszeugnis-testakten-einzel-pdfs.zip) · [Gesamt-PDF](https://github.com/Klotzkette/arbeitszeugnispruefer-skill/releases/latest/download/arbeitszeugnis-analyse-bluehendes-leben_gesamt.pdf) | [`README`](testakten/arbeitszeugnis-analyse-bluehendes-leben/README.md) · [`Vollvermerke`](testakten/arbeitszeugnis-analyse-bluehendes-leben/90-ergaenzende-korrespondenz-und-vollvermerke.md) |
| Jura und Wissenschaft | 10 Zeugnisse: juristische Lehrstuhl-/Universitätsrollen, Kanzleileitung ohne Anwaltszulassung, Junior Associate, ReNo-Fachkraft, Senior Associates. | [ZIP mit 10 Einzel-PDFs](https://github.com/Klotzkette/arbeitszeugnispruefer-skill/releases/latest/download/arbeitszeugnisse-jura-und-wissenschaft-einzel-pdfs.zip) · [Gesamt-PDF](https://github.com/Klotzkette/arbeitszeugnispruefer-skill/releases/latest/download/arbeitszeugnisse-jura-und-wissenschaft_gesamt.pdf) | [`README`](testakten/arbeitszeugnisse-jura-und-wissenschaft/README.md) · [`Erwartungshorizont`](testakten/arbeitszeugnisse-jura-und-wissenschaft/90-erwartungshorizont-und-pruefpunkte.md) |
| Leitungsfunktionen | 5 Zeugnisse: Rechtsabteilungsleitung, kaufmännische Leitung/CFO, Personal und Arbeitsrecht, Compliance/Datenschutz, Werk- und Standortleitung. | [ZIP mit 5 Einzel-PDFs](https://github.com/Klotzkette/arbeitszeugnispruefer-skill/releases/latest/download/arbeitszeugnisse-leitungsfunktionen-einzel-pdfs.zip) · [Gesamt-PDF](https://github.com/Klotzkette/arbeitszeugnispruefer-skill/releases/latest/download/arbeitszeugnisse-leitungsfunktionen_gesamt.pdf) | [`README`](testakten/arbeitszeugnisse-leitungsfunktionen/README.md) · [`Erwartungshorizont`](testakten/arbeitszeugnisse-leitungsfunktionen/90-erwartungshorizont-und-pruefpunkte.md) |

Praktischer Einsatz: Einzel-PDFs eignen sich für gezielte Chats und Regressionstests; Gesamt-PDFs eignen sich für Batch- oder One-Shot-Läufe. Die README-Dateien der Testakten erklären, welche Rollen, formalen Auffälligkeiten und typischen Bewertungsfallen jeweils trainiert werden.

## Anwendung: So einfach geht's

Begleitsatz zum Kopieren (egal ob Weg A oder Weg B) — zusammen mit dem Skill in den Chat geben:

```text
Bitte halte dich an diesen Skill/Prompt. Gleich kommt ein Arbeitszeugnis — bearbeite es danach.
```

Weg A — Text kopieren:

1. [`skill/SKILL.md`](skill/SKILL.md) oder [`skill/SKILL-mini.md`](skill/SKILL-mini.md) öffnen, den gesamten Text mit `Strg+A` / `Cmd+A` markieren und in den Chat einfügen.
2. Dazuschreiben: *„Bitte halte dich an diesen Skill/Prompt. Gleich kommt ein Arbeitszeugnis — bearbeite es danach."* Enter drücken.
3. Das Zeugnis einfügen (Text, PDF oder Foto). Die Analyse startet von selbst.

Weg B — Datei hineinziehen (Drag & Drop):

1. `SKILL.md` oder `SKILL-mini.md` über die [Direktdownloads oben](#direktdownloads) auf das Gerät laden.
2. Die Datei per Drag & Drop in das Chatfenster ziehen, dazuschreiben: *„Bitte halte dich an diesen Skill/Prompt. Gleich kommt ein Arbeitszeugnis — bearbeite es danach."* Enter drücken.
3. Das Zeugnis nachreichen — fertig.

Sofortstart in beiden Wegen: Der Skill analysiert ohne Rückfragen-Kaskade, kennzeichnet fehlende Angaben als Annahmen und liefert Einschätzungsmatrix, Ampel-Bilanz (🔴/🟠/🟢), Gesamtnotenspanne und Handlungsempfehlung in einem Durchgang. Wird der Skill als One-Shot/Megaprompt mit Zeugnis genutzt, soll er aus Perspektive der beurteilten Person bei Berichtigungsbedarf zusätzlich sofort ein Mandantenschreiben und ein außergerichtliches Aufforderungsschreiben an die statusrichtige Gegenseite mitliefern, nicht nur anbieten. Eine gebündelte Rückfrage gibt es höchstens dann, wenn die Analyse sonst objektiv falsch würde.

### Welche Ausgabe bekomme ich?

- **Erster Blick / Status:** Analyse, Ampel-Bilanz, Notenspanne, Hauptkritik und klare nächste Weiche.
- **One-Shot / Megaprompt:** aus Perspektive der beurteilten Person bei Berichtigungsbedarf Analyse, Mandantenschreiben und außergerichtliches Aufforderungsschreiben an Arbeitgeber, Dienstgeber oder Ausbildende in einem Durchgang.
- **HR / Arbeitgeberseite:** neutraler Korrekturvermerk mit Risiko, sicherer Ersatzformulierung und Formcheck statt Arbeitnehmer-Aufforderungsschreiben.
- **Antwort bricht ab:** „Bitte fahre mit dem nächsten offenen Block fort." Der Skill soll dann nicht neu anfangen, sondern an der Fortsetzungsmarke weiterarbeiten.

## Repository-Landkarte

| Bereich | Einstieg | Enthaltene Dateien |
| --- | --- | --- |
| Skills | [`skill/`](skill/) | [`SKILL.md`](skill/SKILL.md) Vollversion · [`SKILL-mini.md`](skill/SKILL-mini.md) Kurzversion |
| Öffentliche Downloadseite | [`docs/`](docs/) · [GitHub Pages](https://klotzkette.github.io/arbeitszeugnispruefer-skill/) | [`index.html`](docs/index.html) · [`download-skill.html`](docs/download-skill.html) · [`download-mini.html`](docs/download-mini.html) · [`SHA256SUMS.txt`](docs/SHA256SUMS.txt) |
| Allgemeine Testakte | [`README`](testakten/arbeitszeugnis-analyse-bluehendes-leben/README.md) | 10 Einzel-PDFs · Gesamt-PDF · ZIP · [`Vollvermerke`](testakten/arbeitszeugnis-analyse-bluehendes-leben/90-ergaenzende-korrespondenz-und-vollvermerke.md) |
| Jura und Wissenschaft | [`README`](testakten/arbeitszeugnisse-jura-und-wissenschaft/README.md) | 10 Einzel-PDFs · Gesamt-PDF · ZIP · [`Erwartungshorizont`](testakten/arbeitszeugnisse-jura-und-wissenschaft/90-erwartungshorizont-und-pruefpunkte.md) |
| Leitungsfunktionen | [`README`](testakten/arbeitszeugnisse-leitungsfunktionen/README.md) | 5 Einzel-PDFs · Gesamt-PDF · ZIP · [`Erwartungshorizont`](testakten/arbeitszeugnisse-leitungsfunktionen/90-erwartungshorizont-und-pruefpunkte.md) |
| Prüf- und Buildskripte | [`scripts/`](scripts/) | [`check_release_integrity.py`](scripts/check_release_integrity.py) · [`build_generated_testakten.py`](scripts/build_generated_testakten.py) · [`build_jura_und_wissenschaft_testakten.py`](scripts/build_jura_und_wissenschaft_testakten.py) · [`build_leitungsfunktionen_testakten.py`](scripts/build_leitungsfunktionen_testakten.py) |
| Projektpflege | [`CHANGELOG.md`](CHANGELOG.md) · [Integritäts-Workflow](.github/workflows/verify-integrity.yml) | Release-Historie und lesende Prüfung von Skills, Pages-Spiegeln, Links, Rechtsankern und Artefakten |
| Lizenzen | [`LICENSE-APACHE`](LICENSE-APACHE) · [`LICENSE-MIT`](LICENSE-MIT) | Dual-Lizenz Apache-2.0 OR MIT |

Die Datei ist in folgende Hauptteile gegliedert (interne Sprungmarken):

- Workflow in acht Stufen — Intake bis Klagestrategie, rechtlicher Anker, Antwortformate, Qualitätsgate.
- Teil A — Zufriedenheitsformel — Notenstufen 1 bis 5 der Hauptformel.
- Teil B — Schlussformel — Bedauern/Dank/Wunsch, Signal versus Anspruch.
- Teil C — Geheimcode-Katalog — Standardphrasen nach Themenachsen.
- Teil D — Ampel-Flaggen — Steigerungsadverbien, grüne/orange/rote Flaggen, negative Codeworte.
- Teil E — Analyse-Techniken — Drift, Auslassungen, Negationen, Widersprüche, Formalia.
- Teil F — Mandatsmodule — Aufforderungsschreiben, Wortlaut-Verbesserungen, Klageantrag.
- Teil G — Musterzeugnisse und Sonderfälle — Drei Musterzeugnisse, leitende Positionen, Azubi, Branchen.

Zusätzlich enthält der Skill durchgängig:

- Sofortstart und Rückfrage-Disziplin — Zeugnis rein, Analyse läuft; Annahmen statt Fragenkaskade.
- Lieferumfang nach Einsatzkontext — interaktiv (Claude-Apps, Claude Code) bietet der Skill Aufforderungs- und Klageschritte am Ende als Option an; im nicht-interaktiven Einsatz (API, Agent-SDK, Automatisierung) macht er die Arbeit rollenrichtig fertig: Die beurteilte Person erhält bei Berichtigungsbedarf das statusrichtige Aufforderungsschreiben, HR-/Arbeitgeberprüfung stattdessen eine neutrale Korrekturprüfung.
- Fortsetzungs- und Abbruchprotokoll — lange One-Shot-Ausgaben bekommen Statuskopf und Fortsetzungsmarke, damit kleine Modelle oder API-Limits nicht zum Neuansatz zwingen.
- Ampel-Darstellung — Befunde immer als 🔴/🟠/🟢, mit Ampel-Bilanz im Hauptbefund.
- Rechtsprechungsanker — verifizierte BAG-Leitentscheidungen zu Notenstufen, Beweislast, Schlussformel, Maßregelungsverbot, Zeugnisklarheit, Auslassungen, Datumswahrheit, Tabellenform, Vollstreckbarkeit und äußerer Form, ergänzt um frei verfügbare LAG- und instanzgerichtliche Rechtsprechung.

## Qualitätssicherung und Release-Check

Vor einer neuen Version sollte der lokale Integritätscheck ausgeführt werden:

```bash
python3 scripts/check_release_integrity.py
```

| Skript | Zweck |
| --- | --- |
| [`scripts/check_release_integrity.py`](scripts/check_release_integrity.py) | Prüft Skill-Frontmatter, Versionsgleichlauf, byte-identische `skill/`- und `docs/`-Dateien, das 7.500-Zeichen-Limit der Mini-Fassung, zentrale Rechtsfundstellen und bekannte Fehlzuordnungen, sämtliche lokalen Markdown-Ziele, interne Markdown- und HTML-Menüanker, die lesende CI-Konfiguration, Release-Asset-Kandidaten, `SHA256SUMS.txt`, öffentliche Testakten-Artefakte sowie PDF-/ZIP-Sanity der Trainingsakten. Nach Veröffentlichung vergleicht `--github-release vX.Y.Z` zusätzlich Tag und `main`-Commit sowie Namen, Größen und SHA-256-Digests der realen GitHub-Release-Assets mit den lokalen Dateien. |
| [`scripts/build_generated_testakten.py`](scripts/build_generated_testakten.py) | Baut alle generierten Testakten-Artefakte neu, ohne kuratierte READMEs zu verändern. `--verify-reproducible` baut zweimal und vergleicht jede erzeugte Datei bytegenau. |
| [`scripts/build_jura_und_wissenschaft_testakten.py`](scripts/build_jura_und_wissenschaft_testakten.py) | Erzeugt Einzel-PDFs, Gesamt-PDF, ZIP und Pages-Downloads der Jura-/Wissenschaftsakte. |
| [`scripts/build_leitungsfunktionen_testakten.py`](scripts/build_leitungsfunktionen_testakten.py) | Erzeugt Einzel-PDFs, Gesamt-PDF, ZIP und Pages-Downloads der Leitungsfunktionen-Akte. |

Alle generierten Testakten-Artefakte gemeinsam neu bauen:

```bash
python3 scripts/build_generated_testakten.py

# Strenger Release-Lauf: zweimal bauen und Byte-Reproduzierbarkeit prüfen
python3 scripts/build_generated_testakten.py --verify-reproducible
```

Nach dem GitHub-Release kann zusätzlich der veröffentlichte Asset-Satz geprüft werden:

```bash
python3 scripts/check_release_integrity.py --github-release v3.0.20
```

## Workflow in acht Stufen

1. Intake und Rollenklärung
2. Zeugnisart und Kopfdaten sichern
3. Notenrelevante Sätze markieren
4. Einschätzungsmatrix (satzweise, mit Ampelsymbolen und Rechtsprechungsstütze)
5. Drift, Auslassungen und Widersprüche
6. Gesamtnotenspanne und Hauptbefund
7. Mandantenbericht und Verhandlungsmodul
8. Klagestrategie Zeugnisberichtigung

## Rechtlicher Anker

- [§ 109 GewO](https://www.gesetze-im-internet.de/gewo/__109.html) — Arbeitnehmer-Endzeugnis; Klarheit, Verständlichkeit und Geheimzeichenverbot gelten für jedes Zeugnis, Leistung und Verhalten gehören nur in das qualifizierte Zeugnis. Elektronische Form setzt die Einwilligung des Arbeitnehmers voraus; Zeugniswahrheit und verständiges Wohlwollen folgen aus der BAG-Linie.
- [§ 630 BGB](https://www.gesetze-im-internet.de/bgb/__630.html) — Zeugnis bei dauernden Dienstverhältnissen außerhalb des Arbeitnehmerstatus; für Arbeitnehmer verweist die Norm auf § 109 GewO.
- [§ 16 Abs. 1 und 2 BBiG](https://www.gesetze-im-internet.de/bbig_2005/__16.html) — Erteilung, Form und Mindestinhalt des Zeugnisses für ein Berufsausbildungsverhältnis; Verhalten und Leistung nur auf Verlangen. [§ 26 BBiG](https://www.gesetze-im-internet.de/bbig_2005/__26.html) kann § 16 auf bestimmte andere Lernverhältnisse erstrecken; Umschulung und Fortbildung sind gesondert einzuordnen.
- § 241 Abs. 2 BGB — mögliche Grundlage des Zwischenzeugnisses bei triftigem Grund; §§ 280 Abs. 1 und 2, 286 BGB — möglicher Verzögerungsschaden nur bei erfüllten Haftungs- und Verzugsvoraussetzungen.
- Beweislastregel BAG: Note 3 ist Ausgangspunkt; besser als Note 3 muss grundsätzlich der Arbeitnehmer darlegen und beweisen, schlechter als Note 3 der Arbeitgeber (BAG 14.10.2003 – 9 AZR 12/03; BAG 18.11.2014 – 9 AZR 584/13).
- Rechtsweg — bei Arbeitnehmern regelmäßig Arbeitsgericht ([§ 2 Abs. 1 Nr. 3 ArbGG](https://www.gesetze-im-internet.de/arbgg/__2.html)) und Leistungsklage; bei Organpersonen Status und [§§ 2, 5 ArbGG](https://www.gesetze-im-internet.de/arbgg/__5.html) gesondert prüfen. [§ 12a ArbGG](https://www.gesetze-im-internet.de/arbgg/__12a.html) gilt nur bei eröffnetem Arbeitsrechtsweg.

Die `SKILL.md` enthält einen eigenen Rechtsprechungsanker mit den Leitentscheidungen des Bundesarbeitsgerichts zu Notenstufen, Beweislast, Schlussformel, Zeugnisklarheit, Status, Form und Vollstreckung. Darüber hinaus gilt: Rechtsprechung wird in diesem Skill nie ungeprüft aus Modellwissen zitiert — jede tragende Aussage wird über `gesetze-im-internet.de`, die BAG-Datenbank oder ein amtliches Landes-/Bundesportal mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifiziert. `dejure.org` kann bei der Suche helfen, ersetzt aber keine verfügbare Primärquelle.

## Einsatzlagen

- Mandant oder Mandantin will Zeugnis einordnen.
- Kanzlei prüft Berichtigungs-, Vergleichs- oder Klagestrategie.
- HR will Entwurf gegenprüfen.
- Betriebsrat sucht Schulungseinschätzung.
- Ausbildungs- oder Zwischenzeugnis.

## Verwandte Projekte

Dieser Skill ist aus dem Plugin `arbeitszeugnis-analyse` der Sammlung [`claude-fuer-deutsches-recht`](https://github.com/Klotzkette/claude-fuer-deutsches-recht) extrahiert und konsolidiert. Die ursprünglichen 50 Einzelskills wurden in eine einzige `SKILL.md` zusammengeführt, ohne fachliche Substanz zu verlieren.

## 🚨 KEINE Aussage über Berufsrecht, Datenschutz, KI-VO oder Beschlagnahmeverbote

Lesen, bevor irgendetwas davon eingesetzt wird. Dieses Repository ist ausschließlich ein technisches Experiment. Es trifft keinerlei Aussage darüber, ob der Einsatz dieses Skills in einer konkreten Praxisumgebung berufs-, datenschutz- oder KI-rechtlich zulässig ist. Alle nachstehenden Fragen muss jede Nutzerin und jeder Nutzer in eigener Verantwortung vor der ersten Nutzung prüfen — das Repository, seine Autorin / sein Autor und alle Mitwirkenden übernehmen dafür keinerlei Verantwortung oder Haftung:

- Strafrechtlicher Geheimnisschutz — §§ 203, 204 StGB. Der Skill sagt nichts darüber aus, ob ein konkreter Einsatz mit § 203 StGB (Verletzung von Privatgeheimnissen) und, soweit einschlägig, § 204 StGB (Verwertung fremder Geheimnisse) vereinbar ist — auch nicht mit Blick auf mitwirkende Personen und sonstige Stellen nach § 203 Abs. 3 und 4 StGB.
- Berufsrecht — § 43e BRAO, § 2 BORA, § 53 StPO. Es wird nicht geprüft, ob der Einsatz mit § 43e BRAO (Inanspruchnahme von Dienstleistern, insbesondere Cloud/KI), § 2 BORA (Verschwiegenheit), den Zeugnisverweigerungsrechten nach § 53 StPO und den Beschlagnahmeverboten nach § 97 StPO vereinbar ist. Gleiches gilt sinngemäß für andere freie Berufe mit eigenem Berufsrecht (StBerG für Steuerberater:innen, WPO für Wirtschaftsprüfer:innen, ÄrztInnen, Notar:innen, Patentanwält:innen u. a.).
- Datenschutz — DSGVO, BDSG. Es wird nicht beurteilt, ob die Verarbeitung personenbezogener Daten DSGVO-konform ist, ob eine ausreichende Rechtsgrundlage nach Art. 6 DSGVO und bei tatsächlich enthaltenen besonderen Kategorien zusätzlich Art. 9 DSGVO vorliegt, ob ein Auftragsverarbeitungsvertrag nach Art. 28 DSGVO geschlossen werden muss, ob eine Datenschutz-Folgenabschätzung nach Art. 35 DSGVO erforderlich ist oder ob die Informationspflichten nach Art. 13, 14 DSGVO erfüllt sind. Arbeitszeugnisse enthalten stets personenbezogene Daten; besondere Kategorien nach Art. 9 DSGVO nur, wenn der konkrete Inhalt solche Informationen offenbart.
- KI-Verordnung (KI-VO / EU AI Act, VO (EU) 2024/1689). Es wird nicht entschieden, ob der Einsatz unter eine der Hochrisiko-Kategorien nach Art. 6 KI-VO in Verbindung mit Anhang III KI-VO fällt (insbesondere Zugang zur Justiz, Beschäftigungskontext), ob Transparenzpflichten nach Art. 50 KI-VO greifen, ob es sich um ein General-Purpose-AI-Modell nach Art. 51 ff. KI-VO handelt und welche Pflichten als Betreiber (Art. 26 KI-VO) zu erfüllen sind.
- Beschlagnahmeverbote und auslandsrechtliche Zugriffe. Es wird nicht geprüft, ob Eingabedaten und Modellantworten gegen Beschlagnahme nach §§ 97, 160a StPO oder gegen Zugriffe aufgrund ausländischer und extraterritorial wirkender Rechtsgrundlagen, etwa CLOUD Act oder FISA, hinreichend geschützt sind. Dafür ist die jeweilige Nutzerin / der jeweilige Nutzer allein verantwortlich.
- Zugang, Auftragsverarbeitung, Hosting. Wie der API-Zugang zum Modell beschafft wird (Anthropic direkt, AWS Bedrock, Google Vertex, eigenes Hosting), ob mit dem Anbieter ein Auftragsverarbeitungsvertrag geschlossen wird, ob ein berufsrechtskonformer Cloud-Vertrag vorliegt und ob die Anforderungen an die Verschwiegenheit / Mandatsgeheimnis und Datenflusskontrolle in der konkreten Deployment-Konstellation eingehalten sind, bleibt vollständig in der Eigenverantwortung der Nutzerin / des Nutzers.

Anwältinnen, Anwälte und andere Berufsgeheimnisträgerinnen/-träger müssen vor jeder produktiven Nutzung selbst prüfen, ob die konkrete Anbieter-, Hosting- und Datenflusskonstellation mit Mandatsgeheimnis, Berufsrecht und Datenschutz vereinbar ist. Dieses Repository bestätigt keinen Anbieter und ersetzt keine Prüfung von § 203 StGB, § 43e BRAO, Art. 28 DSGVO, Kapitel V DSGVO, TOMs, Löschkonzept, Audit-Rechten, Subunternehmern, Datenresidenz und vertraglicher Verschwiegenheit.

## Lizenz

Dual licensed: Apache-2.0 OR MIT — siehe [LICENSE-APACHE](LICENSE-APACHE) und [LICENSE-MIT](LICENSE-MIT).
