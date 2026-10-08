"""📞 Téléphone (Build Battle version « téléphone arabe ») — id 83, 5 à 12 joueurs.

    python tools/telephone/gen_tel.py .        (depuis la racine du dépôt ; idempotent)

Une chaîne par joueur, tout le monde joue en même temps (le joueur d'indice i travaille sur la chaîne (i + étape) mod N) :
  étape 0  écrire un mot (livre, 60 s)          → ch[c].s0
  étape 1  construire ce mot (2 min 30)         → parcelle (c, 0)
  étape 2  deviner la construction (60 s)       → ch[c].s2
  étape 3  construire la devinette (2 min 30)   → parcelle (c, 1)
  étape 4  deviner (60 s)                       → ch[c].s4
  révélation chaîne par chaîne ; devinette identique au mot de départ = +1 pour le devineur et le constructeur d'avant.
Parcelles 25×25 : x = 64·c − 352, z = 19500 (+64 pour la 2e construction), y 64. Salle d'attente : 0 64 19420.
"""
import json
import os
import sys

R = sys.argv[1] if len(sys.argv) > 1 else '.'
D = os.path.join(R, 'data/mg')
F = os.path.join(D, 'function')
GID = 83
NMAX = 12
PX = lambda c: 64 * c - 352
PZ = lambda b: 19500 + 64 * b
T_WRITE, T_BUILD, T_GUESS = 1200, 3000, 1200


def w(rel, lines):
    p = os.path.join(F, 'tel', rel + '.mcfunction')
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(lines) + '\n')


def js(o):
    return json.dumps(o, ensure_ascii=False, separators=(',', ':'))


VALID = js(['', {'text': ' [✔ Valider]', 'color': 'green', 'bold': True,
                 'click_event': {'action': 'run_command', 'command': '/trigger mg.tel set 1'},
                 'hover_event': {'action': 'show_text', 'value': 'Écris sur la 1re page du livre, clique « Terminé », puis valide'}}])
BOOK = 'minecraft:writable_book[custom_name=[{"text":"📞 Écris ici (1re page)","color":"gold","italic":false}]]'

# ------------------------------------------------------------------ décor
w('plot', ['# Parcelle du Téléphone (position = centre, y 64) : 25×25 + chemin de ronde pour les devineurs',
           'execute positioned ~-18 ~-8 ~-18 run kill @e[type=!minecraft:player,dx=36,dy=60,dz=36]',
           'fill ~-17 ~-6 ~-17 ~17 ~5 ~17 minecraft:air', 'fill ~-17 ~6 ~-17 ~17 ~17 ~17 minecraft:air',
           'fill ~-17 ~18 ~-17 ~17 ~29 ~17 minecraft:air', 'fill ~-17 ~30 ~-17 ~17 ~41 ~17 minecraft:air',
           'fill ~-15 ~-2 ~-15 ~15 ~-1 ~15 minecraft:dirt', 'fill ~-15 ~ ~-15 ~15 ~ ~15 minecraft:polished_andesite',
           'fill ~-12 ~ ~-12 ~12 ~ ~12 minecraft:stone_bricks', 'fill ~-11 ~ ~-11 ~11 ~ ~11 minecraft:grass_block',
           'setblock ~-12 ~ ~-12 minecraft:sea_lantern', 'setblock ~12 ~ ~-12 minecraft:sea_lantern',
           'setblock ~-12 ~ ~12 minecraft:sea_lantern', 'setblock ~12 ~ ~12 minecraft:sea_lantern'])
w('room', ['# Salle d\'attente / révélation (0 64 19420)',
           'fill -8 60 19412 8 72 19428 minecraft:air', 'fill -7 63 19413 7 63 19427 minecraft:smooth_quartz',
           'fill -6 63 19414 6 63 19426 minecraft:light_blue_concrete', 'fill -7 64 19413 7 66 19413 minecraft:glass',
           'fill -7 64 19427 7 66 19427 minecraft:glass', 'fill -7 64 19414 -7 66 19426 minecraft:glass', 'fill 7 64 19414 7 66 19426 minecraft:glass'])
L = ['# Toutes les parcelles du Téléphone (remise à neuf)']
for c in range(NMAX):
    for b in range(2):
        L.append(f'execute positioned {PX(c)} 64 {PZ(b)} run function mg:tel/plot')
w('plots', L)
w('fl_add', ['# Zones chargées pendant la partie'] + [f'forceload add {PX(c) - 18} {PZ(b) - 18} {PX(c) + 18} {PZ(b) + 18}' for c in range(NMAX) for b in range(2)]
  )
w('fl_remove', ['# Fin de partie : zones libérées'] + [f'forceload remove {PX(c) - 18} {PZ(b) - 18} {PX(c) + 18} {PZ(b) + 18}' for c in range(NMAX) for b in range(2)]
  )

