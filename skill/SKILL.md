---
name: arbeitszeugnis-pruefer
description: "Vollständige anwaltliche Arbeitsroute für deutsche Arbeitszeugnisse nach dem Ampelsystem (Rot/Orange/Grün). Erkennt Geheimcodes, Zufriedenheits- und Schlussformeln, Steigerungsadverbien, Schaufenster-Drift, Auslassungen und Widersprüche. Liefert satzweise Notenmatrix, begründete Gesamtnotenspanne, Mandantenbericht, Aufforderungsschreiben an den Arbeitgeber und Klagestrategie zur Zeugnisberichtigung. Stützt sich auf § 109 GewO, § 16 BBiG und § 241 II, § 280 I BGB; weicht auf §§ 1004, 823 BGB nur in Ausnahmefällen aus."
---

# Arbeitszeugnis-Prüfer (Ampelsystem)

Diese Skill-Datei trägt den vollständigen Workflow zur Analyse deutscher Arbeitszeugnisse — vom ersten Intake bis zum Klageentwurf. Die Code-, Flaggen-, Mandats- und Musterzeugnistabellen liegen in `references/`. Die Tabellen werden im Body nur zitiert, nicht dupliziert; lade die jeweilige Referenz, wenn der Schritt sie braucht.

## Rechtlicher Anker

- **§ 109 GewO** — Anspruch auf einfaches oder qualifiziertes Zeugnis; Wahrheits- und Wohlwollensgrundsatz; Klarheits- und Verständlichkeitsgebot.
- **§ 109 Abs. 2 S. 2 GewO** — Geheimzeichen und Formulierungen, die etwas anderes als aus der Wortwahl ersichtlich aussagen, sind unzulässig.
- **§ 16 BBiG** — Ausbildungszeugnis; auf Verlangen mit Angaben zu Verhalten und Leistung.
- **§ 241 Abs. 2 BGB**, **§ 280 Abs. 1 BGB** — Nebenpflicht des Arbeitgebers, ein leistungsgerechtes Zeugnis zu erteilen; Schadensersatz bei Verletzung.
- **Beweislastregel BAG:** Bis Note 3 trägt der Arbeitgeber die Beweislast für eine schlechtere Beurteilung; ab Note 2 abwärts trägt der Arbeitnehmer die Beweislast für eine bessere Beurteilung.
- **Zuständigkeit:** Arbeitsgericht (§ 2 Abs. 1 Nr. 3 ArbGG), Klage auf Zeugnisberichtigung als Leistungsklage.

> **Rechtsprechung live prüfen.** Keine Entscheidung aus Modellwissen zitieren. Vor Ausgabe über `gesetze-im-internet.de`, `dejure.org`, das Rechtsprechungsportal des Bundes oder ein anderes amtliches/frei prüfbares Verzeichnis mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Wann diese Skill greift

- Mandant oder Mandantin hat ein Zeugnis erhalten und will es einordnen.
- Anwaltskanzlei prüft Berichtigungs-, Vergleichs- oder Klagestrategie.
- Personalabteilung will einen Entwurf gegenprüfen lassen.
- Betriebsrat sucht eine Schulungseinschätzung.
- Ausbildungs- oder Zwischenzeugnis liegt vor.

Wenn dagegen nur ein Bewerbungsschreiben, eine Stellenausschreibung oder eine Beurteilung außerhalb des Zeugnisses zu prüfen ist: anderes Mandat, dieser Skill ist nicht zuständig.

## Referenzbibliothek

| Referenz | Inhalt |
| --- | --- |
| `references/zufriedenheitsformel.md` | Notenstufen 1 bis 5 der Hauptformel mit Steigerungs- und Abschwächungssignalen. |
| `references/schlussformel.md` | Bedauern/Dank/Wunsch, Signal versus Anspruch, Fünf-Bausteine-Schema. |
| `references/geheimcode-katalog.md` | Standardphrasen zu Leistung, Engagement, Belastbarkeit, Teamarbeit, Führung, Compliance. |
| `references/ampel-flaggen.md` | Steigerungsadverbien, grüne, orange und rote Flaggen, negative Codeworte nach Themen. |
| `references/analyse-techniken.md` | Bereichs-Drift, Auslassungen, Negationen, Widersprüche, formale Kopfdaten-Prüfung. |
| `references/mandatsmodule.md` | Aufforderungsschreiben, Wortlaut-Verbesserungstabelle, Klageantrag, Streitwert, Beweislast. |
| `references/muster-und-sonderfaelle.md` | Drei vollständige Musterzeugnisse (Note 1, gemischt, rote Flaggen) plus leitende Positionen, Azubi-Zeugnis, branchenspezifische Pflichtaussagen. |

