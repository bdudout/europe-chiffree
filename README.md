# L’Europe chiffrée

[Lire le site](https://bdudout.github.io/europe-chiffree/) · [Français](https://bdudout.github.io/europe-chiffree/fr/) · [English](https://bdudout.github.io/europe-chiffree/en/) · [日本語](https://bdudout.github.io/europe-chiffree/ja/)

Lettres et télégrammes chiffrés européens. Premier dossier : Marie de Médicis à Savary de Brèves, 15 septembre et 10 novembre 1610, d’après les documents et relectures de Brice Dudout.

À notre connaissance, premier déchiffrement de ces deux passages ; certains caractères restent probables mais non confirmés. La table candidate est BnF Français 3462, vue 112.

Ce dépôt contient uniquement les pages et les images finales du site, dans `dist/`. Les données de recherche, réponses individuelles et fichiers intermédiaires restent hors publication. La page Documents présente les fac-similés et les passages lus, sans fiches de décision. Les références figurent dans Sources.

## Vérifier et prévisualiser

Python 3.9+, sans dépendance :

```sh
python3 tools/check-public.py
python3 -m http.server 8790 --bind 127.0.0.1 --directory dist
```

Le menu de langues à drapeaux conserve la page courante, mémorise le choix manuel et détecte la langue du navigateur à la première navigation. La version japonaise est une traduction de travail pour relecture. Le site fonctionne sans service tiers, y compris hors ligne après téléchargement.

## Publication

Le workflow `.github/workflows/pages.yml` vérifie et déploie `dist/` sur GitHub Pages après chaque push sur `github-main`. Il utilise les permissions Pages du jeton temporaire de GitHub Actions ; aucun secret n’est enregistré dans le dépôt.

Les illustrations d’ambiance sont identifiées comme générées, distinctes des fac-similés BnF/Gallica. Voir `NOTICE.md` et `LICENSE` pour les crédits et les droits.
