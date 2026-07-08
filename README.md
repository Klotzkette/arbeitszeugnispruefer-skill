# Arbeitszeugnis-Prüfer Skill

> Experimenteller Agent-Skill für die anwaltliche Prüfung deutscher Arbeitszeugnisse — als Anregung für Kanzlei-Arbeitsabläufe. Orientiert sich an der deutschen Rechtspraxis, an Gesetzestexten, amtlichen Materialien und frei überprüfbarer Rechtsprechung. Enthält keinerlei Fachgutachten oder Rechtsberatung, alle Angaben ohne Gewähr — jede Nutzerin und jeder Nutzer kalibriert den Skill selbst für die eigene Praxis.

> Transparenz: Dieser Skill ist strukturierter Markdown-Text — ein umfangreicher, sorgfältig gegliederter Prompt, den ein Sprachmodell bei der Analyse eines Arbeitszeugnisses als Arbeitsanweisung lädt. Kein eigenes Modell, keine Blackbox, keine versteckte Logik. Der gesamte Inhalt ist offen einsehbar, nachvollziehbar, anpassbar und forkbar.
>
> Eine einzige Datei, modellunabhängig einsetzbar. Der vollständige Skill steckt in einer einzigen Markdown-Datei: [`skill/SKILL.md`](skill/SKILL.md) — ohne Anhänge, ohne externe Referenzen. Er funktioniert in jedem leistungsfähigen KI-Chatbot bzw. Sprachmodell: Claude, ChatGPT, Gemini, Mistral, Perplexity, lokal betriebene Modelle. Es ist keine Installation, kein Konto und kein zusätzliches Werkzeug erforderlich — siehe [Anwendung](#anwendung-so-einfach-gehts).

Konsolidierter Skill (Version 3.0.17) für die Prüfung deutscher Arbeitszeugnisse nach dem Ampelsystem — Befunde werden als farbige Ampelsymbole 🔴/🟠/🟢 ausgegeben, nicht als Farbwörter. Der Skill bündelt eine ursprünglich 50-teilige Plugin-Sammlung in eine einzige `SKILL.md` und deckt den vollständigen Bogen ab — vom Mandanten-Intake über die satzweise Notenmatrix bis zur Klagestrategie auf Zeugnisberichtigung. Version 3.0.17 ergänzt eine SHA-256-Prüfsummenliste für die Release-Dateien und verifiziert sie im Integritätscheck.

## Schnellzugriff

| Ziel | Direktlink | Hinweis |
| --- | --- | --- |
| Vollversion herunterladen | [SKILL.md Download](https://klotzkette.github.io/arbeitszeugnispruefer-skill/download-skill.html) | Startet den Markdown-Download mit Fallback-Button. |
| Kurzversion herunterladen | [SKILL-mini.md Download](https://klotzkette.github.io/arbeitszeugnispruefer-skill/download-mini.html) | Kompaktfassung unter 7.500 Zeichen mit Matrix, Note, Mandantenerklärung und Arbeitgeber-Schreiben. |
| Öffentliche Downloadseite | [GitHub Pages öffnen](https://klotzkette.github.io/arbeitszeugnispruefer-skill/) | Vollversion, Mini-Version und Testakten an einem Ort. |
| Neueste Release-Assets | [GitHub Release öffnen](https://github.com/Klotzkette/arbeitszeugnispruefer-skill/releases/latest) | Markdown-Dateien, PDFs und ZIPs als versionierte Anhänge. |
| Prüfsummen | [SHA256SUMS.txt](https://klotzkette.github.io/arbeitszeugnispruefer-skill/SHA256SUMS.txt) | SHA-256-Werte der Markdown-, PDF- und ZIP-Assets. |
| Skill-Quelltext ansehen | [`skill/SKILL.md`](skill/SKILL.md) | Formatierte Repository-Ansicht zum Prüfen oder Kopieren. |
| Mini-Quelltext ansehen | [`skill/SKILL-mini.md`](skill/SKILL-mini.md) | Freistehende Kurzfassung für kleine Assistenten. |
| Release-Historie | [`CHANGELOG.md`](CHANGELOG.md) | Änderungen und Prüfpunkte je Version. |
| Testakten gesamt | [Übersicht unten](#testakten-im-überblick) | 25 fiktive Arbeitszeugnisse in drei Akten. |
| Release-Check | [`scripts/check_release_integrity.py`](scripts/check_release_integrity.py) | Prüft Versionen, Links, Spiegeldateien und Testakten-Artefakte. |

## Download

[📥 SKILL.md jetzt herunterladen](https://klotzkette.github.io/arbeitszeugnispruefer-skill/download-skill.html)

Kurzversion für kleine Assistenten: Wenn Claude, ChatGPT, Gemini, ein Agent-Harness oder ein kleines Skillset die große Datei nicht sauber annimmt, nimm die kompakte Sparversion: [SKILL-mini.md herunterladen](https://klotzkette.github.io/arbeitszeugnispruefer-skill/download-mini.html). Sie bleibt unter 7.500 Zeichen inklusive Leerzeichen, ist nicht so tief wie die Vollversion, bildet aber den Kernworkflow mit Ampel, Rollenlogik, tabellarischer Satzmatrix, Notenspanne, Mandantenerklärung in normaler Sprache und Gegenseitenschreiben ab. Beide Dateien sind freistehend nutzbar: herunterladen oder kopieren, in ein KI-System geben, Zeugnis nachreichen.

Ein Klick genügt — die neuen Download-Startseiten stoßen den Download der ausgewählten Markdown-Datei automatisch an und zeigen zusätzlich einen großen Fallback-Button, falls eine App den automatischen Download blockiert. Kein Rechtsklick, kein „Speichern unter…", kein Umweg über Menüs.

Wenn einer der Download-Links in einer App nicht direkt funktioniert (manche In-App-Browser ignorieren Download-Anweisungen): Die Startseite geöffnet lassen und den sichtbaren Download-Button antippen. Oder die [komfortable Download-Seite](https://klotzkette.github.io/arbeitszeugnispruefer-skill/) im normalen Browser öffnen — dort stehen Vollversion, Mini-Version und Testakten nebeneinander.

Versionierte Komplettpakete stehen zusätzlich im jeweils neuesten [GitHub Release](https://github.com/Klotzkette/arbeitszeugnispruefer-skill/releases/latest): Dort hängen die Vollversion, die Mini-Version sowie die PDF-/ZIP-Testakten als Release-Assets. Das ist der robusteste Weg, wenn ein Browser den `download`-Hinweis ignoriert oder ein bestimmter Versionsstand archiviert werden soll. Die Datei [SHA256SUMS.txt](https://klotzkette.github.io/arbeitszeugnispruefer-skill/SHA256SUMS.txt) enthält die Prüfsummen der freigegebenen Markdown-, PDF- und ZIP-Dateien.

Wer den Inhalt lieber direkt sehen und kopieren will, öffnet [`skill/SKILL.md`](skill/SKILL.md) oder die Kurzfassung [`skill/SKILL-mini.md`](skill/SKILL-mini.md) — das sind die formatierten Ansichten hier im Repository. Der gesamte Text lässt sich dort mit `Strg+A` / `Cmd+A` markieren und kopieren.

## Testakten im Überblick

Fünfundzwanzig fiktive Arbeitszeugnisse zum Durchtesten des Skills. Alle Akten sind frei erfunden, als Einzel-PDFs und Gesamt-PDF verfügbar und zusätzlich mit Erwartungshorizont beziehungsweise Prüfpunkten im Repository dokumentiert.

| Akte | Inhalt | Direktdownloads | Details im Repository |
| --- | --- | --- | --- |
| Allgemeine Branchen | 10 Zeugnisse: PTA, Rechtsanwalt, MTA-R, Lagermeister, ZFA, Sparkassen-Filialleitung, Spedition, Hotel-Empfang, Altenpflege, Industriemechanik. | [ZIP mit 10 Einzel-PDFs](https://klotzkette.github.io/arbeitszeugnispruefer-skill/testakten/arbeitszeugnis-testakten-einzel-pdfs.zip) · [Gesamt-PDF](https://klotzkette.github.io/arbeitszeugnispruefer-skill/testakten/arbeitszeugnis-analyse-bluehendes-leben_gesamt.pdf) | [`README`](testakten/arbeitszeugnis-analyse-bluehendes-leben/README.md) · [`Vollvermerke`](testakten/arbeitszeugnis-analyse-bluehendes-leben/90-ergaenzende-korrespondenz-und-vollvermerke.md) |
| Jura und Wissenschaft | 10 Zeugnisse: juristische Lehrstuhl-/Universitätsrollen, Kanzleileitung ohne Anwaltszulassung, Junior Associate, ReNo-Fachkraft, Senior Associates. | [ZIP mit 10 Einzel-PDFs](https://klotzkette.github.io/arbeitszeugnispruefer-skill/testakten/arbeitszeugnisse-jura-und-wissenschaft-einzel-pdfs.zip) · [Gesamt-PDF](https://klotzkette.github.io/arbeitszeugnispruefer-skill/testakten/arbeitszeugnisse-jura-und-wissenschaft_gesamt.pdf) | [`README`](testakten/arbeitszeugnisse-jura-und-wissenschaft/README.md) · [`Erwartungshorizont`](testakten/arbeitszeugnisse-jura-und-wissenschaft/90-erwartungshorizont-und-pruefpunkte.md) |
| Leitungsfunktionen | 5 Zeugnisse: Rechtsabteilungsleitung, kaufmännische Leitung/CFO, Personal und Arbeitsrecht, Compliance/Datenschutz, Werk- und Standortleitung. | [ZIP mit 5 Einzel-PDFs](https://klotzkette.github.io/arbeitszeugnispruefer-skill/testakten/arbeitszeugnisse-leitungsfunktionen-einzel-pdfs.zip) · [Gesamt-PDF](https://klotzkette.github.io/arbeitszeugnispruefer-skill/testakten/arbeitszeugnisse-leitungsfunktionen_gesamt.pdf) | [`README`](testakten/arbeitszeugnisse-leitungsfunktionen/README.md) · [`Erwartungshorizont`](testakten/arbeitszeugnisse-leitungsfunktionen/90-erwartungshorizont-und-pruefpunkte.md) |

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

1. `SKILL.md` oder `SKILL-mini.md` über den [Direktdownload oben](#download) auf das Gerät laden.
2. Die Datei per Drag & Drop in das Chatfenster ziehen, dazuschreiben: *„Bitte halte dich an diesen Skill/Prompt. Gleich kommt ein Arbeitszeugnis — bearbeite es danach."* Enter drücken.
3. Das Zeugnis nachreichen — fertig.

Sofortstart in beiden Wegen: Der Skill analysiert ohne Rückfragen-Kaskade, kennzeichnet fehlende Angaben als Annahmen und liefert Einschätzungsmatrix, Ampel-Bilanz (🔴/🟠/🟢), Gesamtnotenspanne und Handlungsempfehlung in einem Durchgang. Wird der Skill als One-Shot/Megaprompt mit Zeugnis genutzt, soll er bei Arbeitnehmerperspektive und Berichtigungsbedarf zusätzlich sofort ein Mandantenschreiben und ein außergerichtliches Aufforderungsschreiben an den Arbeitgeber/Gegenseite mitliefern, nicht nur anbieten. Eine gebündelte Rückfrage gibt es höchstens dann, wenn die Analyse sonst objektiv falsch würde.

### Welche Ausgabe bekomme ich?

- **Erster Blick / Status:** Analyse, Ampel-Bilanz, Notenspanne, Hauptkritik und klare nächste Weiche.
- **One-Shot / Megaprompt:** bei Arbeitnehmerperspektive und Berichtigungsbedarf Analyse, Mandantenschreiben und außergerichtliches Aufforderungsschreiben in einem Durchgang.
- **HR / Arbeitgeberseite:** neutraler Korrekturvermerk mit Risiko, sicherer Ersatzformulierung und Formcheck statt Arbeitnehmer-Aufforderungsschreiben.
- **Antwort bricht ab:** „Bitte fahre mit dem nächsten offenen Block fort." Der Skill soll dann nicht neu anfangen, sondern an der Fortsetzungsmarke weiterarbeiten.

## Inhalt

```
skill/
├── SKILL.md        Vollversion: Workflow, Codes, Flaggen, Mandatsmodule, Musterzeugnisse
└── SKILL-mini.md   Sparversion unter 7.500 Zeichen für kleinere Assistenten und Skillsets

testakten/
├── arbeitszeugnis-analyse-bluehendes-leben/       10 allgemeine Branchen
├── arbeitszeugnisse-jura-und-wissenschaft/        10 Jura-/Wissenschaftsfälle
└── arbeitszeugnisse-leitungsfunktionen/           5 Führungszeugnisse

docs/
├── index.html       öffentliche Downloadseite
├── SKILL.md         Pages-Spiegel der Vollversion
└── SKILL-mini.md    Pages-Spiegel der Kurzversion
```

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
- Lieferumfang nach Einsatzkontext — interaktiv (Claude-Apps, Claude Code) bietet der Skill Aufforderungs- und Klageschritte am Ende als Option an; im nicht-interaktiven Einsatz (API, Agent-SDK, Automatisierung) macht er die Arbeit rollenrichtig fertig: Arbeitnehmerperspektive erhält bei Berichtigungsbedarf das Aufforderungsschreiben, HR-/Arbeitgeberprüfung stattdessen eine neutrale Korrekturprüfung.
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
| [`scripts/check_release_integrity.py`](scripts/check_release_integrity.py) | Prüft Versionsgleichlauf, byte-identische `skill/`- und `docs/`-Dateien, das 7.500-Zeichen-Limit der Mini-Fassung, interne Markdown-Anker, lokale Download-Links, Release-Asset-Kandidaten, `SHA256SUMS.txt`, öffentliche Testakten-Artefakte sowie PDF-/ZIP-Sanity der Trainingsakten. Nach Veröffentlichung kann es mit `--github-release vX.Y.Z` zusätzlich die realen GitHub-Release-Assets gegen die lokalen Dateien prüfen. |
| [`scripts/build_generated_testakten.py`](scripts/build_generated_testakten.py) | Baut alle generierten Testakten-Artefakte aus den vorhandenen Buildern neu. |
| [`scripts/build_jura_und_wissenschaft_testakten.py`](scripts/build_jura_und_wissenschaft_testakten.py) | Erzeugt Einzel-PDFs, Gesamt-PDF, ZIP und Pages-Downloads der Jura-/Wissenschaftsakte. |
| [`scripts/build_leitungsfunktionen_testakten.py`](scripts/build_leitungsfunktionen_testakten.py) | Erzeugt Einzel-PDFs, Gesamt-PDF, ZIP und Pages-Downloads der Leitungsfunktionen-Akte. |

Alle generierten Testakten-Artefakte gemeinsam neu bauen:

```bash
python3 scripts/build_generated_testakten.py
```

Nach dem GitHub-Release kann zusätzlich der veröffentlichte Asset-Satz geprüft werden:

```bash
python3 scripts/check_release_integrity.py --github-release v3.0.17
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

- § 109 GewO — Anspruch auf einfaches oder qualifiziertes Zeugnis; Klarheit, Verständlichkeit und Geheimzeichenverbot; elektronische Form nur mit Einwilligung. Zeugniswahrheit und verständiges Wohlwollen folgen aus der BAG-Linie.
- § 16 BBiG — Ausbildungszeugnis; auf Verlangen mit Verhalten und Leistung; elektronische Form nur mit Einwilligung der Auszubildenden.
- §§ 241 Abs. 2, 280 Abs. 1 BGB — Nebenpflicht; Schadensersatz bei Verletzung.
- Beweislastregel BAG: Note 3 ist Ausgangspunkt; besser als Note 3 muss grundsätzlich der Arbeitnehmer darlegen und beweisen, schlechter als Note 3 der Arbeitgeber (BAG 14.10.2003 – 9 AZR 12/03; BAG 18.11.2014 – 9 AZR 584/13).
- Zuständigkeit Arbeitsgericht (§ 2 Abs. 1 Nr. 3 ArbGG); Klage als Leistungsklage.

Die `SKILL.md` enthält einen eigenen Rechtsprechungsanker mit den Leitentscheidungen des Bundesarbeitsgerichts zu Notenstufen, Beweislast, Schlussformel, Zeugnisklarheit und äußerer Form. Darüber hinaus gilt: Rechtsprechung wird in diesem Skill nie ungeprüft aus Modellwissen zitiert — jede tragende Aussage wird über `gesetze-im-internet.de`, `dejure.org` oder das Rechtsprechungsportal des Bundes mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifiziert.

## Einsatzlagen

- Mandant oder Mandantin will Zeugnis einordnen.
- Kanzlei prüft Berichtigungs-, Vergleichs- oder Klagestrategie.
- HR will Entwurf gegenprüfen.
- Betriebsrat sucht Schulungseinschätzung.
- Ausbildungs- oder Zwischenzeugnis.

## Verwandte Projekte

Dieser Skill ist aus dem Plugin `arbeitszeugnis-analyse` der Sammlung [`claude-fuer-deutsches-recht`](https://github.com/Klotzkette/claude-fuer-deutsches-recht) extrahiert und konsolidiert. Die ursprünglichen 50 Einzelskills wurden in eine einzige `SKILL.md` zusammengeführt, ohne fachliche Substanz zu verlieren.

## Testakten zum Üben — Details

Der Direktdownload steht oben im Abschnitt [Testakten im Überblick](#testakten-im-überblick). Die Detailansichten führen jeweils durch Aktenzweck, einzelne Rollen, Einzel-PDFs und Prüfpunkte:

| Detailansicht | Inhalt |
| --- | --- |
| [`testakten/arbeitszeugnis-analyse-bluehendes-leben/README.md`](testakten/arbeitszeugnis-analyse-bluehendes-leben/README.md) | Zehn allgemeine Branchenzeugnisse mit Korrespondenz und Vollvermerken. |
| [`testakten/arbeitszeugnisse-jura-und-wissenschaft/README.md`](testakten/arbeitszeugnisse-jura-und-wissenschaft/README.md) | Zehn juristisch-akademische Zeugnisse mit Erwartungshorizont und Prüfpunkten. |
| [`testakten/arbeitszeugnisse-leitungsfunktionen/README.md`](testakten/arbeitszeugnisse-leitungsfunktionen/README.md) | Fünf ausführliche Führungszeugnisse mit eigener Prüflogik. |

## 🚨 KEINE Aussage über Berufsrecht, Datenschutz, KI-VO oder Beschlagnahmeverbote

Lesen, bevor irgendetwas davon eingesetzt wird. Dieses Repository ist ausschließlich ein technisches Experiment. Es trifft keinerlei Aussage darüber, ob der Einsatz dieses Skills in einer konkreten Praxisumgebung berufs-, datenschutz- oder KI-rechtlich zulässig ist. Alle nachstehenden Fragen muss jede Nutzerin und jeder Nutzer in eigener Verantwortung vor der ersten Nutzung prüfen — das Repository, seine Autorin / sein Autor und alle Mitwirkenden übernehmen dafür keinerlei Verantwortung oder Haftung:

- Strafrechtliches Mandatsgeheimnis — §§ 203, 204 StGB. Der Skill sagt nichts darüber aus, ob ein konkreter Einsatz mit dem strafbewehrten Geheimnisschutz des § 203 StGB (Verletzung von Privatgeheimnissen) und § 204 StGB (Verwertung fremder Geheimnisse) vereinbar ist — auch nicht in der Variante § 203 Abs. 3, 4 StGB (mitwirkende Personen, sonstige Stellen).
- Berufsrecht — § 43e BRAO, § 2 BORA, § 53 StPO. Es wird nicht geprüft, ob der Einsatz mit § 43e BRAO (Inanspruchnahme von Dienstleistern, insbesondere Cloud/KI), § 2 BORA (Verschwiegenheit), den Zeugnisverweigerungsrechten nach § 53 StPO und den Beschlagnahmeverboten nach § 97 StPO vereinbar ist. Gleiches gilt sinngemäß für andere freie Berufe mit eigenem Berufsrecht (StBerG für Steuerberater:innen, WPO für Wirtschaftsprüfer:innen, ÄrztInnen, Notar:innen, Patentanwält:innen u. a.).
- Datenschutz — DSGVO, BDSG. Es wird nicht beurteilt, ob die Verarbeitung personenbezogener Daten DSGVO-konform ist, ob eine ausreichende Rechtsgrundlage (Art. 6, 9 DSGVO) vorliegt, ob ein Auftragsverarbeitungsvertrag nach Art. 28 DSGVO geschlossen werden muss, ob eine Datenschutz-Folgenabschätzung (Art. 35 DSGVO) erforderlich ist oder ob die Informationspflichten nach Art. 13, 14 DSGVO erfüllt sind. Arbeitszeugnisse enthalten typischerweise personenbezogene Daten besonderer Kategorien.
- KI-Verordnung (KI-VO / EU AI Act, VO (EU) 2024/1689). Es wird nicht entschieden, ob der Einsatz unter eine der Hochrisiko-Kategorien nach Art. 6 KI-VO in Verbindung mit Anhang III KI-VO fällt (insbesondere Zugang zur Justiz, Beschäftigungskontext), ob Transparenzpflichten nach Art. 50 KI-VO greifen, ob es sich um ein General-Purpose-AI-Modell nach Art. 51 ff. KI-VO handelt und welche Pflichten als Betreiber (Art. 26 KI-VO) zu erfüllen sind.
- Beschlagnahmeverbote und auslandsrechtliche Zugriffe. Es wird nicht geprüft, ob Eingabedaten und Modellantworten gegen Beschlagnahme nach §§ 97, 160a StPO, gegen US Cloud Act, FISA § 702, CLOUD Act warrants, PATRIOT Act § 215 oder sonstige extraterritoriale Zugriffsbefugnisse hinreichend geschützt sind. Dafür ist die jeweilige Nutzerin / der jeweilige Nutzer allein verantwortlich.
- Zugang, Auftragsverarbeitung, Hosting. Wie der API-Zugang zum Modell beschafft wird (Anthropic direkt, AWS Bedrock, Google Vertex, eigenes Hosting), ob mit dem Anbieter ein Auftragsverarbeitungsvertrag geschlossen wird, ob ein berufsrechtskonformer Cloud-Vertrag vorliegt und ob die Anforderungen an die Verschwiegenheit / Mandatsgeheimnis und Datenflusskontrolle in der konkreten Deployment-Konstellation eingehalten sind, bleibt vollständig in der Eigenverantwortung der Nutzerin / des Nutzers.

Anwältinnen, Anwälte und andere Berufsgeheimnisträgerinnen/-träger müssen vor jeder produktiven Nutzung selbst prüfen, ob die konkrete Anbieter-, Hosting- und Datenflusskonstellation mit Mandatsgeheimnis, Berufsrecht und Datenschutz vereinbar ist. Dieses Repository bestätigt keinen Anbieter und ersetzt keine Prüfung von § 203 StGB, § 43e BRAO, Art. 28 DSGVO, Kapitel V DSGVO, TOMs, Löschkonzept, Audit-Rechten, Subunternehmern, Datenresidenz und vertraglicher Verschwiegenheit.

## Lizenz

Dual licensed: Apache-2.0 OR MIT — siehe [LICENSE-APACHE](LICENSE-APACHE) und [LICENSE-MIT](LICENSE-MIT).