# ------------------------------------------------------------------ préparation / départ
w('prepare', [
    '# 📞 Téléphone — préparation (id 81) : 5 à 12 joueurs, une chaîne par joueur',
    'tag @a remove mg.tdone', 'scoreboard players reset @a mg.ti', 'scoreboard players reset @a mg.tc',
    'scoreboard players set @a[tag=mg.play] mg.tpt 0', 'scoreboard players set $tp mg.st -1', 'scoreboard players set $tt mg.st 0',
    'execute store result score $tn mg.st if entity @a[tag=mg.play]',
    'execute if score $tn mg.st matches ..4 run return run function mg:tel/too_few',
    f'execute if score $tn mg.st matches {NMAX + 1}.. run scoreboard players set $tn mg.st {NMAX}',
    'scoreboard players set $tk mg.st 0',
    'execute as @a[tag=mg.play,sort=random] run function mg:tel/assign',
    'function mg:bb/words_init',
    'data modify storage mg:tel ch set value []',
    'scoreboard players set $tk mg.st 0', 'function mg:tel/init_ch',
    'function mg:tel/fl_add', 'function mg:tel/room', 'schedule function mg:tel/plots 40t',
    'clear @a[tag=mg.play]', 'gamemode adventure @a[tag=mg.play]',
    'tp @a[tag=mg.play] 0.5 64 19420.5', 'execute as @a[tag=mg.play] run spawnpoint @s 0 64 19420',
    'scoreboard players set $px mg.st 0', 'scoreboard players set $py mg.st 66', 'scoreboard players set $pz mg.st 19420',
    'tellraw @a[tag=mg.play] ' + js([{'text': '📞 TÉLÉPHONE : ', 'color': 'gold', 'bold': True},
                                     {'text': 'écris un mot → un autre le construit → un autre devine → un autre construit → un dernier devine. À la fin, on découvre ce que chaque mot est devenu !', 'color': 'gray'}]),
    'execute if entity @a[tag=mg.play,scores={mg.ti=-1}] run tellraw @a[tag=mg.play,scores={mg.ti=-1}] {"text":"(12 joueurs maximum : tu regardes cette partie.)","color":"dark_gray","italic":true}'])
w('too_few', ['tellraw @a {"text":"📞 Le Téléphone se joue à 5 joueurs minimum (une chaîne = 5 étapes).","color":"red"}', 'function mg:core/abort'])
w('assign', [f'execute if score $tk mg.st matches ..{NMAX - 1} run scoreboard players operation @s mg.ti = $tk mg.st',
             f'execute if score $tk mg.st matches {NMAX}.. run scoreboard players set @s mg.ti -1',
             'scoreboard players add $tk mg.st 1'])
w('init_ch', ['execute if score $tk mg.st >= $tn mg.st run return 0',
              'data modify storage mg:tel ch append value {s0:"",s2:"",s4:""}', 'scoreboard players add $tk mg.st 1', 'function mg:tel/init_ch'])
w('go', ['# Départ : étape 0 (écrire le mot)', 'scoreboard objectives setdisplay sidebar', 'function mg:tel/phase_start'])

# ------------------------------------------------------------------ étapes
P = '@a[tag=mg.play,scores={mg.ti=0..}]'
w('phase_start', [
    '# Début de l\'étape $tp+1 (0 écrire, 1 construire, 2 deviner, 3 construire, 4 deviner, 5 révélation)',
    'scoreboard players add $tp mg.st 1', 'scoreboard players set $tt mg.st 0', 'tag @a remove mg.tdone',
    'execute if score $tp mg.st matches 5 run return run function mg:tel/reveal_start',
    f'clear {P}',
    f'execute if score $tp mg.st matches 0 run scoreboard players set $tlim mg.st {T_WRITE}',
    f'execute if score $tp mg.st matches 1 run scoreboard players set $tlim mg.st {T_BUILD}',
    f'execute if score $tp mg.st matches 2 run scoreboard players set $tlim mg.st {T_GUESS}',
    f'execute if score $tp mg.st matches 3 run scoreboard players set $tlim mg.st {T_BUILD}',
    f'execute if score $tp mg.st matches 4 run scoreboard players set $tlim mg.st {T_GUESS}',
    f'execute if score $tp mg.st matches 0 as {P} run function mg:tel/start_write',
    f'execute if score $tp mg.st matches 1 as {P} run function mg:tel/start_build',
    f'execute if score $tp mg.st matches 3 as {P} run function mg:tel/start_build',
    f'execute if score $tp mg.st matches 2 as {P} run function mg:tel/start_guess',
    f'execute if score $tp mg.st matches 4 as {P} run function mg:tel/start_guess',
    f'execute as {P} at @s run playsound minecraft:block.note_block.bell master @s ~ ~ ~ 1 1.2'])