## Workflow in acht Stufen

Arbeite in der unten genannten Reihenfolge. Springe nur dann zurück, wenn ein späterer Schritt einen früheren in Frage stellt (zum Beispiel: Schlussformel widerspricht der Hauptnote).

### 1 — Intake und Rollenklärung

Erfasse die folgenden Punkte aus dem Material. Frage nur nach, was der Mandant noch nicht in das Material gelegt hat:

| Punkt | Klärung |
| --- | --- |
| Rolle | Arbeitnehmer, Anwalt/Kanzlei, Arbeitgeber/HR, Betriebsrat, Personalabteilung. |
| Ziel | Nur verstehen, nachverhandeln, Arbeitgeber anschreiben, Klage prüfen, Vergleichstext bauen, Schulungsfall. |
| Zeugnisart | Einfach, qualifiziert, Zwischenzeugnis, Ausbildungszeugnis, Entwurf. |
| Beschäftigungs-Eckdaten | Position, Beginn, Ende, Branche, Unternehmensgröße. |
| Anlass | Eigenkündigung, Arbeitgeberkündigung, Aufhebungsvertrag, Befristungsende, Elternzeit, Tod, Insolvenz. |
| Zeitpunkt | Datum Ausstellung, Datum Erhalt, Bewerbungs- oder Vergleichsdruck. |
| Vergleichsmaterial | Vorzeugnis, Zwischenzeugnis, Zielvereinbarungen, Boni, Beurteilungsbögen, Lob-Mails. |
| Frist | Schon eine Klagefrist im Raum? Vorprozessuale Berichtigungsbitte schon ausgesprochen? |

Notiere die Antworten in einem Mandatsblatt. Wenn das Zeugnis als PDF kommt, prüfe zuerst die formale Ebene aus `references/analyse-techniken.md` (Briefkopf, Datum, Unterschriftsberechtigung, vollständige Beschäftigungsangabe).

### 2 — Zeugnisart und Kopfdaten sichern

- Einfaches Zeugnis: nur Art und Dauer der Tätigkeit.
- Qualifiziertes Zeugnis: zusätzlich Leistung und Verhalten.
- Zwischenzeugnis: gleiche Anforderungen, aber Bezug auf den noch laufenden Zeitabschnitt.
- Ausbildungszeugnis (§ 16 BBiG): mit Angaben zu Verhalten und Leistung nur auf Verlangen.

Kopfdaten gegen Arbeitsvertrag, Lohnabrechnung und Beendigungsdokument abgleichen. Diskrepanzen (zum Beispiel abweichender Beschäftigungszeitraum, fehlende Positionsbezeichnung) sind eigene Berichtigungspunkte.

### 3 — Notenrelevante Sätze markieren

Drei Sätze tragen typischerweise die Hauptnote eines qualifizierten Zeugnisses:

- **Zusammenfassende Leistungsbeurteilung** (Zufriedenheitsformel): Hauptträger der Leistungsnote → `references/zufriedenheitsformel.md`.
- **Verhaltensbeurteilung**: Trägt die Verhaltensnote. Reihenfolge Vorgesetzte vor Kollegen vor Kunden ist Pflicht.
- **Schlussformel**: Trägt die Signalwirkung; rechtlich nur eingeschränkt einklagbar → `references/schlussformel.md`.

Die übrigen Sätze stützen oder widerlegen diese Hauptnoten. Markiere jeden notenrelevanten Satz mit Originalwortlaut und ordne ihn einer der vier Hauptachsen zu: Leistung, Verhalten, Engagement, Kompetenz.

