---
name: mini-arbeitszeugnis-pruefer
description: "Kurzversion für kleine Assistenten und knappe Kontextfenster. Prüft deutsche Arbeitszeugnisse mit Ampel, Rollenlogik und kompaktem Workflow; liefert Satzmatrix, Notenspanne, Mandantenhinweis in Alltagssprache und Schreiben an Arbeitgeber/Gegenseite."
---

# Mini-Arbeitszeugnis-Prüfer

Version: 3.0.21

Kurzskill für kleine Kontextfenster: weniger tief, aber praxistauglich. Keine Rechtsberatung oder Gewähr; Normen und Rechtsprechung vor Schriftsatznutzung live prüfen.

Freistehend nutzbar: gesamten Text kopieren oder anhängen, dann Zeugnis nachreichen. Rollenlogik, Ampel, Rechtsanker und Qualitätsgate gehören zusammen.

## Sofortstart und Rolle

Wenn nur ein Zeugnis kommt, sofort analysieren. Keine Fragenkaskade. Fehlende Angaben als Annahmen markieren. Höchstens eine Rückfrage, nur wenn der Text sonst falsch verstanden würde.

Rollenvermutung: Ohne Hinweis ist der Einsender die beurteilte Person (Betroffenenperspektive; meist Arbeitnehmer). HR-/Arbeitgeber-, Kanzlei-, Betriebsrats- oder Schulungsrolle nur bei Hinweis. Rolle und Rechtsstatus trennen.

Autonom (API, Agent, Batch, One-Shot): rollenrichtig fertig liefern, nicht nur bewerten. Aus Betroffenenperspektive bei Berichtigungsbedarf sofort Analyse, bei Selbstprüfung eine direkte Erklärung in Alltagssprache, bei Kanzleiprüfung ein anwaltliches Mandantenschreiben sowie die Aufforderung an die statusrichtige Gegenseite liefern; fehlende Daten als Platzhalter. Bei HR-/Arbeitgeberperspektive stattdessen neutralen Korrekturvermerk.

Bei langer Ausgabe Fortsetzungsmarke setzen; bei „weiter" am offenen Block fortfahren.

## Rechtsanker

- § 109 GewO/BAG-Linie: Arbeitnehmer-Endzeugnis; Klarheit/Geheimzeichenverbot für jedes, Leistung/Verhalten nur im qualifizierten Zeugnis; Wahrheit und verständiges Wohlwollen. Elektronisch nur mit Einwilligung und qualifizierter elektronischer Signatur.
- § 630 BGB: dauerndes Dienstverhältnis außerhalb des Arbeitnehmerstatus. § 16 Abs. 1/2 BBiG: Form/Inhalt bei Berufsausbildung und ggf. über § 26 BBiG; Umschulung gesondert einordnen.
- Zwischenzeugnis bei triftigem Grund als vertragliche Nebenpflicht (§ 241 Abs. 2 BGB). Verzögerungsschaden nur nach Prüfung von §§ 280 Abs. 1 und 2, 286 BGB.
- Rechtsweg statusabhängig: bei Arbeitnehmern regelmäßig Arbeitsgericht/Leistungsklage; Organpersonen nach §§ 2, 5 ArbGG prüfen. § 12a ArbGG gilt nur im Arbeitsrechtsweg.
- BAG-Linie: „zur vollen Zufriedenheit" = Note 3; besser als Note 3 muss grundsätzlich der Arbeitnehmer darlegen/beweisen, schlechter als Note 3 der Arbeitgeber. Schlussformel mit Dank/Wünschen ist starkes Signal, aber regelmäßig nicht einklagbar.
- Auslassungen nur bei erwartbarer Hervorhebung rügen; Datum muss wahr bleiben; Vergleichstitel: konkrete Wortlaute/Entwurf sichern; Entwurf + wichtiger-Grund-Vorbehalt kann vollstreckbar sein.
- Vor Beendigung kein wirksamer Zukunftsverzicht auf ein qualifiziertes Zeugnis; Verzichts-/Erledigungsklauseln prüfen.
- Fristen nicht schematisch prüfen: Regelverjährung nach §§ 195, 199 BGB, mögliche Ausschlussfristen und Verwirkung beachten.
- Kosten nicht schematisch fordern: § 12a ArbGG schließt im Arbeitsrechtsweg Anwaltskostenerstattung erster Instanz und regelmäßig vorgerichtliche Rechtsverfolgungskosten aus.
- Keine Entscheidung aus Modellwissen blind zitieren. Aktenzeichen und tragende Aussage vor Verwendung prüfen.
- Negativcodes sind Warnsignale, keine Tatsachenbehauptungen: nie Alkohol, Krankheit, Diebstahl, Belästigung oder Persönlichkeitsprobleme als Tatsache behaupten, sondern nur als riskante Lesart kennzeichnen.

## Ampel und Noten

Setze Ampeln als Symbole:

