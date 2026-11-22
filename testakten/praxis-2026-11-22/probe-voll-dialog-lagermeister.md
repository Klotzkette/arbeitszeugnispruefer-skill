Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.

This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

# Nutzungsprobe mit dem vollständigen Zeugnis von Lagermeister Friedhelm Pöttering

Am 22. November 2026 prüfte GPT-6.2-Astra das [einseitige Original der Musterakte 04](../arbeitszeugnis-analyse-bluehendes-leben/04-friedhelm-poettering-lagermeister/Arbeitszeugnis_04-friedhelm-poettering-lagermeister.pdf) in einer frischen Sitzung mit Codex CLI 0.169.0-alpha.11.1. Der anwaltliche Auftrag spielt am 4. Dezember 2025. Das Endzeugnis stammt aus dem Repository. Die Nachreichung, die Mandantenangaben und die späteren Aufträge wurden für diese fiktive Probe verfasst.

## Aufbau des Blindtests

Ausgangspunkt war der veröffentlichte Commit `c3f49469dc1082476076a3df7368aa7918f41dcc`. Die erste Eingabe enthielt die [gesamte Vollfassung 4.1.0](https://github.com/Klotzkette/arbeitszeugnispruefer-skill/blob/c3f49469dc1082476076a3df7368aa7918f41dcc/skill/SKILL.md), den nachstehenden Auftrag, den Textauszug mit `pdftotext -layout` und alle Bildinformationen der als PNG gerenderten PDF-Seite (`pdftoppm -singlefile -r 150 -png`). Die Vollfassung enthält ihre allgemeinen Beispiele. Fallspezifischer Erwartungshorizont, Fallmatrix, Musterkorrespondenz und die nachstehenden Auswertungen gehörten nicht zum Modellkontext. Die Folgeeingaben gingen erst nach Eingang der jeweiligen Antwort über `codex exec resume` an dieselbe Sitzung.

Der Start erfolgte in einem leeren Arbeitsverzeichnis mit `--ignore-user-config --ignore-rules --skip-git-repo-check -s read-only -m gpt-6.2-astra` und Reasoning-Einstellung `low`. Das Laufprotokoll verzeichnete für jede Runde genau eine abgeschlossene Modellantwort und keinen Werkzeugaufruf. Die externe Kontrolle der Rechtsgrundlagen und der Abgleich mit dem Erwartungshorizont erfolgten außerhalb der Testsitzung. Es wurden keine Schreiben versandt.

Die Tabelle nennt die SHA-256-Werte der Eingabedateien und der Antworten aus der CLI. Unten folgt ihr vollständiger Wortlaut. Lediglich horizontale Leerzeichen an Zeilenenden wurden für die Markdown-Wiedergabe entfernt.

| Datei | SHA-256 |
| --- | --- |
| Vollfassung | `13d8b736d485167aa2c82d006a4590a0ee1eba89b9da413e93b1f035a13cbd5c` |
| Original-PDF | `c184fa4298f68bf01fe5a89969ae3821608f2ddded080385db65d1adf7737724` |
| als Bild übergebene Seite | `0e3afdc3c5d65f7a1d48907504e521181d0a8385c127284dc3e2afd62103af30` |
| Text der ersten Eingabe einschließlich Anweisung und Anlagenwortlaut | `e8f493ff93dbd48edc403c99a7c472f76e47d5bacb202fabd119f8488314d2be` |
| Antwort 1 | `15b3665ea1097d2753623b0f52741d5248e4a1fdfde1e1aa0727596841938a07` |
| Eingabe 2 | `23cb8cc70ea1989999a14d1bf73cfcad9a6c2e092c414aaf60f5e351b4ba8829` |
| Antwort 2 | `eefd622913c8b56cd59aa6efadc9fd521686088b2f0428c7758a859c431f921f` |
| Eingabe 3 | `13e95bea745cb330f4f873a3d2f0b77537548272c9bb53044d12da442efd1df3` |
| Antwort 3 | `abee486fe6e250812e7077f0b5be182cad40f42557a5212290ff3e4de6ce974d` |

## Fachliche Auswertung

| Frage | Beobachtung im tatsächlich geführten Dialog |
| --- | --- |
| Was ergibt sich aus dem Endzeugnis allein? | Runde 1 kommt insgesamt auf etwa Note 4. Sie verbindet „stets bemüht“ und „nach Anweisung“ mit der Lagermeisterfunktion und grenzt die Führung von acht Personen vom bloßen Kommunikationsstil ab. Sie erkennt den Widerspruch zwischen dem Beschäftigungsbeginn 2009 und der Bestellung 2016. Das entspricht im Gesamtbild dem [Erwartungshorizont zu Fall 04](../arbeitszeugnis-analyse-bluehendes-leben/90-erwartungshorizont-und-pruefpunkte.md#fall-04-friedhelm-pöttering). Die ausreichende Belastbarkeit und den zurückhaltenden Verhaltensteil benennt der ausführliche Vermerk in Runde 2. |
| Welche Rückfragen ändern die Entscheidung? | Runde 1 fragt nach Wortlaut und Art der früheren Beurteilung, Änderungen bis zum Ausscheiden, tatsächlichen Beanstandungen, Zielnote und Erteilung. Sie bemerkt die fehlende sichtbare Unterschrift auf der Kopie und fragt nach dem Original. Beide Briefe warten auf diese Angaben. |
| Welchen Beweiswert hat die Nachreichung? | Der Mandantenbrief aus Runde 2 erklärt die gute Bewertung und das Risiko der späteren Inventurverzögerung. Der Prüfvermerk trennt den belegten Eingangstag von den offenen Ursachen und Auswirkungen. Das tatsächlich erteilte Zwischenzeugnis stützt die Note 2 bis Ende August. Die Kontinuität im Herbst beruht auf der Angabe des Mandanten. Der private Text mit der Note 1 bleibt aus dem Arbeitgeberbrief heraus. Für das überdurchschnittliche Ziel und den zeitlichen Umfang der Bindung sind [BAG, 18.11.2014, 9 AZR 584/13, Rn. 9–10](https://www.bundesarbeitsgericht.de/entscheidung/9-azr-584-13/) und [BAG, 16.10.2007, 9 AZR 248/07, Rn. 23, Abschrift](https://www.zeugnis-center.de/wp-content/uploads/2016/04/9-AZR-248-07-U-pp.pdf) einschlägig. |
| Welche Form und welcher Termin sind verlangt? | In den Runden 2 und 3 verlangen die Arbeitgeberbriefe nach der tatsächlich unsignierten PDF ohne Einwilligung ein eigenhändig unterschriebenes Papieroriginal. Einen Scan erbitten sie zusätzlich für die Bewerbung. Der 16. Dezember ist als gewünschter Bereitstellungstermin zwei Tage vor der Bewerbung erläutert. [§ 109 GewO](https://www.gesetze-im-internet.de/gewo/__109.html) und [§ 126a BGB](https://www.gesetze-im-internet.de/bgb/__126a.html). |
| Wie wird aus dem ersten Brief der endgültige Entwurf? | Runde 2 schlägt aufgrund des Zwischenzeugnisses eine bessere Verhaltensbeurteilung vor. Erst die dritte Eingabe klärt ausdrücklich, dass der Mandant den Abschnitt beibehalten möchte. Beide neuen Schreiben folgen diesem Wunsch. Der externe Brief verlangt den bisherigen Verhaltens- und Beendigungsabschnitt einschließlich der Wünsche wortgleich. Der eigenständige Führungsabsatz vor „Verhalten“ erhält die belegte Schichtplanung, Anleitung und Teamleistung. |
| Sind die Briefe verwendbar? | Beide Entwurfssätze haben Datum, Betreff, Anrede und Schluss. Der Arbeitgeberbrief hat die Anschrift aus dem Originalzeugnis und konkrete Anträge zu Tätigkeitsbeginn, Zielnote, Führung und Papierform. Die Kanzleisignatur bleibt ein Platzhalter. Die Mandantenbriefe erläutern das persönliche Bewerbungsziel, das Verfahrensrisiko und die ausstehende Versandfreigabe. Kein Arbeitgeberbrief offenbart den privaten Entwurf, die Inventur-E-Mail oder Überlegungen zur Beweisstrategie. |

Diese Probe belegt das Verhalten einer Vollfassung in genau einem fiktiven Mandat. Das Modellergebnis legt weder den Ausgang eines Rechtsstreits noch die Vollständigkeit aller Fallgruppen fest.

## Eingaben und Antworten

### Nutzerinput 1

Vor der Vollfassung stand folgende technische Anweisung:

Verwende die folgende vollständige Anweisung für diesen Zeugnisprüfer. Antworte der Anwältin im Dialog auf ihre Eingabe. Die Akte wird ausschließlich im Dialog übergeben. Benutze keine Tools oder externen Quellen.

Auf die vollständige Anweisung folgte die Nachricht der Anwältin:

Heute ist für dieses Mandat der 4. Dezember 2025. Ich vertrete Herrn Friedhelm Pöttering. Sein vollständiges Endzeugnis liegt als einseitige Kopie vor. Er hält das Bild seiner Leistung und Führung für zu schlecht und möchte sich als Lagerleiter bewerben. Er sagt, dass es eine frühere schriftliche Bewertung gibt. Bitte prüfen Sie das Zeugnis und bereiten Sie den Mandantenbrief und das Schreiben an den früheren Arbeitgeber vor.

Anlage: vollständige Wiedergabe der Kopie, zusätzlich als Bild.

```text
Eisenwarenhandlung Großkopf Söhne KG
  EGS               Industriebedarf · Werkzeuge · Befestigungstechnik
                    Gewerbering 14 · 33334 Gütersloh
                    Telefon 05241 / 22 90 80 · Telefax 05241 / 22 90 89
                    info@großkopf-soehne.de
                    Handelsregister AG Gütersloh HRA 8842




                                                                                                Gütersloh, den 30. November 2025


                                                           Arbeitszeugnis

  Herr Friedhelm Pöttering, geboren am 3. April 1969 in Rietberg, war vom 1. Mai 2009 bis zum 30. November 2025 in
  unserem Betrieb als Lagermeister beschäftigt. Vor seiner Bestellung zum Lagermeister im Jahr 2016 war er bei uns als
  Fachkraft für Lagerlogistik tätig.

  Aufgabenbereich
  Zum Aufgabenbereich von Herrn Pöttering gehörten:

  •   Organisation und Überwachung der Wareneingangs- und Warenausgangsprozesse

  •   Disposition des Hochregallagers sowie der vier Außenlager

  •   fachliche und disziplinarische Führung von sechs Lagermitarbeitern und zwei Auszubildenden

  •   Pflege des Warenwirtschaftssystems und Durchführung der jährlichen Inventur

  •   Sicherstellung der Einhaltung der Arbeitsschutzvorschriften im Lagerbetrieb
  Fachkenntnisse und Arbeitsweise
  Herr Pöttering verfügt über die für seine Tätigkeit erforderlichen Fachkenntnisse, die er im Wesentlichen in der täglichen
  Arbeit anwendet. Er war mit den übertragenen Aufgaben vertraut und kannte die betrieblichen Abläufe. Seine Arbeitsweise
  war im Großen und Ganzen ordnungsgemäß. Er war stets bemüht, die ihm übertragenen Aufgaben sorgfältig zu erledigen.

  Belastbarkeit und Engagement
  Herr Pöttering erledigte die ihm übertragenen Aufgaben nach Anweisung. Er nahm an den betrieblichen Pflichtschulungen
  teil. Seine Belastbarkeit war ausreichend für die übertragenen Aufgaben.

  Arbeitserfolg
  Die Arbeitsergebnisse von Herrn Pöttering haben unsere Erwartungen erfüllt.

  Verhalten
  Sein Verhalten gegenüber der Geschäftsleitung war korrekt. Gegenüber den ihm unterstellten Mitarbeitern pflegte er eine
  direkte Kommunikationsweise. Im Umgang mit Lieferanten und Kunden trat er sachlich auf.

  Beendigung des Arbeitsverhältnisses
  Das Arbeitsverhältnis endet aus betriebsbedingten Gründen zum 30. November 2025 im Rahmen einer Umstrukturierung
  unserer Lagerlogistik. Wir wünschen Herrn Pöttering für seine berufliche Zukunft alles Gute.



                                                                          Stempel: Eisenwarenhandlung Großkopf Söhne KG
Heinrich Großkopf jun.

Geschäftsführer




Fiktive Testakte | Fall 04                                                                                                  Seite 1
```

### Tatsächlich erzeugte Antwort 1

Das Endzeugnis vom 30. November 2025 vermittelt für die Leistung insgesamt etwa **Note 4**, bei der Arbeitsweise mit Tendenz zur **Note 5**. Der Arbeitgeber bestätigt zwar, dass die Arbeitsergebnisse seine Erwartungen erfüllt haben. Die Arbeitsweise bezeichnet er aber nur als „im Großen und Ganzen ordnungsgemäß“. Mit „stets bemüht“ lässt er offen, ob Herr Pöttering seine Aufgaben tatsächlich sorgfältig erledigt hat. „Nach Anweisung“ weckt bei einem Lagermeister mit Verantwortung für fünf Lager Zweifel an seiner Selbstständigkeit.

**Für die Bewerbung als Lagerleiter wiegt die fehlende Beurteilung der Führungsleistung besonders schwer.** Der Arbeitgeber bestätigt ausdrücklich die fachliche und disziplinarische Führung von sechs Lagermitarbeitern und zwei Auszubildenden. Wie Herr Pöttering die Arbeit organisiert, sein Team angeleitet und welche Ergebnisse er damit erreicht hat, bleibt offen. Die „direkte Kommunikationsweise“ beschreibt lediglich seinen Umgangston. Aus ihr allein lässt sich kein Konflikt ableiten. Daneben lässt sich der berufliche Aufstieg klarer darstellen. Der erste Satz schreibt Herrn Pöttering die Meisterfunktion schon ab Mai 2009 zu, der zweite nennt die Bestellung im Jahr 2016.

Für die beiden Schreiben kommt es vor allem auf drei Punkte an:

1. **Frühere Bewertung.** Bitte geben Sie die Bewertung hier möglichst vollständig wieder, einschließlich Datum, Überschrift, Aussteller und Funktion des Unterzeichners. In welcher Form hat Herr Pöttering sie erhalten? Ein erteiltes Zwischenzeugnis kann den Arbeitgeber für den bereits beurteilten Zeitraum grundsätzlich binden. Ein Beurteilungsbogen kann ebenfalls belegen, wie der Arbeitgeber Leistung und Führung damals eingeschätzt hat. Besonders wichtig ist, ob die Bewertung bereits die Zeit als Lagermeister umfasst.
2. **Entwicklung und Bewertungsziel.** Was änderte sich nach der früheren Bewertung an Aufgaben, Befugnissen oder Ergebnissen? Welche konkreten Beanstandungen hat der Arbeitgeber gegebenenfalls erhoben, und was entgegnet Herr Pöttering darauf? Strebt er eine befriedigende oder eine gute Gesamtbewertung an? Eine unterdurchschnittliche Gesamtleistung muss grundsätzlich der Arbeitgeber darlegen und gegebenenfalls beweisen. Für das weitergehende Ziel „gut“ wären eigene, über einen aussagekräftigen Zeitraum belegbare Beiträge wichtig, etwa bei Inventuren, Einsatzplanung oder Ausbildung. Die Beweislastlinie stützt sich auf die mitgeteilten BAG-Urteile vom 14.10.2003 – 9 AZR 12/03 und vom 18.11.2014 – 9 AZR 584/13. Die Fundstellen sind vor Schriftsatzverwendung aktuell zu prüfen.
3. **Erteilung und Zeitdruck.** Wann und in welcher Form erhielt Herr Pöttering das Zeugnis? Auf der Kopie sind Name und Funktion des Geschäftsführers lesbar, ein handschriftlicher Namenszug ist nicht erkennbar. Liegt ihm ein unterschriebenes Papieroriginal oder eine mit seiner Einwilligung qualifiziert elektronisch signierte Datei vor? Bitte nennen Sie auch einen konkreten Bewerbungstermin, eine bereits erhobene Beanstandung und gegebenenfalls den Wortlaut einer Zeugnisabrede oder Ausschlussfrist.

Für den Mandantenbrief und das Arbeitgeberanschreiben ist die frühere Bewertung der wichtigste nächste Beleg. Ihr Wortlaut und der anschließende Beschäftigungsverlauf entscheiden darüber, welche Leistungsformel und welche Aussage zur Führung sich konkret vertreten lassen.

### Nutzerinput 2

Ich habe inzwischen das vom Geschäftsführer handschriftlich unterzeichnete Papieroriginal vom 31. August 2025 und den Arbeitsvertrag in der Kanzlei gesehen. Hier ist der vollständige Text der früheren Bewertung:

„Zwischenzeugnis
Herr Friedhelm Pöttering ist seit dem 1. Mai 2009 bei uns beschäftigt, zunächst als Fachkraft für Lagerlogistik und seit dem 1. Februar 2016 als Lagermeister. Er organisiert die Ein- und Ausgänge, disponiert das Hochregallager und die vier Außenlager, leitet sechs Lagermitarbeiter und zwei Auszubildende fachlich und disziplinarisch und verantwortet Warenwirtschaft, Inventur und Arbeitsschutz im Lager. Herr Pöttering erfüllt die ihm übertragenen Aufgaben stets zu unserer vollen Zufriedenheit. Er organisiert die Schichten vorausschauend, leitet die Mitarbeiter klar an und erzielt mit seinem Team gute Arbeitsergebnisse. Sein Verhalten gegenüber Vorgesetzten, Kollegen, Mitarbeitern und Geschäftspartnern ist stets einwandfrei. Dieses Zwischenzeugnis erteilen wir auf seinen Wunsch.
Gütersloh, 31. August 2025
Heinrich Großkopf jun., Geschäftsführer“

Für September bis November hat mir Herr Pöttering gesagt, dass Team und Aufgaben gleich blieben. Am 12. November kam eine Inventurliste einen Tag später als intern vorgesehen. Die E-Mail des Lagerbüros vom Folgetag mit dem Eingangsdatum liegt mir vor. Zur Ursache und zu den Auswirkungen haben wir keine Unterlagen. Weitere Beanstandungen sind ihm nicht bekannt. Einen Abschiedstext „stets zu unserer vollsten Zufriedenheit“ hat er am Heimcomputer selbst entworfen. Der Arbeitgeber hat ihn nie erhalten. Bitte den eigenen Text nicht übersenden.

Das Endzeugnis erhielt er am 2. Dezember ausschließlich als normalen unsignierten PDF-Anhang per E-Mail. Er hat der elektronischen Erteilung nicht zugestimmt und kein Papieroriginal erhalten. Er will eine gute Bewertung, Berichtigung der beruflichen Stationen und Führungsleistung sowie ein unterschriebenes Papierzeugnis. Die betriebsbedingte Beendigung und die Schlussformel sollen so bleiben. Für die Bewerbung am 18. Dezember wäre es gut, vorab eine korrigierte Kopie zu haben. Eine Beanstandung ist bisher nicht rausgegangen. Es gibt keine Zeugnisabrede, im Arbeitsvertrag keine Ausschlussfrist und nach unserer Prüfung keinen anwendbaren Tarifvertrag.

### Tatsächlich erzeugte Antwort 2

Die verlangte **Gesamtbewertung „gut“ ist tragfähig begründet**. Das vom Geschäftsführer unterzeichnete Zwischenzeugnis vom 31. August 2025 bewertet dieselbe Lagermeistertätigkeit mit „stets zu unserer vollen Zufriedenheit“. Es bescheinigt außerdem ausdrücklich gute Führungsergebnisse. Die drei Monate bis zum Ausscheiden sind gesondert zu würdigen. Der um einen Tag verspätete Eingang einer Inventurliste erklärt nach dem bisherigen Sachstand weder die breite Abwertung der Arbeitsweise noch das Weglassen der Führungsbeurteilung. Der Anspruch auf ein unterschriebenes Papierzeugnis lässt sich unabhängig vom Notenstreit geltend machen.

### Mandantenbrief

4. Dezember 2025

**Ihr Arbeitszeugnis vom 30. November 2025**

Sehr geehrter Herr Pöttering,

für Ihre Bewerbung als Lagerleiter haben Sie einen guten Grund, eine Berichtigung zu verlangen. Noch Ende August hat Ihnen der Geschäftsführer schriftlich bestätigt, dass Sie die Schichten vorausschauend organisierten, Ihre Mitarbeiter klar anleiteten und mit Ihrem Team gute Ergebnisse erzielten. Das Endzeugnis nennt zwar Ihre Personalverantwortung, lässt aber gerade diese für Ihre Bewerbung wichtige Bewertung aus.

Wir empfehlen, die gute Leistungs-, Führungs- und Verhaltensbeurteilung aus dem Zwischenzeugnis für das Endzeugnis zu verlangen. Der Eingang einer Inventurliste mit einem Tag Verspätung ist dokumentiert. Welche Bedeutung das für Ihre Gesamtleistung hatte, ist offen. Nach dem bisherigen Stand rechtfertigt dieser einzelne Vorgang die deutliche Abwertung kaum.

Der beigefügte Briefentwurf verlangt außerdem die korrekte Darstellung Ihres Aufstiegs zum Lagermeister und ein unterschriebenes Papierzeugnis. Für Ihre Bewerbung am 18. Dezember bitten wir vorab um eine korrigierte Kopie. Bitte geben Sie uns den Entwurf kurzfristig zum Versand frei.

Mit freundlichen Grüßen
[Rechtsanwältin]

### Entwurf an den früheren Arbeitgeber

Eisenwarenhandlung Großkopf Söhne KG
Herrn Heinrich Großkopf jun.
Gewerbering 14
33334 Gütersloh

4. Dezember 2025

**Friedhelm Pöttering – Berichtigung und Erteilung des Arbeitszeugnisses vom 30. November 2025**

Sehr geehrter Herr Großkopf,

wir vertreten Herrn Friedhelm Pöttering. Am 2. Dezember 2025 erhielt unser Mandant sein Endzeugnis als unsignierten PDF-Anhang. Wir bitten Sie, ihm gemäß § 109 GewO ein inhaltlich berichtigtes, eigenhändig unterschriebenes Papierzeugnis zu erteilen. Herr Pöttering hat einer elektronischen Erteilung nicht zugestimmt.

Bitte stellen Sie zunächst die berufliche Entwicklung eindeutig dar. Der Eingangssatz ordnet die Tätigkeit als Lagermeister der gesamten Beschäftigungszeit ab Mai 2009 zu. Ihrem Zwischenzeugnis vom 31. August 2025 entspricht folgende Fassung:

„Herr Friedhelm Pöttering, geboren am 3. April 1969 in Rietberg, war vom 1. Mai 2009 bis zum 30. November 2025 in unserem Betrieb beschäftigt. Er war zunächst als Fachkraft für Lagerlogistik und ab dem 1. Februar 2016 als Lagermeister tätig.“

In Ihrem von Ihnen unterzeichneten Zwischenzeugnis haben Sie sowohl die Gesamtleistung als auch die Führung und das Verhalten unseres Mandanten ausdrücklich positiv beurteilt. Nach Angaben unseres Mandanten blieben Aufgaben und Team bis zum Ausscheiden gleich. Die Einschränkungen „im Großen und Ganzen ordnungsgemäß“, „stets bemüht“ und „nach Anweisung“ vermitteln demgegenüber ein deutlich schwächeres Leistungsbild. Zugleich beschränkt sich die Beurteilung der Mitarbeiterführung auf den Kommunikationsstil.

Wir bitten Sie, die Abschnitte zu Fachkenntnissen, Arbeitsweise, Belastbarkeit, Engagement und Arbeitserfolg mit der dokumentierten guten Beurteilung in Einklang zu bringen und die Führungsleistung ausdrücklich aufzunehmen. Für die tragenden Aussagen schlagen wir in Anlehnung an Ihr Zwischenzeugnis vor:

„Herr Pöttering erfüllte die ihm übertragenen Aufgaben stets zu unserer vollen Zufriedenheit. Er organisierte die Schichten vorausschauend, leitete die Mitarbeiter klar an und erzielte mit seinem Team gute Arbeitsergebnisse.“

Für den Abschnitt zum Verhalten bitten wir um folgende Fassung:

„Sein Verhalten gegenüber Vorgesetzten, Kollegen, Mitarbeitern und Geschäftspartnern war stets einwandfrei.“

Sollten Sie die abweichende Beurteilung auf spätere Entwicklungen oder nachträglich bekannt gewordene Tatsachen stützen, bitten wir um konkrete Mitteilung, welche Vorgänge welche Änderung aus Ihrer Sicht rechtfertigen.

Herr Pöttering benötigt das Zeugnis für eine Bewerbung am 18. Dezember 2025. Bitte stellen Sie das berichtigte, unterschriebene Papieroriginal **bis zum 16. Dezember 2025** zur Abholung bereit und teilen Sie uns die Abholmöglichkeit mit. Für die Bewerbung bitten wir ergänzend, uns bis dahin einen Scan des unterzeichneten Zeugnisses zu übersenden.

Mit freundlichen Grüßen
[Rechtsanwältin]

### Anwaltlicher Prüfvermerk zum 4. Dezember 2025

**Beweisgrundlage und Reichweite der Bindung.** Nach Ihrer eigenen Einsicht liegt das Zwischenzeugnis als handschriftlich unterzeichnetes Papieroriginal vor. Beide Zeugnisse stammen von derselben Arbeitgeberin und benennen denselben Geschäftsführer. Das Zwischenzeugnis erfasst die Beschäftigung vom 1. Mai 2009 bis zum 31. August 2025, darunter mehr als neun Jahre als Lagermeister. Die Aufgabenbeschreibungen beider Fassungen stimmen in den wesentlichen Verantwortungsbereichen überein. Die tatsächliche Kontinuität des Teams und der Aufgaben in den letzten drei Monaten beruht zusätzlich auf der Angabe des Mandanten.

Für den bereits beurteilten Zeitraum ist der Arbeitgeber grundsätzlich an das Zwischenzeugnis gebunden. Spätere Entwicklungen oder nachträglich bekannt gewordene erhebliche Tatsachen können eine Abweichung rechtfertigen. Bei einer verlangten überdurchschnittlichen Gesamtbewertung trägt grundsätzlich der Arbeitnehmer die Darlegungs- und Beweislast. Hier verfügt er mit der guten, zeitnahen Eigenbewertung des Arbeitgebers über einen konkreten Beleg gerade für die streitige Note. Soweit die Arbeitgeberin eine unterdurchschnittliche Gesamtleistung verteidigt, muss sie deren tatsächliche Grundlage darlegen und gegebenenfalls beweisen. Maßgeblich nach dem bereitgestellten Material sind BAG, Urteil vom 16.10.2007 – 9 AZR 248/07, sowie zur Notenschwelle BAG, Urteile vom 14.10.2003 – 9 AZR 12/03 und vom 18.11.2014 – 9 AZR 584/13. Die Fundstellen und ihre Fortgeltung wurden im Mandat nicht extern überprüft und sind vor Schriftsatzverwendung zu verifizieren.

| Streitstelle | Kontext und Tendenz | Ampel | Rechtsstatus, Beleg und Änderungsziel |
|---|---|---|---|
| Berufliche Stationen | Der erste Satz erscheint schon für 2009 als Meisterbescheinigung. Erst der Folgesatz nennt die frühere Funktion. | 🟠 | Sachliche Klarstellung gut begründet. Das Zwischenzeugnis belegt den genauen Wechsel zum 1. Februar 2016. |
| Fachkenntnisse und Arbeitsweise | „Im Wesentlichen“ schränkt die Anwendung der Kenntnisse ein. „Im Großen und Ganzen“ und „stets bemüht“ ziehen vor allem die Sorgfalt in Zweifel. Arbeitsweise etwa 4–5. | 🔴 | Berichtigung des abwertenden Gesamtbilds plausibel. Die frühere gute Gesamtbewertung und die ausdrücklich bescheinigte vorausschauende Organisation tragen den vorgeschlagenen Ersatz. |
| Belastbarkeit und Engagement | „Nach Anweisung“, Teilnahme an Pflichtschulungen und „ausreichend“ vermitteln für eine langjährige Leitungskraft geringe Selbstständigkeit und wenig Initiative. Tendenz 4. | 🔴 | Die dokumentierte eigenständige Schichtorganisation spricht gegen die pauschale Darstellung. Für eine gesonderte überdurchschnittliche Belastbarkeitsaussage fehlt ein eigener Beleg. Der Entwurf verlangt eine stimmige Gesamtfassung. |
| Arbeitserfolg | „Unsere Erwartungen erfüllt“ bestätigt einen Erfolg. Im Zusammenhang mit den Einschränkungen liegt das Gesamtleistungsbild etwa bei 4. | 🔴 | Die frühere ausdrückliche Note 2 trägt das Ziel „stets zu unserer vollen Zufriedenheit“. Die übrigen Leistungssätze müssen dazu passen. |
| Führung | Fachliche und disziplinarische Leitung von sechs Lagermitarbeitern und zwei Auszubildenden ist in beiden Fassungen belegt. Das Endzeugnis lässt den Führungserfolg offen. | 🔴 | Ergänzung besonders gut begründet. Das Zwischenzeugnis benennt Schichtplanung, klare Anleitung und gute Teamergebnisse ausdrücklich. Ein Branchenbrauch muss für diesen konkreten Tatsachenvergleich nicht erst hergeleitet werden. |
| Sozialverhalten | „Korrekt“, „direkte Kommunikationsweise“ und „sachlich“ wirken insgesamt zurückhaltend, etwa 3–4. Aus dem Wort „direkt“ lässt sich kein konkreter Konflikt ableiten. | 🟠🔴 | Die frühere Beurteilung umfasst sämtliche relevanten Kontaktgruppen und lautet „stets einwandfrei“. Eine spätere Verhaltensbeanstandung ist nach Mandantenangabe unbekannt. |
| Erteilungsform | Ausschließlich unsignierte PDF per E-Mail, keine Einwilligung und kein Papieroriginal. | 🔴 | Eigenständiger Erfüllungsanspruch nach § 109 Abs. 1 und 3 GewO in Verbindung mit §§ 126, 126a BGB. Die erbetene Vorabkopie dient der Bewerbung. Für die Erfüllung ist hier das unterschriebene Papieroriginal maßgeblich. |
| Beendigungsgrund und Schluss | Die Umstrukturierung erklärt den betriebsbedingten Austritt. Der berufliche Zukunftswunsch ist knapp. | 🟢 | Entspricht dem Mandantenziel. Kein Änderungsbegehren. |

**Gewicht des Inventurvorgangs.** Termintreue bei der Inventur gehört zum Kern der Stelle. Darin liegt der stärkste denkbare Einwand der Arbeitgeberin. Die vorliegende E-Mail dokumentiert das Eingangsdatum. Ursache, persönliche Verantwortlichkeit und betriebliche Auswirkungen sind offen. Auch bei unterstellter Verantwortung erklärt ein einzelner Tag Verspätung für sich kaum, weshalb die über Jahre bewertete Arbeitsweise insgesamt nur eingeschränkt ordnungsgemäß gewesen sein oder sich das Sozialverhalten verschlechtert haben soll. Weitere Beanstandungen sind dem Mandanten nach seiner Aussage unbekannt. Der Arbeitgeberentwurf bestreitet deshalb keinen dokumentierten Vorgang und gibt der Arbeitgeberin Gelegenheit, etwaige Abweichungsgründe zu konkretisieren.

**Zielwortlaut und weiteres Vorgehen.** Der private Entwurf mit „stets zu unserer vollsten Zufriedenheit“ zielt auf Note 1. Er wurde dem Arbeitgeber nie vorgelegt, hat keinen Beweiswert für dessen Bewertung und ist weder Grundlage noch Anlage des Schreibens. Der vorgeschlagene Text übernimmt die belegte Note 2. Nach Ihrer Vertrags- und Tarifprüfung ist keine Ausschlussfrist ersichtlich. Den 16. Dezember habe ich als erbetenen Bereitstellungstermin gewählt, damit vor der Bewerbung zwei Tage verbleiben. Nach Versandfreigabe sollte der Zugang des Schreibens dokumentiert werden. Bei Eingang der Neufassung sind insbesondere die Entfernung der abwertenden Begleitsätze, die vollständige Führungsbeurteilung und die Unterzeichnung des Papieroriginals zu kontrollieren.

### Nutzerinput 3

Ich habe den Entwurf mit Herrn Pöttering besprochen. Er möchte den Abschnitt „Verhalten“ im Endzeugnis ausdrücklich so lassen, wie er ist. Die eigentliche Führungsleistung bei Schichtplanung und Anleitung bleibt sein Anliegen. Auch die übrigen Punkte bleiben. Es wurde noch nichts versandt. Bitte geben Sie mir die Unterlagen in der jetzt passenden Fassung.

### Tatsächlich erzeugte Antwort 3

Herr Pötterings Anliegen lässt sich durch einen eigenen Absatz zur **Führungsleistung** umsetzen. Dort gehören Schichtplanung, Anleitung und Teamergebnis hin. Der Abschnitt „Verhalten“ mit der Aussage zur direkten Kommunikationsweise kann so vollständig erhalten bleiben. Die folgenden Entwürfe ersetzen die bisherigen, unversandten Fassungen.

### 1. Mandantenbrief

4. Dezember 2025

**Ihr Arbeitszeugnis vom 30. November 2025**

Sehr geehrter Herr Pöttering,

für Ihre Bewerbung als Lagerleiter sollte das Zeugnis zeigen, wie Sie Ihr Team geführt haben. Dafür haben wir einen guten Beleg. Noch am 31. August hat der Geschäftsführer schriftlich bestätigt, dass Sie die Schichten vorausschauend planten, Ihre Mitarbeiter klar anleiteten und mit dem Team gute Ergebnisse erzielten. Auch Ihre Gesamtleistung hat er mit „gut“ bewertet.

Wir empfehlen, beide Aussagen für das Endzeugnis zu verlangen. Die Inventurliste ging im November einen Tag später als vorgesehen ein. Welche Folgen das hatte und wer für die Verzögerung verantwortlich war, ist offen. Nach dem bisherigen Stand erklärt der Vorgang die deutliche Abwertung kaum.

Der beigefügte Entwurf verlangt außerdem, Ihren Aufstieg zum Lagermeister ab dem 1. Februar 2016 klar darzustellen. Wie besprochen, betrifft die gewünschte Ergänzung Ihre Führungsleistung. Der Verhaltensabschnitt, die betriebsbedingte Beendigung und die Schlussformel sind von der Bitte um Berichtigung ausgenommen.

Für Ihre Bewerbung am 18. Dezember bitten wir bis zum 16. Dezember um eine Kopie des unterschriebenen Papierzeugnisses. Bitte geben Sie uns den beigefügten Entwurf zum Versand frei.

Mit freundlichen Grüßen
[Rechtsanwältin]

### 2. Schreiben an den früheren Arbeitgeber

Eisenwarenhandlung Großkopf Söhne KG
Herrn Heinrich Großkopf jun.
Gewerbering 14
33334 Gütersloh

4. Dezember 2025

**Friedhelm Pöttering – Berichtigung und Erteilung des Arbeitszeugnisses vom 30. November 2025**

Sehr geehrter Herr Großkopf,

wir vertreten Herrn Friedhelm Pöttering. Er erhielt das Endzeugnis am 2. Dezember 2025 ausschließlich als unsignierten PDF-Anhang. Wir bitten Sie, ihm gemäß § 109 GewO ein berichtigtes, eigenhändig unterschriebenes Papierzeugnis zu erteilen. Einer elektronischen Erteilung hat unser Mandant nicht zugestimmt.

**Berufliche Stationen.** Der erste Satz bezeichnet Herrn Pöttering für die gesamte Beschäftigungszeit als Lagermeister. Aus Ihrem Zwischenzeugnis vom 31. August 2025 ergibt sich der genaue Zeitpunkt seiner Bestellung. Wir bitten, die ersten beiden Sätze wie folgt zu fassen:

„Herr Friedhelm Pöttering, geboren am 3. April 1969 in Rietberg, war vom 1. Mai 2009 bis zum 30. November 2025 in unserem Betrieb beschäftigt. Er war zunächst als Fachkraft für Lagerlogistik und ab dem 1. Februar 2016 als Lagermeister tätig.“

**Leistung und Führung.** Im Zwischenzeugnis vom 31. August 2025 haben Sie Herrn Pöttering für dieselben Aufgaben eine gute Gesamtleistung bescheinigt. Im Endzeugnis beschreiben Sie seine Arbeitsweise als „im Großen und Ganzen ordnungsgemäß“ und seine Aufgabenerledigung mit „stets bemüht“ und „nach Anweisung“. Als Führungsaufgabe führen Sie die fachliche und disziplinarische Leitung von sechs Lagermitarbeitern und zwei Auszubildenden auf. Die noch im August ausdrücklich beurteilte Qualität seiner Schichtplanung und Anleitung sowie das Ergebnis seiner Führung bleiben offen. Nach den Angaben unseres Mandanten bestanden Aufgaben und Team bis zu seinem Ausscheiden in gleicher Weise fort.

Wir bitten Sie daher, die Abschnitte von „Fachkenntnisse und Arbeitsweise“ bis einschließlich „Arbeitserfolg“ durch eine in sich stimmige gute Leistungsbeurteilung zu ersetzen. Für die Gesamtbewertung schlagen wir die bereits von Ihnen verwendete Formulierung in der Vergangenheitsform vor:

„Herr Pöttering erfüllte die ihm übertragenen Aufgaben stets zu unserer vollen Zufriedenheit.“

Bitte nehmen Sie unmittelbar vor der Überschrift „Verhalten“ einen eigenen Absatz zur Führungsleistung auf. Auch hierfür lässt sich an Ihre Beurteilung vom August anknüpfen:

„Herr Pöttering organisierte die Schichten vorausschauend, leitete die Mitarbeiter klar an und erzielte mit seinem Team gute Arbeitsergebnisse.“

Bitte übernehmen Sie den Abschnitt „Verhalten“ sowie den gesamten Abschnitt „Beendigung des Arbeitsverhältnisses“ einschließlich der Zukunftswünsche wortgleich aus dem Endzeugnis. Sollten Sie hinsichtlich der Leistung oder Führung an einer abweichenden Bewertung festhalten, bitten wir um Mitteilung, welche späteren Entwicklungen oder nachträglich bekannt gewordenen Tatsachen die jeweilige Abweichung begründen.

Herr Pöttering benötigt das Zeugnis für eine Bewerbung am 18. Dezember 2025. Wir bitten Sie, das berichtigte, unterschriebene Papieroriginal **bis zum 16. Dezember 2025** zur Abholung bereitzustellen und uns die Abholmöglichkeit mitzuteilen. Bitte übersenden Sie uns bis dahin für die Bewerbung vorab einen Scan des unterzeichneten Zeugnisses.

Mit freundlichen Grüßen
[Rechtsanwältin]

### 3. Anwaltlicher Prüfvermerk

**Leistungsbild und Beweislage.** Das Endzeugnis vermittelt insgesamt etwa Note 4, in der Arbeitsweise mit Tendenz zu Note 5. „Unsere Erwartungen erfüllt“ bescheinigt einen Arbeitserfolg. Die Kombination mit „stets bemüht“, „im Großen und Ganzen ordnungsgemäß“ und „nach Anweisung“ vermittelt jedoch den Eindruck eingeschränkter Sorgfalt und Selbstständigkeit. Eine gute Gesamtformel allein würde diesen Eindruck fortbestehen lassen. Das Schreiben erfasst deshalb auch die abwertenden Einzelaussagen.

| Streitpunkt | Befund | Einordnung und Ziel |
|---|---|---|
| 🔴 Gesamtleistung | Das von Ihnen eingesehene, vom Geschäftsführer unterzeichnete Zwischenzeugnis bewertet die Leistung bis zum 31. August 2025 ausdrücklich mit Note 2. Für die letzten drei Monate berichtet Herr Pöttering von gleichbleibenden Aufgaben und unverändertem Team. | Die gute Gesamtbewertung ist konkret begründet. Ziel ist „stets zu unserer vollen Zufriedenheit“ mit dazu passenden Einzelaussagen. |
| 🔴 Führungsleistung | Beide Zeugnisse bestätigen die Personalverantwortung. Das Zwischenzeugnis bewertet darüber hinaus vorausschauende Schichtplanung, klare Anleitung und gute Teamergebnisse. Gerade diese Aussagen fehlen im Endzeugnis. | Ein eigener Leistungsabsatz vor „Verhalten“ schließt die für die Lagerleiterbewerbung wesentliche Lücke. Der vorgeschlagene Satz übernimmt die belegte Bewertung in der Vergangenheitsform. |
| 🟠 Berufliche Stationen | Der Eingangssatz legt eine Meistertätigkeit ab 2009 nahe. Das Zwischenzeugnis belegt den Funktionswechsel zum 1. Februar 2016. | Sachlich gut begründete Klarstellung der beiden Tätigkeitsabschnitte. |
| 🔴 Erteilungsform | Nach den Mandatsangaben ging ausschließlich ein unsigniertes PDF zu. Die Einwilligung in elektronische Erteilung fehlt. | Der Anspruch auf formgerechte Erteilung ist offen. Verlangt wird das eigenhändig unterschriebene Papieroriginal nach § 109 Abs. 1 und 3 GewO. Der vorab erbetene Scan dient der Bewerbung. |

**Reichweite der früheren Beurteilung.** Für den vom Zwischenzeugnis erfassten Zeitraum ist die Arbeitgeberin grundsätzlich an ihre Bewertung gebunden. Spätere Leistungen oder nachträglich bekannt gewordene erhebliche Tatsachen können eine Abweichung tragen. Für die angestrebte überdurchschnittliche Gesamtbewertung muss Herr Pöttering grundsätzlich konkrete Tatsachen darlegen und erforderlichenfalls beweisen. Das unterschriebene Zwischenzeugnis ist dafür besonders aussagekräftig, weil es dieselbe Leitungsfunktion bis drei Monate vor dem Ausscheiden bewertet. Soweit die Arbeitgeberin eine unterdurchschnittliche Gesamtleistung verteidigt, muss sie die dafür maßgeblichen Tatsachen darlegen und gegebenenfalls beweisen. Grundlage sind die im Mandatsmaterial wiedergegebenen BAG-Urteile vom 16.10.2007 – 9 AZR 248/07, vom 14.10.2003 – 9 AZR 12/03 und vom 18.11.2014 – 9 AZR 584/13. Fundstellen und Fortgeltung sind vor Schriftsatzverwendung zu verifizieren.

**Inventurvorgang.** Die E-Mail des Lagerbüros dokumentiert das Eingangsdatum der Liste. Termintreue bei der Inventur gehört zum Aufgabenbereich eines Lagermeisters. Für das Gewicht der Verspätung fehlen aber Angaben zu Ursache, persönlicher Verantwortung und betrieblichen Folgen. Selbst eine zurechenbare eintägige Verzögerung hätte nach dem bekannten Sachstand wenig Aussagekraft für die über Jahre ausgeübte Schichtplanung und Mitarbeiteranleitung. Das Anschreiben lässt Raum für konkreten Gegenvortrag, ohne Herrn Pöttering eine Ursache oder Folgenlosigkeit zuzuschreiben.

**Umfang und Termin.** Der ausdrückliche Wunsch des Mandanten schließt jede Änderung des Verhaltensabschnitts aus. Das gilt auch für „direkte Kommunikationsweise“. Die frühere Verhaltensnote wird daher im Arbeitgeberbrief weder zitiert noch verlangt. Der private Entwurf mit einer sehr guten Gesamtformel ist weder Beleg noch Anlage. Nach Ihrer Prüfung ist keine vertragliche oder tarifliche Ausschlussfrist ersichtlich. Der 16. Dezember ist als erbetener Bereitstellungstermin mit zwei Tagen Vorlauf zur Bewerbung gewählt. Bei Eingang sind Papierunterschrift, Tätigkeitsdaten, Leistungsabschnitte und der wortgleiche Fortbestand von Verhalten, Beendigungsgrund und Schlussformel an der vollständigen Neufassung zu kontrollieren.
