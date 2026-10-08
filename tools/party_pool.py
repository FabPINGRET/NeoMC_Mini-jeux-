"""Mini Party : liste des mini-jeux de la roulette (génère pick, pick_show, pick_final, pick_reset, watch).

    python tools/party_pool.py .        (depuis la racine du dépôt)

Chaque jeu : (id de lancement, nom affiché, couleur, limite de temps en ticks pour la Mini Party).
Format court (3 à 6 min) ; la limite est un filet de sécurité : à expiration, One in the Chamber donne la victoire au meilleur tueur,
les autres jeux s'arrêtent sans vainqueur (+3 pièces pour tous).
"""
import os, sys

R = sys.argv[1]
P = os.path.join(R, 'data/mg/function/party/')
M = 60 * 20   # une minute

POOL = [   # format court : 3 à 6 minutes par mini-jeu (Build Battle et Dropper Aventure, trop longs, ne sont pas dans la roulette)
    (1, 'SPLEEF', 'aqua', 3 * M), (2, 'TNT RUN', 'red', 3 * M), (20, 'SPLEGG', 'yellow', 3 * M), (21, 'SPLEGG XXL', 'gold', 4 * M),
    (22, 'SUMO', 'gold', 3 * M), (24, 'SUMO COMPLEXE', 'gold', 3 * M), (23, 'THE DROPPER', 'aqua', 4 * M),
    (25, 'DROPPER : TUBE COMMUN', 'aqua', 4 * M), (65, 'DROPPER : DÉFI', 'aqua', 4 * M), (27, 'TNT TAG', 'red', 4 * M), (28, 'BLOCK PARTY', 'light_purple', 4 * M),
    (29, "PLUIE D'ENCLUMES", 'dark_gray', 3 * M), (42, 'ENCLUMES + SOL TROUÉ', 'red', 3 * M),
    (3, 'ARÈNE PVP', 'yellow', 3 * M), (13, 'PVP : CLASSES', 'gold', 3 * M), (44, 'PVP : POUSSIÈRE', 'gold', 3 * M),
    (45, 'PVP : POUSSIÈRE (CLASSES)', 'gold', 3 * M), (47, 'PVP : MIRAGE', 'aqua', 3 * M), (48, 'PVP : MIRAGE (CLASSES)', 'aqua', 3 * M),
    (50, 'PVP : NUKETOWN', 'green', 3 * M), (51, 'PVP : NUKETOWN (CLASSES)', 'green', 3 * M),
    (26, 'ONE IN THE CHAMBER', 'gold', 3 * M), (52, 'ONE IN THE CHAMBER : CHÂTEAU', 'gold', 3 * M), (53, 'ONE IN THE CHAMBER : FORÊT', 'dark_green', 3 * M),
    (35, 'QUAKECRAFT : GLACIER', 'aqua', 4 * M), (43, 'QUAKECRAFT : POUSSIÈRE', 'gold', 4 * M), (46, 'QUAKECRAFT : MIRAGE', 'aqua', 4 * M),
    (49, 'QUAKECRAFT : NUKETOWN', 'green', 4 * M),
    (36, 'PAINTBALL', 'gold', 3 * M), (54, 'PAINTBALL : MINI-TERRAIN', 'gold', 3 * M), (55, 'PAINTBALL : GRAND TERRAIN', 'gold', 4 * M),
    (30, 'TURF WARS', 'gold', 4 * M),
    (5, 'SHEEP WAR', 'white', 4 * M), (7, 'SHEEP WAR : FORTERESSES', 'white', 4 * M), (15, 'SHEEP WAR : CUBES VOXEL', 'white', 4 * M),
    (17, 'SHEEP WAR : ARCHIPEL', 'white', 4 * M),
    (4, 'BEDWARS', 'light_purple', 5 * M),
    (56, 'COURSE DE BATEAUX', 'aqua', 4 * M), (61, 'KART', 'gold', 5 * M), (62, 'KART : ROYAUME KOOPA', 'red', 6 * M), (63, 'KART : BATAILLE', 'light_purple', 3 * M),
    (70, 'TNT TAG : VILLAGE PERCHÉ', 'aqua', 4 * M), (69, 'TNT TAG : CANYON', 'gold', 4 * M),
    (75, 'ÉLYTRA : COURSE D\'ANNEAUX', 'aqua', 5 * M), (76, 'ÉLYTRA : COURSE + COMBAT', 'red', 5 * M), (77, 'ÉLYTRA : SURVIE EN VOL', 'light_purple', 6 * M),
    # Variantes (tools/variantes/gen_variants.py) : le mode sur une carte d'un autre jeu, tirée au sort au lancement
    (190, 'PVP : VARIANTE ★', 'yellow', 3 * M), (191, 'OITC : VARIANTE ★', 'gold', 3 * M), (192, 'QUAKE : VARIANTE ★', 'aqua', 4 * M),
    (193, 'TNT TAG : VARIANTE ★', 'red', 4 * M), (194, 'SPLEEF : VARIANTE ★', 'aqua', 3 * M), (195, 'TNT RUN : VARIANTE ★', 'red', 3 * M),
    (196, 'SPLEGG : VARIANTE ★', 'yellow', 3 * M),
]
N = len(POOL)

def w(name, lines):
    with open(P + name + '.mcfunction', 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(lines) + '\n')

