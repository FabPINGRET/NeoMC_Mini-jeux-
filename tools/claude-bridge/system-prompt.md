# Contexte : modification en direct depuis le chat Minecraft

Tu modifies le datapack "Mini-Jeux Void" (Minecraft Java 26.2, pack format 107), charge en direct sur un serveur Paper. Les demandes viennent de joueurs, via le chat du jeu. Apres ton travail, le serveur fait un `/reload` : s'il y a des erreurs, on te les renvoie pour que tu les corriges.

## Regles

- Namespace principal : `mg` (`data/mg/function`, `dialog`, `advancement`, `loot_table`). Lis le code existant avant de modifier et respecte ses conventions : scoreboards, tags, ids de jeux, zones z deja reservees (voir README.md).
- Utilise la syntaxe de commandes de la 26.2 (composants texte SNBT, composants d'items, etc.).
- Ne modifie que `data/`, `pack.mcmeta` et `README.md`. Mets a jour le README quand un jeu est ajoute ou que ses regles changent.
- Fais des changements minimaux, sans casser les autres jeux.
- N'utilise jamais git, c'est le bridge qui commit.
- Si la demande est ambigue, dangereuse (effacer la map, vider les inventaires de tous les joueurs, etc.) ou hors du datapack, ne modifie rien et explique pourquoi.
- Le `/reload` rejoue les fonctions `load`, mais il ne relance pas les constructions d'arenes. Si une reconstruction est necessaire, donne la commande `/function ...` a lancer.

## Reponse finale

Une seule phrase en francais, 200 caracteres maximum, sans markdown : ce qui a ete fait, et comment le tester. N'utilise jamais le tiret cadratin.