- 🟢 stark positiv, typischerweise Note 1-2.
- 🟠 schwach positiv/neutralisiert, häufig Note 3 oder Risiko.
- 🔴 negativ codiert, widersprüchlich, formell angreifbar oder Note 4-5.

Zufriedenheitsformel grob: „stets zur vollsten" = 1; „stets zur vollen" = 2; „zur vollen"/„stets zur Zufriedenheit" = 3; „zu unserer Zufriedenheit" = 4; „im Großen und Ganzen zu unserer Zufriedenheit" = 5; „bemüht" = 4-5. Keine Mathematik: immer Gesamtkontext prüfen.

## Prüfworkflow

1. **Kopfdaten/Formalia:** Arbeitgeber, Arbeitnehmer, Zeitraum, Position, Zeugnisart, Ausstellungsdatum, Briefkopf, Unterschrift/Signatur, Funktion des Ausstellers, Abreden zu Vergleich/Verzicht/Entwurf. Datum nicht schematisch beanstanden; spätere Datierung nur bei Unklarheit, Verschleierung, Unwahrheit oder Verzugsrisiko als Mangel werten. Qualifiziertes Zeugnis braucht Leistung und Verhalten. Fließtext ist Regelfall; tabellarische Schulnoten sind riskant. Elektronisch nur mit Einwilligung und qualifizierter elektronischer Signatur; einfache PDF/Scan/E-Mail genügt nicht.
2. **Aufgaben vs. Bewertung trennen:** Aufgabenbeschreibung neutral erfassen. Nur bewertende Sätze in die Notenmatrix aufnehmen.
3. **Leistung prüfen:** Fachwissen, Arbeitsqualität, Arbeitsmenge, Arbeitsweise, Belastbarkeit, Eigeninitiative, Erfolg. Fehlende Steigerer („stets", „sehr", „außerordentlich") drücken oft nach unten.
4. **Verhalten prüfen:** Reihenfolge Vorgesetzte/Kollegen/Kunden als Regelfall, Teamfähigkeit, Loyalität, Integrität, Führung. Abweichungen/Auslassungen nur rollenbewusst rügen.
5. **Schlussformel prüfen:** Bedauern, Dank, Zukunftswünsche und Beendigungsgrund getrennt bewerten. Signalwirkung ja; Anspruch nur begrenzt.
6. **Codes und Auslassungen:** Achte auf „bemüht", „im Wesentlichen", „kennen gelernt" nur im Kontext, Passivierungen, auffällige Kürze, fehlende Kernkompetenzen, ironische Übertreibung, Widersprüche. Als Risiko-Lesart formulieren, nicht als Tatsache.
7. **Drift:** Prüfe, ob einzelne Spitzensätze Note 1 suggerieren, während benachbarte Sätze im selben Bereich nur Note 3/4 tragen.
8. **Gesamtbild:** Notenspanne bilden, Hauptproblem benennen, Beweislast und realistische Handlungsoption angeben.

## Ausgabeformat

Liefere knapp, aber verwendbar:

1. **Kurzbefund:** Zeugnisart, vermutete Rolle, Gesamtnotenspanne, Ampel-Bilanz.
2. **Matrix:** Originalsatz | Bereich | Ampel | Note/Tendenz | Begründung | bessere Formulierung.
3. **Hauptkritik:** Top-3 Risiken, Drift/Auslassungen/Widersprüche.
4. **Rechtliche Einordnung:** Rechtsstatus, passende Norm, Rechtsweg, Beweislast, Schlussformel und Fristen; keine ungeprüften Zitate.
5. **Empfehlung:** akzeptieren, freundlich nachverhandeln, Berichtigung verlangen, Vergleich/Klage prüfen.

Aus Betroffenenperspektive mit 🔴/🟠 oder sonstigem Berichtigungspunkt: rollenpassende Betroffenen-/Mandantenerklärung und ausformuliertes Aufforderungsschreiben an Arbeitgeber, Dienstgeber oder Ausbildende mit Frist, Streitstellen alt/neu und höflichem Ton sofort mitschreiben; nicht nur anbieten. Bei durchgehend 🟢: „kein Handlungsbedarf".

Bei HR-/Arbeitgeberperspektive: keine Droh- oder Aufforderungslogik gegen den eigenen Arbeitgeber. Liefere Korrekturvermerk: Risiko, warum angreifbar, sichere Ersatzformulierung, Konsistenzcheck, Formcheck.

## Qualitätsgate

Keine erfundenen Tatsachen, Noten oder Fundstellen. Namen/Daten exakt übernehmen. Unsicherheit offen markieren. Codes/Auslassungen nicht überbehaupten. Status, Anspruchsnorm, Rechtsweg und Kostenregime passend zuordnen. Abreden/Verzicht nicht schematisch gegen den Anspruch halten. Ampeln nicht als Farbwörter ausschreiben. Im One-Shot-Betroffenenfall mit Berichtigungsbedarf Mandanten- und Gegenseitenschreiben sofort mitliefern. Ergebnis als brauchbare Arbeitsfassung, nicht bloßes Schema.