w('pick', [f'# Roulette : un mini-jeu au hasard parmi les {N} (affichage seulement)',
           f'execute store result score $mgk mg.st run random value 1..{N}', 'function mg:party/pick_show'])
show = ['# Affiche le mini-jeu n° $mgk en titre, règle $mgid (id de lancement) et $mplim (limite de temps en Mini Party)']
for k, (gid, name, col, lim) in enumerate(POOL, 1):
    show += [f'execute if score $mgk mg.st matches {k} run scoreboard players set $mgid mg.st {gid}',
             f'execute if score $mgk mg.st matches {k} run scoreboard players set $mplim mg.st {lim}',
             f'execute if score $mgk mg.st matches {k} run title @a[tag=mg.mpp] title [{{"text":"{name}","color":"{col}","bold":true}}]']
show.append('execute as @a[tag=mg.mpp] at @s run playsound minecraft:block.note_block.hat master @s ~ ~ ~ 1 1.5')
w('pick_show', show)
f = [f'# Tirage final : un mini-jeu pas encore joué dans cette Mini Party (quand les {N} sont passés, le cycle recommence)',
     'scoreboard players set $mgr mg.st 0']
f += [f'execute unless score $mgp{k} mg.st matches 1 run scoreboard players add $mgr mg.st 1' for k in range(1, N + 1)]
f += ['execute if score $mgr mg.st matches 0 run function mg:party/pick_reset',
      'execute store result storage mg:party pk.r int 1 run scoreboard players get $mgr mg.st',
      'function mg:party/pick_rand with storage mg:party pk']
for k in range(1, N + 1):
    f += [f'execute unless score $mgp{k} mg.st matches 1 run scoreboard players remove $mgq mg.st 1',
          f'execute if score $mgq mg.st matches 0 run scoreboard players set $mgk mg.st {k}',
          f'execute if score $mgq mg.st matches 0 run scoreboard players set $mgq mg.st -1']
f += [f'execute if score $mgk mg.st matches {k} run scoreboard players set $mgp{k} mg.st 1' for k in range(1, N + 1)]
f += ['function mg:party/pick_show', 'scoreboard players set $mpgt mg.st 0']
w('pick_final', f)
w('pick_reset', ['# Tous les mini-jeux sont passés : on repart pour un cycle'] +
  [f'scoreboard players set $mgp{k} mg.st 0' for k in range(1, N + 1)] + [f'scoreboard players set $mgr mg.st {N}'])
w('watch', ['# Mini-jeu de la Mini Party en cours (core/game_tick) : format court (limite de temps, mort subite au Bedwars)',
            'execute if score $game mg.st matches 59 run return 0',
            'scoreboard players add $mpgt mg.st 1',
            f'execute if score $game mg.st matches 4 if score $mpgt mg.st matches {2 * M} run tellraw @a[tag=!mg.surv] [{{"text":"⚠ MORT SUBITE dans 30 s : ","color":"red","bold":true}},{{"text":"tous les lits vont être détruits !","color":"gray"}}]',
            f'execute if score $game mg.st matches 4 if score $mpgt mg.st matches {2 * M + 600} run function mg:party/bw_sudden',
            'scoreboard players operation $mprest mg.st = $mplim mg.st', 'scoreboard players operation $mprest mg.st -= $mpgt mg.st',
            f'execute if score $mprest mg.st matches {M} run tellraw @a[tag=!mg.surv] [{{"text":"⏱ ","color":"gold"}},{{"text":"Plus qu’une minute pour ce mini-jeu !","color":"yellow"}}]',
            'execute if score $mplim mg.st matches 1.. if score $mpgt mg.st = $mplim mg.st run function mg:party/watch_end'])
w('bw_sudden', ['# Bedwars en Mini Party : mort subite, tous les lits sont détruits (le tick du Bedwars annonce chaque lit)',
                'fill -36 64 1199 -34 64 1201 minecraft:air replace #minecraft:beds', 'fill 34 64 1199 36 64 1201 minecraft:air replace #minecraft:beds',
                'fill -1 64 1163 1 64 1165 minecraft:air replace #minecraft:beds', 'fill -1 64 1235 1 64 1237 minecraft:air replace #minecraft:beds',
                'title @a[tag=!mg.surv] actionbar [{"text":"☠ MORT SUBITE : plus aucune réapparition !","color":"red","bold":true}]'])
w('watch_end', ['# Temps écoulé : One in the Chamber → le meilleur tueur gagne ; sinon fin sans vainqueur',
                'tellraw @a[tag=!mg.surv] [{"text":"★ ","color":"gold"},{"text":"Temps écoulé pour ce mini-jeu !","color":"gray"}]',
                'execute if score $game mg.st matches 26 run return run function mg:party/watch_oitc',
                'function mg:core/draw'])
w('watch_oitc', ['scoreboard players set $mpbk mg.st -1',
                 'execute as @a[tag=mg.play] if score @s mg.ok > $mpbk mg.st run scoreboard players operation $mpbk mg.st = @s mg.ok',
                 'execute as @a[tag=mg.play] if score @s mg.ok = $mpbk mg.st run tag @s add mg.mpbest',
                 'execute as @a[tag=mg.mpbest,limit=1] run function mg:core/win_player',
                 'tag @a remove mg.mpbest',
                 'execute unless score $state mg.st matches 3 run function mg:core/draw'])
print('mini-jeux dans la roulette :', N)