w('chain_of', ['# @s : sa chaîne pour l\'étape $tp = (indice + étape) mod N, centre de sa parcelle dans mg.tx / mg.tz',
               'scoreboard players operation @s mg.tc = @s mg.ti', 'scoreboard players operation @s mg.tc += $tp mg.st',
               'scoreboard players operation @s mg.tc %= $tn mg.st',
               'scoreboard players set #64 mg.st 64',
               'scoreboard players operation @s mg.tx = @s mg.tc', 'scoreboard players operation @s mg.tx *= #64 mg.st',
               'scoreboard players remove @s mg.tx 352',
               'scoreboard players set @s mg.tz 19500', 'execute if score $tp mg.st matches 3..4 run scoreboard players add @s mg.tz 64',
               'execute store result storage mg:tel p.c int 1 run scoreboard players get @s mg.tc',
               'execute store result storage mg:tel p.x int 1 run scoreboard players get @s mg.tx',
               'execute store result storage mg:tel p.z int 1 run scoreboard players get @s mg.tz',
               'scoreboard players operation $tvz mg.st = @s mg.tz', 'scoreboard players remove $tvz mg.st 14',
               'execute store result storage mg:tel p.vz int 1 run scoreboard players get $tvz mg.st'])
w('start_write', ['# @s : écrire un mot', 'function mg:tel/chain_of',
                  'gamemode adventure @s', 'tp @s 0.5 64 19420.5', f'give @s {BOOK}',
                  'title @s title {"text":"📞 Écris un mot","color":"gold","bold":true}',
                  'title @s subtitle {"text":"Livre : 1re page, « Terminé », puis Valider","color":"gray"}',
                  'tellraw @s ' + js([{'text': '\n📞 Écris un mot ou une petite expression ', 'color': 'gold', 'bold': True},
                                      {'text': '(sur la 1re page du livre, puis « Terminé ») : un autre joueur devra le construire. 60 s.', 'color': 'gray'}]),
                  'tellraw @s ' + VALID])
w('start_build', ['# @s : construire (mot ou devinette précédente de sa chaîne)',
                  'function mg:tel/chain_of', 'function mg:tel/start_build_m with storage mg:tel p'])
w('start_build_m', ['$tp @s $(x).5 65 $(z).5 0 15', 'gamemode creative @s',
                    '$execute if score $tp mg.st matches 1 run title @s title [{"text":"✎ ","color":"gold"},{"nbt":"ch[$(c)].s0","storage":"mg:tel","color":"yellow","bold":true}]',
                    '$execute if score $tp mg.st matches 3 run title @s title [{"text":"✎ ","color":"gold"},{"nbt":"ch[$(c)].s2","storage":"mg:tel","color":"yellow","bold":true}]',
                    'title @s subtitle {"text":"Construis-le en 2 min 30 (sans écrire de texte !)","color":"gray"}',
                    '$execute if score $tp mg.st matches 1 run tellraw @s [{"text":"\\n✎ À CONSTRUIRE : ","color":"gold","bold":true},{"nbt":"ch[$(c)].s0","storage":"mg:tel","color":"yellow","bold":true},{"text":"  (2 min 30, reste sur ta parcelle)","color":"gray"}]',
                    '$execute if score $tp mg.st matches 3 run tellraw @s [{"text":"\\n✎ À CONSTRUIRE : ","color":"gold","bold":true},{"nbt":"ch[$(c)].s2","storage":"mg:tel","color":"yellow","bold":true},{"text":"  (2 min 30, reste sur ta parcelle)","color":"gray"}]'])
w('start_guess', ['# @s : deviner la construction de sa chaîne', 'function mg:tel/chain_of', 'function mg:tel/start_guess_m with storage mg:tel p'])
w('start_guess_m', ['$tp @s $(x).5 65 $(vz).5 0 20', 'gamemode adventure @s', f'give @s {BOOK}',
                    'title @s title {"text":"🔍 Qu\'est-ce que c\'est ?","color":"aqua","bold":true}',
                    'title @s subtitle {"text":"Fais le tour, écris ta réponse dans le livre, puis Valider","color":"gray"}',
                    'tellraw @s ' + js([{'text': '\n🔍 Devine ce que représente cette construction ', 'color': 'aqua', 'bold': True},
                                        {'text': '(1re page du livre, puis « Terminé »). 60 s.', 'color': 'gray'}]),
                    'tellraw @s ' + VALID])

