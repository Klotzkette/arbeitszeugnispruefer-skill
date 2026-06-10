# Arbeitszeugnis-Prüfer Skill

> **Experimenteller Agent-Skill** für die anwaltliche Prüfung deutscher Arbeitszeugnisse — als Anregung für Kanzlei-Arbeitsabläufe. Orientiert sich an der deutschen Rechtspraxis, an Gesetzestexten, amtlichen Materialien und frei überprüfbarer Rechtsprechung. Enthält keinerlei Fachgutachten oder Rechtsberatung, alle Angaben ohne Gewähr — jede Nutzerin und jeder Nutzer kalibriert den Skill selbst für die eigene Praxis.

> **Transparenz:** Dieser Skill ist strukturierter Markdown-Text — ein umfangreicher, sorgfältig gegliederter Prompt, den ein Sprachmodell bei der Analyse eines Arbeitszeugnisses als Arbeitsanweisung lädt. Kein eigenes Modell, keine Blackbox, keine versteckte Logik. Der gesamte Inhalt ist offen einsehbar, nachvollziehbar, anpassbar und forkbar.
>
> **Eine einzige Datei, modellunabhängig einsetzbar.** Der vollständige Skill steckt in einer einzigen Markdown-Datei: [`skill/SKILL.md`](skill/SKILL.md) — ohne Anhänge, ohne externe Referenzen. Er funktioniert in jedem leistungsfähigen KI-Chatbot bzw. Sprachmodell: Claude, ChatGPT, Gemini, Mistral, Perplexity, lokal betriebene Modelle. Anwendung: Inhalt der Datei in den Chat kopieren, darunter das zu prüfende Arbeitszeugnis einfügen. Es ist keine Installation, kein Upload, kein Konto und kein zusätzliches Werkzeug erforderlich.

Konsolidierter Skill (Version 2.0) für die Prüfung deutscher Arbeitszeugnisse nach dem Ampelsystem — ausgegeben als farbige Ampelsymbole 🔴/🟠/🟢, nicht als Farbwörter.

**Sofortstart:** Zeugnis einfügen genügt. Der Skill startet die Vollanalyse ohne Fragenkaskade, kennzeichnet fehlende Angaben als Annahmen und stellt höchstens eine gebündelte Rückfrage — nur dann, wenn die Analyse sonst objektiv falsch würde.

Der Skill bündelt eine ursprünglich 50-teilige Plugin-Sammlung in eine einzige `SKILL.md`. Er deckt den vollständigen Bogen ab — vom Mandanten-Intake über die satzweise Notenmatrix bis zur Klagestrategie auf Zeugnisberichtigung.

## Inhalt

```
skill/
└── SKILL.md   Alles in einer Datei: Workflow, Codes, Flaggen, Mandatsmodule, Musterzeugnisse
```

Die Datei ist in folgende Teile gegliedert (interne Sprungmarken):

- **Workflow in acht Stufen** — Intake bis Klagestrategie, rechtlicher Anker, Antwortformate, Qualitätsgate.
- **Sofortstart und Rückfrage-Disziplin** — Zeugnis rein, Analyse läuft; Annahmen statt Fragenkaskade.
- **Ampel-Darstellung** — Befunde immer als 🔴/🟠/🟢, mit Ampel-Bilanz im Hauptbefund.
- **Rechtsprechungsanker** — verifizierte BAG-Leitentscheidungen (1995–2026) zu Notenstufen, Beweislast, Schlussformel, Maßregelungsverbot, Zeugnisklarheit, Tabellenform, Vollstreckbarkeit und äußerer Form, ergänzt um frei verfügbare LAG- und instanzgerichtliche Rechtsprechung.
- **Teil A — Zufriedenheitsformel** — Notenstufen 1 bis 5 der Hauptformel.
- **Teil B — Schlussformel** — Bedauern/Dank/Wunsch, Signal versus Anspruch.
- **Teil C — Geheimcode-Katalog** — Standardphrasen nach Themenachsen.
- **Teil D — Ampel-Flaggen** — Steigerungsadverbien, grüne/orange/rote Flaggen, negative Codeworte.
- **Teil E — Analyse-Techniken** — Drift, Auslassungen, Negationen, Widersprüche, Formalia.
- **Teil F — Mandatsmodule** — Aufforderungsschreiben, Wortlaut-Verbesserungen, Klageantrag.
- **Teil G — Musterzeugnisse und Sonderfälle** — Drei Musterzeugnisse, leitende Positionen, Azubi, Branchen.

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

- § 109 GewO — Anspruch auf qualifiziertes wohlwollendes Zeugnis; Wahrheits- und Klarheitspflicht.
- § 16 BBiG — Ausbildungszeugnis.
- §§ 241 Abs. 2, 280 Abs. 1 BGB — Nebenpflicht; Schadensersatz bei Verletzung.
- Beweislastregel BAG: bis Note 3 Arbeitgeber, ab Note 2 abwärts Arbeitnehmer (BAG 14.10.2003 – 9 AZR 12/03; BAG 18.11.2014 – 9 AZR 584/13).
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

## Testakte zum Üben

Im Ordner [`testakten/arbeitszeugnis-analyse-bluehendes-leben/`](testakten/arbeitszeugnis-analyse-bluehendes-leben/README.md) liegen zehn fiktive Arbeitszeugnisse aus zehn Branchen (PTA, Rechtsanwalt, MTA-R, Lagermeister, ZFA, Filialleiterin Sparkasse, Spedition, Hotel-Empfang, Altenpflege, Industriemechaniker) zum Durchtesten des Skills, plus ergänzende Korrespondenz und Vollvermerke.

