# 1. Prüfung des großen Arbeitsbuchs vom 8. Oktober 2026

Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.

This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

## 1.1. Gegenstand und Grenzen

Die große Einzeldatei wurde von rund 26.700 auf 50.644 Wörter erweitert. Neu sind vier eingebettete Kapitel: plattformübergreifender Arbeitsablauf; Leistungs- und Verhaltensbewertung; Schlussformeln, Bindung und Status; Form, Fristen und Durchsetzung. Der Umfang ist als Wortzahl gemessen, nicht als feste Seitenzahl eines nicht erstellten Word- oder PDF-Dokuments.

Die juristischen Fachkapitel beruhen auf gezielter Volltextrecherche am 8. Oktober 2026. Aussage, Anwendungsgrenze, Quellenstatus und eigene Arbeitshilfen sind getrennt. Das ist keine vollständige Erfassung sämtlicher Rechtsprechung und keine pauschale Neuverifikation aller älteren Kurzbelege. Die Recherche und der Gegencheck waren KI-gestützt; eine unabhängige menschliche fachliche Abnahme wird nicht behauptet.

## 1.2. Tatsächlich ausgeführte Dialogproben

1. [Anwaltlicher Vollauftrag, zwei Runden](probe-voll-dialog.md): Zunächst offene Bonusgrundlage, gewünschte Aufwertung von ausreichend auf gut und freiwillige Schlussformel. Nach tatsächlicher Antwort und Beschränkung auf befriedigend folgten ein kurzer Mandantenbrief, der vollständige Arbeitgeberbrief und eine getrennte ausführliche rechtliche Begründung. Der allgemeine Weihnachtsbonus wurde nicht als individueller Leistungsbeleg verwendet; der zurückgenommene Bedauernswunsch blieb draußen.
2. [Begrenzter Word-Zugriff, drei Runden](probe-word-dialog.md): Zunächst nur eine markierte Tätigkeitsbeschreibung. Keine Gesamtnote aus dem Absatz; konkrete Fragen zu Zeitraum, Befugnissen und Belegen. Nach vollständigem Text und begrenztem Auftrag folgten Ersatzpassage und Arbeitnehmeranschreiben. Eine semantisch gleichwertige neue Fassung führte zum Abschluss statt zu einem künstlichen weiteren Brief. Diese Probe simuliert die Zugriffslage; sie betätigt kein Word-Add-in.
3. [Mini-Prompt bei Nichterteilung](probe-nichterteilung-mini.md): Alle wesentlichen Angaben lagen vor, aber ein Zeugnis existierte noch nicht. Die tatsächliche Antwort verlangte keinen unmöglichen Upload, sondern lieferte Prüfvermerk, kurzen Mandantenbrief und anwaltliches Erteilungsverlangen. Eine bestimmte Note wurde nicht ohne Tatsachengrundlage vorgegeben. Kein Versand und keine Klage wurden ausgeführt.

Die Voll- und Word-Proben liefen mit einer Zwischenfassung des neuen Arbeitsbuchs. Anschließend wurden die in Abschnitt 1.3 bezeichneten Stellen anhand des Gegenchecks berichtigt. Der Mini-Lauf verwendete bereits die korrigierte endgültige Einstiegsvorgabe. Die Proben belegen die dokumentierten Einzelfallverläufe; sie sind keine repräsentative Modellbenchmark und kein Nachweis identischen Verhaltens jedes fremden Chatbots.

## 1.3. Unabhängiger Gegencheck und Berichtigungen

Ein weiterer Agent prüfte die neuen Fachkapitel und gezielt ihre Vereinbarkeit mit dem Altkatalog. Fünf Befunde wurden umgesetzt und nachgeprüft:

1. BAG 9 AZR 12/03: Beide Vorinstanzen hatten abgewiesen; das BAG verwies auf die Revision des Arbeitnehmers zurück. Der Verfahrensausgang ist berichtigt.
2. Positive Einzelmerkmale und schwache Gesamtformel begründen nicht automatisch einen Widerspruch. Auch zugewiesene Aufgaben können eigenverantwortlich ausgeführt werden.
3. Ein vom Ausfertigungstag abweichendes Zeugnisdatum wird nicht automatisch beanstandet; Datierungspraxis, Erstanfertigung, Berichtigung, Vereinbarung und konkrete Irreführung werden getrennt geprüft.
4. Die vorgelagerten Einstiegsvorgaben einschließlich Mini unterscheiden fehlenden Upload von feststehender Nichterteilung.
5. Der Musterklageantrag verlangt ein vorher rechtlich bestimmtes konkretes Datum; offene Rechtsbedingungen dürfen nicht in den einzureichenden Antrag gelangen.

## 1.4. Technische Prüfungen

- `python3 scripts/check_release_integrity.py`: 412 bestandene Invarianten, einschließlich vier neuer Regressionen zu den genannten Gegencheck-Befunden.
- `python3 scripts/build_handbook.py --check --plugin-root …`: Alle vier Kapitel in Einzeldatei, öffentlicher Kopie, Plugin-Werkstatt und Pluginreferenz synchron.
- `scripts/build_generated_testakten.py --verify-reproducible`: 42 erzeugte Dateien in zwei vollständigen Durchläufen bytegleich. Die vorhandenen 25 Zeugnis-Testfälle wurden nicht inhaltlich verändert.
- Der erste CI-Lauf erkannte, dass der bisherige Sammelpaket-Builder die neue Prüfbericht-README zusätzlich einsammelte. Der Builder ist auf die drei tatsächlichen Zeugnis-Testreihen begrenzt; das bestehende Downloadpaket mit 25 PDFs und neun Begleitdateien bleibt unverändert. Danach wurden beide Builds und die Integritätsprüfung erneut ausgeführt.
- Mini bleibt innerhalb der Grenze von 7.500 Zeichen. Referenzen, Datumszuordnungen, Downloadkopien, Prüfsummen und Links sind maschinell geprüft. Das ersetzt keinen rechtlichen Volltextabgleich oder Modelllauf.

SHA-256 der finalen Vollfassung: `ac4462d3fb02aa4be5ed1037ea3986bb52a4962a7458dbd9b2122c8ebe81dbc9`.

SHA-256 der in der Nichterteilungsprobe verwendeten Mini-Fassung: `3936b2854ab91e5518c146e7c5d882ab7515bce91764f4e54658dde042bcc9dd`.
