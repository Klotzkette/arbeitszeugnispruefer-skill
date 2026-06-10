# Arbeitszeugnis-Prüfer Skill

> **Experimenteller Agent-Skill** für die anwaltliche Prüfung deutscher Arbeitszeugnisse — als Anregung für Kanzlei-Arbeitsabläufe. Orientiert sich an der deutschen Rechtspraxis, an Gesetzestexten, amtlichen Materialien und frei überprüfbarer Rechtsprechung. Enthält keinerlei Fachgutachten oder Rechtsberatung, alle Angaben ohne Gewähr — jede Nutzerin und jeder Nutzer kalibriert den Skill selbst für die eigene Praxis.

> **Und jetzt mal ehrlich, Leute — keine Panik:** Das hier ist eigentlich nur ein riesiger Prompt. Kein Hexenwerk, keine Blackbox, kein heimlich trainiertes Modell, sondern strukturierter Text in Markdown, den ein LLM beim Bearbeiten eines Arbeitszeugnisses als Anleitung lädt. Wer schon mal einen langen ChatGPT-Prompt geschrieben hat, kennt das Prinzip — hier ist es nur sauber sortiert, juristisch geerdet und auf den deutschen Arbeitszeugnis-Kontext zugeschnitten. Man kann reinschauen, mitlesen, anpassen, forken. Mehr ist es nicht.
>
> **Funktioniert in jedem Chatbot.** ChatGPT, Claude, Gemini, Mistral, Perplexity, lokales Llama — egal. Der Skill ist reiner Markdown-Text. Es gibt zwei Wege:
>
> 1. **Copy & Paste (einfachster Weg, kein Upload, kein Konto, kein Tool nötig).** Inhalt von [`skill/SKILL.md`](skill/SKILL.md) kopieren, in den Chat einfügen, dann das zu prüfende Arbeitszeugnis darunter posten. Fertig. Die Dateien unter `references/` sind **optional** — nur mitkopieren, wenn der Chatbot bei einem bestimmten Aspekt nachfragt oder wenn das jeweilige Thema (Schlussformel, Geheimcodes, Ampelflaggen …) für den konkreten Fall relevant ist.
> 2. **Als Datei-Anhang.** In Chatbots, die Dateien akzeptieren (ChatGPT, Claude, Perplexity-Anhänge), `SKILL.md` und bei Bedarf einzelne References einfach hochladen oder per Drag-and-Drop anhängen. In Agent-Umgebungen mit Skill-Loader (Claude Code, Perplexity Computer) den ganzen `skill/`-Ordner als Skill registrieren — dann liest sich der Agent die References bei Bedarf selbst nach.
>
> Kurz: **Man muss nichts installieren und nichts hochladen.** Markdown rein in den Chat, Zeugnis dazu, los.

Konsolidierter Skill für die Prüfung deutscher Arbeitszeugnisse nach dem Ampelsystem (Rot/Orange/Grün).

Diese Skill bündelt eine 50-teilige Plugin-Sammlung in eine einzige `SKILL.md` mit sieben unterstützenden References. Sie deckt den vollständigen Bogen ab — vom Mandanten-Intake über die satzweise Notenmatrix bis zur Klagestrategie auf Zeugnisberichtigung.

## Inhalt

```
skill/
├── SKILL.md                              Acht-Stufen-Workflow, rechtlicher Anker, Antwortformate
└── references/
    ├── zufriedenheitsformel.md           Notenstufen 1 bis 5 der Hauptformel
    ├── schlussformel.md                  Bedauern/Dank/Wunsch, Signal versus Anspruch
    ├── geheimcode-katalog.md             Standardphrasen nach Themenachsen
    ├── ampel-flaggen.md                  Steigerungsadverbien, grüne/orange/rote Flaggen, negative Codeworte
    ├── analyse-techniken.md              Drift, Auslassungen, Negationen, Widersprüche, Formalia
    ├── mandatsmodule.md                  Aufforderungsschreiben, Wortlaut-Verbesserungen, Klageantrag
    └── muster-und-sonderfaelle.md        Drei Musterzeugnisse, leitende Positionen, Azubi, Branchen
```