# validation (trigger mg.tel)
w('cast', ['# @s a utilisé /trigger mg.tel (1 = valider le livre)',
           'execute unless score $state mg.st matches 2 run return run scoreboard players reset @s mg.tel',
           f'execute unless score $game mg.st matches {GID} run return run scoreboard players reset @s mg.tel',
           'execute unless score @s mg.ti matches 0.. run return run scoreboard players reset @s mg.tel',
           'execute unless score $tp mg.st matches 0 unless score $tp mg.st matches 2 unless score $tp mg.st matches 4 run return run scoreboard players reset @s mg.tel',
           'execute if entity @s[tag=mg.tdone] run tellraw @s {"text":"✔ Déjà validé (tu peux encore corriger : réécris puis valide à nouveau).","color":"gray"}',
           'function mg:tel/read_book',
           'scoreboard players reset @s mg.tel'])
w('read_book', ['# @s : lit la 1re page de son livre → ch[mg.tc].s<étape>',
                'data remove storage mg:tel tmp',
                'execute store success score $tok mg.st run data modify storage mg:tel tmp set from entity @s Inventory[{id:"minecraft:writable_book"}].components."minecraft:writable_book_content".pages[0].raw',
                'execute unless score $tok mg.st matches 1 store success score $tok mg.st run data modify storage mg:tel tmp set from entity @s Inventory[{id:"minecraft:writable_book"}].components."minecraft:writable_book_content".pages[0]',
                'execute unless score $tok mg.st matches 1 run return run tellraw @s {"text":"⚠ Livre vide : écris sur la 1re page, clique « Terminé », puis valide.","color":"red"}',
                'execute store result score $tl mg.st run data get storage mg:tel tmp',
                'execute unless score $tl mg.st matches 1..40 run return run tellraw @s {"text":"⚠ De 1 à 40 caractères, s\'il te plaît.","color":"red"}',
                'execute store result storage mg:tel p.c int 1 run scoreboard players get @s mg.tc',
                'execute if score $tp mg.st matches 0 run data modify storage mg:tel p.k set value "s0"',
                'execute if score $tp mg.st matches 2 run data modify storage mg:tel p.k set value "s2"',
                'execute if score $tp mg.st matches 4 run data modify storage mg:tel p.k set value "s4"',
                'function mg:tel/store with storage mg:tel p',
                'tag @s add mg.tdone',
                'tellraw @s [{"text":"✔ Enregistré : ","color":"green"},{"nbt":"tmp","storage":"mg:tel","color":"white"},{"text":" — en attente des autres…","color":"gray"}]',
                'execute at @s run playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 1 1.2'])
w('store', ['$data modify storage mg:tel ch[$(c)].$(k) set from storage mg:tel tmp'])

# fin d'étape : réponses manquantes
w('phase_end', ['# Fin d\'étape : complète les réponses manquantes, puis étape suivante',
                f'execute if score $tp mg.st matches 0 as {P} unless entity @s[tag=mg.tdone] run function mg:tel/fill_word',
                f'execute if score $tp mg.st matches 2 as {P} unless entity @s[tag=mg.tdone] run function mg:tel/fill_guess',
                f'execute if score $tp mg.st matches 4 as {P} unless entity @s[tag=mg.tdone] run function mg:tel/fill_guess',
                f'execute if score $tp mg.st matches 1 run gamemode adventure {P}',
                f'execute if score $tp mg.st matches 3 run gamemode adventure {P}',
                'kill @e[type=minecraft:item,x=-400,y=0,z=19400,dx=800,dy=200,dz=250]',
                'function mg:tel/phase_start'])
w('fill_word', ['# Pas de mot validé → tentative de lecture du livre, sinon mot au hasard',
                'function mg:tel/read_book',
                'execute if entity @s[tag=mg.tdone] run return 0',
                'function mg:bb/pick_word', 'data modify storage mg:tel tmp set from storage mg:bb word',
                'execute store result storage mg:tel p.c int 1 run scoreboard players get @s mg.tc', 'data modify storage mg:tel p.k set value "s0"',
                'function mg:tel/store with storage mg:tel p',
                'tellraw @s [{"text":"⏱ Temps écoulé : mot tiré au hasard → ","color":"gray"},{"nbt":"tmp","storage":"mg:tel","color":"white"}]'])
w('fill_guess', ['# Pas de devinette validée → tentative de lecture du livre, sinon « ??? »',
                 'function mg:tel/read_book',
                 'execute if entity @s[tag=mg.tdone] run return 0',
                 'data modify storage mg:tel tmp set value "???"',
                 'execute store result storage mg:tel p.c int 1 run scoreboard players get @s mg.tc',
                 'execute if score $tp mg.st matches 2 run data modify storage mg:tel p.k set value "s2"',
                 'execute if score $tp mg.st matches 4 run data modify storage mg:tel p.k set value "s4"',
                 'function mg:tel/store with storage mg:tel p'])

