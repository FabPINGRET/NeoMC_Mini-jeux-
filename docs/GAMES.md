# Table des IDs de jeux ($game / trigger mg.go set N)

Référence centrale générée depuis `core/game_tick.mcfunction`.
À mettre à jour quand un jeu est ajouté (go, game_tick, menus, votes).

| ID | Fonction tick |
|---|---|
| 1 | `mg:spleef/tick` |
| 2 | `mg:tntrun/tick` |
| 3 | `mg:pvp/tick` |
| 4 | `mg:bedwars/tick` |
| 5 | `mg:sheepwar/tick` |
| 6 | `mg:mobarena/tick` |
| 7 | `mg:sheepwar/tick` |
| 20 | `mg:splegg/tick` |
| 22 | `mg:sumo/tick` |
| 23 | `mg:dropper/tick` |
| 26 | `mg:oitc/tick` |
| 27 | `mg:tnttag/tick` |
| 28 | `mg:blockparty/tick` |
| 29 | `mg:anvil/tick` |
| 30 | `mg:turf/tick` |
| 31 | `mg:quake/tick` |
| 36 | `mg:paintball/tick` |
| 56 | `mg:icerace/tick` |
| 57..58 | `mg:bb/tick` |
| 59 | `mg:party/tick` |
| 61 | `mg:kart/tick` |
| 64 | `mg:dropadv/tick` |
| 65 | `mg:dropadv/c_tick` |
| 66 | `mg:elyrace/tick` |
| 75 | `mg:sky/tick` (ids 75..78 → $elm) |

Cartes : TNT Tag 27/67..70 → 27 + `$ttm` ; Bedwars 4/71..74 → 4 + `$bwm` ; Élytra 75..78 → 75 + `$elm` (remappage dans `core/request`).

Variantes : ids 100..167 (190..196 = au hasard par mode) → `var/remap` fixe `$vmode` (jeu), `$ar` (arène 1..18 ou sol 21..26) et `$dif` (1..4) ; `var/start` remet `$game` = jeu réel avant la préparation. `$ar = 0` = carte native. Liste : `docs/VARIANTES.md`.