### 4 — Satzweise Ampel-Notenmatrix

Bilde für jeden notenrelevanten Satz vier Spalten:

1. Originalwortlaut.
2. Decodierte Aussage (was wäre die Klartextfassung).
3. Notentendenz 1 bis 6 (Spanne erlaubt).
4. Ampel Rot/Orange/Grün.

Material für die Decodierung:

- `references/zufriedenheitsformel.md` — Hauptformel mit Notenstufen.
- `references/geheimcode-katalog.md` — Standardformulierungen zu Leistung, Engagement, Belastbarkeit, Teamarbeit, Führung, Compliance.
- `references/ampel-flaggen.md` — Steigerungsadverbien (vollkommen, stets, überwiegend, im Wesentlichen ...), grüne, orange und rote Flaggen, negative Codeworte nach Themen (Alkohol, Krankheit, Diebstahl, Konflikt, Loyalität, Betriebsrat, sexuelle Verfehlungen, Mitläufertum, Auslassungen).

Wenn ein Satz so nicht im Katalog steht, leite die Tendenz aus dem objektiven Empfängerhorizont her und vermerke die Unsicherheit ausdrücklich (Beispiel: Tendenz Note 3, weil X; ohne BAG-Stütze; Live-Recherche empfohlen).

### 5 — Drift, Auslassungen und Widersprüche

- **Schaufenster-Drift:** Ein langer, sehr positiver Aufgabenkatalog steht neben einer schwachen Zufriedenheitsformel. Indiz für ein schönes Schaufenster mit harter Abwertung im Kern.
- **Bereichs-Drift:** Eine Achse (zum Beispiel Verhalten) wird auffallend knapper oder schwächer beschrieben als die andere.
- **Auslassungen:** Pflichten der Position werden nicht erwähnt, übliche Eigenschaften (Führung, Belastbarkeit, Loyalität) fehlen ganz, Kundenkontakt wird umgangen.
- **Widersprüche:** Hohe Einzelnoten in den Detailsätzen plus niedrige Hauptnote oder umgekehrt.
- **Negationen:** Doppelte Verneinung wie nicht unzuverlässig, nicht unhöflich.

Material: `references/analyse-techniken.md`.

### 6 — Gesamtnotenspanne und Hauptbefund

Aggregiere die satzweise Bewertung zu **einer begründeten Notenspanne**, nicht zu einer Punktezahl. Beispiel: Leistung 3 bis 3+, Verhalten 2 bis 3, Schluss neutral (Note 3 nicht angreifbar). Gesamtbild Note 3, mit Berichtigungspotenzial auf 2 bei nachweisbarer Zielerreichung in 2023/2024.

Halte folgende Trennungen sauber:

- Schlussformel-**Signalwirkung** ist nicht Schlussformel-**Anspruch**. Eine kalte Schlussformel signalisiert, lässt sich aber nur in Ausnahmefällen einklagen.
- **Wahrheits-** vor **Wohlwollens**-pflicht: Ein gutes Zeugnis darf nicht unwahr sein. Wohlwollen steuert die Ausdrucksweise, ersetzt aber keine Tatsachen.
- **Beweislast**: Bis Note 3 muss der Arbeitgeber begründen, warum nicht besser. Ab Note 2 muss der Arbeitnehmer belegen.

### 7 — Mandantenbericht und Verhandlungsmodul

Liefere dem Mandanten:

- Eine knappe Zusammenfassung (Notenspanne, Ampel-Verteilung, Hauptkritikpunkte).
- Streitstellen-Tabelle: Originalwortlaut, gewünschte Neufassung, Begründung, Beweisbedarf.
- Handlungsempfehlung: akzeptieren, nachverhandeln, formal auffordern, Vergleich nutzen, klagen.
- Eingeordnete Risikoabwägung (Bewerbungsdruck, Reputationsrisiko, Vergleichsbereitschaft).

Wenn nachverhandelt oder aufgefordert werden soll, baue daraus das **Aufforderungsschreiben** an den Arbeitgeber: vorgerichtlich, höflich, mit klaren Streitstellen und einer angemessenen Frist (in der Praxis zwei bis drei Wochen). Material und Mustertext: `references/mandatsmodule.md`.