## 🚨 KEINE Aussage über Berufsrecht, Datenschutz, KI-VO oder Beschlagnahmeverbote

**Lesen, bevor irgendetwas davon eingesetzt wird.** Dieses Repository ist ausschließlich ein technisches Experiment. Es trifft **keinerlei Aussage** darüber, ob der Einsatz dieses Skills in einer konkreten Praxisumgebung berufs-, datenschutz- oder KI-rechtlich zulässig ist. Alle nachstehenden Fragen muss **jede Nutzerin und jeder Nutzer in eigener Verantwortung** vor der ersten Nutzung prüfen — das Repository, seine Autorin / sein Autor und alle Mitwirkenden übernehmen dafür keinerlei Verantwortung oder Haftung:

- **Strafrechtliches Mandatsgeheimnis — §§ 203, 204 StGB.** Der Skill sagt nichts darüber aus, ob ein konkreter Einsatz mit dem strafbewehrten Geheimnisschutz des § 203 StGB (Verletzung von Privatgeheimnissen) und § 204 StGB (Verwertung fremder Geheimnisse) vereinbar ist — auch nicht in der Variante § 203 Abs. 3, 4 StGB (mitwirkende Personen, sonstige Stellen).
- **Berufsrecht — § 43e BRAO, § 2 BORA, § 53 StPO.** Es wird **nicht** geprüft, ob der Einsatz mit § 43e BRAO (Inanspruchnahme von Dienstleistern, insbesondere Cloud/KI), § 2 BORA (Verschwiegenheit), den Zeugnisverweigerungsrechten nach § 53 StPO und den Beschlagnahmeverboten nach § 97 StPO vereinbar ist. Gleiches gilt sinngemäß für andere **freie Berufe** mit eigenem Berufsrecht (StBerG für Steuerberater:innen, WPO für Wirtschaftsprüfer:innen, ÄrztInnen, Notar:innen, Patentanwält:innen u. a.).
- **Datenschutz — DSGVO, BDSG.** Es wird **nicht** beurteilt, ob die Verarbeitung personenbezogener Daten DSGVO-konform ist, ob eine ausreichende **Rechtsgrundlage** (Art. 6, 9 DSGVO) vorliegt, ob ein **Auftragsverarbeitungsvertrag** nach Art. 28 DSGVO geschlossen werden muss, ob eine **Datenschutz-Folgenabschätzung** (Art. 35 DSGVO) erforderlich ist oder ob die **Informationspflichten** nach Art. 13, 14 DSGVO erfüllt sind. Arbeitszeugnisse enthalten typischerweise personenbezogene Daten besonderer Kategorien.
- **KI-Verordnung (KI-VO / EU AI Act, VO (EU) 2024/1689).** Es wird **nicht** entschieden, ob der Einsatz unter eine der Hochrisiko-Kategorien nach **Art. 6 KI-VO** in Verbindung mit **Anhang III KI-VO** fällt (insbesondere Zugang zur Justiz, Beschäftigungskontext), ob **Transparenzpflichten** nach Art. 50 KI-VO greifen, ob es sich um ein **General-Purpose-AI-Modell** nach Art. 51 ff. KI-VO handelt und welche **Pflichten als Betreiber** (Art. 26 KI-VO) zu erfüllen sind.
- **Beschlagnahmeverbote und auslandsrechtliche Zugriffe.** Es wird nicht geprüft, ob Eingabedaten und Modellantworten gegen Beschlagnahme nach **§§ 97, 160a StPO**, gegen **US Cloud Act**, **FISA § 702**, **CLOUD Act warrants**, **PATRIOT Act § 215** oder sonstige extraterritoriale Zugriffsbefugnisse hinreichend geschützt sind. Dafür ist die jeweilige Nutzerin / der jeweilige Nutzer allein verantwortlich.
- **Zugang, Auftragsverarbeitung, Hosting.** Wie der API-Zugang zum Modell beschafft wird (Anthropic direkt, AWS Bedrock, Google Vertex, eigenes Hosting), ob mit dem Anbieter ein **Auftragsverarbeitungsvertrag** geschlossen wird, ob ein **berufsrechtskonformer Cloud-Vertrag** vorliegt und ob die Anforderungen an die Verschwiegenheit / Mandatsgeheimnis und Datenflusskontrolle in der konkreten Deployment-Konstellation eingehalten sind, bleibt vollständig in der **Eigenverantwortung der Nutzerin / des Nutzers**.

Anwältinnen, Anwälte und andere Berufsgeheimnisträgerinnen/-träger müssen vor jeder produktiven Nutzung selbst prüfen, ob die konkrete Anbieter-, Hosting- und Datenflusskonstellation mit Mandatsgeheimnis, Berufsrecht und Datenschutz vereinbar ist. Dieses Repository bestätigt keinen Anbieter und ersetzt keine Prüfung von § 203 StGB, § 43e BRAO, Art. 28 DSGVO, Kapitel V DSGVO, TOMs, Löschkonzept, Audit-Rechten, Subunternehmern, Datenresidenz und vertraglicher Verschwiegenheit.

## Lizenz

Dual licensed: Apache-2.0 OR MIT — siehe [LICENSE-APACHE](LICENSE-APACHE) und [LICENSE-MIT](LICENSE-MIT).