# ------------------------------------------------------------------ tick
w('tick', ['# 📞 Téléphone — tick (état 2)',
           'execute unless entity @a[tag=mg.play] run return run function mg:core/draw',
           'execute if score $tp mg.st matches 5 run return run function mg:tel/reveal_tick',
           'scoreboard players add $tt mg.st 1',
           f'execute if score $tp mg.st matches 1 as {P} run function mg:tel/confine',
           f'execute if score $tp mg.st matches 3 as {P} run function mg:tel/confine',
           f'execute if score $tp mg.st matches 2 as {P} run function mg:tel/confine',
           f'execute if score $tp mg.st matches 4 as {P} run function mg:tel/confine',
           'scoreboard players operation $tq mg.st = $tt mg.st', 'scoreboard players set #20 mg.st 20', 'scoreboard players operation $tq mg.st %= #20 mg.st',
           'execute if score $tq mg.st matches 0 run function mg:tel/hud',
           # tout le monde a validé → étape suivante (écrire / deviner)
           f'execute store result score $tna mg.st if entity {P}',
           f'execute store result score $tnd mg.st if entity @a[tag=mg.play,tag=mg.tdone,scores={{mg.ti=0..}}]',
           'execute unless score $tp mg.st matches 1 unless score $tp mg.st matches 3 if score $tna mg.st matches 1.. if score $tnd mg.st = $tna mg.st run return run function mg:tel/phase_end',
           'execute if score $tt mg.st >= $tlim mg.st run function mg:tel/phase_end'])
w('confine', ['# @s reste sur (ou autour de) sa parcelle', 'execute store result storage mg:tel q.x int 1 run scoreboard players get @s mg.tx',
              'execute store result storage mg:tel q.z int 1 run scoreboard players get @s mg.tz', 'function mg:tel/confine_m with storage mg:tel q'])
w('confine_m', ['$execute positioned $(x) 56 $(z) positioned ~-15 ~ ~-15 if entity @s[dx=31,dy=48,dz=31] run return 0',
                '$tp @s $(x).5 65 $(z).5', 'title @s actionbar {"text":"⚠ Reste sur ta parcelle !","color":"red"}'])
w('hud', ['# Barre d\'action : étape + temps restant',
          'scoreboard players operation $tsec mg.st = $tlim mg.st', 'scoreboard players operation $tsec mg.st -= $tt mg.st',
          'scoreboard players operation $tsec mg.st /= #20 mg.st',
          f'execute if score $tp mg.st matches 0 run title {P} actionbar [{{"text":"📞 Étape 1/5 : écris un mot   ⏱ ","color":"gold"}},{{"score":{{"name":"$tsec","objective":"mg.st"}},"color":"yellow"}},{{"text":" s","color":"gold"}}]',
          f'execute if score $tp mg.st matches 1 run title {P} actionbar [{{"text":"✎ Étape 2/5 : construis   ⏱ ","color":"gold"}},{{"score":{{"name":"$tsec","objective":"mg.st"}},"color":"yellow"}},{{"text":" s","color":"gold"}}]',
          f'execute if score $tp mg.st matches 2 run title {P} actionbar [{{"text":"🔍 Étape 3/5 : devine   ⏱ ","color":"aqua"}},{{"score":{{"name":"$tsec","objective":"mg.st"}},"color":"yellow"}},{{"text":" s","color":"aqua"}}]',
          f'execute if score $tp mg.st matches 3 run title {P} actionbar [{{"text":"✎ Étape 4/5 : construis   ⏱ ","color":"gold"}},{{"score":{{"name":"$tsec","objective":"mg.st"}},"color":"yellow"}},{{"text":" s","color":"gold"}}]',
          f'execute if score $tp mg.st matches 4 run title {P} actionbar [{{"text":"🔍 Étape 5/5 : devine   ⏱ ","color":"aqua"}},{{"score":{{"name":"$tsec","objective":"mg.st"}},"color":"yellow"}},{{"text":" s","color":"aqua"}}]',
          f'execute if score $tsec mg.st matches 1..5 as {P} at @s run playsound minecraft:block.note_block.hat master @s ~ ~ ~ 1 1.4'])

# ------------------------------------------------------------------ révélation
V = '@a[tag=!mg.surv]'
w('reveal_start', ['# Révélation : chaîne par chaîne (mot → construction → devinette → construction → devinette)',
                   f'clear @a[tag=mg.play]', f'gamemode spectator @a[tag=mg.play]',
                   'scoreboard objectives setdisplay sidebar mg.tpt',
                   'scoreboard players set $rc mg.st 0', 'scoreboard players set $rs mg.st -1', 'scoreboard players set $tt mg.st 0',
                   'scoreboard players set $tlim mg.st 1',
                   'tellraw @a[tag=!mg.surv] {"text":"\\n📞 RÉVÉLATION ! Voici ce que chaque mot est devenu…","color":"gold","bold":true}'])