### Was ist `SKILL.md`, was sind die References?

- **`SKILL.md`** ist die Hauptanweisung — der eigentliche Prompt mit dem Acht-Stufen-Workflow, dem rechtlichen Anker und den Antwortformaten. Diese Datei ist **immer dabei**.
- **Die sieben Dateien unter `references/`** sind thematische Nachschlagewerke. Sie sind **nicht zwingend nötig**, um den Skill zu benutzen — `SKILL.md` allein liefert bereits einen vollständigen Workflow. Die References werden erst dann relevant, wenn ein konkreter Punkt vertieft werden soll:
  - `zufriedenheitsformel.md` — wenn die Note der Hauptformel exakt eingeordnet werden soll (Note 1–5).
  - `schlussformel.md` — wenn Bedauern, Dank und Zukunftswunsch im Detail bewertet werden sollen.
  - `geheimcode-katalog.md` — wenn verdächtige Standardphrasen entschlüsselt werden müssen.
  - `ampel-flaggen.md` — wenn Steigerungsadverbien und Codeworte sauber den Ampelfarben zugeordnet werden sollen.
  - `analyse-techniken.md` — wenn nach Drift, Auslassungen, Negationen, Widersprüchen oder Formfehlern gesucht wird.
  - `mandatsmodule.md` — wenn ein Aufforderungsschreiben, eine Wortlaut-Verbesserung oder ein Klageantrag formuliert werden soll.
  - `muster-und-sonderfaelle.md` — wenn ein Musterzeugnis, eine Leitungsposition, ein Azubi-Zeugnis oder ein Branchenspezifikum als Vergleich gebraucht wird.

**Faustregel:** Nur `SKILL.md` reinkopieren reicht für den ersten Durchgang. Die Referenz, die der Chatbot bzw. der konkrete Fall braucht, kann anschließend nachgeschoben werden — entweder per Copy-and-Paste oder als zusätzlicher Datei-Anhang.

## Workflow in acht Stufen

1. Intake und Rollenklärung
2. Zeugnisart und Kopfdaten sichern
3. Notenrelevante Sätze markieren
4. Satzweise Ampel-Notenmatrix
5. Drift, Auslassungen und Widersprüche
6. Gesamtnotenspanne und Hauptbefund
7. Mandantenbericht und Verhandlungsmodul
8. Klagestrategie Zeugnisberichtigung

## Rechtlicher Anker

- § 109 GewO — Anspruch auf qualifiziertes wohlwollendes Zeugnis; Wahrheits- und Klarheitspflicht.
- § 16 BBiG — Ausbildungszeugnis.
- §§ 241 Abs. 2, 280 Abs. 1 BGB — Nebenpflicht; Schadensersatz bei Verletzung.
- Beweislastregel BAG: bis Note 3 Arbeitgeber, ab Note 2 abwärts Arbeitnehmer.
- Zuständigkeit Arbeitsgericht (§ 2 Abs. 1 Nr. 3 ArbGG); Klage als Leistungsklage.

Rechtsprechung wird in dieser Skill nie aus Modellwissen zitiert — jede tragende Aussage wird über `gesetze-im-internet.de`, `dejure.org` oder das Rechtsprechungsportal des Bundes mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage live verifiziert.

## Einsatzlagen

- Mandant oder Mandantin will Zeugnis einordnen.
- Kanzlei prüft Berichtigungs-, Vergleichs- oder Klagestrategie.
- HR will Entwurf gegenprüfen.
- Betriebsrat sucht Schulungseinschätzung.
- Ausbildungs- oder Zwischenzeugnis.

## Verwandte Projekte

Dieser Skill ist aus dem Plugin `arbeitszeugnis-analyse` der Sammlung [`claude-fuer-deutsches-recht`](https://github.com/Klotzkette/claude-fuer-deutsches-recht) extrahiert und konsolidiert. Die ursprünglichen 50 Einzelskills wurden zu sieben thematischen Referenzen zusammengeführt, ohne fachliche Substanz zu verlieren.

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
