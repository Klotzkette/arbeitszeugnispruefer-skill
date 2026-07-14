# Changelog

Alle nennenswerten Änderungen an diesem Skill werden hier festgehalten.
Das Format orientiert sich an [Keep a Changelog](https://keepachangelog.com/de/1.1.0/);
die Versionierung folgt [Semantic Versioning](https://semver.org/lang/de/).
Die Versionsnummer steht zugleich sichtbar am Anfang von `skill/SKILL.md` und `skill/SKILL-mini.md`.

## [Unreleased]

## [3.0.22] — 2026-07-15

### Behoben
- 100 weitere konkrete Fehler-, Risiko-, Stabilitäts- und Reibungspunkte in
  `QUALITY-AUDIT-100.md` erfasst, behoben und durch eine exakte 1-bis-100-
  Regression abgesichert.
- One-Shot-Ausführung auf ein gemeinsames Satz-/Evidenzregister umgestellt:
  Zeugnis nur einmal einlesen, Wiederholungen gruppieren und Kurzbefund,
  Erklärung/Mandantenschreiben sowie geschuldetes Gegenseitenschreiben vor der
  langen Detailmatrix fertigstellen.
- Quellenannahme für PDF, Scan, Foto und Batch gehärtet: Seitenzahl,
  Reihenfolge, Dokumentgrenzen und OCR-Unsicherheiten werden geprüft;
  Briefkopf, Stempel und Unterschrift nur am Originalbild bewertet und
  OCR-Fehler nicht als Zeugnisfehler ausgegeben.
- Weitere Bewertungsautomatismen entfernt: Verhaltensreihenfolge ist keine
  feste Rechtsregel, fehlende Pünktlichkeits- oder Loyalitätsformeln sind kein
  pauschaler Mangel, neutrale Beendigungsdaten kein Kündigungscode und sensible
  Kontextsignale keine Tatsachen über Krankheit, Konflikte oder Integrität.
- Notenskala in Voll- und Mini-Fassung auf 1 bis 5 vereinheitlicht und
  Geburtsdaten aus den Vollskill-Musterzeugnissen entfernt.
- PDF-Normalisierung nach Artefakttyp abgesichert: `cupsfilter`-Einzeldateien
  müssen genau zwei Datumsfelder, `pdfunite`-Sammeldokumente genau null
  enthalten. Damit wurde zugleich ein im ersten Testlauf aufgedeckter
  Sammel-PDF-Regressionsfehler beseitigt.
- ZIP- und Prüfsummenprüfung erkennt nun CRC-Fehler, doppelte, leere oder
  unsichere Einträge, falsche Reihenfolge, fehlerhafte SHA-256-Syntax sowie
  Textdateien mit BOM, CRLF oder fehlender Schlusszeile.
- 30-Punkte-Bug-Hunt durch Rechtslogik, Bewertungsmatrix, Sprachkataloge,
  Musterschreiben, Klageantrag, Ausbildungsmodul, Musterfälle und technische
  Prüfroutine. Ampel, Notentendenz und Durchsetzbarkeit sind jetzt getrennte
  Größen; Orange löst nicht mehr automatisch ein Anspruchsschreiben aus.
- Autonome Ausgabe dreistufig gehärtet: belastbarer Rechtsmangel führt zum
  Berichtigungsverlangen, ein ausschließlich freiwilliger Wunsch nur zur
  ausdrücklich unverbindlichen Änderungsbitte ohne Klageandrohung, fehlender
  Handlungsbedarf zu keinem Gegenseitenschreiben.
- Codewort-, Adverb-, Drift-, Negations- und Auslassungskataloge von
  unzulässigen Tatsachen-, Absichts- und Festnotenautomatismen befreit. BAG
  9 AZR 386/10 wird nun auch methodisch umgesetzt: Codeangaben sind
  kontextabhängige Prüfhypothesen und keine gerichtliche Phrase-zu-Note-Liste.
- Interne Bewertungswidersprüche beseitigt, insbesondere bei „stets
  einwandfrei", Schlussformel-Bausteinen, Fortbildungs-/Lernformulierungen,
  Gesamtformel ohne „stets" sowie dem zusammengesetzten Satz „stets bemüht,
  … zur vollen Zufriedenheit zu erledigen".
- Formalprüfung präzisiert: tatsächlicher Beschäftigungszeitraum statt
  pauschaler Karenz-/Abwesenheitsnennung, Tippfehler nach objektiver Relevanz,
  Unterzeichner nach Funktion und Weisungsbefugnis sowie Beendigungsdatum im
  Zeugnistext getrennt vom tatsächlichen Ausstellungsdatum.
- Gegenseiten- und Klagemuster datensparsamer und beweisgebunden gefasst:
  kein Geburtsdatum als Standard, keine erfundene Spitzennote, kein
  ungeprüfter Kundenbezug und keine freiwillige Schlussformel im
  Leistungsantrag.
- Ausbildungsmodul an § 16 Abs. 2 BBiG angeglichen: Eine
  Berufsschulbewertung ist kein automatischer Mindestinhalt. Branchenübliche
  Auslassungen bleiben nach BAG 9 AZR 632/07 konkrete Kontextfragen.
- Sachfremde und rollenwidersprüchliche Zusatzakte „Blühendes Leben"
  vollständig durch einen konsistenten Zeugnisworkflow mit Tatsachenblatt,
  Matrix, Beweisgate, Mandantenerklärung und Arbeitgeberanschreiben ersetzt.
- Mini-Skill bildet dieselben Schutzschranken unter 7.500 Zeichen ab und nennt
  Rechtschreibung/Format sowie BAG 9 AZR 262/20 und 9 AZR 386/10 ausdrücklich.
- Integritätscheck erfasst jetzt auch undatierte Aktenzeichen im gesamten
  Markdown-/HTML-Bestand und sperrt die wichtigsten beseitigten
  Rechts- und Bewertungsautomatismen als Regressionen.

### Geändert
- BAG 28.01.2025 – 9 AZR 48/24 als aktuelle Bestätigung der Holschuld für
  Arbeitspapiere ergänzt, zugleich aber ausdrücklich auf den dort entschiedenen
  Gegenstand digitale Entgeltabrechnung begrenzt; die Entscheidung ersetzt bei
  Arbeitszeugnissen weder Einwilligung noch qualifizierte elektronische Signatur.
- Testakten-Build beschleunigt: beide Aktenpakete sowie deren Einzel-PDFs
  werden mit begrenzter Parallelität gebaut; Hashes werden gestreamt.
  Integritätschecks cachen wiederholte Lese-/Hashvorgänge, prüfen Gesamt-PDFs
  parallel und bieten eine kompakte Standardausgabe sowie `--quick` und
  `--verbose`.
- Rechtsprechungs-Audits vom 12. und 14.07.2026 gegen die amtliche BAG-Datenbank und
  gerichtseigene Landesportale: LAG Köln 05.12.2024 – 6 SLa 25/24 als direkten
  Anker für tatsächliches Ausstellungsdatum und Grenzen der Rückdatierung
  ergänzt.
- Verwirkungsprüfung mit BAG 11.12.2014 – 8 AZR 838/13 gehärtet: Zeit- und
  Umstandsmoment sind kumulativ erforderlich; bloßes Zuwarten ist keine feste
  Monatsfrist und trägt für sich keinen Anspruchsverlust.
- Schlussformel-Rechtsfolgen aus BAG 11.12.2012 – 9 AZR 227/11 und BAG
  06.06.2023 – 9 AZR 272/22 klar getrennt: regelmäßig nur Entfernung statt
  Wunschtext, Wiederaufnahme nur bei maßregelnder Streichung; objektive
  Tatsachenangaben bleiben gesondert berichtigungsfähig.
- BAG 12.02.2013 – 3 AZR 121/11 präzisiert: Im entschiedenen isolierten
  Umschulungsverhältnis galt § 630 BGB; § 109 GewO bleibt die statusabhängige
  Alternative bei Umschulung im Arbeitsverhältnis.
- Verzugsmodul präzisiert: Erst eine nachweisbar zugegangene Aufforderung
  dokumentiert Verlangen und Fristablauf; ein bloßes Kalenderdatum beweist den
  Zugang einer Mahnung nicht und ersetzt keine Verzugsvoraussetzung.
- Die Holschuld aus BAG 08.03.1995 – 5 AZR 848/93 ausdrücklich auf die
  körperliche Papierurkunde begrenzt und von Übermittlung/Zugang eines wirksam
  mit Einwilligung elektronisch erteilten Zeugnisses getrennt.
- Mini-Skill bei der Datumsprüfung mit Vollversion harmonisiert: Ein späteres
  tatsächliches Ausfertigungsdatum ist nicht schematisch als Mangel zu werten.

### Geprüft
- Alle vorhandenen BAG-, LAG- und ArbG-Fundstellen auf Gericht, Datum,
  Aktenzeichen und tragende Zuordnung geprüft; keine erfundene oder falsch
  datierte Entscheidung festgestellt.
- Die bis 14.07.2026 veröffentlichte BAG-Entscheidungsliste erneut durchsucht;
  8 AZB 25/25 bleibt die jüngste unmittelbar einschlägige Entscheidung und ist
  bereits zutreffend verarbeitet.
- Sämtliche drei Codex-Automatic-Review-Hinweise erneut kontrolliert; sie sind
  im aktuellen Stand umgesetzt. Für die präzisierten Fundstellen wurden neue
  Zuordnungs-Regressionstests ergänzt.

## [3.0.21] — 2026-07-11

### Geändert
- Root-README um einen vollständigen Direktdownload-Katalog aller neun
  Release-Assets und eine kurze Auswahlhilfe für Vollskill, Mini-Skill,
  Einzeltest, Batch-Test, Prüfsummen und Projektarchiv erweitert.
- Repository-Landkarte vervollständigt; insbesondere der zuvor nur indirekt
  erreichbare Helfer für reproduzierbare PDF-/ZIP-Artefakte ist nun direkt
  verlinkt.
- Alle drei Testakten-READMEs führen jetzt einheitlich zur Release-Übersicht
  und zu den Prüfsummen und markieren die jeweils geöffnete Akte eindeutig.
- Pages-Schnellzugriff bündelt sämtliche Release-Dateien mit echten
  Downloadattributen. Repository-Wegweiser, Seitennavigation und beide
  Downloadhilfen erhielten zusätzliche direkte Rückwege zu Quelltext,
  Releases, Prüfsummen, Skripten und Lizenzen.
- Beschreibung der One-Shot-Ausgabe in README und Pages mit dem Skill
  synchronisiert: direkte Erklärung bei Selbstprüfung, anwaltliches
  Mandantenschreiben bei Kanzleiprüfung.

### Geprüft
- Neuer Navigations-Regressionscheck prüft den vollständigen Downloadkatalog,
  Downloadattribute, zentrale Repository-Ziele sowie die Querverlinkung aller
  README- und Downloadhilfeseiten.
- Fachlogik und Rechtsanker bleiben unverändert; Voll- und Mini-Skill sind mit
  ihren Pages-Spiegeln byte-identisch und die Mini-Fassung bleibt unter 7.500
  Zeichen.

## [3.0.20] — 2026-07-11

### Behoben
- Fiesen Generatorfehler beseitigt: Ein dokumentierter Testakten-Neubau
  überschrieb die kuratierten Jura-/Wissenschafts- und Leitungs-READMEs mit
  älteren Vorlagen und änderte bei unverändertem Inhalt sämtliche erzeugten
  PDF-/ZIP-Dateien durch Zeitstempel, zufällige PDF-IDs und ZIP-Metadaten.
- Builder löschen nur noch ihre erzeugten Fallordner und Artefakte; Navigation,
  Direktdownloads und redaktionelle Ergänzungen in den Testakten-READMEs bleiben
  bei jedem Neubau erhalten.
- PDF-Zeitstempel und Datei-IDs sowie Reihenfolge, Zeitstempel und Dateimodus der
  ZIP-Einträge werden kanonisiert. `--verify-reproducible` baut zweimal und
  bricht bei jedem Byte-Unterschied oder einer README-Veränderung ab.
- One-Shot-Ausgabe unterscheidet jetzt ausdrücklich zwischen verständlicher
  Erklärung bei Selbstprüfung und anwaltlichem Mandantenschreiben bei
  Kanzleiprüfung; Gegenseite und Anspruchsnorm bleiben statusrichtig.

### Geprüft
- Sämtliche drei Codex-Automatic-Review-Hinweise des Repositories erneut
  ausgewertet: Rollen-Gate, § 109 Abs. 2 für jedes Zeugnis sowie Wahrheit und
  Wohlwollen in der Mini-Fassung sind umgesetzt und nun durch ausdrückliche
  Regressionstests geschützt.
- Zwei vollständige Generatorläufe ergaben 27 byte-identische Dateien; alle 15
  erzeugten Einzel-PDFs, beide Gesamt-PDFs und beide ZIP-Pakete wurden neu
  erstellt und in die Pages-Downloads gespiegelt.
- Voll- und Mini-Skill bleiben mit den Pages-Spiegeln byte-identisch; die
  Mini-Fassung bleibt unter 7.500 Zeichen.

## [3.0.19] — 2026-07-11

### Geändert
- Root-README mit kompakter Hauptnavigation, eindeutig getrennten Download- und
  Ansichtslinks sowie einer klickbaren Repository-Landkarte neu geordnet.
- Alle drei Testakten-READMEs mit einheitlicher Quernavigation, direkten
  Release-Downloads für ZIP/Gesamt-PDF und separaten Vorschau-/Downloadlinks
  für jedes der 25 Einzel-PDFs ausgestattet.
- Pages-Startseite um Sprungmenü und README-Wegweiser ergänzt; beide
  Download-Zwischenseiten führen nun zu Schwester-Skill, Testakten,
  Haupt-README und Downloadübersicht zurück.
- Integritätscheck prüft jetzt sämtliche lokalen Markdown-Ziele sowie interne
  und dateiübergreifende HTML-Menüanker.
- Rechtsprechungs- und Normenaudit gegen amtliche Quellen: Datum von BAG
  9 AZR 8/15 berichtigt, LAG Hamm 12 Ta 475/16 (ironische Übererfüllung) und
  4 Ta 118/16 (Unterschrift) sauber getrennt sowie 9 Ta 319/25 (Briefkopf)
  ergänzt; BAG 9 AZR 248/07 ist nun der direkte Anker für die Bindung des
  Endzeugnisses an ein Zwischenzeugnis.
- Rechtsstatus-Gate in Voll- und Mini-Skill geschärft: § 109 GewO für
  Arbeitnehmer-Endzeugnisse, § 630 BGB für sonstige dauernde
  Dienstverhältnisse, §§ 16, 26 BBiG für Berufsausbildung und bestimmte
  andere Lernverhältnisse sowie § 241 Abs. 2 BGB für Zwischenzeugnisse bei
  triftigem Grund; Organpersonen erhalten eine
  gesonderte Rechtsweg- und Kostenprüfung nach §§ 2, 5, 12a ArbGG.
- Rollenlogik von Rechtsstatus getrennt: In One-Shot-Fällen erhält die
  beurteilte Person das Korrekturschreiben an Arbeitgeber, Dienstgeber oder
  Ausbildende; HR-/Arbeitgeberrollen erhalten weiterhin nur den neutralen
  Korrekturvermerk.
- Unpassende oder überbreite Rechtsanker entfernt bzw. präzisiert, darunter
  § 288 BGB als pauschale Verzugsgrundlage, § 13 BBiG im Zeugnisblock und die
  pauschale Zuordnung besonderer Datenkategorien zu jedem Arbeitszeugnis.
- Integritätscheck um 26 kanonische Entscheidungsdaten, zentrale Normanker
  und Regressionstests gegen bekannte Fehlzuordnungen erweitert.
- Skill-Frontmatter, aktuelle Versionshinweise und die Trennung von Rolle und
  Rechtsstatus werden jetzt als eigene Release-Invarianten geprüft.
- Schreibender Pages-Synchronisationsworkflow durch eine strikt lesende
  Integritätsprüfung für Pull Requests und `main` ersetzt; ein Release-Tag kann
  dadurch nicht mehr von einem nachgelagerten Bot-Commit überholt werden. Die
  verwendeten offiziellen Actions sind auf Node-24-kompatible Hauptversionen
  aktualisiert und werden gegen einen Versionsrückfall geprüft.
- Downloadseite um amtliche Rechtsquellen und statusrichtige One-Shot-Hinweise
  ergänzt; README, Downloadhilfen und Testakten-Navigation vereinheitlicht.

### Geprüft
- Alle 26 Entscheidungsdaten und ihre Kernaussagen gegen amtliche oder
  gerichtseigene Quellen abgeglichen; bekannte Fehlzuordnungen sind durch
  Regressionstests gesperrt.
- Voll- und Mini-Fassung sind mit den Pages-Spiegeln byte-identisch; sämtliche
  lokalen Links und Anker lösen auf, die Mini-Fassung bleibt unter 7.500 Zeichen.
- Neun Release-Assets werden vor und nach Veröffentlichung nach Name, Größe und
  SHA-256-Inhalt geprüft; der Release-Tag muss auf dem aktuellen `main` liegen.

## [3.0.18] — 2026-07-09

### Geändert
- Notenmatrix anhand BAG 18.11.2014 – 9 AZR 584/13 korrigiert:
  „stets zu unserer Zufriedenheit" wird in der Vollfassung als Note 3
  eingeordnet; die Mini-Fassung trennt „im Großen und Ganzen zu unserer
  Zufriedenheit" (Note 5) wieder sauber von „bemüht" (Note 4 bis 5).
- Klagbarkeits- und Beweislasttabelle juristisch präzisiert: Die BAG-Notenregel
  gilt für die zusammenfassende Leistungsbewertung und wird nicht mehr
  schematisch auf Tatsachen-, Klarheits-, Auslassungs- oder Formmängel
  übertragen.
- Falsche Beweislastaussage im Drift-Muster berichtigt und ausgabenahe
  Mustertabellen konsequent auf Ampelsymbole 🔴/🟠/🟢 umgestellt.
- Nach-Release-Prüfung vergleicht veröffentlichte GitHub-Assets zusätzlich per
  SHA-256 mit den lokalen Dateien und stellt sicher, dass der Release-Tag auf
  dem aktuellen `main`-Commit liegt.
- README und Downloadseite erklären den lokalen Prüfsummenabgleich unter Linux
  und macOS; Versionsbump auf 3.0.18 in Voll- und Mini-Skill sowie Pages-Spiegel.
- Nicht standardkonformes `version`-Feld aus dem YAML-Frontmatter entfernt; die
  Versionsangabe steht nun sichtbar unter der jeweiligen Überschrift, sodass
  Voll- und Mini-Datei als Skill validierbar bleiben.

### Geprüft
- Normtext des § 109 GewO und BAG-Leitlinien zu Notenskala, Beweislast,
  objektivem Empfängerhorizont und Auslassungen erneut anhand amtlicher Quellen
  abgeglichen.
- Mini-Fassung bleibt unter 7.500 Zeichen; lokale und veröffentlichte Assets
  werden nach dem Release auf Name, Größe und SHA-256-Inhalt geprüft.

## [3.0.17] — 2026-07-08

### Geändert
- Release-Paket um `SHA256SUMS.txt` ergänzt; die Datei enthält SHA-256-Werte
  für Vollskill, Mini-Skill sowie alle PDF-/ZIP-Testakten-Assets.
- Integritätscheck prüft nun, ob `SHA256SUMS.txt` exakt zu den lokalen
  Release-Kandidaten passt, und bezieht die Prüfsummenliste in die
  GitHub-Release-Asset-Prüfung ein.
- README und Downloadseite verlinken die Prüfsummenliste sichtbar neben den
  übrigen Download- und Release-Artefakten.
- Versionsbump auf 3.0.17 in Voll- und Mini-Skill; docs-Spiegel, README und
  Release-Check-Hinweis aktualisiert.

### Geprüft
- Lokaler Integritätscheck deckt Versionen, Spiegeldateien, Mini-Limit,
  interne Anker, lokale HTML-Links, Prüfsummen, PDF-/ZIP-Sanity und
  Release-Kandidaten ab.

## [3.0.16] — 2026-07-08

### Geändert
- Mini-Fassung als eigenständigen Kurzprompt geschärft: Sie verlangt nun
  ausdrücklich Satzmatrix, Notenspanne, Mandantenerklärung in normaler Sprache
  und ein ausformuliertes Schreiben an Arbeitgeber/Gegenseite.
- README und Downloadseite stellen klarer heraus, dass `SKILL-mini.md` unter
  7.500 Zeichen bleibt und per einem Klick als Markdown-Datei herunterladbar ist.
- Versionsbump auf 3.0.16 in Voll- und Mini-Skill; docs-Spiegel, README und
  Release-Check-Hinweis aktualisiert.

### Geprüft
- Mini-Fassung bleibt unter 7.500 Zeichen; `skill/` und `docs/` sind
  byte-identisch spiegelbar; direkte Download- und Release-Fallback-Logik bleibt
  unverändert.

## [3.0.15] — 2026-07-07

### Geändert
- Finaler Bug-Hunt nach Version 3.0.14 mit Fokus auf echten Zugriff,
  Release-Assets und hängerarme Nachprüfung.
- Download-Startseiten für Voll- und Mini-Fassung um direkte Fallback-Links auf
  `releases/latest/download/...` ergänzt, falls eine Umgebung den GitHub-Pages-
  Download blockiert.
- Release-Integritätscheck um `--github-release TAG` erweitert: Nach dem
  Veröffentlichen prüft das Skript den realen GitHub-Release auf Tag,
  Zielbranch, Draft-/Prerelease-Status, erwartete Asset-Namen und Dateigrößen.
- README und Pages-Wartungshinweise um die neue Nach-Release-Prüfung ergänzt.
- Versionsbump auf 3.0.15 in Voll- und Mini-Skill; README und Download-Seite
  aktualisiert.

### Geprüft
- Aktuelle BAG-/Normenlage erneut gegen frei verfügbare Primärquellen
  plausibilisiert; keine neue größere Zeugnisrecht-Umsteuerung gegenüber
  3.0.14 festgestellt.

## [3.0.14] — 2026-07-07

### Geändert
- Finaler Bug-Hunt und Usability-Sweep nach Version 3.0.13.
- README und Download-Seite um den direkten Weg zum neuesten GitHub-Release
  ergänzt; neue Releases tragen die freistehenden Markdown-Dateien und die
  Testakten-PDFs/-ZIPs als versionierte Assets.
- Freistehende Nutzung und Fortsetzungslogik leicht geschärft: kleine Modelle
  sollen bei Bedarf auf die Mini-Fassung ausweichen und in langen One-Shot-Läufen
  zuerst Pflichtblöcke fertigstellen, bevor optionale Vertiefungen beginnen.
- Build- und Prüfskripte gegen hängende externe Prozesse gehärtet
  (`cupsfilter`, `pdfunite`, `pdfinfo`, `pdftotext` laufen nun mit Timeouts).
- Release-Integritätscheck prüft zusätzlich, ob alle lokalen Kandidaten für den
  Release-Upload vorhanden und nicht leer sind.
- Versionsbump auf 3.0.14 in Voll- und Mini-Skill; README und Download-Seite
  aktualisiert.

### Geprüft
- Testakten-Artefakte wurden reproduzierbar neu gebaut und in `docs/testakten/`
  gespiegelt.
- Gesetzesanker und aktuelle BAG-Anker aus 3.0.13 bleiben anhand frei
  verfügbarer Primärquellen stimmig; keine neue größere Zeugnisrecht-Umsteuerung
  gegenüber dem vorherigen Stand festgestellt.

## [3.0.13] — 2026-07-07

### Geändert
- Finaler Bug-Hunt und Kohärenz-Sweep durch Voll- und Mini-Fassung.
- BAG 07.05.2026 – 8 AZB 25/25 in der Vollversion näher am Leitsatz
  formuliert: Entwurfsklausel mit Abweichung nur aus wichtigem Grund ist
  vollstreckbar, bleibt aber durch Zeugniswahrheit und Zeugnisklarheit begrenzt.
- Mini-Fassung um den komprimierten Entwurfsklausel-/Vollstreckungsanker
  ergänzt, ohne das 7.500-Zeichen-Limit zu überschreiten.
- Notenlogik zu „bemüht" von einem starren Note-5-Automatismus auf eine
  realistischere Spanne 4 bis 5 gehärtet.
- Sozialverhaltens-Reihenfolge als rollenbewusster Regelfall statt als
  schematische Pflicht formuliert; Beweislasttabelle entsprechend präzisiert.
- Kleine sprachliche Glättung im roten Musterzeugnis.
- Versionsbump auf 3.0.13 in Voll- und Mini-Skill; README und Download-Seite
  aktualisiert.

### Geprüft
- Gesetzesanker (§ 109 GewO, § 16 BBiG) und aktuelle BAG-Anker
  2 AZR 96/24 (B) sowie 8 AZB 25/25 gegen frei verfügbare Primärquellen
  gegengeprüft.

## [3.0.12] — 2026-07-06

### Geändert
- Root-README mit Schnellzugriff, klarerer Testaktenübersicht und sortierter
  Skript-/Release-Check-Tabelle überarbeitet.
- Alle drei Testakten-READMEs vereinheitlicht: öffentliche Downloads,
  Repository-Dateien, Einzel-PDFs, Prüffokus und typische Arbeitsaufträge sind
  nun direkt verlinkt.
- GitHub-Pages-Downloadseite um Schnellzugriff, Repository-Detailverweise und
  Wartungs-/Release-Links ergänzt.
- Versionsbump auf 3.0.12 in Voll- und Mini-Skill; README und Download-Seite
  aktualisiert.

### Geprüft
- README- und Pages-Links sind in die bestehende Integritätsprüfung
  einbezogen; `skill/` und `docs/` bleiben byte-identisch.

## [3.0.11] — 2026-07-06

### Hinzugefügt
- Neues Sammelskript `scripts/build_generated_testakten.py`, das alle
  generierten Testakten-Artefakte aus den vorhandenen Buildern neu erzeugt.

### Geändert
- Release-Integritätscheck prüft nun die Gesamt-PDFs aller drei Testakten-Sätze
  tiefgehend, einschließlich der ursprünglichen allgemeinen Branchenakte:
  PDF-Metadaten, Nichtverschlüsselung, Mindestseitenzahl, Zeugnisüberschriften
  und bei der allgemeinen Akte zusätzlich die zehn PDF-Anhang-Marker.
- README-Abschnitt zur Qualitätssicherung um das zentrale Build-Kommando für
  generierte Testakten ergänzt.
- Versionsbump auf 3.0.11 in Voll- und Mini-Skill; README und Download-Seite
  aktualisiert.

### Geprüft
- Zentrale Testakten-Generierung läuft erfolgreich.
- Voller Integritätscheck läuft erfolgreich; Mini-Fassung bleibt unter
  7.500 Zeichen; `skill/` und `docs/` sind byte-identisch.

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

[3.0.22]: https://github.com/Klotzkette/arbeitszeugnispruefer-skill/releases/tag/v3.0.22
[3.0.21]: https://github.com/Klotzkette/arbeitszeugnispruefer-skill/releases/tag/v3.0.21
[3.0.20]: https://github.com/Klotzkette/arbeitszeugnispruefer-skill/releases/tag/v3.0.20
[3.0.19]: https://github.com/Klotzkette/arbeitszeugnispruefer-skill/releases/tag/v3.0.19
[3.0.18]: https://github.com/Klotzkette/arbeitszeugnispruefer-skill/releases/tag/v3.0.18
[3.0.17]: https://github.com/Klotzkette/arbeitszeugnispruefer-skill/releases/tag/v3.0.17
[3.0.16]: https://github.com/Klotzkette/arbeitszeugnispruefer-skill/releases/tag/v3.0.16
[3.0.15]: https://github.com/Klotzkette/arbeitszeugnispruefer-skill/releases/tag/v3.0.15
[3.0.14]: https://github.com/Klotzkette/arbeitszeugnispruefer-skill/releases/tag/v3.0.14
[3.0.13]: https://github.com/Klotzkette/arbeitszeugnispruefer-skill/releases/tag/v3.0.13
[3.0.12]: https://github.com/Klotzkette/arbeitszeugnispruefer-skill/releases/tag/v3.0.12
[3.0.11]: https://github.com/Klotzkette/arbeitszeugnispruefer-skill/releases/tag/v3.0.11
[3.0.10]: https://github.com/Klotzkette/arbeitszeugnispruefer-skill/releases/tag/v3.0.10
[3.0.9]: https://github.com/Klotzkette/arbeitszeugnispruefer-skill/releases/tag/v3.0.9
[3.0.8]: https://github.com/Klotzkette/arbeitszeugnispruefer-skill/releases/tag/v3.0.8
[3.0.7]: https://github.com/Klotzkette/arbeitszeugnispruefer-skill/releases/tag/v3.0.7
[3.0.6]: https://github.com/Klotzkette/arbeitszeugnispruefer-skill/releases/tag/v3.0.6
[3.0.5]: https://github.com/Klotzkette/arbeitszeugnispruefer-skill/releases/tag/v3.0.5
[3.0.4]: https://github.com/Klotzkette/arbeitszeugnispruefer-skill/releases/tag/v3.0.4
