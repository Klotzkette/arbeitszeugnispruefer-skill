# Arbeitszeugnis-Prüfer Skill

Konsolidierter Agent-Skill für die anwaltliche Prüfung deutscher Arbeitszeugnisse nach dem Ampelsystem (Rot/Orange/Grün).

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

Dieser Skill ist aus dem Plugin `arbeitszeugnis-analyse` der Sammlung `claude-fuer-deutsches-recht` extrahiert und konsolidiert. Die ursprünglichen 50 Einzelskills wurden zu sieben thematischen Referenzen zusammengeführt, ohne fachliche Substanz zu verlieren.

## Lizenz

Dual licensed: Apache-2.0 OR MIT — siehe [LICENSE-APACHE](LICENSE-APACHE) und [LICENSE-MIT](LICENSE-MIT).