w('reveal_tick', ['scoreboard players add $tt mg.st 1', 'execute if score $tt mg.st >= $tlim mg.st run function mg:tel/reveal_next'])
w('reveal_next', ['scoreboard players set $tt mg.st 0', 'scoreboard players add $rs mg.st 1',
                  'execute if score $rs mg.st matches 5.. run scoreboard players add $rc mg.st 1',
                  'execute if score $rs mg.st matches 5.. run scoreboard players set $rs mg.st 0',
                  'execute if score $rc mg.st >= $tn mg.st run return run function mg:tel/finish',
                  # indices : auteur de l'étape s pour la chaîne c = (c − s + N) mod N
                  'scoreboard players operation $ra mg.st = $rc mg.st', 'scoreboard players operation $ra mg.st -= $rs mg.st',
                  'scoreboard players operation $ra mg.st += $tn mg.st', 'scoreboard players operation $ra mg.st %= $tn mg.st',
                  'scoreboard players operation $rb mg.st = $ra mg.st', 'scoreboard players operation $rb mg.st += $tn mg.st',
                  'scoreboard players remove $rb mg.st 1', 'scoreboard players operation $rb mg.st %= $tn mg.st',
                  'execute store result storage mg:tel r.c int 1 run scoreboard players get $rc mg.st',
                  'scoreboard players operation $rcn mg.st = $rc mg.st', 'scoreboard players add $rcn mg.st 1',
                  'execute store result storage mg:tel r.n int 1 run scoreboard players get $rc mg.st',
                  'execute store result storage mg:tel r.a int 1 run scoreboard players get $ra mg.st',
                  'execute store result storage mg:tel r.b int 1 run scoreboard players get $rb mg.st',
                  'scoreboard players set #64 mg.st 64', 'scoreboard players operation $rx mg.st = $rc mg.st', 'scoreboard players operation $rx mg.st *= #64 mg.st',
                  'scoreboard players remove $rx mg.st 352', 'execute store result storage mg:tel r.x int 1 run scoreboard players get $rx mg.st',
                  'execute if score $rs mg.st matches 0 run scoreboard players set $tlim mg.st 100',
                  'execute if score $rs mg.st matches 1 run scoreboard players set $tlim mg.st 200',
                  'execute if score $rs mg.st matches 2 run scoreboard players set $tlim mg.st 100',
                  'execute if score $rs mg.st matches 3 run scoreboard players set $tlim mg.st 200',
                  'execute if score $rs mg.st matches 4 run scoreboard players set $tlim mg.st 140',
                  'function mg:tel/reveal_show with storage mg:tel r'])
