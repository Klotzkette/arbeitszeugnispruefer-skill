# Qualitätsaudit: 100 Befunde und Behebungen

Stand: 14.07.2026. Gezählt werden konkrete Fehler, Überdehnungsrisiken, Stabilitätslücken und vermeidbare Reibungspunkte. Die Tabelle ist bewusst maschinenprüfbar; `scripts/check_release_integrity.py` verlangt genau die laufenden Nummern 1 bis 100, eine konkrete Behebung und den Status `Behoben`.

| Nr. | Befund | Behebung | Status |
| --- | --- | --- | --- |
| 1 | Standardmodus war nicht ausdrücklich definiert | Kompaktmodus als vollständigen Standard festgelegt | Behoben |
| 2 | Vollmodus hatte keinen klaren Auslöser | Streit-, Vergleichs-, Klage- und Vertiefungsfälle als Auslöser benannt | Behoben |
| 3 | Batchmodus fehlte als eigene Betriebsart | Getrennte Register und Pakete je Zeugnis vorgeschrieben | Behoben |
| 4 | Moduswahl konnte eine unnötige Rückfrage auslösen | Automatische Moduswahl ohne Rückfrage angeordnet | Behoben |
| 5 | Zeugnis konnte für jeden Ausgabeblock neu analysiert werden | Ein-Pass-Protokoll eingeführt | Behoben |
| 6 | Bewertende Sätze hatten keine stabilen Bezeichner | Satz-IDs S1, S2 und fortlaufend eingeführt | Behoben |
| 7 | Befunde konnten zwischen Bericht und Schreiben driften | Gemeinsames Evidenzregister als einzige Datengrundlage eingeführt | Behoben |
| 8 | Gleichartige Befunde wurden wiederholt | Gruppierung und Deduplizierung angeordnet | Behoben |
| 9 | Widersprüche konnten durch Gruppierung verschwinden | Getrennte Erhaltung widersprüchlicher Sätze vorgeschrieben | Behoben |
| 10 | Volltext konnte in der Antwort wiederholt werden | Volltextwiederholung untersagt | Behoben |
| 11 | Ein Originalsatz konnte mehrfach vollständig zitiert werden | Einmalzitat plus spätere Satz-ID-Verweise eingeführt | Behoben |
| 12 | Live-Recherche konnte für bloße Stilhinweise wiederholt werden | Verifikation auf tragende Rechtsfragen konzentriert | Behoben |
| 13 | Ein einfaches Zeugnis konnte wie ein qualifiziertes benotet werden | Frühabzweig ohne erfundene Leistungs- oder Verhaltensnote eingeführt | Behoben |
| 14 | Fehlerfreies Zeugnis konnte künstliche Streitpunkte erzeugen | Grüner Kurzabschluss ohne Gegenseitenschreiben eingeführt | Behoben |
| 15 | Freiwillige Schlussformel konnte unnötig zur Klageprüfung führen | Eigener Verhandlungszweig ohne Anspruchsbehauptung eingeführt | Behoben |
| 16 | HR-Perspektive wurde erst spät getrennt | Direkter HR-Korrekturvermerk-Zweig eingeführt | Behoben |
| 17 | One-Shot-Schreiben konnten hinter langer Matrix abgeschnitten werden | Zwingende Schreiben vor Detailmatrix angeordnet | Behoben |
| 18 | Fortsetzungsmarke konnte vor Pflichtblöcken erscheinen | Fortsetzung erst nach Kurzbefund und geschuldeten Schreiben erlaubt | Behoben |
| 19 | Kompaktmodus konnte mit unvollständig verwechselt werden | Vollständigkeit bei bloßer Verdichtung ausdrücklich gesichert | Behoben |
| 20 | Statuskopf zeigte Quellenvollständigkeit nicht | Quellenstatus in den Statuskopf aufgenommen | Behoben |
| 21 | Rote Ampel nannte eine nicht verwendete Skala bis Note 6 | Skala auf die im Projekt verwendeten Noten 1 bis 5 vereinheitlicht | Behoben |
| 22 | Matrix erlaubte inkonsistent Noten 1 bis 6 | Matrix auf Notentendenz 1 bis 5 korrigiert | Behoben |
| 23 | Sozialreihenfolge wirkte wie eine feste Rechtsregel | Als Sprachkonvention ohne gesetzlichen oder festen BAG-Code klargestellt | Behoben |
| 24 | Teamintegration wurde pauschal negativ gelesen | Als positive, aber wenig differenzierte Aussage kalibriert | Behoben |
| 25 | Das isolierte Wort bemüht erhielt eine feste Note | Benotung an einen vollständigen Leistungssatz ohne Erfolg geknüpft | Behoben |
| 26 | Das isolierte Wort im Wesentlichen erhielt eine feste Note | Wirkung an den eingeschränkten Gesamtsatz gebunden | Behoben |
| 27 | Kommentarloses Vertragsende galt pauschal als Distanzsignal | Als neutrale Tatsachenangabe eingeordnet | Behoben |
| 28 | Monatsmitte als Ende galt pauschal als Kündigungssignal | Ohne falsches Datum oder Widerspruch als neutral eingeordnet | Behoben |
| 29 | Einvernehmliche Beendigung wurde vorschnell konfliktbezogen gelesen | Neutrale Grundlesart mit Beleggate eingeführt | Behoben |
| 30 | Gesundheitswunsch wurde zu stark als Krankheitscode behandelt | Freundliche Grundlesart und strenges Kontextgate eingeführt | Behoben |
| 31 | Superlative ohne Tatsachenkern galten automatisch als Ironie | Objektiv erkennbare Nicht-Ernstlichkeit als Voraussetzung ergänzt | Behoben |
| 32 | Lob für Selbstverständlichkeiten behauptete eine negative Tatsache | Nur auffällige Schwerpunktsetzung ohne Tatsachenunterstellung zugelassen | Behoben |
| 33 | Kontrast zwischen Überlob und blassem Rest unterstellte Absicht | Als möglicher Konsistenzbruch ohne Motivbehauptung gefasst | Behoben |
| 34 | Fehlende Ehrlichkeitsaussage war pauschal rot | Auf belegte Kassen-, Vermögens- oder Treuhandverantwortung begrenzt | Behoben |
| 35 | Fehlende Pünktlichkeitsaussage im Schichtjob wurde beanstandet | Schematischen Auslassungsbefund entfernt | Behoben |
| 36 | Fehlende Loyalitätsformel bei Führungskräften war pauschal rot | Ohne konkrete Treuhandaufgabe als neutral eingeordnet | Behoben |
| 37 | Fehlendes Kundenwort war pauschal rot | Prägenden Kundenkontakt, Erwartbarkeit und neutrale Erklärung verlangt | Behoben |
| 38 | Fehlende Eigeninitiative war pauschal orange | Eigenständige Kernverantwortung als Voraussetzung ergänzt | Behoben |
| 39 | Fehlende Belastbarkeitsaussage war pauschal rot | Belastungsgeprägte Rolle und negative Gesamtlesart verlangt | Behoben |
| 40 | Warme Schlussformel bei schwacher Leistung erzeugte Gefälligkeitsverdacht | Nur wertungsfreien Konsistenzhinweis beibehalten | Behoben |
| 41 | Negativkonstruktionen konnten einen Vorfall suggerieren | Tatsachenunterstellung ausdrücklich untersagt | Behoben |
| 42 | Musterzeugnis 1 führte unnötig ein Geburtsdatum | Geburtsdatum aus dem Positivmuster entfernt | Behoben |
| 43 | Musterzeugnis 3 führte unnötig ein Geburtsdatum | Geburtsdatum aus dem Negativmuster entfernt | Behoben |
| 44 | Geburtsdatum war nicht als optionaler Inhalt markiert | Datenschutzarme Konsistenzregel ergänzt | Behoben |
| 45 | Branchenabschnitt sprach zu pauschal von Pflichtaussagen | In rollen- und branchenspezifische Kerninhalte umbenannt | Behoben |
| 46 | Allgemeine Loyalitätsaussage erschien als Führungspflicht | Auf konkrete Treuhand- und Vertraulichkeitsaufgaben umgestellt | Behoben |
| 47 | Ausbildungsabschnitt beanstandete fehlende Pünktlichkeit | Diesen erfundenen Standard entfernt | Behoben |
| 48 | Pünktlichkeitslob konnte die eigentliche Azubi-Bewertung ersetzen | Als bloße positive Basisaussage begrenzt | Behoben |
| 49 | Überschrift Geheimcode-Katalog verstärkte Codewortmythen | In Formulierungs- und Kontextkatalog umbenannt | Behoben |
| 50 | Überschrift negative Codeworte verstärkte Tatsachenbehauptungen | In sensible Kontextsignale umbenannt | Behoben |
| 51 | Dateityp wurde im Intake nicht festgehalten | Dateityp als Quellenmerkmal ergänzt | Behoben |
| 52 | Seitenzahl wurde nicht zwingend protokolliert | Seitenzahl in Quellen- und Ein-Pass-Gate aufgenommen | Behoben |
| 53 | Seitenreihenfolge wurde nicht zwingend geprüft | Reihenfolgeprüfung vorgeschrieben | Behoben |
| 54 | Fehlende Seiten konnten unbemerkt bleiben | Vollständigkeitsprüfung und echter Blocker eingeführt | Behoben |
| 55 | Mehrere Zeugnisse konnten vermischt werden | Dokumentgrenzen und getrennte Register vorgeschrieben | Behoben |
| 56 | OCR-Text konnte als Originalwortlaut gelten | Originalbild und OCR ausdrücklich getrennt | Behoben |
| 57 | OCR konnte Schlüsselwörter wie stets oder nicht verfälschen | Visuelle Einzelprüfung unsicherer Schlüsselwörter angeordnet | Behoben |
| 58 | OCR-Fehler konnten als Rechtschreibfehler beanstandet werden | Fehlerarten strikt getrennt | Behoben |
| 59 | Originalfehler konnten still korrigiert werden | Stillschweigende Reparatur zitierter Passagen untersagt | Behoben |
| 60 | Briefkopf konnte allein aus OCR beurteilt werden | Visuelle Originalprüfung verlangt | Behoben |
| 61 | Unterschrift konnte allein aus OCR beurteilt werden | Visuelle Originalprüfung verlangt | Behoben |
| 62 | Stempel konnte allein aus OCR beurteilt werden | Visuelle Originalprüfung verlangt | Behoben |
| 63 | Seitenübergänge konnten verborgen bleiben | Visuelle Übergangsprüfung verlangt | Behoben |
| 64 | Namenswechsel war kein eigener Formalpunkt | Identitäts- und Konsistenzzeile ergänzt | Behoben |
| 65 | Pronomenwechsel war kein eigener Formalpunkt | Pronomenkonsistenz ergänzt | Behoben |
| 66 | Positionswechsel im Text war kein eigener Formalpunkt | Positionskonsistenz ergänzt | Behoben |
| 67 | Datumswechsel im Text war kein eigener Formalpunkt | Datenkonsistenz ergänzt | Behoben |
| 68 | Zielwortlaut konnte ohne Beleg erzeugt werden | Beleg und Zieltext gemeinsam im Evidenzregister geführt | Behoben |
| 69 | Platzhalter konnten zwischen Schreiben abweichen | Gemeinsame Registerquelle für Platzhalter vorgeschrieben | Behoben |
| 70 | Quellenmangel konnte als Vollprüfung ausgegeben werden | Vorläufigkeitskennzeichnung bis zur lesbaren Vollquelle verlangt | Behoben |
| 71 | Beide Testakten-Builder liefen nacheinander | Aggregate Builds parallelisiert | Behoben |
| 72 | Zehn Jura-/Wissenschafts-PDFs liefen nacheinander | Einzel-PDF-Bau parallelisiert | Behoben |
| 73 | Fünf Leitungs-PDFs liefen nacheinander | Einzel-PDF-Bau parallelisiert | Behoben |
| 74 | Parallelität konnte das System überlasten | Workerzahl pro Satz auf vier begrenzt | Behoben |
| 75 | Parallele Builder-Ausgaben könnten sich vermischen | Ausgabe je Builder gepuffert und geordnet ausgegeben | Behoben |
| 76 | Builder-Fehler verloren leicht ihren Kontext | Exitcode, Standardfehler und Scriptname gemeinsam gemeldet | Behoben |
| 77 | Hashing las große Artefakte vollständig in den Speicher | Streaming-SHA-256 mit Ein-MiB-Blöcken eingeführt | Behoben |
| 78 | Integritätscheck las dieselbe Textdatei mehrfach | Unbegrenzten Laufzeitcache für Textlesevorgänge eingeführt | Behoben |
| 79 | Integritätscheck berechnete denselben Digest mehrfach | Digestcache eingeführt | Behoben |
| 80 | Erfolgreicher Check druckte über hundert Einzelzeilen | Kompakte Standardausgabe eingeführt | Behoben |
| 81 | Ausführliche Diagnose war nach der Verdichtung nicht abrufbar | Schalter `--verbose` ergänzt | Behoben |
| 82 | Schneller Editierlauf führte externe PDF-Tools immer aus | Schalter `--quick` ergänzt | Behoben |
| 83 | Fehlende PDF-Werkzeuge erzeugten je Datei dieselbe Warnung | Je Werkzeug nur eine Sammelwarnung ausgegeben | Behoben |
| 84 | Drei Gesamt-PDFs wurden seriell inspiziert | PDF-Metadaten- und Textextraktion parallelisiert | Behoben |
| 85 | PDF-Subprozessfehler erschienen nur als globaler Fehler | Fehler dem betroffenen Aktenpaket und Werkzeug zugeordnet | Behoben |
| 86 | ZIP-CRC wurde nicht geprüft | `testzip`-Prüfung für jedes Testakten-ZIP ergänzt | Behoben |
| 87 | Doppelte ZIP-Einträge wurden nicht erkannt | Eindeutigkeitsprüfung ergänzt | Behoben |
| 88 | ZIP-Pfadtraversal wurde nicht geprüft | Absolute und übergeordnete Pfade verboten | Behoben |
| 89 | Leere ZIP-Einträge wurden nicht erkannt | Dateigröße jedes Eintrags geprüft | Behoben |
| 90 | Kanonische ZIP-Reihenfolge wurde nicht geprüft | Sortierreihenfolge der generierten Archive abgesichert | Behoben |
| 91 | Prüfsummenmanifest akzeptierte unklare Syntax | Striktes SHA-256-Zeilenformat geprüft | Behoben |
| 92 | Prüfsummenmanifest konnte doppelte Namen enthalten | Duplikatprüfung ergänzt | Behoben |
| 93 | Prüfsummenmanifest konnte falsche Reihenfolge haben | Exakten Asset-Satz in kanonischer Reihenfolge verlangt | Behoben |
| 94 | Textdateien konnten BOM oder Mischzeilenenden enthalten | UTF-8-, BOM-, LF- und Abschlusszeilenprüfung ergänzt | Behoben |
| 95 | Betriebssystem- oder Python-Caches konnten eingecheckt werden | Git-basierte Junkdateiprüfung ergänzt | Behoben |
| 96 | PDF-Normalisierung prüfte die Zahl volatiler Daten nicht | Pro Artefakttyp exakt zwei Felder im Einzel-PDF und null im Sammel-PDF verlangt | Behoben |
| 97 | Literal-PDF konnte mehrere IDs unbemerkt enthalten | Eindeutige PDF-ID verlangt | Behoben |
| 98 | ZIP-Helfer akzeptierte doppelte oder externe Eingaben | Eingaben auf Datei, Root, Eindeutigkeit und Nichtleere validiert | Behoben |
| 99 | Die Zahl 100 war nicht regressionsfest | Maschinenprüfung auf genau 1 bis 100 ergänzt | Behoben |
| 100 | Audit, Modi und schnelle Prüfwege waren nicht auffindbar | README- und Downloadnavigation mit Audit und Schnellbefehlen ergänzt | Behoben |
