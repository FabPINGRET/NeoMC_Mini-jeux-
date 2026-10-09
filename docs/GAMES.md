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
| 66 | `mg:elyrace/tick` (ids 81..82 → $xc) |
| 75 | `mg:sky/tick` (ids 75..78 → $elm) |

Cartes : TNT Tag 27/67..70 → 27 + `$ttm` ; Bedwars 4/71..74 → 4 + `$bwm` ; Élytra 75..78 → 75 + `$elm` ; Course d'élytres 81..82 (Canyon du Couchant, Pic Blanc) → 66 + `$xc` (remappage dans `core/request`) ; contre-la-montre solo (`/trigger mg.xs`, ouvert à tous) : hors machine à états (ni `$state` ni `$game` : tag `mg.xso`, scores par joueur `mg.xph` / `xst` / `xcr` / `xse` / `xsl`, 4 solos au plus, joueur mis en pause `mg.spectate`), lancé par `mg:elyrace/solo/start`, tick `mg:elyrace/solo/tick` (appelé par `core/tick`).

Variantes : ids 100..167 (190..196 = au hasard par mode) → `var/remap` fixe `$vmode` (jeu), `$ar` (arène 1..18 ou sol 21..26) et `$dif` (1..4) ; `var/start` remet `$game` = jeu réel avant la préparation. `$ar = 0` = carte native. Liste : `docs/VARIANTES.md`.

Téléphone : id 83 → `mg:tel/tick` (`tools/telephone/gen_tel.py`).

Arcade (générateurs `tools/arcade/*.py`, câblage commun `tools/arcade/common.py`) :
Tron 84..85 → `mg:tron/tick` (z 20000) ; King of the Hill 86..87 → `mg:koth/tick` (z 20400) ;
The Towers 88 → `mg:tower/tick` (z 20800) ; Convoi 89..90 → `mg:convoy/tick` (z 21200, bossbar `mg:convoy`) ; Capture the Flag 93 → `mg:ctf/tick` (z 21600) ;
Mini UHC Run 94 / Mini Hunger Games 95 → `mg:survival/tick` → `mg:uhc/*` (z 22400) / `mg:hg/*` (z 22800). Zone = carré `$zr` (dégâts hors zone), pas de worldborder (globale). Prop Hunt 96 → `mg:ph/tick` (z 23600, équipe `mg_ph` sans pseudo) ; Zombies 97 / Infection 98 → `mg:zmode/tick` → `mg:zm/*` / `mg:inf/*` (z 23200). Armes : `mg:gun/*` (`tools/arcade/guns.py`), modèles `mg:gun_*` du resource pack (`tools/resourcepack/guns_rp.py`), arbalète vanilla si `$rp` = 0.
Les objets au sol y sont tagués `mg.keep` dans `survie/tick`, sinon le nettoyage global les supprime.
Block Party bandes/mixte 91..92 → jeu 28 + `$bpm` (`tools/blockparty/gen_bp.py`).
Montagne russe (hors jeux) : `mg:coaster/tick` appelé par `core/tick` quand un joueur est dans x −200..−100 ; voie générée `mg:coaster/track`.
Monstres/animaux invoqués par un jeu : leur mettre le tag `mg.mob` (ou `mg.npc`), sinon `survie/sweep_mobs` les envoie en y −300.
