# L’Europe chiffrée

[Lire le site](https://bdudout.github.io/europe-chiffree/) · [Français](https://bdudout.github.io/europe-chiffree/fr/) · [English](https://bdudout.github.io/europe-chiffree/en/) · [日本語](https://bdudout.github.io/europe-chiffree/ja/)

Lettres et télégrammes chiffrés européens. Premier dossier : Marie de Médicis à Savary de Brèves, 15 septembre et 10 novembre 1610, d’après les documents et relectures de Brice Dudout. Deuxième dossier : l’instruction de Rome au légat Filippo Sega, 14 mai 1593 (BnF Français 3984, no 6), déchiffrement probable et partiel. Page Documents : lettre de Niccolò Ferducci à Ferdinand Iᵉʳ, Fiume, 19 juillet 1532 (HHStA Türkei I 2-2-19 ; catalogue de Daniel Bourdeau n° 498), lecture nouvelle d’une pièce sans glose ; lettre chiffrée de Charles XII au Conseil du royaume et à ses envoyés, Bender, 26 avril 1710 (NLA Stade, Rep. 5a Nr. 670 ; catalogue de Daniel Bourdeau n° 599), lecture nouvelle des copies chiffrées de Stade ; dépêches chiffrées de Copenhague à Just Høeg, La Haye, 2 janvier – 9 février 1675 (onze lettres) (Rigsarkivet, copiebook de Conrad Biermann ; catalogue de Daniel Bourdeau n° 465), premier déchiffrement publié à notre connaissance ; chiffres de lettres de Du Maurier et de Serviez à Duplessis-Mornay, été 1593, imprimés sans clé dans les *Mémoires et correspondance* (1824) (catalogue de Daniel Bourdeau n° 371, hypothèse « deux lettres par groupe » de Daniel Bourdeau), premier déchiffrement publié à notre connaissance. Lettre chiffrée d’Afonso VI au comte de Vila Flor, Lisbonne, 26 mai 1663 (ANTT, Luís de Miranda Pereira, liv. 2 ; catalogue de Daniel Bourdeau n° 391), « secourir Évora à tout risque », premier déchiffrement publié à notre connaissance. Six lignes chiffrées d’A. H. Everett à H. Clay, Madrid, 25 septembre 1825 (NARA M31 ; catalogue de Daniel Bourdeau n° 638, table de code de Daniel Bourdeau), partie coupée en 1826, premier déchiffrement publié à notre connaissance. Huit lignes chiffrées de F. Dana à R. R. Livingston, Saint-Pétersbourg, 6/17 avril 1783 (NARA, PCC 89 II ; catalogue de Daniel Bourdeau n° 485 ; table de Dana d’octobre 1782 retrouvée p. 656), « there is no Minister here », premier déchiffrement publié à notre connaissance. Six lettres de L. Wąsowicz à A. M. Lubomirski, 1662–1663 (ANK, AKPot 3227 ; DECODE R7503, R7505–R7509 ; catalogue de Daniel Bourdeau n° 439), passages chiffrés lus avec la table reconstituée du XIXᵉ siècle (validation aveugle sur R7508), premier déchiffrement publié à notre connaissance ; aucune image DECODE reproduite. Trois lettres d’Henri II à Soliman (1547), en copie latine chiffrée par G. M. Malvezzi (HHStA Türkei I 7-2-18 ; catalogue de Daniel Bourdeau n° 500), lues à ≈ 97,5 % des groupes avec l’alphabet de Malvezzi validé à l’aveugle, premier déchiffrement publié à notre connaissance ; aucune image AIS reproduite. Lettre entièrement chiffrée de W. H. Crawford à J. Monroe, Paris, 15 août 1813 (NARA M34 ; catalogue de Daniel Bourdeau n° 652, table de code de Daniel Bourdeau), sans déchiffrement d’époque sur le microfilm, premier déchiffrement publié à notre connaissance.

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

## 🔴 Images DECODE : jamais publiées (consigne du 29/10/2026)
- Les images DECODE servent **à la recherche privée et à la transcription** seulement. Aucune image DECODE n'est publiée ni redistribuée, **ni recadrage, ni vignette, ni dérivé** : site, PR vers Daniel, artifact, mail, archive .zip partagée. Il faut l'autorisation écrite de l'archive qui détient l'original.
- Rangement : toujours sous un chemin qui contient `decode` (`<dossier>/sources/decode/R<n>/`, avec SHA256 et NOTICE). Ainsi le registre les reconnaît.
- Toute lecture ou correction publiée qui s'appuie sur une notice DECODE **cite DECODE** : « DECODE R<n> » avec le lien `https://de-crypt.org/decrypt-web/RecordsView/<n>`, dans la fiche et dans Sources.
- Contrôle avant publication : `python3 europe-chiffree-site/tools/decode_registry.py` puis `python3 europe-chiffree-site/tools/check-public.py`. Le contrôle échoue si une image DECODE est dans dist/ ou si une notice DECODE est citée sans lien.
