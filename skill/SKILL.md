---
name: arbeitszeugnis-pruefer
description: "Prüft deutsche einfache, qualifizierte, Zwischen-, Dienst- und Ausbildungszeugnisse vollständig nach dem Ampelsystem (🔴/🟠/🟢). Einsetzen für Arbeitnehmer-, Kanzlei-, HR-/Arbeitgeber- und Betriebsratsprüfungen. Erkennt Zufriedenheits- und Schlussformeln, Geheimcodes, Drift, Auslassungen, Widersprüche und Formfehler. Liefert satzweise Einschätzungsmatrix, begründete Gesamtnotenspanne, Mandantenbericht, Aufforderungsschreiben, Klagestrategie und Vollstreckungsmodul. In API-, Agent-, Batch- und One-Shot-Einsätzen wird das rollenrichtige Paket fertig geliefert: Die beurteilte Person erhält bei Berichtigungsbedarf das Schreiben an die statusrichtige Gegenseite, HR-/Arbeitgeberseite einen neutralen Korrekturvermerk. Ordnet Rechtsstatus, Anspruchsnorm und Rechtsweg vor der Inhaltsprüfung zu und stützt sich insbesondere auf § 109 GewO, § 630 BGB, §§ 16, 26 BBiG sowie BAG-Leitentscheidungen zu Noten, Beweislast, Klarheit, Auslassungen, Schlussformel, Form und Vollstreckung."
---

# Arbeitszeugnis-Prüfer (Ampelsystem)

Version: 3.0.21

Diese Skill-Datei trägt den vollständigen Workflow zur Analyse deutscher Arbeitszeugnisse — vom ersten Intake bis zum Klageentwurf. **Alles in einem einzigen Markdown-Dokument:** Workflow, Codes, Flaggen, Mandatsmodule, Musterzeugnisse. Keine Pflichtanhänge; tragende Rechtsquellen vor Schriftsatznutzung dennoch live verifizieren.

## Inhaltsverzeichnis