SEL = lambda k: f'{{"selector":"@a[scores={{mg.ti=$({k})}}]","color":"yellow"}}'
w('reveal_show', [
    '# Macro : c (chaîne), a (auteur de l\'étape), b (auteur de l\'étape précédente), x (parcelle)',
    'execute if score $rs mg.st matches 0 run tp @a[tag=!mg.surv,tag=mg.play] 0.5 66 19420.5',
    '$execute if score $rs mg.st matches 0 run tellraw @a[tag=!mg.surv] [{"text":"\\n📞 Chaîne ","color":"gold","bold":true},{"score":{"name":"$rcn","objective":"mg.st"},"color":"gold","bold":true},{"text":" — ","color":"gray"},' + SEL('a') + ',{"text":" a écrit : ","color":"gray"},{"nbt":"ch[$(c)].s0","storage":"mg:tel","color":"white","bold":true}]',
    '$execute if score $rs mg.st matches 0 run title @a[tag=!mg.surv] title [{"text":"« ","color":"gold"},{"nbt":"ch[$(c)].s0","storage":"mg:tel","color":"white","bold":true},{"text":" »","color":"gold"}]',
    '$execute if score $rs mg.st matches 1 run tp @a[tag=!mg.surv,tag=mg.play] $(x).5 74 19480.5 0 30',
    '$execute if score $rs mg.st matches 1 run tellraw @a[tag=!mg.surv] [{"text":"  ✎ construit par ","color":"gray"},' + SEL('a') + ']',
    '$execute if score $rs mg.st matches 1 run title @a[tag=!mg.surv] subtitle [{"text":"✎ construit par ","color":"gray"},' + SEL('a') + ']',
    'execute if score $rs mg.st matches 1 run title @a[tag=!mg.surv] title {"text":""}',
    '$execute if score $rs mg.st matches 2 run tellraw @a[tag=!mg.surv] [{"text":"  🔍 ","color":"gray"},' + SEL('a') + ',{"text":" a deviné : ","color":"gray"},{"nbt":"ch[$(c)].s2","storage":"mg:tel","color":"white","bold":true}]',
    '$execute if score $rs mg.st matches 2 run title @a[tag=!mg.surv] title [{"text":"« ","color":"aqua"},{"nbt":"ch[$(c)].s2","storage":"mg:tel","color":"white","bold":true},{"text":" »","color":"aqua"}]',
    '$execute if score $rs mg.st matches 2 run function mg:tel/check {c:$(c),a:$(a),b:$(b),k:"s2"}',
    '$execute if score $rs mg.st matches 3 run tp @a[tag=!mg.surv,tag=mg.play] $(x).5 74 19544.5 0 30',
    '$execute if score $rs mg.st matches 3 run tellraw @a[tag=!mg.surv] [{"text":"  ✎ construit par ","color":"gray"},' + SEL('a') + ']',
    '$execute if score $rs mg.st matches 3 run title @a[tag=!mg.surv] subtitle [{"text":"✎ construit par ","color":"gray"},' + SEL('a') + ']',
    'execute if score $rs mg.st matches 3 run title @a[tag=!mg.surv] title {"text":""}',
    '$execute if score $rs mg.st matches 4 run tellraw @a[tag=!mg.surv] [{"text":"  🔍 ","color":"gray"},' + SEL('a') + ',{"text":" a deviné : ","color":"gray"},{"nbt":"ch[$(c)].s4","storage":"mg:tel","color":"white","bold":true}]',
    '$execute if score $rs mg.st matches 4 run title @a[tag=!mg.surv] title [{"text":"« ","color":"aqua"},{"nbt":"ch[$(c)].s4","storage":"mg:tel","color":"white","bold":true},{"text":" »","color":"aqua"}]',
    '$execute if score $rs mg.st matches 4 run function mg:tel/check {c:$(c),a:$(a),b:$(b),k:"s4"}',
    'execute as @a[tag=!mg.surv] at @s run playsound minecraft:block.note_block.chime master @s ~ ~ ~ 1 1'])
w('check', ['# Macro : la devinette $(k) de la chaîne $(c) est-elle le mot de départ ? +1 au devineur (a) et au constructeur (b)',
            '$data modify storage mg:tel cmp set from storage mg:tel ch[$(c)].s0',
            '$execute store success score $tneq mg.st run data modify storage mg:tel cmp set from storage mg:tel ch[$(c)].$(k)',
            'execute if score $tneq mg.st matches 1 run return run tellraw @a[tag=!mg.surv] {"text":"     ✘ ce n\'est plus le mot de départ…","color":"red"}',
            '$scoreboard players add @a[scores={mg.ti=$(a)}] mg.tpt 1',
            '$scoreboard players add @a[scores={mg.ti=$(b)}] mg.tpt 1',
            'tellraw @a[tag=!mg.surv] {"text":"     ✔ C\'EST LE MOT DE DÉPART ! +1 au devineur et au constructeur","color":"green","bold":true}',
            'execute as @a[tag=!mg.surv] at @s run playsound minecraft:entity.player.levelup master @s ~ ~ ~ 1 1.2'])
w('finish', ['# Fin : le plus de points gagne (égalité ou 0 point = pas de vainqueur)',
             'tp @a[tag=mg.play] 0.5 64 19420.5', 'gamemode adventure @a[tag=mg.play]',
             'scoreboard players set $tmax mg.st 0', 'scoreboard players operation $tmax mg.st > @a[tag=mg.play] mg.tpt',
             'execute if score $tmax mg.st matches 0 run tellraw @a[tag=!mg.surv] {"text":"📞 Aucun mot n\'a survécu jusqu\'au bout : pas de vainqueur !","color":"gold"}',
             'execute if score $tmax mg.st matches 0 run return run function mg:core/draw',
             'scoreboard players set $twn mg.st 0',
             'execute as @a[tag=mg.play] if score @s mg.tpt = $tmax mg.st run scoreboard players add $twn mg.st 1',
             'execute if score $twn mg.st matches 2.. run tellraw @a[tag=!mg.surv] {"text":"📞 Égalité en tête : pas de vainqueur unique !","color":"gold"}',
             'execute if score $twn mg.st matches 2.. run return run function mg:core/draw',
             'execute as @a[tag=mg.play] if score @s mg.tpt = $tmax mg.st run function mg:core/win_player'])
