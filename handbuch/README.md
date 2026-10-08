# 1. Redaktionelle Quellen des großen Arbeitsbuchs

Diese Kapitel werden vollständig in `skill/SKILL.md` eingebettet. Nutzer benötigen weiterhin nur die fertige einzelne Promptdatei, keine zusätzlichen Kapiteldateien. Die getrennten Quellen erleichtern die Pflege der ausführlichen Rechtsprechungs- und Anwendungskapitel.

## 1.1. Zusammenbauen und prüfen

`python3 scripts/build_handbook.py` aktualisiert die Vollfassung, ihre öffentliche Kopie, die Mini-Kopie und die bestehenden Prüfsummen. `--check` prüft ohne Änderungen auf Gleichheit. Der optionale Parameter `--plugin-root /absoluter/pfad/zum/monorepo` synchronisiert dieselben Kapitel in Werkstatt-Prompt und gepackte Pluginreferenz des vorhandenen Arbeitszeugnisprüfers.

Die Kapitel werden nicht bei jedem Mandat vollständig ausgegeben. Sie sind die eingebettete Grundlage für fallbezogene Rückfragen, Rechtsprüfung, Schreiben und Korrekturkontrolle. Rechtsprechungsstand und Quellenlücken stehen in den Kapiteln selbst. Technische Gleichheit beweist weder juristische Richtigkeit noch erfolgreiches Modellverhalten.

## 1.2. Inhaltliche Pflege

Änderungen an den Kapiteln erfolgen hier; danach wird der Zusammenbau erneut ausgeführt. Die juristischen Kernaussagen, Grenzen und Kurzanker im vorderen Teil der Vollfassung müssen dabei abgeglichen werden. Ein neues Recherchedatum darf nur die tatsächlich nachgeprüften Quellen erfassen. Eigenständige Fallbeispiele bleiben als solche bezeichnet und werden nicht einem Gericht zugeschrieben.