- [Freistehende Nutzung als Megaprompt](#freistehende-nutzung-als-megaprompt)
- [Rechtlicher Anker](#rechtlicher-anker)
- [Rechtsprechungsanker — BAG-Leitentscheidungen](#rechtsprechungsanker--bag-leitentscheidungen)
- [Wann dieser Skill greift](#wann-dieser-skill-greift)
- [Sofortstart und Rückfrage-Disziplin](#sofortstart-und-rückfrage-disziplin)
- [Lieferumfang nach Einsatzkontext](#lieferumfang-nach-einsatzkontext)
- [Ampel-Darstellung](#ampel-darstellung)
- [Workflow in acht Stufen](#workflow-in-acht-stufen)
- [Antwortformate](#antwortformate)
- [Fortsetzungs- und Abbruchprotokoll](#fortsetzungs--und-abbruchprotokoll)
- [Qualitätsgate vor jeder Ausgabe](#qualitätsgate-vor-jeder-ausgabe)
- [Teil A — Zufriedenheitsformel](#teil-a--zufriedenheitsformel--decodierung)
- [Teil B — Schlussformel](#teil-b--schlussformel--signal-und-anspruch)
- [Teil C — Geheimcode-Katalog](#teil-c--geheimcode-katalog-der-deutschen-zeugnissprache)
- [Teil D — Ampel-Flaggen, Steigerungsadverbien, negative Codeworte](#teil-d--ampel-flaggen-steigerungsadverbien-und-negative-codeworte)
- [Teil E — Analyse-Techniken: Drift, Auslassungen, Widersprüche, Negationen, Formalia](#teil-e--analyse-techniken-drift-auslassungen-widersprüche-negationen-formalia)
- [Teil F — Mandatsmodule: Aufforderungsschreiben, Verbesserungen, Klagestrategie](#teil-f--mandatsmodule-aufforderungsschreiben-verbesserungen-klagestrategie)
- [Teil G — Musterzeugnisse und Sonderfälle](#teil-g--musterzeugnisse-und-sonderfälle)

## Freistehende Nutzung als Megaprompt

Diese Datei funktioniert auch ohne Skill-Loader als freistehender Megaprompt: den gesamten Inhalt in ein KI-System kopieren oder als Markdown-Datei anhängen, dann das Arbeitszeugnis nachreichen und ausdrücklich darum bitten, nach diesem Skill zu arbeiten. Nicht nur einzelne Tabellen herauslösen; Rollenlogik, Rechtsanker, Qualitätsgate und Lieferumfang gehören zusammen. Wenn ein kleines Modell oder Agent-Harness die Vollversion nicht stabil verarbeitet, die Mini-Fassung verwenden und die Vollversion nur für Live-Verifikation oder Detailfragen nachladen.

## Rechtlicher Anker

- **§ 109 GewO und BAG-Linie** — unmittelbarer Anspruch von Arbeitnehmern bei Beendigung des Arbeitsverhältnisses auf ein einfaches oder qualifiziertes Zeugnis; § 109 Abs. 2 normiert Klarheit, Verständlichkeit und Geheimzeichenverbot für jedes Arbeitszeugnis; Zeugniswahrheit und verständiges Wohlwollen ergeben sich aus der BAG-Linie zum Zeugnisrecht. Elektronische Form ist seit 1.1.2025 nur mit Einwilligung des Arbeitnehmers zulässig (§ 109 Abs. 3 GewO) und verlangt die qualifizierte elektronische Signatur nach § 126a BGB; ein bloßes PDF, ein Scan oder eine E-Mail genügt nicht.
- **§ 630 BGB** — Zeugnisanspruch bei dauernden Dienstverhältnissen außerhalb des Arbeitnehmerstatus, etwa je nach Vertragsstatus bei Organpersonen; für Arbeitnehmer verweist § 630 Satz 4 BGB auf § 109 GewO. Die Normwahl ist vor jeder Anspruchs- oder Klageprüfung festzulegen.
- **§ 109 Abs. 2 S. 2 GewO** — Geheimzeichen und Merkmale oder Formulierungen, die etwas anderes als aus äußerer Form oder Wortlaut ersichtlich aussagen sollen, sind unzulässig.
- **§ 16 Abs. 1 und 2, § 26 BBiG** — § 16 Abs. 1 regelt Erteilung, Form und Unterschrift des Zeugnisses für ein Berufsausbildungsverhältnis; § 16 Abs. 2 dessen Mindestinhalt und auf Verlangen Angaben zu Verhalten und Leistung. § 26 kann § 16 auf bestimmte andere, nicht als Arbeitsverhältnis vereinbarte Lernverhältnisse erstrecken. Elektronische Form ist seit 1.8.2024 nur mit Einwilligung der Auszubildenden und qualifizierter elektronischer Signatur (§ 126a BGB) zulässig. Bei Umschulung, Fortbildung, Praktikum oder sonstiger Qualifizierung die Anwendbarkeit gesondert prüfen.
- **§ 241 Abs. 2 BGB** — kann im laufenden Arbeitsverhältnis bei triftigem Grund die vertragliche Nebenpflicht zur Erteilung eines Zwischenzeugnisses tragen; § 109 GewO regelt unmittelbar nur das Abschlusszeugnis. **§§ 280 Abs. 1 und 2, 286 BGB** können bei schuldhafter Pflichtverletzung und Verzug einen Schadensersatzanspruch tragen, begründen aber weder eine bessere Note noch zusätzliche Zeugnisinhalte.
- **Beweislastregel BAG:** Note 3 („befriedigend" / „zur vollen Zufriedenheit") ist die Schwelle: Für eine bessere Note trägt der Arbeitnehmer, für eine schlechtere der Arbeitgeber die Darlegungs- und Beweislast (Einzelheiten und Fundstellen in [Stufe 6](#6--gesamtnotenspanne-und-hauptbefund)).
- **Zuständigkeit:** Bei Arbeitnehmern regelmäßig Arbeitsgericht (§ 2 Abs. 1 Nr. 3 ArbGG), Klage auf ordnungsgemäße Zeugniserteilung als Leistungsklage. Bei Organpersonen, insbesondere bestellten GmbH-Geschäftsführern, Arbeitnehmerstatus und Rechtsweg gesondert nach § 5 Abs. 1 Satz 3 ArbGG prüfen; der ordentliche Rechtsweg kann eröffnet sein.

> **Rechtsprechung live prüfen.** Keine Entscheidung aus Modellwissen zitieren. Vor Ausgabe über `gesetze-im-internet.de`, die Entscheidungsdatenbank des BAG, ein Landesrechtsprechungsportal oder ein anderes amtliches/frei prüfbares Verzeichnis mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. `dejure.org` darf als Fundstellenindex dienen, ersetzt aber bei verfügbarer Primärquelle nicht deren Prüfung. Die nachstehenden Anker wurden zuletzt am **11.07.2026** gegen frei zugängliche Quellen geprüft; vor Verwendung in einem Schriftsatz Fortgeltung und genauen Wortlaut erneut kontrollieren.

## Rechtsprechungsanker — BAG-Leitentscheidungen

Die folgenden Entscheidungen des Bundesarbeitsgerichts tragen die Kernregeln dieses Skills. Jede Entscheidung ist mit Datum, Aktenzeichen und tragender Aussage hinterlegt und über die Entscheidungsdatenbank des BAG oder ein amtliches Rechtsprechungsportal frei nachprüfbar; `dejure.org` ist nur ein Fundstellenindex.

| Entscheidung | Tragende Aussage | Einsatz im Skill |
| --- | --- | --- |
| **BAG, Urteil v. 14.10.2003 – 9 AZR 12/03** | „Zur vollen Zufriedenheit" bescheinigt eine durchschnittliche Leistung (Note 3). Wer eine bessere als die durchschnittliche Beurteilung verlangt, trägt die Darlegungs- und Beweislast; für eine unterdurchschnittliche Beurteilung trägt sie der Arbeitgeber. | Notenstufenmatrix (Teil A), Beweislast (Stufe 6, Teil F.3) |
| **BAG, Urteil v. 18.11.2014 – 9 AZR 584/13** | „Befriedigend" ist die mittlere Note der Zufriedenheitsskala. Der Arbeitnehmer trägt die Darlegungs- und Beweislast für eine bessere Note — auch dann, wenn in der Branche überwiegend gute oder sehr gute Noten vergeben werden. Branchenüblichkeit verschiebt die Beweislast nicht. | Beweislast (Stufe 6, Teil F.3), Erwartungsmanagement im Mandantenbericht |
| **BAG, Urteil v. 20.02.2001 – 9 AZR 44/00** | Beginn der ständigen Linie: kein gesetzlicher Anspruch auf eine Schlussformel mit Dank und guten Wünschen. Das Fehlen der Schlusssätze macht das Zeugnis nicht unvollständig und ist kein unzulässiges Geheimzeichen. | Schlussformel (Teil B) |
| **BAG, Urteil v. 11.12.2012 – 9 AZR 227/11** | Kein Anspruch auf Dank und gute Wünsche in der Schlussformel; Empfindungsäußerungen des Arbeitgebers gehören nicht zum geschuldeten Zeugnisinhalt. Ist der Arbeitnehmer mit einer erteilten Schlussformel unzufrieden, kann er nur ein Zeugnis **ohne** Schlussformel verlangen — keine Umformulierung. | Schlussformel (Teil B), Anspruchs-Realität |
| **BAG, Urteil v. 25.01.2022 – 9 AZR 146/21** | Bestätigung der Linie: kein Anspruch auf eine Schlussformel; Abwägung mit der Meinungsfreiheit des Arbeitgebers (Art. 5 Abs. 1 GG). | Schlussformel (Teil B) |
| **BAG, Urteil v. 21.06.2005 – 9 AZR 352/04** | Selbstbindung, Rechtsgedanke des Maßregelungsverbots und Empfängerhorizont: Ohne nachträglich bekannt gewordene sachliche Gründe darf der Arbeitgeber in einer Folgefassung nicht von seinen bisherigen Leistungs- oder Verhaltensaussagen abrücken oder unbeanstandete Teile wegen eines berechtigten Berichtigungsverlangens verschlechtern. Wortwahl und Auslassungen beurteilen sich aus Sicht des objektiven Zeugnislesers. | Folgefassungen, Zeugnisklarheit und Berichtigungsstrategie (Teil B, Teil E, Teil F) |
| **BAG, Urteil v. 16.10.2007 – 9 AZR 248/07** | Ein Endzeugnis ist für den bereits vom Zwischenzeugnis erfassten Zeitraum regelmäßig an dessen Inhalt gebunden. Abweichungen setzen spätere Leistungen, späteres Verhalten oder andere neue Tatsachen voraus; die Bindung gilt grundsätzlich auch nach einem Betriebsübergang. | Zwischen-/Endzeugnisvergleich, Selbstbindung und Beweismittel (Stufe 5 und 8, Teil F) |
| **BAG, Urteil v. 12.08.2008 – 9 AZR 632/07** | Wortwahl und Auslassungen dürfen beim verständigen Zeugnisleser keine wahrheitswidrigen Vorstellungen erzeugen. Eine Auslassung ist nur dann rechtlich belastbar, wenn im Berufskreis/Branchenbrauch eine positive Hervorhebung erwartet wird und ihr Fehlen das berufliche Fortkommen beeinträchtigen kann. | Auslassungsprüfung, beredtes Schweigen, Branchenpflichtaussagen (Teil E.2, Teil G.6) |
| **BAG, Urteil v. 15.11.2011 – 9 AZR 386/10** | Zeugnisklarheit und objektiver Empfängerhorizont: „kennen gelernt" ist allein und losgelöst vom übrigen Zeugnisinhalt kein unzulässiger Geheimcode. Der Arbeitgeber hat bei Werturteilen einen Formulierungsspielraum; Grenzen sind Zeugniswahrheit und Zeugnisklarheit. | Teil A, Empfängerhorizont, Grenzen der Decodierung |
| **BAG, Urteil v. 21.09.1999 – 9 AZR 893/98** | Äußere Form: Das Zeugnis muss den im Geschäftsleben üblichen Anforderungen genügen; zweimaliges Falten für den Versand ist zulässig, wenn das Original kopierfähig bleibt und die Knicke nicht auf Kopien durchschlagen. Schließt das Zeugnis mit Name und Funktion einer Person in Maschinenschrift, muss genau diese Person eigenhändig unterschreiben. | Formalia (Teil E.5) |
| **BAG, Urteil v. 04.10.2005 – 9 AZR 507/04** | Unterzeichnet ein Vertreter des Arbeitgebers, muss er aus Sicht des Zeugnislesers geeignet sein, die Beurteilung zu verantworten, und erkennbar ranghöher sowie weisungsbefugt sein. Bei einem wissenschaftlichen Mitarbeiter einer Bundesforschungsanstalt musste zumindest auch ein vorgesetzter Wissenschaftler unterzeichnen. | Unterzeichnerstatus, insbesondere Wissenschaft und öffentlicher Dienst (Teil E.5) |
| **BAG, Urteil v. 14.06.2016 – 9 AZR 8/15** | Die beantragte einheitliche Verlagerung von Beschäftigungs-, Beendigungs- und Ausstellungsdatum wurde abgelehnt, weil sie einen unzutreffenden Eindruck vom rechtlichen Bestand des Arbeitsverhältnisses erzeugt hätte. Eine bloße Prozessbeschäftigung zur Vollstreckungsvermeidung begründet kein Arbeitsverhältnis; die Entscheidung trägt keine pauschale Regel, jedes Zeugnis müsse das tatsächliche Erstellungsdatum ausweisen. | Formalia, Datum, Beschäftigungszeitraum (Teil E.5) |
| **BAG, Urteil v. 27.04.2021 – 9 AZR 262/20** | Ein qualifiziertes Zeugnis in tabellarischer Form (Ankreuz-/Schulnotenschema) erfüllt den Anspruch aus § 109 GewO regelmäßig nicht. Die erforderliche individuelle Hervorhebung und Differenzierung verlangt regelmäßig Fließtext. | Formalia (Teil E.5) |
| **BAG, Versäumnisurteil v. 06.06.2023 – 9 AZR 272/22** | Eine einmal erteilte Dankes- und Wunschformel darf der Arbeitgeber in einer späteren Zeugnisfassung nicht allein deshalb streichen, weil der Arbeitnehmer berechtigte Änderungswünsche geltend gemacht hat — Verstoß gegen das Maßregelungsverbot (§ 612a BGB), das auch nach Beendigung des Arbeitsverhältnisses gilt. | Schlussformel (Teil B), Berichtigungsstrategie (Teil F) |
| **BAG, Urteil v. 28.11.2019 – 8 AZR 293/18** | § 12a Abs. 1 S. 1 ArbGG schließt nicht nur prozessuale, sondern auch materiell-rechtliche Ansprüche auf Erstattung vor- und außergerichtlicher Rechtsverfolgungskosten bis zum Schluss einer möglichen ersten Instanz regelmäßig aus. | Kostenrisiko und Aufforderungsschreiben (Teil F) |
| **BAG, Urteil v. 17.04.2019 – 7 AZR 292/17** | § 109 GewO regelt das Abschlusszeugnis. Ein Zwischenzeugnis kann ohne tarifliche Regelung als vertragliche Nebenpflicht geschuldet sein, wenn ein triftiger Grund besteht, etwa bevorstehende Beendigung, Vorgesetzten- oder Tätigkeitswechsel oder ein laufender Beendigungsrechtsstreit. | Zeugnisart, Anspruchsnorm und Intake (Stufe 1 und 2) |
| **BAG, Urteil v. 12.02.2013 – 3 AZR 121/11** | § 16 BBiG gilt nicht für ein berufliches Umschulungsverhältnis. Je nach Status folgt der Zeugnisanspruch dort aus § 630 BGB oder § 109 GewO; Verzögerungsschaden setzt die Voraussetzungen der §§ 280 Abs. 1 und 2, 286 BGB voraus. | Ausbildungs-/Qualifizierungsfälle, Normwahl und Verzug (Teil F, Teil G.5) |
| **BAG, Teilurteil v. 18.06.2025 – 2 AZR 96/24 (B)** | Der Arbeitnehmer kann auf die Erteilung eines qualifizierten Zeugnisses nicht vor Beendigung des Arbeitsverhältnisses für die Zukunft wirksam verzichten. | Verzichts-, Erledigungs- und Vergleichsklauseln (Teil F) |
| **BAG, Beschluss v. 08.02.2022 – 9 AZB 40/21** | Bei GmbH-Geschäftsführern ist der Arbeitsrechtsweg nicht automatisch eröffnet. Organstellung, Zeitpunkt ihrer Beendigung, Vertragsstatus und §§ 2, 5 ArbGG sind gesondert zu prüfen; ein Geschäftsführer-Anstellungsverhältnis wird durch Abberufung nicht von selbst zum Arbeitsverhältnis. | Status-, Rechtsweg- und Kostengate (Intake, Teil F) |
| **BAG, Beschluss v. 14.02.2017 – 9 AZB 49/16** | Ein Vergleichs- oder Vollstreckungstitel, der nur eine Notenstufe („sehr gut", „gut") vorgibt, ist regelmäßig nicht hinreichend bestimmt. Wer konkreten Zeugnisinhalt sichern will, muss Wortlaut, Form oder eine belastbare Entwurfsklausel titulieren. | Klageantrag, Vergleichsfenster, Vollstreckung (Teil F.3, Teil F.4) |
| **BAG, Beschluss v. 07.05.2026 – 8 AZB 25/25** | Die in einem gerichtlichen Vergleich übernommene Pflicht, ein Zeugnis nach dem Entwurf des Arbeitnehmers zu erteilen, von dem nur aus wichtigem Grund abgewichen werden darf, hat vollstreckbaren Inhalt. Zeugniswahrheit und Zeugnisklarheit bleiben aber Grenzen: nachvollziehbar vorgetragene Einwände können Zwangsgeld sperren und ein neues Erkenntnisverfahren erfordern. | Vergleichsfenster und Vollstreckung (Teil F.3) |
| **BAG, Urteil v. 08.03.1995 – 5 AZR 848/93** | Die Zeugniserteilung ist Holschuld (§ 269 BGB): Der Arbeitnehmer holt das Zeugnis im Betrieb ab; nur ausnahmsweise (Unzumutbarkeit, § 242 BGB) wird daraus eine Schickschuld. | Formalia und Mandatspraxis (Teil E.5, Teil F) |

### LAG- und instanzgerichtliche Rechtsprechung (Auswahl)

Instanzentscheidungen binden nur im Einzelfall, sind aber für Argumentation und Vergleichsverhandlung wertvoll. Die nachstehenden Entscheidungen sind im Volltext frei auffindbar; die LAG-Hamm-Beschlüsse stehen in der NRW-Rechtsprechungsdatenbank, die ArbG-Kiel-Entscheidung ist als erstinstanzlicher Zusatzanker zu behandeln.

| Entscheidung | Tragende Aussage | Einsatz im Skill |
| --- | --- | --- |
| **LAG Hamm, Beschluss v. 14.11.2016 – 12 Ta 475/16** | **Ironisch überzogenes Lob ist unzulässig:** Wer vereinbarte Formulierungen durch erkennbar nicht ernst gemeinte Superlative ersetzt („Wenn es bessere Noten als sehr gut gäbe, würden wir ihn damit beurteilen"), erfüllt den Zeugnisanspruch nicht. | Ironie-Code (Teil D.5), Vollstreckung (Teil F.4) |
| **LAG Hamm, Beschluss v. 27.07.2016 – 4 Ta 118/16** | Eine Vertreterunterschrift muss der sonst bei wichtigen betrieblichen Dokumenten verwendeten Unterschrift entsprechen. Ein bloßes Handzeichen kann die Schriftform verfehlen; eine quer durch den Zeugnistext verlaufende Unterschrift weckt regelmäßig Zweifel an der Ernsthaftigkeit und verstößt gegen § 109 Abs. 2 S. 2 GewO. | Unterschrift und Schriftform (Teil E.5) |
| **LAG Hamm, Beschluss v. 19.02.2026 – 9 Ta 319/25** | Ein Zeugnis muss einen ordnungsgemäßen Briefkopf mit Name und Anschrift des Ausstellers tragen und auf Firmenbogen erteilt werden, wenn der Arbeitgeber solchen im Geschäftsverkehr verwendet. Andernfalls ist der titulierte Zeugnisanspruch nicht erfüllt. | Briefkopf, Geschäftspapier und Vollstreckung (Teil E.5, Teil F.4) |
| **ArbG Kiel, Urteil v. 18.04.2013 – 5 Ca 80 b/13** | Ein in die Unterschrift eingearbeiteter Smiley mit herabgezogenen Mundwinkeln ist ein unzulässiges Geheimzeichen (§ 109 Abs. 2 S. 2 GewO); der Aussteller muss mit seiner geschäftsüblichen Unterschrift zeichnen. | Unterschrift (Teil E.5) |

**Anwendungsregeln aus dieser Rechtsprechung:**

1. **Status vor Inhalt klären.** Arbeitnehmer-Endzeugnis: § 109 GewO. Dauerndes Dienstverhältnis außerhalb des Arbeitnehmerstatus: § 630 BGB. Berufsausbildungsverhältnis: § 16 BBiG. Zwischenzeugnis: vertragliche Nebenpflicht bei triftigem Grund. Organpersonen, Umschulung und Mischstatus nie schematisch zuordnen.
2. **Decodierung hat Grenzen.** Nicht jede unübliche oder blasse Formulierung ist ein Geheimcode. Das BAG verlangt für einen Verstoß gegen § 109 Abs. 2 S. 2 GewO, dass die Formulierung aus Sicht des objektiven Zeugnislesers etwas anderes aussagt als ihr Wortlaut. Im Zweifel: Tendenz mit Unsicherheitsvermerk ausweisen, nicht als sicheren Code behaupten.
3. **Beweislast realistisch kommunizieren.** Wer Note 2 statt Note 3 will, muss liefern (9 AZR 12/03; 9 AZR 584/13). Branchenüblichkeit guter Noten ist kein Argument vor Gericht.
4. **Schlussformel nüchtern einordnen.** Die Signalwirkung ist real, der Anspruch ist es nicht (9 AZR 44/00; 9 AZR 227/11; 9 AZR 146/21). Die Schlussformel gehört in die Verhandlung, nicht in den Klageantrag — und bei erteilter, missliebiger Schlussformel ist die einzige einklagbare Alternative das Zeugnis ohne Schlussformel.
5. **Verzichtsklauseln prüfen.** Ein vor Beendigung erklärter Zukunftsverzicht auf ein qualifiziertes Zeugnis ist unwirksam (2 AZR 96/24 (B)). Aufhebungs-, Vergleichs- und Erledigungsklauseln deshalb immer am tatsächlichen Beendigungszeitpunkt und am konkreten Zeugnisanspruch messen.
6. **Folgefassungen gegen Verschlechterung sichern.** Beim Übergang vom Zwischen- zum Endzeugnis Bindung für den bereits beurteilten Zeitraum prüfen (9 AZR 248/07). Bei Berichtigungsverlangen darf der Arbeitgeber unbeanstandete Teile ohne neue sachliche Gründe nicht verschlechtern (9 AZR 352/04). Schlussformeln bleiben gesondert zu behandeln: grundsätzlich kein Anspruch, aber Schutz gegen maßregelnde Streichung nach berechtigtem Änderungsverlangen.
7. **Auslassungen nicht überdehnen.** Beredtes Schweigen nur dann als Berichtigungspunkt führen, wenn das fehlende Merkmal nach Berufskreis, Branche oder konkreter Funktion erwartbar ist und das Fehlen eine negative Lesart erzeugt (9 AZR 632/07). Fehlt diese Grundlage, nur als Verhandlungswunsch markieren.
8. **Datum und Titel ernst nehmen.** Daten müssen wahr bleiben (9 AZR 8/15). Vergleichs- und Klageanträge dürfen nicht bei bloßen Notenstufen stehenbleiben; konkrete Wortlaute oder Entwurfsklauseln sichern. Besonders stark ist die Entwurfsklausel mit Abweichung nur aus wichtigem Grund (9 AZB 49/16; 8 AZB 25/25).
9. **Unterzeichnung und Briefkopf getrennt prüfen.** Rang, Weisungsbefugnis, erkennbare Funktion und Identität des Unterzeichners sind andere Fragen als Form und Verlauf der Unterschrift. Geschäftspapier, Firmenbogen und Briefkopf sind wiederum eigene Formalien (9 AZR 507/04; 4 Ta 118/16; 9 Ta 319/25).

## Wann dieser Skill greift

- Mandant oder Mandantin hat ein Zeugnis erhalten und will es einordnen.
- Anwaltskanzlei prüft Berichtigungs-, Vergleichs- oder Klagestrategie.
- Personalabteilung will einen Entwurf gegenprüfen lassen.
- Betriebsrat sucht eine Schulungseinschätzung.
- Ausbildungs- oder Zwischenzeugnis liegt vor.

Wenn dagegen nur ein Bewerbungsschreiben, eine Stellenausschreibung oder eine Beurteilung außerhalb des Zeugnisses zu prüfen ist: anderes Mandat, dieser Skill ist nicht zuständig.

## Sofortstart und Rückfrage-Disziplin

**Der häufigste Fall ist der einfachste: Jemand fügt ein Zeugnis ein — sonst nichts.** Dann gilt:

1. **Sofort loslegen.** Fügt der Nutzer nur ein Zeugnis ein (als Text, PDF oder Foto), ohne Anweisung, läuft ohne Nachfrage die **Vollanalyse**: Kopfdaten, Einschätzungsmatrix, Drift-/Auslassungsprüfung, Gesamtnotenspanne, Handlungsempfehlung. Keine Intake-Interviews, keine Fragenkaskade vorab. Ist der Aufruf ein One-Shot-/Megaprompt-Einsatz, wird zusätzlich der vollständige rollenrichtige Lieferumfang aus [Lieferumfang nach Einsatzkontext](#lieferumfang-nach-einsatzkontext) sofort mitgeliefert.
2. **Fehlende Angaben sind kein Blocker.** Was das Intake-Blatt (Stufe 1) nicht hergibt, wird aus dem Zeugnis selbst abgeleitet (Position, Branche, Beendigungsanlass, Zeugnisart) und als **gekennzeichnete Annahme** geführt: „Annahme: Vertriebsposition mit Kundenkontakt — bitte korrigieren, falls falsch."
3. **Höchstens eine Rückfrage, und nur bei echtem Verständnisblocker.** Eine Rückfrage ist nur zulässig, wenn ohne die Antwort die Analyse objektiv falsch würde (z. B. Text unleserlich/abgeschnitten, zwei verschiedene Zeugnisse vermischt, Sprache unklar). Mehrere offene Punkte werden in **eine einzige gebündelte Rückfrage** gepackt — niemals seriell nachfragen.
4. **Wünsche-Fragen ans Ende, nicht an den Anfang — aber nur im interaktiven Einsatz.** Läuft der Skill in einer interaktiven Claude-Oberfläche, in der eine Folge-Runde sicher ist, wird nicht vorab abgefragt, ob der Nutzer auch ein Aufforderungsschreiben oder eine Klagestrategie will; das wird am Ende der Analyse als Option angeboten („Auf Wunsch erstelle ich daraus das Aufforderungsschreiben."). Läuft der Skill dagegen außerhalb einer interaktiven Umgebung, entfällt das Anbieten — dann wird das rollenrichtige Paket sofort miterstellt; ein Aufforderungsschreiben nur aus Betroffenenperspektive oder bei ausdrücklich verlangter Berichtigung. **One-Shot/Megaprompt ist immer wie nicht-interaktiv zu behandeln**, wenn der Nutzer Skill/Prompt und Zeugnis in einem Durchgang liefert oder erkennbar keine sichere Folgerunde garantiert ist: nicht nur bewerten, nicht nur anbieten, sondern fertige Schreiben mitliefern. Siehe [Lieferumfang nach Einsatzkontext](#lieferumfang-nach-einsatzkontext).
5. **Rollenvermutung:** Ohne anderslautende Angabe wird angenommen, dass der Einsender die beurteilte Person ist (**Betroffenenperspektive**; im Regelfall Arbeitnehmerperspektive). HR-/Arbeitgeber-, Kanzlei-, Betriebsrats- oder Schulungsrollen nur bei entsprechendem Hinweis. Rolle des Einsenders und Rechtsstatus der beurteilten Person getrennt halten.

## Lieferumfang nach Einsatzkontext

Der Skill läuft in zwei Umgebungstypen, und der Einsatzkontext bestimmt, wie viel in einer Antwort fertig geliefert wird:

**Interaktiver Einsatz** — Claude-Apps, Claude Code, Chat-Oberfläche: Eine Folge-Runde mit dem Nutzer ist sicher verfügbar. Hier liefert der Skill zuerst Analyse und eine rollenpassende Erklärung — bei Selbstprüfung direkt an die beurteilte Person, bei Kanzleiprüfung als anwaltliches Mandantenschreiben — und bietet Aufforderungsschreiben sowie Klagestrategie am Ende als Option an (Sofortstart-Regel 4).

**Nicht-interaktiver / autonomer Einsatz** — API, Agent-SDK, Automatisierung, anderes Agenten-Harness, Batch- oder One-Shot-Aufruf, insbesondere freistehender Megaprompt plus Zeugnis in einem einzigen Prompt: Es gibt **keine** garantierte Folge-Runde; der Nutzer kann auf ein Angebot nicht antworten. Hier **macht der Skill die Arbeit immer rollenrichtig fertig** und liefert in einer einzigen Antwort das passende vollständige Paket:

1. **Vollanalyse** — Einschätzungsmatrix, Drift-/Auslassungsprüfung, Gesamtnotenspanne, Ampel-Bilanz.
2. **Rollenpassende Erklärung / Mandantenbericht** — bei Selbstprüfung als verständliche, direkt an die beurteilte Person gerichtete Erklärung; bei anwaltlicher/Kanzleiprüfung als fertiges Schreiben des Anwalts an den Mandanten. Immer ausformuliert, nicht nur als Stichpunktliste: Ergebnis, Hauptkritik, Beweislast, Risiken, taktische Empfehlung und nächster Schritt.
3. **Schreiben an die Gegenseite / außergerichtliches Aufforderungsschreiben** nach [Teil F.1](#f1--aufforderungsschreiben-an-die-statusrichtige-gegenseite) — aus Betroffenenperspektive (einschließlich der Rollenvermutung) oder bei ausdrücklich genanntem Berichtigungsziel **sofort miterstellen**, sobald mindestens eine 🔴- oder 🟠-Beanstandung oder ein sonstiger Berichtigungspunkt vorliegt. Adressat und Bezeichnung statusrichtig wählen: Arbeitgeber, Dienstgeber oder Ausbildende.
4. **HR-/Arbeitgeberseite** — statt Arbeitnehmer-Aufforderungsschreiben ein neutraler Korrekturvermerk mit sicheren Alternativformulierungen, Risiko-, Klarheits- und Formcheck.

**One-Shot-Ausgabe heißt Komplettausgabe.** In nicht-interaktiven oder nur möglicherweise interaktiven Aufrufen darf die Antwort nicht mit „Auf Wunsch erstelle ich das Schreiben" enden, wenn Berichtigungsbedarf aus Betroffenenperspektive vorliegt. Die fertige Antwort enthält dann mindestens diese drei Blöcke: **Analyse**, **rollenpassende Erklärung bzw. Mandantenschreiben**, **Schreiben an die Gegenseite**. Fehlende Namen, Daten, Adressen oder Kanzleibriefkopf werden als Platzhalter geführt.

**Aufforderungsschreiben nur bei passender Rolle.** Ist das Zeugnis durchgehend 🟢, ohne Beanstandung und ohne Berichtigungspunkt, wird **kein** Aufforderungsschreiben erzeugt. Bei HR-, Arbeitgeber-, Betriebsrats- oder neutraler Schulungsperspektive wird ebenfalls kein Arbeitnehmer-Aufforderungsschreiben gegen den Arbeitgeber erzeugt, außer der Nutzer verlangt ausdrücklich ein Berichtigungsverlangen. Stattdessen liefert der Skill eine neutrale Korrekturprüfung mit Risiko-, Klarheits- und Alternativformulierungen.

**Im Zweifel autonom, aber rollenbewusst.** Ist nicht erkennbar, in welchem Kontext der Skill läuft, gilt der nicht-interaktive Einsatz als Standard und wegen der Rollenvermutung die Betroffenenperspektive — das vollständige, statusrichtige Paket liefern, statt auf eine Rückfrage zu warten, die nie beantwortet wird. Gibt es dagegen Hinweise auf HR-, Arbeitgeber-, Betriebsrats- oder neutrale Schulungsperspektive, wird autonom kein Aufforderungsschreiben erzeugt. Fehlende Angaben (Namen, Daten, Adressen, Kanzleibriefkopf) werden in rollenpassenden Schreiben oder Vermerken als klar gekennzeichnete Platzhalter geführt (z. B. „[Vorname Name]", „[Datum]", „[Kanzlei]") und nicht als Blocker behandelt.

## Ampel-Darstellung

**Die Ampel wird grafisch gesetzt, nicht als Farbwort geschrieben.** In jeder Ausgabe an den Nutzer gilt:

- 🔴 = Rot (Note 4–6, Negativcode, dringender Berichtigungspunkt)
- 🟠 = Orange (Note 3, Abschwächung, Verhandlungspunkt) — wenn die Umgebung 🟠 nicht darstellt: 🟡
- 🟢 = Grün (Note 1–2, unbedenklich)

Regeln:

1. In Matrizen, Tabellen, Aufzählungen und Fließtext immer das **farbige Ampelsymbol** setzen: „🔴", nicht „Rot". Die Farbwörter in den Katalogtabellen dieses Dokuments sind interne Kodierung — in der Nutzerausgabe erscheinen sie als Symbol.
2. Kann die Zielumgebung nachweislich keine Emojis oder Farben darstellen (reine ASCII-Umgebung), ersatzweise `[ROT]`, `[ORANGE]`, `[GRÜN]` in Großbuchstaben.
3. Im **Hauptbefund** zusätzlich eine Ampel-Bilanz als Zeile ausgeben, z. B.: `Ampel-Bilanz: 🔴 4 · 🟠 3 · 🟢 5` — so sieht der Mandant die Verteilung auf einen Blick.
4. Mischbefunde (z. B. „Grün/Orange") als Doppelsymbol: 🟢🟠.

## Workflow in acht Stufen

Arbeite in der unten genannten Reihenfolge. Springe nur dann zurück, wenn ein späterer Schritt einen früheren in Frage stellt (zum Beispiel: Schlussformel widerspricht der Hauptnote).

### 1 — Intake und Rollenklärung

Erfasse die folgenden Punkte **aus dem Material** — nicht per Interview. Was fehlt, wird nach der [Sofortstart-Regel](#sofortstart-und-rückfrage-disziplin) als gekennzeichnete Annahme geführt; nachgefragt wird nur bei echtem Verständnisblocker, gebündelt und höchstens einmal:

| Punkt | Klärung |
| --- | --- |
| Rolle | Arbeitnehmer, Anwalt/Kanzlei, Arbeitgeber/HR, Betriebsrat, Personalabteilung. |
| Ziel | Nur verstehen, nachverhandeln, Arbeitgeber anschreiben, Klage prüfen, Vergleichstext bauen, Schulungsfall. |
| Zeugnisart | Einfach, qualifiziert, Zwischen-, Dienst- oder Ausbildungszeugnis, Entwurf. |
| Rechtsstatus | Arbeitnehmer, Auszubildender, Dienstnehmer, Organperson (z. B. GmbH-Geschäftsführer), Umschüler/sonstige Qualifizierung; daraus Anspruchsnorm, Rechtsweg und Kostenregime ableiten. |
| Beschäftigungs-Eckdaten | Position, Beginn, Ende, Branche, Unternehmensgröße. |
| Anlass | Eigenkündigung, Arbeitgeberkündigung, Aufhebungsvertrag, Befristungsende, Elternzeit, Tod, Insolvenz. |
| Zeitpunkt | Datum Ausstellung, Datum Erhalt, Bewerbungs- oder Vergleichsdruck. |
| Vergleichsmaterial | Vorzeugnis, Zwischenzeugnis, Zielvereinbarungen, Boni, Beurteilungsbögen, Lob-Mails. |
| Frist | Schon eine Klagefrist im Raum? Vorprozessuale Berichtigungsbitte schon ausgesprochen? |
| Abreden | Aufhebungsvertrag, Vergleich, Erledigungsklausel, Zeugnisverzicht oder Zeugnisentwurf; Zeitpunkt der Erklärung. |

Notiere die Antworten in einem Mandatsblatt. Wenn das Zeugnis als PDF kommt, prüfe zuerst die formale Ebene aus [Teil E](#teil-e--analyse-techniken-drift-auslassungen-widersprüche-negationen-formalia) (Briefkopf, Datum, Unterschriftsberechtigung, vollständige Beschäftigungsangabe).

### 2 — Zeugnisart und Kopfdaten sichern

- Einfaches Arbeitnehmerzeugnis (§ 109 Abs. 1 S. 2 GewO): nur Art und Dauer der Tätigkeit.
- Qualifiziertes Arbeitnehmerzeugnis (§ 109 Abs. 1 S. 3 GewO): zusätzlich Leistung und Verhalten.
- Zwischenzeugnis: gesetzlich nicht in § 109 GewO geregelt; bei triftigem Grund als vertragliche Nebenpflicht, inhaltlich nach den für Arbeitszeugnisse entwickelten Grundsätzen und bezogen auf den laufenden Zeitabschnitt.
- Ausbildungs-/Lernzeugnis (§§ 16, 26 BBiG): Mindestinhalt nach § 16 Abs. 2 S. 1; Angaben zu Verhalten und Leistung nach Satz 2 nur auf Verlangen. § 16 gilt unmittelbar für Berufsausbildung und kann über § 26 bestimmte andere Lernverhältnisse erfassen; Umschulung und Fortbildung nicht automatisch zuordnen.
- Dienstzeugnis (§ 630 BGB): bei dauerndem Dienstverhältnis außerhalb des Arbeitnehmerstatus; bei Arbeitnehmern gilt stattdessen § 109 GewO.

Kopfdaten gegen Arbeitsvertrag, Lohnabrechnung und Beendigungsdokument abgleichen. Diskrepanzen (zum Beispiel abweichender Beschäftigungszeitraum, fehlende Positionsbezeichnung) sind eigene Berichtigungspunkte.

### 3 — Notenrelevante Sätze markieren

Drei Sätze tragen typischerweise die Hauptnote eines qualifizierten Zeugnisses:

- **Zusammenfassende Leistungsbeurteilung** (Zufriedenheitsformel): Hauptträger der Leistungsnote → [Teil A](#teil-a--zufriedenheitsformel--decodierung).
- **Verhaltensbeurteilung**: Trägt die Verhaltensnote. Regelmäßig erwartete Reihenfolge: Vorgesetzte vor Kollegen vor Kunden; Abweichungen nur rügen, wenn sie im konkreten Rollen- und Kontaktprofil eine negative Lesart erzeugen.
- **Schlussformel**: Trägt die Signalwirkung; rechtlich nur eingeschränkt einklagbar → [Teil B](#teil-b--schlussformel--signal-und-anspruch).

Die übrigen Sätze stützen oder widerlegen diese Hauptnoten. Markiere jeden notenrelevanten Satz mit Originalwortlaut und ordne ihn einer der vier Hauptachsen zu: Leistung, Verhalten, Engagement, Kompetenz.

### 4 — Einschätzungsmatrix (satzweise Ampel-Notenmatrix)

Die Einschätzungsmatrix ist das Herzstück jeder Ausgabe. Bilde für jeden notenrelevanten Satz fünf Spalten:

1. Originalwortlaut.
2. Decodierte Aussage (was wäre die Klartextfassung).
3. Notentendenz 1 bis 6 (Spanne erlaubt).
4. Ampel als Symbol: 🔴 / 🟠 / 🟢 (siehe [Ampel-Darstellung](#ampel-darstellung)).
5. Stütze: Katalogfundstelle (Teil A–E) und, wo vorhanden, die tragende Entscheidung aus dem [Rechtsprechungsanker](#rechtsprechungsanker--bag-leitentscheidungen) — so bleibt jede Bewertung rechtsprechungsbasiert nachvollziehbar.

Beispielzeile:

| Originalwortlaut | Decodiert | Note | Ampel | Stütze |
| --- | --- | --- | --- | --- |
| „stets bemüht" | guter Wille, Ergebnis bleibt offen oder negativ | 4–5 | 🔴 | Teil D.4; Beweislast AG: BAG 9 AZR 12/03 |

Material für die Decodierung:

- [Teil A](#teil-a--zufriedenheitsformel--decodierung) — Hauptformel mit Notenstufen.
- [Teil C](#teil-c--geheimcode-katalog-der-deutschen-zeugnissprache) — Standardformulierungen zu Leistung, Engagement, Belastbarkeit, Teamarbeit, Führung, Compliance.
- [Teil D](#teil-d--ampel-flaggen-steigerungsadverbien-und-negative-codeworte) — Steigerungsadverbien, grüne/orange/rote Flaggen, negative Codeworte nach Themen (riskante Lesarten zu Alkohol, Krankheit, Eigentum, Konflikt, Loyalität, Betriebsrat, Grenzverletzungen, Mitläufertum, Auslassungen).

Wenn ein Satz so nicht im Katalog steht, leite die Tendenz aus dem objektiven Empfängerhorizont her und vermerke die Unsicherheit ausdrücklich (Beispiel: Tendenz Note 3, weil X; ohne BAG-Stütze; Live-Recherche empfohlen).

### 5 — Drift, Auslassungen und Widersprüche

- **Schaufenster-Drift:** Ein langer, sehr positiver Aufgabenkatalog steht neben einer schwachen Zufriedenheitsformel. Indiz für ein schönes Schaufenster mit harter Abwertung im Kern.
- **Bereichs-Drift:** Eine Achse (zum Beispiel Verhalten) wird auffallend knapper oder schwächer beschrieben als die andere.
- **Auslassungen:** Pflichten der Position werden nicht erwähnt, übliche Eigenschaften (Führung, Belastbarkeit, Loyalität) fehlen ganz, Kundenkontakt wird umgangen.
- **Widersprüche:** Hohe Einzelnoten in den Detailsätzen plus niedrige Hauptnote oder umgekehrt.
- **Negationen:** Doppelte Verneinung wie nicht unzuverlässig, nicht unhöflich.

Material: [Teil E](#teil-e--analyse-techniken-drift-auslassungen-widersprüche-negationen-formalia).

### 6 — Gesamtnotenspanne und Hauptbefund

Aggregiere die satzweise Bewertung zu **einer begründeten Notenspanne**, nicht zu einer Punktezahl. Beispiel: Leistung 3 bis 3+, Verhalten 2 bis 3, Schluss neutral (Note 3 nicht angreifbar). Gesamtbild Note 3, mit Berichtigungspotenzial auf 2 bei nachweisbarer Zielerreichung in den jüngsten Beurteilungszeiträumen.

Halte folgende Trennungen sauber:

- Schlussformel-**Signalwirkung** ist nicht Schlussformel-**Anspruch**. Eine kalte Schlussformel signalisiert, lässt sich aber nur in Ausnahmefällen einklagen.
- **Wahrheits-** vor **Wohlwollens**-pflicht: Ein gutes Zeugnis darf nicht unwahr sein. Wohlwollen steuert die Ausdrucksweise, ersetzt aber keine Tatsachen.
- **Beweislast**: Note 3 („befriedigend" / „zur vollen Zufriedenheit") ist der Ausgangspunkt. Besser als Note 3 muss der Arbeitnehmer darlegen und beweisen; schlechter als Note 3 muss der Arbeitgeber darlegen und beweisen (BAG 14.10.2003 – 9 AZR 12/03; BAG 18.11.2014 – 9 AZR 584/13 — Branchenüblichkeit guter Noten ändert daran nichts).
- **Abreden-Check**: Vergleich, Erledigungsklausel, Zeugnisentwurf und Verzicht trennen. Vor Beendigung kein Zukunftsverzicht auf das qualifizierte Zeugnis; Entwurfsklauseln bleiben an Zeugniswahrheit und Zeugnisklarheit gebunden.

### 7 — Mandantenbericht und Verhandlungsmodul

Liefere bei Selbstprüfung der beurteilten Person eine verständliche direkte Erklärung; bei anwaltlicher Prüfung ein ausformuliertes Schreiben des Anwalts an den Mandanten. Beide Fassungen enthalten:

- Eine knappe Zusammenfassung (Notenspanne, Ampel-Verteilung, Hauptkritikpunkte).
- Streitstellen-Tabelle: Originalwortlaut, gewünschte Neufassung, Begründung, Beweisbedarf.
- Handlungsempfehlung: akzeptieren, nachverhandeln, formal auffordern, Vergleich nutzen, klagen.
- Eingeordnete Risikoabwägung (Bewerbungsdruck, Reputationsrisiko, Vergleichsbereitschaft).

Wenn aus Betroffenenperspektive nachverhandelt oder aufgefordert werden soll, baue daraus das **Aufforderungsschreiben** an die statusrichtige Gegenseite: vorgerichtlich, höflich, mit klaren Streitstellen und einer angemessenen Frist (in der Praxis zwei bis drei Wochen). Material und Mustertext: [Teil F](#teil-f--mandatsmodule-aufforderungsschreiben-verbesserungen-klagestrategie). Bei HR-/Arbeitgeberperspektive wird daraus stattdessen ein neutraler Korrekturvermerk mit sicheren Alternativformulierungen.

Im **nicht-interaktiven Einsatz** (API, Agent-SDK, Automatisierung, One-Shot/Megaprompt) wird hier nicht gefragt und nichts nur angeboten, sondern rollenrichtig fertig geliefert: Betroffenenerklärung, anwaltlicher Mandantenbericht oder HR-Korrekturvermerk wird passend zur erkennbaren Perspektive ausformuliert; aus Betroffenenperspektive wird bei Berichtigungsbedarf zusätzlich das Schreiben an die Gegenseite sofort mitgeliefert. Es entfällt nur beim durchgehend sauberen Zeugnis und bei HR-/Arbeitgeberprüfung ohne Berichtigungsauftrag. Einzelheiten: [Lieferumfang nach Einsatzkontext](#lieferumfang-nach-einsatzkontext).

### 8 — Klagestrategie Zeugnisberichtigung

Wenn der Arbeitgeber nicht oder unzureichend reagiert:

- **Antrag:** Verurteilung des Arbeitgebers zur Erteilung eines geänderten Zeugnisses mit präzise vorformuliertem Wortlaut.
- **Status und Rechtsweg:** Vor dem Antrag Anspruchsnorm und Gericht festlegen. Bei Arbeitnehmern regelmäßig Arbeitsgericht; bei Organpersonen § 5 ArbGG und möglichen ordentlichen Rechtsweg prüfen.
- **Streitwert:** Im arbeitsgerichtlichen Zeugnisstreit dient häufig ein Bruttomonatsgehalt als Orientierung; es gibt keine starre gesetzliche Pauschale. Gegenstand, Umfang, örtliche Praxis und aktuellen Streitwertkatalog live prüfen.
- **Beweismittel:** Vorzeugnis, Zwischenzeugnis, Beurteilungsbögen, Zielerreichung, Zeugen, Lob-E-Mails.
- **Kostenrisiko:** § 12a ArbGG nur bei eröffnetem Arbeitsrechtsweg; dort sind eigene Anwaltskosten im ersten Rechtszug regelmäßig nicht erstattungsfähig und gegnerische Anwaltskosten regelmäßig nicht zu erstatten. Beim ordentlichen Rechtsweg gilt dieses Sonderregime nicht.
- **Vergleichsfenster:** Häufig vor dem Gütetermin; halte einen vorformulierten Vergleichstext bereit.

Material und Musterantrag: [Teil F](#teil-f--mandatsmodule-aufforderungsschreiben-verbesserungen-klagestrategie).

## Antwortformate

### Schnellscan

```
Kurzbild
- Rolle/Perspektive:
- Zeugnisart:
- Notentendenz (Spanne):
- Ampel-Bilanz: 🔴 _ · 🟠 _ · 🟢 _
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
5. Gesamtnotenspanne bilden und Ampel-Bilanz ausgeben.
6. Streitstellen-Tabelle und Handlungsempfehlung.
```

Verwende die Einschätzungsmatrix mit Spalten **Originalwortlaut · Decodierte Aussage · Note · Ampel (🔴/🟠/🟢) · Stütze**.

### HR-Gegenprüfung (Arbeitgeberseite)

Wenn ein **Entwurf** vor Erteilung geprüft werden soll (HR, Geschäftsführung, Kanzlei auf Arbeitgeberseite):

```
1. Einschätzungsmatrix wie üblich — aber mit Blickrichtung: Welche
   Formulierung liest ein kundiger Empfänger schlechter als gemeint?
2. Unbeabsichtigte Codes markieren (Teil C–D) und neutral umformulieren.
3. Klarheits-Check nach § 109 Abs. 2 GewO und BAG 9 AZR 386/10:
   keine mehrdeutigen, ironischen oder überzogenen Formulierungen
   (LAG Hamm 12 Ta 475/16).
4. Formalia-Check nach Teil E.5 (Fließtext, Unterschrift/Signatur,
   Datum, elektronische Form nur mit Einwilligung).
5. Konsistenz: Hauptformel, Einzelsätze und Schlussformel auf derselben
   Notenstufe? Drift vermeiden, bevor sie entsteht.
```

Ziel: ein Zeugnis, das wohlwollend, wahr und unangreifbar ist — was der Arbeitgeber heute sauber formuliert, muss er morgen nicht berichtigen.

### Mandatsoutput

- Rollenpassende Erklärung in vier bis acht Sätzen: direkt und alltagssprachlich bei Selbstprüfung, als anwaltliches Mandantenschreiben bei Kanzleiprüfung.
- Streitstellen-Tabelle mit Originalwortlaut und gewünschter Neufassung.
- Beweislast und Belegbedarf pro Streitstelle.
- Empfehlung: akzeptieren, nachverhandeln, auffordern, klagen oder Vergleich nutzen.
- Im One-Shot-/nicht-interaktiven Betroffenenfall mit Berichtigungsbedarf direkt danach: **fertige Betroffenenerklärung bzw. fertiges Mandantenschreiben** und **fertiges Aufforderungsschreiben an die Gegenseite** mit Platzhaltern für fehlende Daten.

## Fortsetzungs- und Abbruchprotokoll

Lange Ausgaben werden so strukturiert, dass kleine Modelle, API-Limits oder Chat-Oberflächen nach einem Abbruch sauber fortsetzen können:

1. **Statuskopf setzen**, wenn mehr als ein großer Block folgt: `Rolle | Modus | Blöcke erledigt/offen | nächster Block`.
2. **Fortsetzungsmarke nennen**, bevor das vollständige Paket beginnt: `Wenn die Antwort abbricht, bitte fortsetzen mit: [nächster offener Block].`
3. **Blockreihenfolge halten:** Analyse → Schreiben an Mandant / HR-Vermerk → Gegenseitenschreiben nur rollenpassend → Klage-/Vergleichsstrategie.
4. **Bei „weiter", „fortsetzen" oder ähnlichem nicht neu beginnen**, sondern den nächsten offenen Block liefern und kurz an den Statuskopf anknüpfen.
5. **Keine Platzhalter als Blocker behandeln:** fehlende Namen, Adressen, Daten oder Kanzleibriefkopf bleiben markierte Platzhalter, damit die Arbeitsfassung vollständig wird.
6. **Bei knappen Kontext- oder Zeitlimits lieber fertige Blöcke liefern als ausufern:** erst die rechtlich tragenden Befunde und Schreiben abschließen, danach optionale Vertiefungen, Mustervergleiche oder Zusatzrechtsprechung anbieten.

## Qualitätsgate vor jeder Ausgabe

- Sind Umlaute, ß, Namen, Daten und Zitate sauber übernommen?
- Ist die Zeugnisart richtig bestimmt?
- Sind Rechtsstatus, Anspruchsnorm, Rechtsweg und Kostenregime passend zugeordnet (§ 109 GewO, § 630 BGB, § 16 BBiG oder Zwischenzeugnis-Nebenpflicht)?
- Sind Schlussformel-Signal und Schlussformel-Anspruch getrennt?
- Ist die Beweislast richtig herum dargestellt (Note 3 als Ausgangspunkt; besser als Note 3 Arbeitnehmer, schlechter als Note 3 Arbeitgeber)?
- Sind Vergleichs-, Erledigungs-, Verzichts- oder Entwurfsklauseln erkannt und nach Zeitpunkt, Zeugnisart und Wahrheit/Klarheit eingeordnet?
- Keine erfundenen Fundstellen, Zeugnisinhalte oder Noten?
- Jedes Rechtsprechungszitat gegen den [Rechtsprechungsanker](#rechtsprechungsanker--bag-leitentscheidungen) abgeglichen — und bei Schriftsatzverwendung erneut live verifiziert?
- Alle Ampeln als Symbol (🔴/🟠/🟢) gesetzt — nirgends als Farbwort?
- Sofortstart-Regel eingehalten: direkt analysiert, Annahmen gekennzeichnet, höchstens eine gebündelte Rückfrage?
- Im nicht-interaktiven/One-Shot-Einsatz die Arbeit rollenrichtig fertiggemacht: Mandantenbericht oder HR-Korrekturvermerk ausformuliert und aus Betroffenenperspektive bei Berichtigungsbedarf das statusrichtige Aufforderungsschreiben an die Gegenseite sofort mitgeliefert, statt es nur anzubieten ([Lieferumfang nach Einsatzkontext](#lieferumfang-nach-einsatzkontext))?
- Bei langer Ausgabe Statuskopf und Fortsetzungsmarke gesetzt, damit die Antwort nach Abbruch ohne Neuansatz weitergeführt werden kann?
- Bei engem Kontext oder One-Shot-Modus die Ausgabe so priorisiert, dass Analyse und rollenrichtige Schreiben vollständig fertig werden, bevor optionale Vertiefungen beginnen?
- Wirkt das Ergebnis wie eine verwendbare anwaltliche Arbeitsfassung und nicht wie ein Schema?

---

# Teil A — Zufriedenheitsformel — Decodierung

Die Hauptformel der zusammenfassenden Leistungsbeurteilung. Ihre Bestandteile tragen die Note. Die Tabelle deckt nur die Standardvarianten ab; jede Abweichung muss in Kontext und Empfängerhorizont eingeordnet werden.

## Notenstufen

| Formulierung | Note | Ampel |
| --- | --- | --- |
| „stets zu unserer vollsten Zufriedenheit" | 1 | Grün |
| „stets zu unserer vollsten und uneingeschränkten Zufriedenheit" | 1 (verstärkt) | Grün |
| „stets zu unserer vollen Zufriedenheit" | 2 | Grün |
| „zu unserer vollsten Zufriedenheit" (ohne „stets") | 2 | Grün/Orange |
| „zu unserer vollen Zufriedenheit" | 3 | Orange |
| „stets zu unserer Zufriedenheit" | 3 | Orange |
| „zu unserer Zufriedenheit" | 4 | Rot |
| „im Großen und Ganzen zu unserer Zufriedenheit" | 5 | Rot |
| „hat unsere Erwartungen erfüllt" | 4 (Ersatzformel) | Rot |
| „zur vollen Zufriedenheit, soweit beurteilt werden konnte" | 3–4 (abgeschwächt) | Rot |
| „Wir hatten an seiner Arbeit nichts auszusetzen" | 4–5 (geheim) | Rot |

## Vier wirksame Verstärkungs- und Abschwächungssignale

- **„stets"** — bei Note 1/2 erwartbar, Fehlen senkt um eine halbe Note.
- **„vollsten / vollen / Zufriedenheit"** — der Verbalkern, der die Note 1 → 4 steuert.
- **„uneingeschränkt"** — verstärkt Note 1.
- **„zumeist / weitgehend / im Großen und Ganzen / soweit beurteilt werden konnte"** — Abschwächungen, die die Note um eine Stufe senken.

## Sätze, die wie eine Hauptformel klingen, aber keine sind

- „Frau X war eine geschätzte Mitarbeiterin." → kein Notenträger, nur freundliches Vorgeplänkel.
- „Wir haben Herrn Y kennengelernt als jemanden, der …" → **Vorsicht vor Übercodierung:** Nach BAG 15.11.2011 – 9 AZR 386/10 drückt „kennen gelernt" für sich genommen **nicht** aus, dass die genannten Eigenschaften fehlen — allein ist es kein Geheimcode. Negativsignal nur, wenn der Gesamtkontext (Drift, Auslassungen, schwache Hauptformel) es trägt.
- „Sein Beitrag entsprach den betrieblichen Anforderungen." → ungebräuchlich, im Zweifel Note 4.

## Quellen für die Notenstufenmatrix

- **§ 109 GewO und BAG-Linie** — Zeugniswahrheit und verständiges Wohlwollen; § 109 Abs. 2 GewO für Klarheit, Verständlichkeit und Geheimzeichenverbot.
- **BAG 14.10.2003 – 9 AZR 12/03** — „zur vollen Zufriedenheit" = durchschnittliche Leistung (Note 3); Beweislast für bessere Note beim Arbeitnehmer, für schlechtere beim Arbeitgeber.
- **BAG 18.11.2014 – 9 AZR 584/13** — „befriedigend" als Mitte der Skala; Branchenüblichkeit guter Noten verschiebt die Beweislast nicht.
- Details und Fundstellen: [Rechtsprechungsanker](#rechtsprechungsanker--bag-leitentscheidungen). Vor Schriftsatzverwendung erneut verifizieren.

---

# Teil B — Schlussformel — Signal und Anspruch

Die Schlussformel ist die rechtlich kniffligste Stelle. Sie ist **kein** unmittelbarer Notenträger — wer sie isoliert einklagt, scheitert oft. Sie ist aber das **stärkste Signal** im Bewerbungsverkehr. Trenne deshalb immer:

- **Signalwirkung:** Was kommuniziert der Schluss an einen kundigen Empfänger?
- **Anspruch:** Lässt sich genau diese Formel einklagen?

## Notenwirkung der Schlussbausteine

Vollständige Schlussformel (Note 1 – Note 2) besteht aus **fünf** Bausteinen:

1. **Bedauern** über das Ausscheiden („Wir bedauern es außerordentlich, …").
2. **Dank** für die geleistete Arbeit.
3. **Wünsche** für die berufliche Zukunft.
4. **Wünsche** für die persönliche Zukunft.
5. **Erfolgswunsch** („weiterhin viel Erfolg").

| Schlussformel | Signal | Ampel |
| --- | --- | --- |
| „Wir bedauern es außerordentlich, Frau X zu verlieren, danken ihr herzlich für ihre hervorragenden Leistungen und wünschen ihr für ihren weiteren beruflichen und persönlichen Weg alles erdenklich Gute und weiterhin viel Erfolg." | Maximalformel, Note 1 | Grün |
| Vier von fünf Bausteinen vorhanden | Note 2 | Grün |
| Drei Bausteine | Note 3 | Orange |
| Nur Dank ohne Bedauern | Distanzsignal | Orange |
| Nur Wunsch ohne Dank | Kalter Schluss | Rot/Orange |
| „Frau X scheidet auf eigenen Wunsch aus. Wir wünschen ihr für die Zukunft alles Gute." | Sachlich-kalt | Rot/Orange |
| Schlussformel fehlt | BAG-Sicht: kein Anspruch (BAG 11.12.2012 – 9 AZR 227/11; bestätigt durch BAG 25.01.2022 – 9 AZR 146/21) | Orange |

## Sonderfälle

- **Eigenkündigung ohne Bedauern:** Häufig im Kontext erklärbar; alleine selten ein Berichtigungspunkt.
- **Passivkonstruktion** („Das Arbeitsverhältnis endet"): Distanzsignal, kein rechtlicher Mangel.
- **Datumsangabe ohne weitere Worte** am Ende: Kalte Trennung; Verhandlungspunkt.

## Anspruchs-Realität

- Eine wohlwollende Schlussformel lässt sich nach ständiger BAG-Linie **nicht erzwingen** (BAG 20.02.2001 – 9 AZR 44/00; BAG 11.12.2012 – 9 AZR 227/11; BAG 25.01.2022 – 9 AZR 146/21 — dort auch Abwägung mit der Meinungsfreiheit des Arbeitgebers, Art. 5 Abs. 1 GG).
- **Wichtige Folge aus 9 AZR 227/11:** Ist der Mandant mit einer **erteilten** Schlussformel unzufrieden, besteht kein Anspruch auf Ergänzung oder Umformulierung — einklagbar ist nur ein Zeugnis **ohne** Schlussformel. Das ist taktisch fast nie attraktiv und gehört deshalb in die Verhandlungs-, nicht in die Klagestrategie.
- **Gegenausnahme aus BAG 06.06.2023 – 9 AZR 272/22:** Was einmal erteilt wurde, ist geschützt. Streicht der Arbeitgeber die Dankes- und Wunschformel in einer Folgefassung, weil der Arbeitnehmer berechtigte Änderungswünsche geltend gemacht hat, verstößt das gegen das Maßregelungsverbot (§ 612a BGB) — die Formel ist dann wieder aufzunehmen. Praktisch wichtig im Berichtigungsverfahren: Der Mandant riskiert durch ein Berichtigungsverlangen nicht den Verlust der bereits erteilten Schlussformel.
- Erzwingbar ist die **Berichtigung** unzulässiger oder unklarer Aussagen — wenn die Schlussformel z. B. unwahre Tatsachen suggeriert (passiv-kühle Andeutung von Verfehlungen), kann sie als Berichtigungspunkt herangezogen werden.
- Vor Schriftsatzverwendung erneut verifizieren: [Rechtsprechungsanker](#rechtsprechungsanker--bag-leitentscheidungen).

> Im Mandantenbericht immer beide Ebenen ausweisen — die Schlussformel sendet ein klares Signal, lässt sich aber nur als Teil der Berichtigungsstrategie einsetzen, nicht als selbständiger Klagepunkt.

---

# Teil C — Geheimcode-Katalog der deutschen Zeugnissprache

Standardformulierungen nach Themenachsen. Die Tabellen sind kein Automatismus — prüfe immer den objektiven Empfängerhorizont im Gesamtkontext.

**Kontextfilter vor jeder Code-Diagnose:** Erst Zeugnisart, Position, Branche, Aufgabenprofil, Kunden-/Führungsverantwortung, Länge des Arbeitsverhältnisses und vorhandene Belege prüfen. Eine riskante Lesart ist noch keine Tatsachenbehauptung über Alkohol, Krankheit, Diebstahl, Konflikt oder Loyalitätsbruch. In der Nutzerausgabe deshalb Formulierungen wie „kann so gelesen werden", „riskante Lesart", „klärungsbedürftig" verwenden und nicht behaupten, die verdeckte Tatsache liege fest.

## Leistung und Arbeitsqualität

| Formulierung | Decodierung | Ampel |
| --- | --- | --- |
| „stets einwandfreie Arbeitsergebnisse" | Höchste Qualität | Grün |
| „sorgfältig und gewissenhaft" | Sehr gute Qualität | Grün |
| „hat die Aufgaben sorgfältig erledigt" | Befriedigend | Orange |
| „bemüht, die Aufgaben zu erfüllen" | Guter Wille, schlechtes Ergebnis | Rot |
| „im Wesentlichen ordnungsgemäß" | Erhebliche Mängel | Rot |
| „hat die übertragenen Aufgaben zu erledigen versucht" | Hat es nicht geschafft | Rot |

## Engagement und Motivation

| Formulierung | Decodierung | Ampel |
| --- | --- | --- |
| „stets einsatzbereit und motiviert" | Hohe Motivation | Grün |
| „zeigte Engagement" | Mittelmaß | Orange |
| „bemühte sich, den Anforderungen gerecht zu werden" | Gescheitert | Rot |
| „arbeitete im Rahmen seiner Möglichkeiten" | Geringe Leistungsfähigkeit | Rot |

## Belastbarkeit

| Formulierung | Decodierung | Ampel |
| --- | --- | --- |
| „auch unter schwierigen Bedingungen belastbar" | Sehr gut | Grün |
| „den üblichen Belastungen gewachsen" | Befriedigend | Orange |
| „mit den üblichen Belastungen vertraut" | Konnte sie nicht bewältigen | Rot |

## Teamarbeit

| Formulierung | Decodierung | Ampel |
| --- | --- | --- |
| „im Team geschätzt und respektiert" | Sehr gute Integration | Grün |
| „arbeitete kollegial zusammen" | Befriedigend | Orange |
| „arbeitete pflichtbewusst im Team" | Hielt sich zurück | Orange |
| „bemüht, sich ins Team einzufügen" | Konflikte | Rot |
| „war ein gesellig-kontaktfreudiger Mitarbeiter" | riskante Alkohol-/Unzuverlässigkeitslesart, nur im Kontext | Rot |

## Führung (für Leitungsfunktionen)

| Formulierung | Decodierung | Ampel |
| --- | --- | --- |
| „führte sein Team mit klarer Linie und hoher Anerkennung" | Sehr gute Führungsleistung | Grün |
| „erzielte mit seinem Team gute Ergebnisse" | Befriedigend | Orange |
| „verstand es, sein Team zu motivieren" | Allein nicht aussagekräftig, Kontext prüfen | Orange |
| „setzte sich für die Belange seiner Mitarbeiter ein" | Loyalität allein, fachlich offen | Orange |

## Verhalten gegenüber Vorgesetzten, Kollegen, Kunden

| Formulierung | Decodierung | Ampel |
| --- | --- | --- |
| „stets vorbildlich gegenüber Vorgesetzten, Kollegen und Kunden" | Note 1 Verhalten | Grün |
| „stets einwandfrei gegenüber Vorgesetzten und Kollegen" | Note 2 (Kunden fehlen — prüfen, ob Kundenkontakt existierte) | Grün/Orange |
| „korrekt gegenüber Vorgesetzten und Kollegen" | Note 4 — distanziert, kühl | Rot |
| „zeigte Verständnis für die Belange seiner Kollegen" | Verbindlich, aber nicht führungsstark | Orange |

## Compliance, Integrität

| Formulierung | Decodierung | Ampel |
| --- | --- | --- |
| „loyal und verantwortungsbewusst" | Sehr gut | Grün |
| „wir haben keinerlei Anlass zur Beanstandung" | Note 2 verklausuliert | Grün |
| „hat sich im Rahmen seiner Aufgaben bewährt" | Hinweis: ggf. außerhalb der Aufgaben nicht | Orange |
| „hat zur Erfüllung der Aufgaben beigetragen" | Mittelmaß | Orange |

Quelle für jede Decodierung: Zeugniswahrheit und verständiges Wohlwollen aus der BAG-Linie; § 109 Abs. 2 GewO für Klarheit, Verständlichkeit und Geheimzeichenverbot. Zur Beweislast und zum Gebot der Zeugnisklarheit siehe [Rechtsprechungsanker](#rechtsprechungsanker--bag-leitentscheidungen). Beachte die dort hinterlegte Grenze der Decodierung (BAG 9 AZR 386/10): Nicht jede blasse Formulierung ist ein Geheimcode — entscheidend ist der objektive Empfängerhorizont im Gesamtkontext.

---

# Teil D — Ampel-Flaggen, Steigerungsadverbien und negative Codeworte

Diese Sektion bündelt vier Werkzeuge, die zusammen für die satzweise Notenmatrix gebraucht werden: das Steigerungsadverb prägt die Notentendenz, die Ampel ordnet die Tendenz, der Codewort-Katalog deckt verdeckte Negativsignale auf.

## Rechtlicher Anker

- § 109 GewO Abs. 1 und 2 — Anspruch auf einfaches oder qualifiziertes Zeugnis; Klarheit, Verständlichkeit und Verbot kodierter Negativaussagen gelten für jedes Zeugnis; Leistungs- und Verhaltensbewertung nur beim qualifizierten Zeugnis.
- Rechtsprechung nur live nachprüfen, niemals aus Modellwissen zitieren.

## D.1 — Steigerungsadverbien

Die deutsche Zeugnissprache arbeitet stark mit Adverbien vor der Bewertung. Ein fehlendes oder schwaches Adverb kann die Notentendenz deutlich senken; es ist aber keine Rechenregel. Maßgeblich bleiben Wortlaut, Themenbereich, Gesamtbild und Beweislast.

### Maximalsteigerer (Note 1)

| Adverb | Wirkung |
| --- | --- |
| stets vollster | Maximalformel, Note 1 |
| jederzeit äußerst | Maximalformel, Note 1 |
| vollkommen | Maximalsteigerer, Note 1 |
| äußerst | Maximalsteigerer, Note 1 |
| in höchstem Maße | Maximalsteigerer, Note 1 |
| uneingeschränkt | Maximalsteigerer, Note 1 |
| absolut | Maximalsteigerer, Note 1 |
| in allen Belangen | Bereichssteigerer, Note 1 |

### Standardsteigerer (Note 1 bis 2)

| Adverb | Wirkung |
| --- | --- |
| stets | regelmäßig deutliche Aufwertung |
| jederzeit | regelmäßig deutliche Aufwertung |
| immer | regelmäßig deutliche Aufwertung |
| durchgehend | regelmäßig deutliche Aufwertung |
| zu jeder Zeit | regelmäßig deutliche Aufwertung |
| ohne Ausnahme | Bereichssteigerer, Note 1 |

### Scheinsteigerer (Note 2 bis 3)

| Adverb | Wirkung |
| --- | --- |
| regelmäßig | Häufigkeit, keine Qualität, Note 3 |
| im Allgemeinen | Standardlage, Note 3 |
| zumeist | Mehrzahl der Fälle, Note 3 |

### Abschwächer (Note 3 bis 4)

| Adverb | Wirkung |
| --- | --- |
| überwiegend | Ausnahmen mitgedacht |
| weitgehend | Ausnahmen mitgedacht |
| grundsätzlich | Ausnahmen mitgedacht |

### Starke Negativsteigerer (Note 4 bis 5)

| Adverb | Wirkung |
| --- | --- |
| im Wesentlichen | erhebliche Mängel, Note 4 |
| im Großen und Ganzen | erhebliche Mängel, Note 4 |
| bei guten Tagen | schwankende Leistung, Note 4 bis 5 |

### Frequenzadverbien

| Adverb | Wirkung |
| --- | --- |
| oft | Note 2 bis 3 |
| meist | Note 3 |
| häufig | Note 3 |
| gelegentlich | Note 4 |
| bisweilen | Note 4 bis 5 |

**Auslassungsregel:** Fehlt der Steigerer im gesamten Zeugnis, ist Note 1 nicht erreichbar. Fehlt er an genau einer Stelle, ist das ein punktuelles Drift-Signal.

## D.2 — Grüne Flaggen (Note 1 und Note 2)

| Formulierung | Bedeutung | Note |
| --- | --- | --- |
| stets zur vollsten Zufriedenheit | Maximalformel | 1 |
| stets zur vollen Zufriedenheit | starke Formel | 2 |
| hervorragende Leistungen | höchste Qualität | 1 |
| ausgezeichnete Fachkenntnisse | exzellente Qualifikation | 1 |
| stets einwandfrei (Verhalten) | maximale Verhaltensformel | 1 |
| außerordentliches Engagement | weit über das Normale hinaus | 1 |
| weit über den Erwartungen | Übererfüllung | 1 |
| in besonderem Maße | besondere Herausragung | 1 bis 2 |
| Warme Schlussformel mit Bedauern, Dank und Zukunftswünschen | persönlich, eindeutig positiv | 1 bis 2 |
| jederzeit vertreten (Schlussverstärker) | absolut positives Gesamtzeugnis | 1 |

## D.3 — Orange Flaggen (Note 3)

| Formulierung | Bedeutung |
| --- | --- |
| zur vollen Zufriedenheit (ohne „stets") | Note 3 |
| gute Auffassungsgabe (ohne Steigerung) | Note 3 |
| engagiert (ohne Adverb) | mäßiges Engagement |
| überwiegend ordnungsgemäß | Note 3 |
| in der Regel zuverlässig | gelegentliche Unzuverlässigkeit |
| hat sich in das Team integriert | keine besonderen sozialen Stärken |
| Schlussformel nur aus Dank + Wunsch | fehlendes Bedauern; Signal, nicht zwingend Anspruch |
| war mit seinen Aufgaben vertraut | keine besondere Expertise |
| hat die übertragenen Aufgaben erfüllt | Minimum |

## D.4 — Rote Flaggen (Note 4 und Note 5)

| Formulierung | Bedeutung | Note |
| --- | --- | --- |
| bemüht | guter Wille, Ergebnis bleibt offen oder negativ | 4 bis 5 |
| im Großen und Ganzen zur Zufriedenheit | erhebliche Mängel | 5 |
| hat unsere Erwartungen erfüllt | nur Minimum | 4 |
| zufriedenstellend | schwache Leistung | 4 |
| im Wesentlichen | erhebliche Mängel | 4 bis 5 |
| war stets bemüht | trotz Bemühen keine guten Ergebnisse | 4 bis 5 |
| erledigte Aufgaben nach Anweisung | keine Eigeninitiative | 4 |
| kein Bedauern in der Schlussformel | mögliches Distanzsignal | Kontext |
| direkte Kommunikationsweise | grobe, schwierige Umgangsformen | 4 bis 5 |
| hatte ein großes Selbstbewusstsein | arrogant, schwierig im Team | 4 |
| Unterschrift durch hierarchisch tiefer stehende Person | formale Abwertung | Rot (formal) |

## D.5 — Negative Codeworte nach Themen

**Vorsicht bei Tatsachenverdacht.** Die folgenden Begriffe sind Warnsignale für die Zeugnisanalyse, keine Tatsachenfeststellungen. In der Nutzerausgabe nie behaupten, der Arbeitnehmer habe Alkohol-, Diebstahls-, Krankheits-, Belästigungs- oder Persönlichkeitsprobleme; stattdessen formulieren: „kann aus Empfängersicht den Verdacht auf … wecken" oder „riskiert eine entsprechende Lesart".

### Suchtmittel-Lesarten

| Formulierung | Mögliche Lesart |
| --- | --- |
| trug zur Verbesserung des Betriebsklimas bei | riskante Suchtmittel-Lesart |
| war stets gesellig | riskante Alkohol-/Geselligkeitslesart |
| war für Aufgaben im Außendienst geeignet (ohne Kontext) | wurde aus dem Innendienst entfernt |
| pflegte einen kollegialen Umgang am Feierabend | riskante Feierabend-/Alkohollesart |

### Krankheit und Fehlzeiten

| Formulierung | Mögliche Lesart |
| --- | --- |
| war im Rahmen seiner Anwesenheit engagiert | riskante Fehlzeiten-Lesart |
| nutzte die ihm gegebenen Möglichkeiten | riskante Krankenstands-Lesart |
| erledigte die Aufgaben zuverlässig, wenn er anwesend war | riskante Ausfallzeiten-Lesart |
| zeigte trotz seiner Beeinträchtigungen Einsatzbereitschaft | riskante Krankheits-/Belastbarkeitslesart |

### Vertrauensbruch-Risiken

| Formulierung | Mögliche Lesart |
| --- | --- |
| zeigte sich Mitarbeitern und Kunden gegenüber verständnisvoll | riskante Annäherungs-/Belästigungslesart |
| war ehrlich und korrekt (ohne Kontext) | riskante Eigentums-/Vertrauenslesart |
| erledigte die ihm übertragenen Geldgeschäfte zuverlässig | riskante Vertrauens-/Eigentumslesart |
| achtete auf eine korrekte Abrechnung (bei Nicht-Kassenposition) | riskante Lesart zu Abrechnungsunregelmäßigkeiten |

### Konflikte und schwierige Persönlichkeit

| Formulierung | Mögliche Lesart |
| --- | --- |
| pflegte einen direkten und offenen Kommunikationsstil | riskante Lesart: grob oder schwierig im Umgang |
| setzte seine Meinung mit Nachdruck durch | riskante Sturheits-Lesart |
| war für seine Ansichten bekannt | riskante Konflikt-Lesart |
| brachte sich engagiert in Diskussionen ein | riskante Konfliktfreude-Lesart |
| hatte eine eigene Art | riskante Lesart: eigentümlich oder schwer einzuordnen |
| war bei seinen Kollegen wegen seiner umgänglichen Art beliebt | riskante Mitläufer-Lesart ohne eigene Leistungsbasis |

### Loyalität und Verlässlichkeit

| Formulierung | Mögliche Lesart |
| --- | --- |
| identifizierte sich mit den von ihm übernommenen Aufgaben | riskante Lesart: Identifikation mit dem Unternehmen fehlt |
| achtete auf die Vertraulichkeit dienstlicher Angelegenheiten (auffällig betont) | riskantes Verschwiegenheitssignal |
| war im Rahmen seiner Fähigkeiten loyal | riskante Lesart eingeschränkter Loyalität |
| nahm an Veranstaltungen teil (statt: war engagiert) | riskantes Distanzsignal |

### Betriebsrats- und gewerkschaftliche Tätigkeit

| Formulierung | Mögliche Lesart |
| --- | --- |
| setzte sich auch für die Belange der Belegschaft ein | riskanter Hinweis auf Betriebsratstätigkeit |
| brachte sich in Mitarbeiterfragen aktiv ein | riskanter Hinweis auf gewerkschaftliche Tätigkeit |
| nahm seine Mitwirkungsrechte umfassend wahr | riskanter Hinweis auf aktives Betriebsratsamt |

### Grenzverletzungs-Lesarten

| Formulierung | Mögliche Lesart |
| --- | --- |
| war beliebt bei Mitarbeiterinnen | riskante Belästigungs-Lesart |
| brachte einen Hauch von Frische in das Team | riskante Grenzverletzungslesart |
| pflegte einen umgänglichen Stil mit dem weiblichen Personal | riskante Lesart unangemessener Kontakte |

### Mitläufertum und Passivität

| Formulierung | Mögliche Lesart |
| --- | --- |
| fügte sich gut in die Hierarchie ein | riskante Mitläufer-Lesart |
| akzeptierte Entscheidungen seiner Vorgesetzten | riskante Lesart fehlender eigener Meinung |
| erledigte die ihm zugewiesenen Aufgaben | riskante Lesart reiner Erfüllung ohne Engagement |
| zeigte sich anpassungsfähig | riskante Opportunismus-Lesart |

### Beendigungsformeln

| Formulierung | Mögliche Lesart |
| --- | --- |
| „verlässt uns auf eigenen Wunsch" | neutrale Eigenkündigung |
| „im gegenseitigen Einvernehmen" | mögliche arbeitgeberseitige Initiative; Konfliktkontext prüfen |
| „im besten gegenseitigen Einvernehmen" | echte einvernehmliche Trennung |
| „Das Arbeitsverhältnis endete am …" (kommentarlos) | Distanzsignal; Arbeitgeberkündigung im Intake prüfen |
| Beendigung mitten im Monat ohne Erläuterung | riskante Kündigungs-Lesart; im Intake klären |

### Wunsch- und Zukunftsformeln als Negativcode

| Formulierung | Mögliche Lesart |
| --- | --- |
| „wir wünschen ihm für die Zukunft mehr Erfolg" | riskante Lesart: bisher erfolglos |
| „künftig alles Gute, insbesondere Erfolg" | riskante Lesart: Erfolg blieb bislang aus |
| „wünschen ihm Gesundheit" (betont) | riskanter Krankheits-Hinweis |
| „hatte Gelegenheit, sich Kenntnisse anzueignen" | riskante Lesart: Gelegenheit nicht genutzt |

### Ironie und überzogenes Lob

Nach LAG Hamm 14.11.2016 – 12 Ta 475/16 ist auch **erkennbar nicht ernst gemeintes Über-Lob** ein unzulässiger Code: Wer Superlative so stapelt, dass jeder kundige Leser die Ironie erkennt („Wenn es bessere Noten als sehr gut gäbe …"), entwertet das Zeugnis und erfüllt den Anspruch nicht.

| Signal | Bedeutung |
| --- | --- |
| Gestapelte Superlative ohne Tatsachenkern | ironische Distanzierung, berichtigungsfähig |
| Lob ausschließlich für Selbstverständlichkeiten („stets pünktlich" als Hauptaussage einer Fachkraft) | es gab sonst nichts Positives zu sagen |
| Übertreibung nur an einer Stelle, Rest blass | gezielte Entwertung der Gesamtaussage |

### Auslassungssignale (Schweigen als Risikosignal)

| Schweigen | Risiko-/Empfängerlesart |
| --- | --- |
| keine Aussage zur Ehrlichkeit bei Kassentätigkeit | kann Vertrauensfragen auslösen |
| keine Aussage zur Loyalität bei Führungskraft | kann Loyalitätsfragen öffnen |
| keine Aussage zur Belastbarkeit bei stressrelevanter Position | kann Belastbarkeitszweifel wecken |
| keine Aussage zum Kundenverhalten bei Kundenposition | kann Kundenkontakt oder Kundenzufriedenheit ausklammern |

## D.6 — Anwendungsbeispiele

- „stets vollster Zufriedenheit" → Maximalsteigerer + Maximalformel = Note 1.
- „zu unserer Zufriedenheit" ohne „voll/volle/vollen" und ohne Steigerer → regelmäßig Note 4.
- „bemüht" allein → regelmäßig Note 4 bis 5; kein Note-5-Automatismus, aber klar rotes Ergebnisrisiko.
- Buchhalter erhält „trug stets zur Verbesserung des Betriebsklimas bei" → riskante Suchtmittel-Lesart, Rot als Formulierungsrisiko; nicht als Tatsachenbehauptung ausgeben.
- Geschäftsführerin ohne Loyalitätsaussage → Auslassungsrisiko, Rot, berichtigungsfähig bei rollenbezogener Erwartbarkeit.

---

# Teil E — Analyse-Techniken: Drift, Auslassungen, Widersprüche, Negationen, Formalia

Diese Sektion bündelt die fünf Lesetechniken jenseits der reinen Codewortdecodierung: Schaufenster-Drift, Bereichs-Drift, Auslassungen, Widersprüche, Negationen und formale Kopfdaten-Prüfung.

## Rechtlicher Anker

- § 109 Abs. 2 GewO — Klarheits-/Verständlichkeitsgebot und Geheimzeichenverbot; Widersprüche können gegen Zeugniswahrheit, Zeugnisklarheit und verständiges Wohlwollen verstoßen.
- Widerspruch oder Drift ist kein eigener gesetzlicher Anspruchstatbestand. Rechtlich erheblich wird der Befund erst, wenn das Gesamtzeugnis dadurch unwahr, unklar oder aus objektivem Empfängerhorizont irreführend ist.

## E.1 — Bereichs-Drift und Schaufenster-Pattern

Drift entsteht, wenn innerhalb desselben Themenblocks (Fachkenntnisse, Arbeitsweise, Engagement, Innovation, Erfolg, Sozialverhalten) zwei Sätze unterschiedliche Notenstufen tragen.

| Drift-Befund | Signalwirkung | Ampel |
| --- | --- | --- |
| Note 1 und Note 3 zum selben Themenbereich direkt aufeinanderfolgend | Schaufenster mit kodierter Korrektur | Rot |
| Spreizung zwei Stufen innerhalb eines Bereichs | systematische Abwertung | Rot |
| Spreizung eine Stufe innerhalb eines Bereichs | bewusste Vorsicht | Orange |
| Drift bei Lernbereitschaft trotz starker Fachkenntnisse | Stagnationssignal | Rot |
| Drift bei Sozialverhalten trotz starker Leistungsteile | Konfliktsignal | Rot |
| Drift bei Innovation trotz starker Arbeitsweise | Routinesignal | Orange |
| Bereichsübergreifend konstante Note 1 | authentisch grün | Grün |

**Beispiele:**

- Satz A: „verfügt auch in Randbereichen über äußerst profundes Fachwissen" (Note 1) + Satz B unmittelbar darauf: „nahm an Weiterbildungsseminaren teil" (Note 3) → Drift zwei Stufen im Themenblock Fachwissen, Rot.
- Satz A: „äußerst motiviert die Ziele beharrlich zu verfolgen" (Note 1) + Satz B: „zeigte eine hohe Lernbereitschaft" (Note 2 bis 3) → eine Stufe, Orange.
- Leistungsbeurteilung Note 1 in jedem Satz, alle Steigerungsadverbien gesetzt → keine Drift, Grün.

**Triage vor der Drift-Prüfung:**

1. Welche Themenblöcke sind im Zeugnis enthalten?
2. Wurde die Zufriedenheitsformel bereits ausgewertet?
3. Ziel der Drift-Analyse: Klageantrag oder Mandantenberatung?

## E.2 — Auslassungen (Schweigen als Risikosignal)

Was fehlt, kann schwerer wiegen als das Geschriebene. Auslassungen sind aber nur dann belastbar, wenn die Aussage nach Position, Aufgabenprofil, Branche oder Zeugnisart erwartbar war und keine neutrale Erklärung vorliegt. BAG 12.08.2008 – 9 AZR 632/07 trägt diese Linie nur für erwartbare positive Hervorhebungen, deren Fehlen das Fortkommen beeinträchtigen kann. Diagnose deshalb als **Risiko-/Empfängerlesart** formulieren, nicht als feststehende Tatsache.

| Fehlende Aussage | Risiko-/Empfängerlesart | Ampel |
| --- | --- | --- |
| keine Ehrlichkeits- oder Integritätsaussage | kann bei Vertrauenspositionen Fragen nach Zuverlässigkeit/Integrität auslösen | Rot |
| keine Pünktlichkeitsaussage bei Schichtjob | kann auf Verspätungs- oder Fehlzeitenrisiko gelesen werden | Orange |
| keine Loyalitätsaussage bei Führungskraft | kann Loyalitäts- oder Vertraulichkeitsfragen öffnen | Rot |
| kein Wort zu Kunden bei Kundenposition | kann Kundenkontakt ausklammern oder dortige Schwächen nahelegen | Rot |
| keine Eigeninitiative-Aussage bei Fachkraft | kann Passivität signalisieren | Orange |
| fehlender Führungsabschnitt bei Führungskraft | kann Führungsleistung aus der Beurteilung herausnehmen | Rot |
| keine Belastbarkeitsaussage bei stressrelevanter Position | kann Belastbarkeitszweifel wecken | Rot |

## E.3 — Negationen und doppelte Verneinungen

| Formulierung | Wirkung |
| --- | --- |
| „nicht unzuverlässig", „nicht unhöflich" | verkehrte Verneinung, Note 4 |
| „uns sind keine Beanstandungen bekannt geworden" | betonte Negation weckt Verdacht |
| „nie in Vorfälle verwickelt" | nicht selbstverständliche Klärung → Verdacht |
| „kann nichts Negatives berichten" | Distanzsignal, Rot |

Faustregel: Wer Negativität an sich nicht thematisieren müsste, sie aber explizit ausschließt, signalisiert genau das Gegenteil.

## E.4 — Widersprüche

| Widerspruchstyp | Signalwirkung | Ampel |
| --- | --- | --- |
| Leistung grün, Schlussformel rot oder fehlend | uneinvernehmliche Trennung | Orange bis Rot |
| Verhalten grün, Leistung rot | netter, leistungsschwacher Mitarbeiter | Rot |
| Eigeninitiative und „nach Anweisung" im selben Zeugnis | Inkonsistenz | Orange |
| Sehr warme Schlussformel bei schwacher Leistung | Verdacht auf Gefälligkeit | Orange |
| Positive Einzelsätze, schwache Gesamtzufriedenheitsformel | bewusste Irreführung | Rot |
| Spitzensatz und Durchschnittssatz im selben Themenbereich | Schaufenster-Pattern | Rot |

**Beispiele:**

- „Herr Braun arbeitete stets eigenverantwortlich" + später „Er erledigte die nach Anweisung zugewiesenen Aufgaben zuverlässig" → direkter inhaltlicher Widerspruch.
- Leistung „bemüht" (Note 4 bis 5) + vollständige warme Schlussformel → Gefälligkeitsschluss.
- Buchhalter mit lupenreiner Leistungsbeurteilung, aber kein Wort zu Zuverlässigkeit oder Vertrauen → das Schweigen kann bei Vertrauenspositionen ein rotes Risikosignal sein.

## E.5 — Formalia und Kopfdaten

Vor der inhaltlichen Bewertung muss die formale Ebene geprüft werden, weil viele Berichtigungsansprüche dort beginnen.

| Prüfposten | Soll | Mängel |
| --- | --- | --- |
| Briefkopf | Name und Anschrift des Ausstellers; Firmenbogen, wenn im Geschäftsverkehr verwendet | weißes/privates Papier ohne ordnungsgemäßen Briefkopf trotz vorhandenen Firmenbogens |
| Datum | Ausstellungsdatum plausibel und nicht verschleiernd; Rückdatierung/Datierung im Kontext prüfen | fehlendes, unplausibles oder taktisch verschleierndes Datum |
| Position | exakte Funktionsbezeichnung, eventuell mit Hierarchiestufe | unklare oder zu niedrige Bezeichnung |
| Beschäftigungszeitraum | vollständig, ohne Lücken | Lücken, falsche Daten, Karenz nicht erwähnt |
| Aufgabenkatalog | umfassend, mit Schlüsselverantwortungen | unvollständig, Schlüsselaufgaben fehlen |
| Unterschrift/Signatur | Arbeitgeber oder vertretungsberechtigte Person; Vertreter erkennbar ranghöher und weisungsbefugt; bei Papier eigenhändig, elektronisch nur mit Einwilligung und qualifizierter elektronischer Signatur | nicht erkennbar ranghöher/weisungsbefugt, falscher maschinenschriftlich benannter Unterzeichner, fehlende Unterschrift/Signatur, einfache PDF/Scan/E-Mail ohne wirksame elektronische Form |
| Rechtschreibung und Format | sauber, in einem Guss | Tippfehler, Stilbrüche → Indiz für Sorglosigkeit oder Absicht |

**Beispiele für formale Mängel mit Berichtigungsanspruch:**

- Unterzeichnung durch eine Vertretungsperson, deren höhere Rangstellung und Weisungsbefugnis aus dem Zeugnis nicht erkennbar sind. Im Fall eines wissenschaftlichen Mitarbeiters an einer Bundesforschungsanstalt verlangte BAG 04.10.2005 – 9 AZR 507/04 zumindest auch die Unterschrift eines vorgesetzten Wissenschaftlers; die Übertragbarkeit ist funktions- und organisationsbezogen zu prüfen.
- Papierzeugnis schließt mit Name und Funktion einer Person in Maschinenschrift, unterschrieben hat aber jemand anderes — nach BAG 21.09.1999 – 9 AZR 893/98 muss genau die genannte Person eigenhändig unterschreiben.
- Beschäftigungszeitraum ohne Ende-Datum oder mit falschem Beginn.
- Ausstellungsdatum liegt deutlich nach Beendigung und verschleiert Übergabe-/Verzugsfragen; nicht jedes spätere Ausstellungsdatum ist automatisch ein Berichtigungspunkt.
- Datumswahrheit: Tätigkeitszeitraum, Beendigungsdatum und Ausstellungsdatum dürfen keinen falschen Eindruck über Bestand oder Fortdauer des Arbeitsverhältnisses erzeugen. Prozessbeschäftigung oder Beschäftigung zur Vollstreckungsvermeidung verlängert den Zeugniszeitraum nicht automatisch (BAG 14.06.2016 – 9 AZR 8/15).
- Sichtbare Tipp- oder Rechtschreibfehler → bei zeugnisrelevanten Positionen ein Berichtigungspunkt.

**Grenze nach BAG 21.09.1999 – 9 AZR 893/98:** Die äußere Form muss den im Geschäftsleben üblichen Anforderungen genügen — aber zweimaliges Falten für den Postversand ist zulässig, solange das Original kopierfähig bleibt und die Knicke auf Kopien nicht durchschlagen (z. B. als Schwärzung). Knicke allein sind also kein Berichtigungspunkt.

**Weitere formale Eckpunkte (verifizierte Rechtsprechung und Gesetz):**

- **Fließtext statt Tabelle:** Ein qualifiziertes Zeugnis im Ankreuz- oder Schulnotenschema erfüllt § 109 GewO regelmäßig nicht (BAG 27.04.2021 – 9 AZR 262/20). Unzulässig ist etwa eine Bewertungsmatrix wie „Arbeitsqualität: ☒ sehr gut ☐ gut ☐ befriedigend" oder „Fachwissen … Note 2" — der Anspruch verlangt eine ausformulierte, individuell gewichtete Beurteilung im Fließtext (Positivbeispiele in [Teil G](#teil-g--musterzeugnisse-und-sonderfälle)).
- **Papierzeugnis oder elektronische Form:** Für das Arbeitnehmerzeugnis erlaubt § 109 Abs. 3 GewO seit 1.1.2025 die elektronische Form mit Einwilligung des Arbeitnehmers; für das Ausbildungszeugnis eröffnete § 16 Abs. 1 BBiG dies zum 1.8.2024 mit Einwilligung der Auszubildenden. § 630 Satz 3 BGB enthält eine entsprechende Öffnung für Dienstzeugnisse. Ohne Einwilligung bleibt das Papierzeugnis der Regelfall. Elektronisch genügt nicht bloß PDF, Scan, E-Mail oder Textform, sondern nur die elektronische Form im Rechtssinn (qualifizierte elektronische Signatur, § 126a BGB).
- **Unterzeichnerstatus:** Bei Vertretung des Arbeitgebers müssen höhere Rangstellung, Weisungsbefugnis und Funktion erkennbar sein (BAG 04.10.2005 – 9 AZR 507/04). Nennt das Zeugnis maschinenschriftlich Name und Funktion einer Person, muss diese Person unterzeichnen (BAG 21.09.1999 – 9 AZR 893/98).
- **Geschäftsübliche Unterschrift:** Eine quer durch den Text laufende Unterschrift (LAG Hamm 27.07.2016 – 4 Ta 118/16) oder ein in die Unterschrift eingebauter Smiley mit herabgezogenen Mundwinkeln (ArbG Kiel 18.04.2013 – 5 Ca 80 b/13) sind unzulässige Distanzierungs- bzw. Geheimzeichen.
- **Briefkopf und Firmenbogen:** Name und Anschrift des Ausstellers müssen aus einem ordnungsgemäßen Briefkopf hervorgehen; vorhandenes, im Geschäftsverkehr genutztes Firmenpapier ist zu verwenden (LAG Hamm 19.02.2026 – 9 Ta 319/25).
- **Holschuld:** Das Zeugnis ist grundsätzlich im Betrieb abzuholen (§ 269 BGB; BAG 08.03.1995 – 5 AZR 848/93); nur bei Unzumutbarkeit wird daraus eine Schickschuld. Für die Verzugsargumentation im Aufforderungsschreiben relevant.

## E.6 — Anwendung in der Notenmatrix

Sobald Drift, Auslassungen, Negationen oder Widersprüche erkannt sind, fließen sie nicht mechanisch in die Einzelnote des Satzes ein, sondern in das **Hauptbefundkapitel** des Mandantenberichts. Sie tragen eine Berichtigungsforderung nur, wenn der objektive Empfängerhorizont und der Zeugniszusammenhang sie stützen.

---

# Teil F — Mandatsmodule: Aufforderungsschreiben, Verbesserungen, Klagestrategie

Diese Sektion hält die anwaltlichen Output-Bausteine bereit: außergerichtliches Berichtigungsverlangen, Wortlaut-Verbesserungstabelle, Klageantrag, Streitwert und Vollstreckung.

## Rechtlicher Anker

- § 109 GewO — Arbeitnehmer-Endzeugnis; § 630 BGB — dauerhaftes Dienstverhältnis außerhalb des Arbeitnehmerstatus; § 16 BBiG — Berufsausbildungsverhältnis; § 241 Abs. 2 BGB/BAG 7 AZR 292/17 — Zwischenzeugnis bei triftigem Grund. Vor Anspruchsschreiben und Klage die passende Grundlage festlegen.
- §§ 280 Abs. 1 und 2, 286 BGB — möglicher Verzögerungsschaden erst bei Pflichtverletzung, Vertretenmüssen und Verzug; eine kalendermäßige Frist macht die Mahnung beweisbar, ist aber nicht selbst Anspruchsgrundlage. Vorgerichtliche Anwaltskosten im arbeitsgerichtlichen Kontext wegen § 12a ArbGG/BAG 8 AZR 293/18 nicht schematisch als Verzugsschaden verlangen.
- § 242 BGB — Treu und Glauben; Verwirkung bei langem Zuwarten.
- §§ 195, 199 BGB — regelmäßige Verjährung drei Jahre ab Schluss des Jahres, in dem der Anspruch entstanden ist und Kenntnis vorliegt; Zeugnis-/Beendigungsjahr und Ausschlussfristen immer konkret prüfen.
- §§ 2, 5 ArbGG — Arbeitsrechtsweg statusabhängig; bei Organpersonen gesondert prüfen. Nur bei eröffnetem Arbeitsrechtsweg: § 46 ArbGG zum Verfahren und § 12a ArbGG zum Ausschluss der Anwaltskostenerstattung in erster Instanz.
- BAG 18.06.2025 – 2 AZR 96/24 (B) — vor Beendigung kein wirksamer Zukunftsverzicht auf das qualifizierte Zeugnis; Verzichts- und Erledigungsklauseln nicht ungeprüft gegen den Zeugnisanspruch halten.

## F.1 — Aufforderungsschreiben an die statusrichtige Gegenseite

### Funktion

Drei Aufgaben: faire Korrekturgelegenheit, Schärfung der Streitpunkte, Grundlage für Fristsetzung und Verzug. Ton: höflich, sachlich, bestimmt — keine Drohgebärden, keine Ironie, einmalige Klageandrohung am Ende.

### Aufbau in acht Bausteinen

1. **Mandatsanzeige** — Vollmacht beigefügt, Mandant mit vollem Namen, Geburtsdatum, Beschäftigungszeitraum.
2. **Bezugnahme auf das Zeugnis** — Datum der Erteilung, Datum der Aushändigung, Form (qualifiziert/einfach/Zwischen/Ausbildung/Dienst), Feststellung, welcher einschlägigen Anspruchsnorm es nicht genügt.
3. **Rechtsgrundlage** — im Arbeitnehmerfall § 109 Abs. 1 GewO; § 109 Abs. 1 S. 3 GewO nur beim qualifizierten Zeugnis für Leistung/Verhalten; § 109 Abs. 2 GewO für Klarheit, Verständlichkeit und Geheimzeichenverbot; sonst § 630 BGB, § 16 BBiG oder die Zwischenzeugnis-Nebenpflicht passend zum Status. Zeugniswahrheit, verständiges Wohlwollen und Beweislast nur mit der jeweils übertragbaren BAG-Linie begründen.
4. **Beanstandungen pro Streitstelle** — pro Stelle ein Block: Originalwortlaut in Anführungszeichen, Decodierung (Geheimcode, Drift, Auslassung, fehlendes Adverb), Vorschlag in Anführungszeichen, Begründung.
5. **Schlussformel und Gesamtbild** — wenn relevant, separat behandeln.
6. **Fristsetzung** — kalendermäßig (kein „binnen zwei Wochen"), Standard zwei bis drei Wochen; bei Eilbedarf kürzer mit Begründung.
7. **Klageandrohung** — einmal, knapp, sachlich.
8. **Kostenrisiko und Anlagenverzeichnis** — keine standardmäßige Anwaltskostengeltendmachung; Vollmacht, Zeugnis, Vorzeugnis, Korrespondenz.

### Mustertext

Das folgende Muster ist für ein Arbeitnehmer-Endzeugnis nach § 109 GewO formuliert. Bei Dienst-, Ausbildungs- oder Zwischenzeugnissen Anspruchsnorm, Parteibezeichnungen und Gericht anpassen; bei Organpersonen den Arbeitsrechtsweg nicht ungeprüft androhen.

> Sehr geehrte Damen und Herren,
>
> unter Beifügung der auf uns lautenden Vollmacht zeigen wir die anwaltliche Vertretung der Mandantin [Vorname Name], geboren am [Datum], an. Bei Ihnen bestand vom [Datum] bis zum [Datum] ein Arbeitsverhältnis.
>
> Unsere Mandantin hat am [Datum] das beigefügte qualifizierte Zeugnis erhalten. Es entspricht nicht den Ansprüchen aus § 109 GewO. Aus Zeugniswahrheit, verständigem Wohlwollen und dem Klarheits-/Geheimzeichenverbot des § 109 Abs. 2 GewO ergeben sich Berichtigungspflichten zu folgenden Punkten:
>
> **Punkt 1 — Leistungsformel.** Originalwortlaut: „[…]". In der Zeugnissprache bedeutet dies [Geheimcode/Drift/Auslassung]. Wir bitten um folgende Neufassung: „[…]".
>
> **Punkt 2 — Verhaltensbeurteilung.** Originalwortlaut: „[…]". Reihenfolge oder Adverbschwäche signalisiert [Befund]. Vorgeschlagene Neufassung: „[…]".
>
> **Punkt 3 — Schlussformel.** Es fehlt das Bedauern. Uns ist bewusst, dass nach der Rechtsprechung des Bundesarbeitsgerichts (zuletzt Urteil vom 25.01.2022 – 9 AZR 146/21) kein einklagbarer Anspruch auf eine Schlussformel besteht; wir bitten gleichwohl im Interesse eines stimmigen Gesamtbildes um folgende Neufassung: „[…]".
>
> Wir bitten, das berichtigte Zeugnis bis zum [Datum] auf Geschäftspapier ohne Anlassbezug auf das Berichtigungsverlangen zu erteilen. Sollte das Zeugnis nicht fristgerecht in der vorgeschlagenen Form neu erteilt werden, werden wir nach abschließender Prüfung des Rechtswegs Klage beim zuständigen Gericht erheben.
>
> Mit freundlichen Grüßen
>
> [Kanzlei]
> Anlagen: Vollmacht, Zeugnis vom [Datum], Vorzeugnis vom [Datum]

### Stilregeln

| Regel | Hinweis |
| --- | --- |
| höflich, bestimmt, sachlich | keine Drohgebärden |
| Kosten | vorgerichtliche Anwaltskosten im arbeitsgerichtlichen Kontext nicht standardmäßig als Verzugsschaden verlangen; § 12a ArbGG und BAG 8 AZR 293/18 prüfen |
| konkrete Wortlaute statt „bitte verbessern" | pro Streitstelle alt + neu in Anführungszeichen |
| Belege für Geheimcodes | BAG-Rechtsprechung live verifizieren |
| Verzichtsklauseln | vor Beendigung erklärten Zukunftsverzicht nicht als Ausschlussgrund behandeln; BAG 2 AZR 96/24 (B) prüfen |
| Frist kalendermäßig | konkretes Datum |
| Klageandrohung nur am Ende | einmal, knapp |

## F.2 — Verbesserungsvorschläge: Wortlaut-Tabelle

Operative Umformulierungen vom beanstandeten zum tragfähigen Wortlaut.
Jeder Zielwortlaut steht unter Zeugniswahrheit: nicht automatisch aufwerten, sondern nur eine durch Tatsachen und Gesamtbild gedeckte Formulierung verlangen.

| Original (🔴/🟠) | Operation | Ergebnis (🟢) |
| --- | --- | --- |
| „zur Zufriedenheit" | stets + vollsten ergänzen | „stets zur vollsten Zufriedenheit" |
| „bemüht" | Ergebnis statt Wille | „stets mit Erfolg erledigt" |
| „im Wesentlichen" | Einschränkung streichen | Formulierung ohne Einschränkung |
| „nach Anweisung" | Eigenverantwortung einsetzen | „eigenverantwortlich und selbstständig" |
| kein Bedauern | Bedauern ergänzen | „Wir bedauern es sehr, Herrn X zu verlieren" |
| „korrekt" (Verhalten) | auf „stets einwandfrei" aufwerten | „Sein Verhalten war stets einwandfrei" |
| „zeigte hohe Lernbereitschaft" | Verb und Steigerer aufwerten | „bildete sich stets eigeninitiativ und mit großem Erfolg fort" |
| „fand gute neue Ideen" | Verb und Adjektiv aufwerten | „entwickelte stets hervorragende innovative Lösungsansätze" |
| „war in der Lage, Konflikte zu bewältigen" | Fähigkeit zu Tatsache | „löste Konflikte stets souverän und mit Augenmaß" |
| „geschätzter Ansprechpartner" | Steigerung ergänzen | „äußerst geschätzter und gefragter Ansprechpartner" |
| Drift im Themenbereich | beide Sätze auf dasselbe Niveau heben | schwacher Satz wird aktiv aufgewertet |

### Operationsprinzipien

1. **Adverb und Prädikat zusammen lesen** — „stets/jederzeit" prägt die Beständigkeit, „voll/vollsten" die Bewertungsstufe. Kein einzelnes Wort entscheidet ohne Satz- und Gesamtkontext die Note.
2. **Ergebnis statt Wille** — „bemüht" und „in der Lage" durch konkrete Erfolgsaussage ersetzen.
3. **Reihenfolge im Verhaltensteil** — Vorgesetzte vor Kollegen vor Kunden ist ein verbreiteter Regelfall. Eine Abweichung wird erst bei rollenrelevantem Kontakt und objektiv negativer Lesart zum Berichtigungspunkt.
4. **Schlussformel in drei Elementen** — Bedauern, Dank, Wunsch. Vollständigkeit ist Verhandlungspunkt, kein automatischer Klageanspruch.

## F.3 — Klagestrategie Zeugnisberichtigung

### Erfolgsaussichten je Befundtyp

| Befund | Rechtliche Einordnung | Erfolgsaussicht |
| --- | --- | --- |
| „bemüht" als zusammenfassende Leistungsformel | Berichtigung einer unterdurchschnittlichen Bewertung; der Arbeitgeber muss die Tatsachengrundlage für eine Bewertung unterhalb von Note 3 darlegen und beweisen | mittel bis hoch, abhängig vom Gesamtzeugnis |
| abweichende Reihenfolge im Sozialverhalten | kein Automatismus; Berichtigung nur bei rollenrelevantem Kontakt und objektiv negativer Lesart ohne neutrale Erklärung | niedrig bis mittel |
| unvollständige Schlussformel | regelmäßig nur Verhandlungspunkt; grundsätzlich kein Anspruch auf Dank, Bedauern oder gute Wünsche | niedrig |
| vermeintliches negatives Codewort | Berichtigung nur, wenn Wortlaut und Gesamtkontext aus objektivem Empfängerhorizont eine verdeckte Negativaussage tragen | einzelfallabhängig |
| Drift oder Widerspruch im selben Themenbereich | kein eigener Anspruchstatbestand; relevant, wenn das Gesamtzeugnis dadurch unwahr, unklar oder objektiv irreführend wird | einzelfallabhängig |
| Note 3 bei verlangter Aufwertung | bessere Bewertung nur bei konkretem Zielwortlaut und Tatsachen für überdurchschnittliche Leistung | niedrig bis mittel; Arbeitnehmer beweisbelastet |
| Note 4 als Gesamtbewertung | Arbeitgeber muss Tatsachen für die unterdurchschnittliche Leistung darlegen und beweisen | mittel bis hoch |

### Beweislast

| Streitfrage | Darlegungs- und Beweislast |
| --- | --- |
| verlangte Gesamtbewertung besser als befriedigend | Arbeitnehmer: konkrete Tatsachen für die überdurchschnittliche Leistung |
| erteilte Gesamtbewertung schlechter als befriedigend | Arbeitgeber: konkrete Tatsachen für die unterdurchschnittliche Leistung |
| unrichtige Kopfdaten oder Tatsachenangaben | beanstandete Abweichung und verlangten richtigen Inhalt konkret darlegen; Beweislast nach der jeweils streitigen Tatsache, nicht schematisch nach der Notenregel |
| Geheimzeichen oder unklare Formulierung | Arbeitnehmer legt Wortlaut, Kontext und objektiv verdeckte bzw. unklare Lesart dar; bloß subjektives Missfallen genügt nicht |
| rollen- oder branchenbezogene Auslassung | Arbeitnehmer legt dar, warum die positive Hervorhebung nach Funktion oder Branchenbrauch erwartet wird und ihr Fehlen nachteilig wirkt (BAG 9 AZR 632/07) |
| Reihenfolge im Sozialverhalten | Arbeitnehmer muss Rollen-/Kontaktrelevanz und negative Lesart darlegen; Arbeitgeber kann neutrale Erklärung oder Branchenkontext einwenden |

Die BAG-Notenregel betrifft die zusammenfassende Leistungsbewertung. Sie darf nicht mechanisch auf jedes Adjektiv, jeden Formmangel oder jede Tatsachenangabe übertragen werden. Grundlage: BAG 14.10.2003 – 9 AZR 12/03 und BAG 18.11.2014 – 9 AZR 584/13; für Klarheit, Empfängerhorizont und Auslassungen BAG 15.11.2011 – 9 AZR 386/10 und BAG 12.08.2008 – 9 AZR 632/07 ([Rechtsprechungsanker](#rechtsprechungsanker--bag-leitentscheidungen)).

### Streitwert

Im arbeitsgerichtlichen Zeugnisstreit wird häufig ein Bruttomonatsgehalt als Orientierung angesetzt. Das ist keine starre gesetzliche Pauschale; Gegenstand, Umfang der begehrten Änderung, örtliche Praxis und aktueller Streitwertkatalog sind live zu prüfen. Mehrere Formulierungswünsche erhöhen den Wert nicht automatisch. Bei ordentlichem Rechtsweg gelten die dortigen Wert- und Kostenregeln.

| Klagegegenstand | Streitwert |
| --- | --- |
| vollständige Zeugnisberichtigung | häufig bis zu einem Monatsbruttogehalt; örtliche Praxis prüfen |
| einzelne Note oder begrenzte Korrektur im Hauptteil | Abschlag oder Monatsbruttogehalt je nach Umfang; örtliche Praxis prüfen |
| Schlussformel als Nebenpunkt | regelmäßig kein eigenständiger Streitwert; nur bei selbständigem Streit nach Live-Prüfung |
| mehrere Punkte gemeinsam | keine schematische Addition; Gesamtgegenstand bewerten |
| erstmalige Erteilung | häufig ein Monatsbruttogehalt; örtliche Praxis prüfen |

### Musterklageantrag

> Der Beklagte wird verurteilt, der Klägerin ein qualifiziertes Arbeitszeugnis zu erteilen, das auf dem Briefkopf der Beklagten ausgestellt ist, das Beendigungsdatum trägt, vom dazu Befugten unterschrieben ist und folgenden Inhalt aufweist:
>
> Erstens, in der Leistungsbeurteilung statt „war stets bemüht" die Formulierung „erledigte die ihr übertragenen Aufgaben stets zu unserer vollen Zufriedenheit".
>
> Zweitens, in der Verhaltensbeurteilung statt „Kollegen und Vorgesetzten" die Reihenfolge „Vorgesetzten, Kollegen und Kunden" mit dem Steigerer „stets" und dem Prädikat „einwandfrei".
>
> Drittens, [weitere Punkte analog].

### Beweismittel für bessere Note

- Zwischenzeugnisse mit gutem oder sehr gutem Inhalt.
- Zielvereinbarungen, Bonusabrechnungen, Performance-Reviews.
- Lob-E-Mails, Kundenbewertungen.
- Zeugen: unmittelbare Vorgesetzte, Projektleiter.

### Kostenrisiko, Fristen und Verwirkung

- § 12a ArbGG: im erstinstanzlichen arbeitsgerichtlichen Kontext sind eigene Anwaltskosten regelmäßig nicht erstattungsfähig; die Gegenseite kann ihre Anwaltskosten ebenfalls regelmäßig nicht erstattet verlangen. Der Ausschluss erfasst nach BAG 8 AZR 293/18 auch materielle Ansprüche auf vor- und außergerichtliche Rechtsverfolgungskosten.
- Bei Organpersonen oder sonst eröffnetem ordentlichen Rechtsweg gilt § 12a ArbGG nicht; Kostenfolge und vorgerichtliche Erstattungsfähigkeit sind nach dem dort einschlägigen Zivilprozess- und materiellen Recht neu zu prüfen.
- Verwirkung: wer ohne nachvollziehbaren Grund lange zuwartet, riskiert den Anspruchsverlust. Empfehlung: Berichtigungsverlangen innerhalb der ersten Monate nach Zeugnisübergabe.
- Ausschlussfristen: Arbeitsvertrag, Tarifvertrag oder Vergleich können deutlich kürzere Geltendmachungsfristen enthalten; vor Aufforderungsschreiben und Klage immer prüfen.
- Verjährung: regelmäßige Verjährung drei Jahre ab Schluss des Jahres, in dem der Anspruch entstanden ist und Kenntnis vorliegt (§§ 195, 199 BGB); nicht schematisch nur auf das Ausstellungsdatum abstellen.

### Vergleichsfenster

Häufig schon vor dem Gütetermin. Vorformulierten Vergleichstext bereithalten: Wortlaut der Streitstellen, Zeitpunkt der Übergabe des berichtigten Zeugnisses, Erledigungserklärung.

**Vollstreckbarkeit des Zeugnisvergleichs (BAG 07.05.2026 – 8 AZB 25/25):** Die im gerichtlichen Vergleich übernommene Pflicht, das Zeugnis nach dem **Entwurf des Arbeitnehmers** zu erteilen — mit Abweichungsvorbehalt nur aus wichtigem Grund — hat vollstreckbaren Inhalt. Praxisfolge: Diese Entwurfsklausel ist ein starkes Vergleichsinstrument und sollte im Vergleichstext mitgedacht werden. Sie eröffnet Vollstreckung, wenn der Arbeitgeber keinen nachvollziehbaren wichtigen Grund vorträgt. Beruft er sich dagegen substantiiert auf Zeugniswahrheit oder Zeugnisklarheit, kann das Zwangsgeld scheitern; der Inhalt ist dann nicht im Vollstreckungsverfahren auszujudizieren, sondern in einem neuen Erkenntnisverfahren zu klären (BAG 8 AZB 25/25, Rn. 19-21). Nicht ausreichend ist eine bloße Notenformel ohne konkreten Zeugnisinhalt („sehr gute Führungs- und Leistungsbeurteilung"): Das ist regelmäßig zu unbestimmt für die Vollstreckung (BAG 14.02.2017 – 9 AZB 49/16).

## F.4 — Vollstreckung des Zeugnisanspruchs

Wenn Urteil oder Vergleich vorliegt, der Arbeitgeber aber nicht oder falsch erfüllt:

| Lage | Instrument |
| --- | --- |
| Titulierter Zeugnisanspruch wird nicht erfüllt | Zwangsgeld, ersatzweise Zwangshaft (§ 888 ZPO — nicht vertretbare Handlung, da nur der Arbeitgeber die Beurteilung abgeben kann) |
| Vergleich mit Entwurfsklausel („Zeugnis nach Entwurf des Arbeitnehmers, Abweichung nur aus wichtigem Grund") | Vollstreckbarer Inhalt (BAG 07.05.2026 – 8 AZB 25/25); Zwangsmittel aber nur, wenn kein nachvollziehbarer Wahrheits-/Klarheitseinwand besteht |
| Vergleich nur mit Notenstufe („sehr gut", „gut") ohne konkrete Formulierungen | Regelmäßig nicht hinreichend bestimmt und nicht tragfähig vollstreckbar (BAG 14.02.2017 – 9 AZB 49/16); im Vergleich konkrete Wortlaute, Form oder Entwurfsklausel festlegen |
| Erteiltes Zeugnis weicht vom Titel ab | Im Vollstreckungsverfahren rügen; ironische Übererfüllung ist Nichterfüllung (LAG Hamm 14.11.2016 – 12 Ta 475/16) |
| Streit über „wichtigen Grund" der Abweichung | Arbeitgeber muss nachvollziehbar vortragen; bei substantiiertem Streit über Zeugniswahrheit/-klarheit Klärung im Erkenntnisverfahren, nicht per Zwangsgeld |

**Praxisregel:** Schon beim Vergleichsschluss an die Vollstreckung denken — die Entwurfsklausel mit Wichtiger-Grund-Vorbehalt (F.3) macht aus dem Vergleich einen praktisch verwertbaren Titel, aber keinen Freibrief gegen Zeugniswahrheit und Zeugnisklarheit. Bloße Notenstufen helfen in der Verhandlung als Zielbild, nicht als sauberer Titel.

## F.5 — Anschlussschritte

- Aufforderung blieb fruchtlos → Klage einreichen.
- Vollberichtigung → Abschlussschreiben an die statusrichtige Gegenseite; Mandatsabschluss und Abrechnung gegenüber dem Mandanten, keine Kostengeltendmachung gegen die Gegenseite ohne gesonderte Prüfung.
- Teilberichtigung → mit Mandant entscheiden: Akzeptanz oder Restklage.
- Titel liegt vor, Erfüllung bleibt aus → Vollstreckungsmodul F.4.

---

# Teil G — Musterzeugnisse und Sonderfälle

Diese Sektion hält drei vollständige Musterzeugnisse (Note 1, gemischt mit Drift, rote Flaggen) und drei Sonderfälle (leitende Positionen, Ausbildungszeugnis nach § 16 BBiG, branchenspezifische Pflichtaussagen) bereit. Die Muster sind Schulungsfälle — erst eigene Hypothese bilden, dann mit der Analyse abgleichen.

## G.1 — Muster 1: Note 1 (Positivreferenz)

### Volltext

> **Musterunternehmen GmbH | Musterstraße 1 | 10000 Musterstadt**
>
> **Arbeitszeugnis**
>
> Frau Anna Musterfrau, geboren am 1. Januar 1985, war vom 1. März 2018 bis zum 28. Februar 2025 in unserem Unternehmen als Leiterin der Abteilung Controlling tätig.
>
> **Aufgaben:** Frau Musterfrau verantwortete die vollständige Führung unserer Controlling-Abteilung mit zwölf direkt unterstellten Mitarbeiterinnen und Mitarbeitern. Sie war zuständig für die monatliche Ergebnisberichterstattung an den Vorstand, die Erstellung der Jahresplanung und des mittelfristigen Finanzplans, die Durchführung von Abweichungsanalysen sowie die Koordination externer Prüfungsgesellschaften.
>
> **Leistungsbeurteilung:** Frau Musterfrau verfügt über hervorragende Fachkenntnisse, die sie stets sicher, souverän und mit außerordentlichem Erfolg eingesetzt hat. Ihre Arbeitsweise war stets strukturiert, präzise und ergebnisorientiert. Auch in Phasen hoher Arbeitsbelastung behielt sie stets die Übersicht und erzielte konstant hervorragende Ergebnisse. Ihre Eigeninitiative und ihr außerordentliches Engagement haben unser Unternehmen maßgeblich vorangebracht. Alle ihr übertragenen Aufgaben erledigte sie stets zu unserer vollsten Zufriedenheit.
>
> **Verhaltensbeurteilung:** Das Verhalten von Frau Musterfrau gegenüber Vorgesetzten, Kolleginnen und Kollegen sowie externen Partnern war stets einwandfrei. Sie führte ihre Mitarbeiterinnen und Mitarbeiter mit klarer Zielorientierung, hoher Wertschätzung und nachhaltigem Erfolg. Ihre Kommunikation war stets klar, konstruktiv und auf das Gesamtergebnis ausgerichtet. Frau Musterfrau genoss das vollste Vertrauen der Geschäftsführung.
>
> **Schlussformel:** Frau Musterfrau scheidet auf eigenen Wunsch aus unserem Unternehmen aus. Wir bedauern dies außerordentlich und danken ihr herzlich für ihre hervorragenden Leistungen, ihren unermüdlichen Einsatz und ihren wertvollen Beitrag zum Erfolg unseres Unternehmens. Für ihren weiteren beruflichen und persönlichen Weg wünschen wir ihr nur das Allerbeste und weiterhin großen Erfolg.

### Ampel-Befund

| Element | Ampel | Note |
| --- | --- | --- |
| „stets zur vollsten Zufriedenheit" | 🟢 | 1 |
| „hervorragende Fachkenntnisse" | 🟢 | 1 |
| „außerordentliches Engagement" | 🟢 | 1 |
| „stets einwandfrei" (Verhalten) | 🟢 | 1 |
| Warme Schlussformel mit Bedauern, Dank, Wunsch | 🟢 | 1 |

Konsistent 🟢, keine Drift, keine Auslassung. Gesamtnote 1.

## G.2 — Muster 2: Schaufenster-Drift (Note 2 bis 3 nach Aggregation)

### Volltext (Auszüge mit Drift-Signal)

> Herr Beispiel verfügt auch in Randbereichen seines vielfältigen Aufgabenbereiches über äußerst profundes Fachwissen.
>
> Herr Beispiel nahm in eigener Initiative regelmäßig erfolgreich an internen und externen Weiterbildungsseminaren teil.
>
> Hervorzuheben ist sein ausgeprägt strategisches Denkvermögen, das es ihm ermöglichte, auch bei neuen geschäftlichen Entwicklungen stets in kürzester Zeit optimale Lösungen zu entwickeln.
>
> Er zeigte sich auch bei der Bewältigung neuer Aufgabenbereiche flexibel und aufgeschlossen.
>
> Herr Beispiel verfügt über eine besonders hohe Arbeitsmoral und war stets äußerst motiviert, die gesetzten Ziele beharrlich zu verfolgen.
>
> Herr Beispiel zeigte eine hohe Lernbereitschaft.
>
> Alle Aufgaben führte er jederzeit vollkommen selbstständig, äußerst sorgfältig und planvoll durchdacht aus.
>
> Herr Beispiel war Neuem gegenüber aufgeschlossen, fand gute neue Ideen und innovative Ansätze.
>
> Herr Beispiel hat die an ihn gestellten sehr hohen Erwartungen zu unserer vollsten Zufriedenheit erfüllt und teilweise sogar übertroffen.
>
> Wegen seines freundlichen und hilfsbereiten Auftretens war Herr Beispiel ein geschätzter Ansprechpartner. Sein persönliches Verhalten gegenüber Vorgesetzten, Mitarbeitern und Externen war einwandfrei.

### Bereichs-Drift-Analyse

| Themenbereich | Höchste Note | Niedrigste Note | Drift | Ampel |
| --- | --- | --- | --- | --- |
| Fachkenntnisse | 1 | 1 | keine | 🟢 |
| Lernbereitschaft | 1 (indirekt) | 3 | zwei Stufen | 🔴 |
| Strategisches Denken | 1 | 1 | keine | 🟢 |
| Flexibilität | 3 | 3 | keine | 🟠 |
| Engagement | 1 | 1 | keine | 🟢 |
| Arbeitsweise | 1 | 1 | keine | 🟢 |
| Innovation | 3 | 3 | keine | 🟠 |
| Sozialverhalten | 3 | 3 | keine | 🟠 |
| Gesamtbeurteilung und Schluss | 1 | 1 | keine | 🟢 |

**Aggregation:** Spitzensätze authentisch (Fachkenntnisse, Arbeitsweise, Engagement). Drift zwei Stufen im Themenblock Lernbereitschaft. Konstante Note 3 in Innovation und Sozialverhalten. Gesamtnote nach Aggregation: 2 bis 3.

**Empfehlung:** Nachverhandlung der Sätze zu Lernbereitschaft, Innovation und Sozialverhalten. Wird eine eindeutige Gesamtnote 2 oder die Aufwertung einzelner durchschnittlicher Aussagen verlangt, muss der Arbeitnehmer die dafür sprechenden überdurchschnittlichen Leistungen konkret darlegen und gegebenenfalls beweisen; die vorhandenen Spitzensätze sind dafür Indizien, ersetzen den Tatsachenvortrag aber nicht.

## G.3 — Muster 3: Rote Flaggen (Note 4)

### Volltext

> **Beispiel GmbH | Beispielstraße 5 | 20000 Beispielstadt**
>
> **Arbeitszeugnis**
>
> Herr Thomas Beispiel, geboren am 15. Juni 1980, war vom 1. Januar 2020 bis zum 30. Juni 2024 in unserem Unternehmen als Vertriebsmitarbeiter beschäftigt.
>
> **Aufgaben:** Herr Beispiel war im Außendienst tätig und betreute einen definierten Kundenkreis im Bereich Industriebedarf. Er war für regelmäßige Kundenbesuche, die Angebotserstellung und die Bearbeitung von Reklamationen zuständig.
>
> **Leistungsbeurteilung:** Herr Beispiel verfügt über ausreichende Fachkenntnisse für seinen Aufgabenbereich. Er war stets bemüht, die ihm übertragenen Aufgaben zur vollen Zufriedenheit zu erledigen, und zeigte dabei durchgehend guten Willen. Seine Arbeitsweise war im Wesentlichen strukturiert.
>
> **Verhaltensbeurteilung:** Gegenüber Kollegen und Vorgesetzten verhielt sich Herr Beispiel korrekt. Er zeichnete sich durch eine direkte Kommunikationsweise aus.
>
> **Schlussformel:** Wir danken Herrn Beispiel für seine Mitarbeit und wünschen ihm für die Zukunft alles Gute.

### Befund

| Befund | Bedeutung | Ampel | Note |
| --- | --- | --- | --- |
| „ausreichende Fachkenntnisse" | unterdurchschnittlich | 🔴 | 4 |
| „stets bemüht" | trotz Willen keine Ergebnisse | 🔴 | 4 bis 5 |
| „zur vollen Zufriedenheit" ohne „stets" | fehlende Steigerung | 🟠 | 3 |
| „im Wesentlichen strukturiert" | erhebliche Mängel | 🔴 | 4 |
| „Kollegen und Vorgesetzten" (Reihenfolge) | auffällige Reihenfolge; Kontext prüfen | 🟠 | 3 |
| „korrekt" (Verhalten) | schwache Formel | 🟠 | 3 |
| „direkte Kommunikationsweise" | riskiert Lesart „grob/schwierig" | 🔴 | 4 bis 5 |
| Schweigen zu Kunden bei Vertriebsjob | riskiert negative Lesart zum Kundenkontakt | 🔴 | — |
| Schlussformel ohne Bedauern | Distanzsignal, grundsätzlich kein Anspruch | 🟠 | — |

**Gesamtbild:** Leistung 4, Verhalten 4, Schluss 3 bis 4. Gesamtnote 4.

**Handlungsempfehlung:** Nachverhandlung aller Leistungs- und Verhaltensformulierungen sowie wärmere Schlussformel. Bei Weigerung: Klage zu Leistung und Verhalten gut tragfähig; Schlussformel nur mit Zusatzkontext.

## G.4 — Sonderfall A: Leitende Positionen

Führungskräftezeugnisse haben typische Erwartungsbausteine. Ihr Fehlen ist nicht automatisch ein Mangel, kann aber bei entsprechender Rolle ein eigener Berichtigungspunkt sein.

| Erwartungsbaustein | Fehlen kann gelesen werden als | Ampel |
| --- | --- | --- |
| Mitarbeiterführung und -entwicklung | Führungsleistung ausgeklammert | 🔴 |
| Strategische Verantwortung | Strategiebeteiligung unklar oder nicht belegt | 🟠🔴 |
| Budget- und P&L-Verantwortung | wirtschaftliche Führungsrolle unklar | 🟠 |
| Repräsentation nach außen | externe Wirkung ausgeklammert | 🟠 |
| Loyalitätsaussage gegenüber Gesellschaftern oder Vorstand | Loyalitäts- oder Vertraulichkeitsfrage | 🔴 |

**Beispiel 🟢 Führungsaussage (Note 1):** „Frau Dr. Hoffmann führte ihre über 80 Mitarbeiter mit klarem Ziel, hoher Empathie und nachhaltigem Erfolg. Unter ihrer Leitung verzeichnete der Bereich eine Steigerung der Mitarbeiterzufriedenheit und eine signifikante Verbesserung der Ergebnisse."

**Beispiel 🟠 Führungsaussage (Note 3):** „Herr Vogel pflegte einen kooperativen Führungsstil und wurde von seinen Mitarbeitern geschätzt." — passiv, kein Erfolgsnachweis.

**Beispiel 🔴 Schweigen:** Abteilungsleiter mit 15 Mitarbeitenden ohne eine einzige Aussage zur Mitarbeiterführung — starkes Risikosignal, dessen Branchen- und Rollenerwartung konkret zu belegen ist.

## G.5 — Sonderfall B: Ausbildungszeugnis (§ 16 BBiG)

### Rechtsgrundlagen

- § 16 Abs. 1 BBiG — Pflicht zur Zeugniserteilung bei Beendigung des Berufsausbildungsverhältnisses und Form; haben Ausbildende nicht selbst ausgebildet, **soll** auch der Ausbilder oder die Ausbilderin unterschreiben.
- § 16 Abs. 2 S. 1 BBiG — zwingender Mindestinhalt: Art, Dauer und Ziel der Berufsausbildung sowie erworbene berufliche Fertigkeiten, Kenntnisse und Fähigkeiten. § 16 Abs. 2 S. 2 BBiG — Angaben zu Verhalten und Leistung nur auf Verlangen.
- § 26 BBiG kann § 16 auf bestimmte andere, nicht als Arbeitsverhältnis vereinbarte Vertragsverhältnisse zum Erwerb beruflicher Fertigkeiten, Kenntnisse, Fähigkeiten oder Erfahrungen erstrecken. Umschulung und Fortbildung werden davon nicht allein wegen ihres Qualifizierungszwecks erfasst; je nach Status kann der Zeugnisanspruch aus § 630 BGB oder § 109 GewO folgen (BAG 12.02.2013 – 3 AZR 121/11).

### Azubi-Geheimcodes

| Formulierung | Bedeutung | Ampel |
| --- | --- | --- |
| „schnell und sicher aufgenommen" | hervorragender Lernfortschritt | 🟢 |
| „zuverlässig die Ausbildungsinhalte angeeignet" | guter Lernfortschritt | 🟢 |
| „hat sich die Inhalte erarbeitet" | befriedigender Fortschritt | 🟠 |
| „war bereit zu erlernen" | unterdurchschnittlicher Fortschritt | 🔴 |
| fehlender Berufsschulabschnitt (duale Ausbildung) | Schulprobleme möglich; Kontext prüfen | 🟠 |
| „hat sich positiv entwickelt" (im Azubi-Kontext) | gut | 🟢 |
| „pünktlich und zuverlässig" | wichtiges Grundverhalten | 🟢 |
| fehlende Pünktlichkeitsaussage | mögliche Auffälligkeit; Branchenbrauch prüfen | 🟠 |

### Triage

1. Echtes Berufsausbildungsverhältnis nach BBiG, Umschulung, Fortbildung, Praktikum oder sonstige Qualifizierung? Anspruchsnorm zuerst festlegen.
2. Abschlusszeugnis oder Zwischenzeugnis?
3. Duale Ausbildung → Berufsschulbewertung vorhanden?
4. Ausbildung abgebrochen → Mindestinhalt bleibt geschuldet; Angaben zu Verhalten und Leistung nach § 16 Abs. 2 S. 2 BBiG auf Verlangen prüfen.
5. Beendigungsgrund: bestandene Prüfung oder Kündigung/Aufhebung?

**Beispiel 🟢:** „Herr Müller hat die Ausbildungsinhalte stets schnell und sicher aufgenommen, zeigte großes Interesse an seinem Ausbildungsberuf und zeichnete sich durch hervorragende Berufsschulleistungen aus."

**Beispiel 🔴:** „Herr Bauer war stets bereit, die Ausbildungsinhalte zu erlernen, und hat die Anforderungen im Wesentlichen erfüllt." — doppeltes Negativsignal.

## G.6 — Sonderfall C: Branchenspezifische Pflichtaussagen

Wer im Vertrieb ohne Zielerreichungssatz dasteht oder in der Pflege ohne Patientenkontakt-Satz, hat ein verdecktes Negativsignal — unabhängig davon, wie gut die übrigen Sätze klingen.

| Branche | Erwartbare Aussage | Fehlen kann gelesen werden als |
| --- | --- | --- |
| Vertrieb | Zielerreichung, Kundenbindung, Neukundengewinnung | unterdurchschnittliche Vertriebsleistung |
| Recht und Kanzlei | Mandatsführung, Schriftsatzqualität | Qualitätsprobleme im Kernjob |
| IT | Projektabschlüsse, Technologiekompetenz | fehlende Kernergebnisse |
| Pflege | Patientenkontakt, Empathie | Probleme mit Patienten |
| Finanzwesen und Buchhaltung | Zuverlässigkeit, Genauigkeit, Vertrauen | Integritäts- oder Sorgfaltsfragen |
| Personalwesen | Mitarbeiterentwicklung, Verhandlungsführung | Schwäche im Kernbereich |
| Einzelhandel | Kassenführung, Warenkenntnis | Kassenproblem |
| Öffentlicher Dienst | Gesetzeskenntnis, Verfahrensführung, Bürgerkontakt | mangelhafte Amtsführung |

**Beispiel Vertrieb 🟢:** „Herr Kurz übertraf seine Vertriebsziele im Beobachtungszeitraum durchgehend und war maßgeblich an der Neukundengewinnung beteiligt."

**Beispiel IT 🟠:** „Frau Kramer hat an mehreren Softwareprojekten mitgewirkt und dabei ihre technischen Fähigkeiten eingesetzt." — passiv, keine Erfolgs- oder Verantwortungsaussage.

**Beispiel Pflege 🔴 durch Schweigen:** Stationsschwester-Zeugnis ohne eine einzige Aussage zu Patientenversorgung oder Empathie; erst nach belegter Rollen- und Branchenerwartung als Berichtigungspunkt führen.