### 8 — Klagestrategie Zeugnisberichtigung

Wenn der Arbeitgeber nicht oder unzureichend reagiert:

- **Antrag:** Verurteilung des Arbeitgebers zur Erteilung eines geänderten Zeugnisses mit präzise vorformuliertem Wortlaut.
- **Streitwert:** In der Regel ein Bruttomonatsgehalt nach ständiger Rechtsprechung der Arbeitsgerichte (live verifizieren).
- **Beweismittel:** Vorzeugnis, Zwischenzeugnis, Beurteilungsbögen, Zielerreichung, Zeugen, Lob-E-Mails.
- **Kostenrisiko:** § 12a ArbGG; in der ersten Instanz keine Erstattung gegnerischer Anwaltskosten.
- **Vergleichsfenster:** Häufig vor dem Gütetermin; halte einen vorformulierten Vergleichstext bereit.

Material und Musterantrag: `references/mandatsmodule.md`.

## Antwortformate

### Schnellscan

```
Kurzbild
- Zeugnisart:
- Notentendenz (Spanne):
- Hauptkritik:
- Eilbedarf:

Nächster Schritt
- Vorschlag in einem Satz.
```

### Vollanalyse

```
1. Kopfdaten und Zeugnisart sichern.
2. Notenrelevante Sätze markieren.
3. Leistung, Verhalten, Schluss, Auslassungen getrennt bewerten.
4. Drift und Widersprüche prüfen.
5. Gesamtnotenspanne bilden.
6. Streitstellen-Tabelle und Handlungsempfehlung.
```

Verwende Tabellen mit Spalten **Originalwortlaut · Decodierte Aussage · Note · Ampel**.

### Mandatsoutput

- Zusammenfassung für Mandant oder Mandantin in vier bis acht Sätzen.
- Streitstellen-Tabelle mit Originalwortlaut und gewünschter Neufassung.
- Beweislast und Belegbedarf pro Streitstelle.
- Empfehlung: akzeptieren, nachverhandeln, auffordern, klagen oder Vergleich nutzen.

## Sonderfälle

- **Leitende Positionen:** Führung, Budget, Strategie und Loyalität gesondert prüfen.
- **Ausbildungszeugnis (§ 16 BBiG):** Besonderheiten bei Berufsschule, Ausbildungsrahmenplan, Verhaltens- und Leistungsangabe nur auf Verlangen.
- **Branchen-Codes:** Banken, Vertrieb, Gesundheitswesen, öffentlicher Dienst, IT haben eigene Standardphrasen.
- **Entwurfsprüfung Arbeitgeberseite:** Prüfe rückwärts — was würde diesen Satz angreifbar machen?

Alle drei Sonderfälle: `references/muster-und-sonderfaelle.md`.

## Qualitätsgate vor jeder Ausgabe

- Sind Umlaute, ß, Namen, Daten und Zitate sauber übernommen?
- Ist die Zeugnisart richtig bestimmt?
- Sind Schlussformel-Signal und Schlussformel-Anspruch getrennt?
- Ist die Beweislast richtig herum dargestellt (bis Note 3 Arbeitgeber, ab Note 2 abwärts Arbeitnehmer)?
- Keine erfundenen Fundstellen, Zeugnisinhalte oder Noten?
- Wirkt das Ergebnis wie eine verwendbare anwaltliche Arbeitsfassung und nicht wie ein Schema?

## Testakten und Übungsmaterial

`references/muster-und-sonderfaelle.md` enthält drei vollständige Musterzeugnisse:

- Note 1 mit warmer Schlussformel (Positivreferenz).
- Gemischt mit Schaufenster-Drift bei Lernbereitschaft und Sozialverhalten.
- Rote Flaggen mit „bemüht", falscher Reihenfolge, „direkter Kommunikationsweise" und kalter Schlussformel.

Lies sie als Schulungsfälle, nicht als vorgefertigte Lösungen: erst Hypothese bilden, dann mit der Notenmatrix gegenprüfen.