w('cleanup', ['# Fin de partie Téléphone', 'function mg:tel/fl_remove', 'tag @a remove mg.tdone', 'scoreboard players reset @a mg.ti',
              'scoreboard players reset @a mg.tc', 'scoreboard players reset @a mg.tpt', 'clear @a minecraft:writable_book', 'data remove storage mg:tel ch'])


# ------------------------------------------------------------------ crochets
def patch(rel, anchor, new_lines, where='after'):
    p = os.path.join(F, rel + '.mcfunction')
    lines = open(p, encoding='utf-8').read().split('\n')
    if all(l in lines for l in new_lines):
        return
    idx = [i for i, l in enumerate(lines) if l == anchor]
    if len(idx) != 1:
        raise SystemExit(f'{rel} : ancre {anchor!r} trouvée {len(idx)} fois')
    i = idx[0] + (1 if where == 'after' else 0)
    lines[i:i] = new_lines
    with open(p, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(lines))


def replace(rel, old, new):
    p = os.path.join(F, rel + '.mcfunction')
    t = open(p, encoding='utf-8').read()
    if new in t:
        return
    assert t.count(old) == 1, (rel, old)
    with open(p, 'w', encoding='utf-8', newline='\n') as f:
        f.write(t.replace(old, new))


replace('core/go', 'matches 1..82 unless', 'matches 1..83 unless')
patch('core/request', 'execute if score $game mg.st matches 57..58 run function mg:bb/prepare', [f'execute if score $game mg.st matches {GID} run function mg:tel/prepare'])
first_bb = next(l for l in open(os.path.join(F, 'core/request.mcfunction'), encoding='utf-8').read().split('\n')
                if l.startswith('execute if score $game mg.st matches 57 run tellraw'))
patch('core/request', first_bb, [f'execute if score $game mg.st matches {GID} run tellraw @a ' + js([
    {'selector': '@s', 'color': 'yellow'}, {'text': ' lance un ', 'color': 'gray'}, {'text': '📞 TÉLÉPHONE', 'color': 'gold', 'bold': True},
    {'text': ' : mot → construction → devinette → construction → devinette !', 'color': 'gray'}])])
patch('core/begin', 'execute if score $game mg.st matches 57..58 run function mg:bb/go', [f'execute if score $game mg.st matches {GID} run function mg:tel/go'])
patch('core/game_tick', 'execute if score $game mg.st matches 57..58 run function mg:bb/tick', [f'execute if score $game mg.st matches {GID} run function mg:tel/tick'])
patch('core/return_lobby', 'execute if score $game mg.st matches 57..58 run function mg:bb/cleanup', [f'execute if score $game mg.st matches {GID} run function mg:tel/cleanup'])
patch('core/tick', 'scoreboard players enable @a mg.bw', ['scoreboard players enable @a mg.tel'])
patch('core/forceloads', 'function mg:tnttag/map/fl', ['# Téléphone : salle d\'attente (les parcelles sont chargées pendant la partie)', 'forceload add -8 19412 8 19428'], where='before')
patch('core/tick', 'execute as @a[scores={mg.bw=1..}] run function mg:bb/word_cast', ['execute as @a[scores={mg.tel=1..}] run function mg:tel/cast'])
patch('core/load', 'scoreboard objectives add mg.bw trigger', ['scoreboard objectives add mg.tel trigger', 'scoreboard objectives add mg.ti dummy',
                                                                'scoreboard objectives add mg.tc dummy', 'scoreboard objectives add mg.tx dummy',
                                                                'scoreboard objectives add mg.tz dummy',
                                                                'scoreboard objectives add mg.tpt dummy {"text":"📞 Points","color":"gold"}'])
patch('desinstaller', 'scoreboard objectives remove mg.bw', ['scoreboard objectives remove mg.tel', 'scoreboard objectives remove mg.ti',
                                                             'scoreboard objectives remove mg.tc', 'scoreboard objectives remove mg.tx',
                                                             'scoreboard objectives remove mg.tz', 'scoreboard objectives remove mg.tpt'])
# menu : catégorie Fête et création (généré par gen_variants : on ajoute au tableau CATS via le dialog directement)
p = os.path.join(D, 'dialog/cat_fete.json')
d = json.load(open(p, encoding='utf-8'))
if not any(a.get('action', {}).get('command') == f'trigger mg.go set {GID}' for a in d['actions']):
    d['actions'].insert(len(d['actions']) - 1, {'label': [{'text': '📞 Téléphone (5+)', 'color': 'gold'}],
                                                 'tooltip': [{'text': 'Mot → construction → devinette → construction → devinette. 5 à 12 joueurs.', 'color': 'gray'}],
                                                 'action': {'type': 'minecraft:run_command', 'command': f'trigger mg.go set {GID}'}})
    with open(p, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
        f.write('\n')
print('Téléphone : OK')
