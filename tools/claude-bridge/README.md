# claude-bridge

Permet de demander des modifications du datapack directement dans le chat Minecraft (serveur Paper).

```
!claude ajoute un chrono de 60 s au parkour
!claude undo          annule la derniere modification
!claude aide
```

Le bridge lit `logs/latest.log`, lance Claude Code en mode headless dans ce repo, fait un `minecraft:reload` par RCON, renvoie les erreurs du reload a Claude pour correction (2 tentatives max), commit sur la branche courante, puis affiche le resultat dans le chat.

## Installation

1. **Serveur Paper** : dans `server.properties`
   ```
   enable-rcon=true
   rcon.port=25575
   rcon.password=un-mot-de-passe-solide
   online-mode=true
   ```
   `online-mode=true` est indispensable : la liste blanche repose sur les pseudos.

2. **Branche dediee** (les commits du bridge n'arrivent pas sur `main`) :
   ```
   git checkout -b live
   ```

3. **Brancher le repo comme datapack** (supprime d'abord l'ancien zip de `world/datapacks`) :
   ```
   mklink /J "C:\ServeurPaper\world\datapacks\minijeux" "C:\Projets\NeoMC_Mini-jeux-"
   ```

4. **Config** : copie `config.example.json` en `config.json` (ignore par git), puis renseigne `serverDir`, le mot de passe RCON, `allowedPlayers` et `anthropicApiKey`.

5. **Lancer** (Node 18 ou plus, Claude Code installe) :
   ```
   node tools/claude-bridge/bridge.mjs
   ```

## Securite

- Claude tourne en `--bare` avec uniquement les outils Read, Edit, Write, Glob et Grep, sans Bash ni acces web.
- Seuls les joueurs de `allowedPlayers` sont ecoutes.
- `maxBudgetUsd` plafonne le cout de chaque demande.
- Le bridge refuse de travailler si le repo contient des modifications non commitees.
