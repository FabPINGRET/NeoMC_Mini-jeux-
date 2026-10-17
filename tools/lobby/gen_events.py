"""🎉 Événements surprises du lobby : python tools/lobby/gen_events.py .   (après tools/admin/gen_tp_general.py : ancre `tpg/run` de core/opt)

Toutes les 30 min (jeu au repos, au moins un joueur au lobby), annonce 1 min avant puis un des trois événements (3 min) :
  👑 Roi Zombie : un husk géant (vie selon le nombre de joueurs) et ses sbires ; épée prêtée ; le plus gros cogneur gagne.
  💰 Pluie de pièces : des pépites (1) et des lingots (5) tombent sur l'île pendant 60 s ; le plus riche gagne.
     Décor saisonnier actif ($theme) : devient 🍬 Chasse aux bonbons (Halloween) ou 🎁 Chasse aux cadeaux (Noël).
  🗝 Chasse au trésor : un coffre caché sur l'île, indices chaud / froid ; le premier qui clique dessus gagne.
Gagnant : couronne (jusqu'à la prochaine partie), feu d'artifice, mg.evw + 1. Une partie qui démarre arrête l'événement.
Admin : menu ≡ → 🎉 Événements du lobby (mg.opt 67 : au hasard 68, événement k 68+k, arrêter/annuler 72),
ou /function mg:lobby/ev/force (au hasard, annonce 10 s), mg:lobby/ev/force_1..3, mg:lobby/ev/cancel.
"""
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'arcade'))
import common as C

C.init(sys.argv[1] if len(sys.argv) > 1 else '.')
w, js = C.w, C.js
EVERY, LEN = 1800, 180                             # secondes
L = '@a[tag=mg.evl]'
NAMES = {1: ('👑 Roi Zombie', 'red', 'Un zombie géant attaque le spawn ! Tape-le fort, le plus gros cogneur gagne.'),
         2: ('💰 Pluie de pièces', 'gold', 'Des pièces tombent du ciel ! Pépite = 1, lingot = 5. Le plus riche gagne.'),
         3: ('🗝 Chasse au trésor', 'aqua', 'Un coffre est caché sur l\'île. Suis les indices, le premier qui le trouve gagne.')}
EVI = '[minecraft:custom_data~{mg_ev:1b}]'

w('lobby/ev/tick', ['# Événements surprises (chaque tick, $setup 1)',
                    'scoreboard players add $evtk mg.st 1',
                    'execute if score $evtk mg.st matches 20.. run function mg:lobby/ev/second',
                    'execute if score $evon mg.st matches 1 run function mg:lobby/ev/e1_tick',
                    'execute if score $evon mg.st matches 3 as @e[type=minecraft:interaction,tag=mg.evti] if data entity @s interaction run function mg:lobby/ev/e3_click'])

w('lobby/ev/second', ['scoreboard players set $evtk mg.st 0',
                      'tag @a remove mg.evl',
                      'execute in minecraft:overworld run tag @a[x=-70,y=30,z=-70,dx=140,dy=100,dz=140,tag=!mg.play,tag=!mg.surv,gamemode=!spectator] add mg.evl',
                      'execute unless score $evn mg.st matches -2147483648.. run scoreboard players set $evn mg.st ' + str(EVERY),
                      'execute if score $evon mg.st matches 1.. unless score $state mg.st matches 0 run return run function mg:lobby/ev/stop',
                      'execute if score $evon mg.st matches 1.. run return run function mg:lobby/ev/run',
                      # annonce en cours mais partie lancée / lobby vide : on la remet à plus tard (barre retirée)
                      'execute unless score $state mg.st matches 0 if score $evn mg.st matches 1..60 run function mg:lobby/ev/postpone',
                      f'execute unless entity {L} if score $evn mg.st matches 1..60 run function mg:lobby/ev/postpone',
                      'execute unless score $state mg.st matches 0 run return 0',
                      f'execute unless entity {L} run return 0',
                      'scoreboard players remove $evn mg.st 1',
                      'execute if score $evn mg.st matches 60 run function mg:lobby/ev/pick',
                      'execute if score $evn mg.st matches 1..60 run function mg:lobby/ev/countdown',
                      'execute if score $evn mg.st matches ..0 run function mg:lobby/ev/start'])

w('lobby/ev/pick', ['execute unless score $evk mg.st matches 1..3 store result score $evk mg.st run random value 1..3',
                    'bossbar add mg:ev ""', 'bossbar set mg:ev max 60', 'bossbar set mg:ev style notched_10'] +
  [f'execute if score $evk mg.st matches {k} run function mg:lobby/ev/ann_{k}' for k in NAMES])
# Habillage saisonnier de la pluie de pièces ($theme mg.st, tools/lobby/gen_themes.py) : mêmes objets
# (pépite = 1, lingot = 5, comptage et nettoyage inchangés), seuls le nom et l'apparence (item_model) changent.
# thème : (condition, nom, couleur, description, petit (nom, modèle), gros (nom, modèle), unité, particule, gagnant)
E2_SKINS = {0: ('unless score $theme mg.st matches 1..2', NAMES[2][0], 'gold', NAMES[2][2],
                ('Pièce (1)', None), ('Gros lingot (5)', None), 'pièces', 'wax_on', '💰 Le plus riche : '),
            1: ('if score $theme mg.st matches 1', '🍬 Chasse aux bonbons', 'gold',
                'Des bonbons tombent du ciel ! Bonbon = 1, citrouille-surprise = 5. Le plus gourmand gagne.',
                ('🍬 Bonbon (1)', 'minecraft:cookie'), ('🎃 Citrouille-surprise (5)', 'minecraft:jack_o_lantern'), 'bonbons', 'soul', '🍬 Le plus gourmand : '),
            2: ('if score $theme mg.st matches 2', '🎁 Chasse aux cadeaux', 'red',
                'Le traîneau perd sa cargaison ! Biscuit = 1, cadeau = 5. Le plus chargé gagne.',
                ('🍪 Biscuit (1)', 'minecraft:cookie'), ('🎁 Cadeau (5)', 'minecraft:red_shulker_box'), 'cadeaux', 'snowflake', '🎁 Le plus chargé : ')}
# Annonce : « dans 1 min » (automatique) ou « dans 10 s » ($evf 1 : lancé par un admin, force_go)
for k, (nm0, col0, desc0) in NAMES.items():
    ann = []
    for tcond, nm, col, desc in ([(s[0], s[1], s[2], s[3]) for s in E2_SKINS.values()] if k == 2 else [('', nm0, col0, desc0)]):
      for cond, short, long in (('unless', '1 min', '1 minute'), ('if', '10 s', '10 secondes')):
        pre = f'execute {tcond + " " if tcond else ""}{cond} score $evf mg.st matches 1 run '
        ann += [pre + 'bossbar set mg:ev name ' + js([{'text': 'Événement : ', 'color': 'white'}, {'text': nm, 'color': col, 'bold': True}, {'text': f' dans {short}', 'color': 'gray'}]),
                pre + 'tellraw @a ' + js([{'text': f'🎉 ÉVÉNEMENT SURPRISE au spawn dans {long} : ', 'color': 'light_purple', 'bold': True},
                                          {'text': nm, 'color': col, 'bold': True}, {'text': f'\n{desc}', 'color': 'gray'}])]
    w(f'lobby/ev/ann_{k}', ann + [f'bossbar set mg:ev color {"red" if col0 == "red" else "yellow" if col0 == "gold" else "blue"}',
                                  f'execute as @a[tag=!mg.surv] at @s run playsound minecraft:block.bell.use master @s ~ ~ ~ 1 0.8'])
w('lobby/ev/countdown', [f'bossbar set mg:ev players {L}',
                         'execute store result bossbar mg:ev value run scoreboard players get $evn mg.st',
                         f'execute if score $evn mg.st matches 1..5 as {L} at @s run playsound minecraft:block.note_block.hat master @s ~ ~ ~ 1 1.4',
                         f'execute if score $evn mg.st matches 10 run title {L} actionbar {{"text":"🎉 L\'événement commence dans 10 s !","color":"light_purple"}}'])

w('lobby/ev/force', ['# Admin : événement au hasard dans 10 s', 'scoreboard players reset $evk mg.st', 'scoreboard players set $evn mg.st 61',
                     'function mg:lobby/ev/force_go'])
w('lobby/ev/postpone', ['# Annonce suspendue (partie lancée ou lobby vide) : même événement réannoncé au retour',
                        'bossbar remove mg:ev', 'scoreboard players set $evn mg.st 61'])
w('lobby/ev/force_go', ['execute unless score $state mg.st matches 0 run scoreboard players reset $evk mg.st',
                        'execute if score $evon mg.st matches 1.. run scoreboard players reset $evk mg.st',
                        'execute unless score $state mg.st matches 0 run return run tellraw @s {"text":"Une partie est en cours.","color":"red"}',
                        'execute if score $evon mg.st matches 1.. run return run tellraw @s {"text":"Un événement est déjà en cours (⛔ Arrêter dans le menu des événements).","color":"red"}',
                        'scoreboard players set $evn mg.st 60', 'scoreboard players set $evf mg.st 1', 'function mg:lobby/ev/pick',
                        'scoreboard players set $evf mg.st 0', 'scoreboard players set $evn mg.st 11', 'bossbar set mg:ev max 10',
                        'tellraw @s {"text":"✔ Événement lancé : il commence dans 10 s.","color":"green"}'])
for k in NAMES:
    w(f'lobby/ev/force_{k}', [f'# Admin : événement {k} dans 10 s', f'scoreboard players set $evk mg.st {k}', 'function mg:lobby/ev/force_go'])
w('lobby/ev/cancel', ['# Admin : arrête l\'événement en cours ou annule celui qui est annoncé (le prochain revient dans 30 min)',
                     'execute unless score $evon mg.st matches 1.. unless score $evn mg.st matches 1..61 run return run tellraw @s {"text":"Aucun événement en cours ni annoncé.","color":"gray"}',
                     f'scoreboard players set $evn mg.st {EVERY}', 'scoreboard players reset $evk mg.st', 'function mg:lobby/ev/stop',
                     'tellraw @a {"text":"🎉 L\'événement du lobby a été annulé par un admin.","color":"gray"}'])

# Menu admin des événements : mg.opt 67 (fenêtre), 68 au hasard, 68 + k événement k, 72 arrêter / annuler
EV_OPT = 67
EV_BTN = [('🎲 Au hasard', 'light_purple', EV_OPT + 1, 'Un des trois événements, annoncé 10 s avant')]
EV_BTN += [(NAMES[k][0], NAMES[k][1], EV_OPT + 1 + k, NAMES[k][2]) for k in NAMES]
EV_BTN += [('⛔ Arrêter / annuler', 'dark_red', EV_OPT + 5, 'Arrête l\'événement en cours ou annule celui qui est annoncé')]
# Décors saisonniers du spawn (tools/lobby/gen_themes.py) : bascule pose / retrait
EV_BTN += [('🎃 Déco Halloween', 'gold', 73, 'Pose ou retire le décor d\'Halloween du spawn (réversible)'),
           ('🎄 Déco Noël', 'red', 74, 'Pose ou retire le décor de Noël du spawn (réversible)')]
dialog = {'type': 'minecraft:multi_action', 'title': {'text': '🎉 Événements du lobby', 'color': 'light_purple', 'bold': True},
          'pause': False, 'can_close_with_escape': True,
          'body': [{'type': 'minecraft:plain_message', 'contents': [
              {'text': 'Lance un événement surprise au spawn (jeu au repos, joueurs au lobby). Il commence 10 s après l\'annonce et dure 3 min.',
               'color': 'gray'}]}],
          'columns': 2, 'exit_action': {'label': [{'text': 'Fermer', 'color': 'gray'}]},
          'actions': [{'label': [{'text': t, 'color': c, 'bold': True}], 'tooltip': [{'text': tip, 'color': 'gray'}],
                       'action': {'type': 'minecraft:run_command', 'command': f'trigger mg.opt set {o}'}} for t, c, o, tip in EV_BTN]
                     + [{'label': [{'text': '« Retour au menu', 'color': 'yellow'}], 'action': {'type': 'minecraft:run_command', 'command': 'trigger mg.menu'}}]}
with open(os.path.join(sys.argv[1] if len(sys.argv) > 1 else '.', 'data/mg/dialog/lobby_events.json'), 'w', encoding='utf-8', newline='\n') as f:
    f.write(json.dumps(dialog, ensure_ascii=False, indent=2) + '\n')
w('lobby/ev/menu', ['# Admin : fenêtre des événements du lobby, sinon menu texte', 'scoreboard players set $dlg mg.st 0',
                   'execute store success score $dlg mg.st run dialog show @s mg:lobby_events',
                   'execute unless score $dlg mg.st matches 1 run function mg:lobby/ev/menu_chat'])
w('lobby/ev/menu_chat', ['# Menu texte des événements du lobby (@s = admin)',
                        'tellraw @s {"text":"🎉 Événements du lobby","color":"light_purple","bold":true}'] +
  [f'tellraw @s ["",{js({"text": " [" + t + "]", "color": c, "click_event": {"action": "run_command", "command": f"trigger mg.opt set {o}"}, "hover_event": {"action": "show_text", "value": tip}})}]'
   for t, c, o, tip in EV_BTN])
C.patch('core/opt', 'execute if score @s mg.opt matches 62..65 run function mg:tpg/run', [
    f'execute if score @s mg.opt matches {EV_OPT}..{EV_OPT + 5} unless entity @s[tag=mg.admin] run tellraw @s {{"text":"⚠ Réservé aux admins.","color":"red"}}',
    f'execute if score @s mg.opt matches {EV_OPT} if entity @s[tag=mg.admin] run function mg:lobby/ev/menu',
    f'execute if score @s mg.opt matches {EV_OPT + 1} if entity @s[tag=mg.admin] run function mg:lobby/ev/force'] +
    [f'execute if score @s mg.opt matches {EV_OPT + 1 + k} if entity @s[tag=mg.admin] run function mg:lobby/ev/force_{k}' for k in NAMES] +
    [f'execute if score @s mg.opt matches {EV_OPT + 5} if entity @s[tag=mg.admin] run function mg:lobby/ev/cancel'])

w('lobby/ev/start', [f'scoreboard players set $evn mg.st {EVERY}', 'scoreboard players operation $evon mg.st = $evk mg.st',
                     'scoreboard players reset $evk mg.st', f'scoreboard players set $evt mg.st {LEN}',
                     f'bossbar set mg:ev max {LEN}', 'bossbar set mg:ev style progress', f'bossbar set mg:ev players {L}',
                     'scoreboard players reset * mg.evd', 'scoreboard players reset * mg.evc',
                     f'execute as {L} at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 1 1.2'] +
  [f'execute if score $evon mg.st matches {k} run function mg:lobby/ev/e{k}_start' for k in NAMES])

w('lobby/ev/run', ['scoreboard players remove $evt mg.st 1', f'bossbar set mg:ev players {L}'] +
  [f'execute if score $evon mg.st matches {k} run function mg:lobby/ev/e{k}_sec' for k in NAMES] +
  ['execute if score $evon mg.st matches 1.. if score $evt mg.st matches ..0 run function mg:lobby/ev/timeup'])
w('lobby/ev/timeup', ['execute if score $evon mg.st matches 1 run function mg:lobby/ev/e1_end',
                      'execute if score $evon mg.st matches 2 run function mg:lobby/ev/e2_end',
                      'execute if score $evon mg.st matches 3 run tellraw @a {"text":"🗝 Personne n\'a trouvé le trésor... il a disparu !","color":"gray"}',
                      'function mg:lobby/ev/stop'])
w('lobby/ev/stop', ['# Fin (ou partie lancée) : tout ce que l\'événement a posé disparaît',
                    'scoreboard players set $evon mg.st 0', 'bossbar remove mg:ev',
                    'kill @e[tag=mg.evx]', f'clear @a minecraft:gold_nugget{EVI}', f'clear @a minecraft:gold_ingot{EVI}',
                    f'clear @a minecraft:iron_sword{EVI}'])
w('lobby/ev/win', ['# @s : gagnant de l\'événement',
                   'scoreboard players add @s mg.evw 1',
                   'item replace entity @s armor.head with minecraft:golden_helmet[minecraft:item_name={"text":"👑 Couronne de champion","color":"gold","bold":true},'
                   'minecraft:enchantment_glint_override=true,minecraft:unbreakable={},minecraft:custom_data={mg_ev:1b}]',
                   'tellraw @a ' + js([{'text': '🏆 ', 'color': 'gold'}, {'selector': '@s', 'color': 'yellow', 'bold': True},
                                       {'text': ' remporte l\'événement ! (', 'color': 'gold'}, {'score': {'name': '@s', 'objective': 'mg.evw'}, 'color': 'yellow'},
                                       {'text': ' victoire(s) d\'événement)', 'color': 'gold'}]),
                   'title @s title {"text":"🏆 Champion !","color":"gold","bold":true}',
                   'execute at @s run summon minecraft:firework_rocket ~ ~1 ~ {LifeTime:20,FireworksItem:{id:"minecraft:firework_rocket",count:1,components:{"minecraft:fireworks":{flight_duration:1,explosions:[{shape:"star",colors:[I;16766720,16777215],has_twinkle:true}]}}}}',
                   'execute at @s run summon minecraft:firework_rocket ~ ~1 ~ {LifeTime:30,FireworksItem:{id:"minecraft:firework_rocket",count:1,components:{"minecraft:fireworks":{flight_duration:2,explosions:[{shape:"large_ball",colors:[I;16711680,65535],has_trail:true}]}}}}',
                   'execute as @a[tag=!mg.surv] at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 1 1'])

# ---------------------------------------------------------------- 👑 Roi Zombie
SWORD = ('minecraft:iron_sword[minecraft:item_name={"text":"⚔ Épée du spawn","color":"red"},minecraft:unbreakable={},'
         'minecraft:custom_data={mg_ev:1b}]')
w('lobby/ev/e1_start', ['execute store result storage mg:ev hp int 120 if entity @a[tag=mg.evl]',
                        'execute store result score $evhp mg.st run data get storage mg:ev hp',
                        'execute if score $evhp mg.st matches ..199 run data modify storage mg:ev hp set value 200',
                        'execute if score $evhp mg.st matches 1001.. run data modify storage mg:ev hp set value 1000',
                        'execute in minecraft:overworld run function mg:lobby/ev/e1_summon with storage mg:ev',
                        f'give {L} {SWORD}',
                        'bossbar set mg:ev color red',
                        f'title {L} title {{"text":"👑 LE ROI ZOMBIE","color":"red","bold":true}}',
                        f'title {L} subtitle {{"text":"Prends l\'épée et tape-le !","color":"gray"}}',
                        f'execute as {L} at @s run playsound minecraft:entity.wither.spawn master @s ~ ~ ~ 0.7 1.3'])
w('lobby/ev/e1_summon', ['$summon minecraft:husk 0 65 6 {Tags:["mg.evx","mg.evb","mg.mob"],PersistenceRequired:1b,Glowing:1b,Health:$(hp)f,'
                         'CustomName:{"text":"👑 Roi Zombie","color":"red","bold":true},CustomNameVisible:1b,'
                         'equipment:{head:{id:"minecraft:golden_helmet",count:1},mainhand:{id:"minecraft:golden_axe",count:1}},drop_chances:{head:0f,mainhand:0f},'
                         'attributes:[{id:"minecraft:scale",base:3.5},{id:"minecraft:max_health",base:$(hp)},{id:"minecraft:attack_damage",base:3},'
                         '{id:"minecraft:movement_speed",base:0.22},{id:"minecraft:knockback_resistance",base:1},{id:"minecraft:follow_range",base:48}]}',
                         '$bossbar set mg:ev max $(hp)'])
w('lobby/ev/e1_tick', ['execute as @e[type=minecraft:husk,tag=mg.evx] at @s if entity @s[y=-64,dy=110] run tp @s 0 66 6'])
w('lobby/ev/e1_sec', ['execute unless entity @e[tag=mg.evb] run return run function mg:lobby/ev/e1_dead',
                      'bossbar set mg:ev name [{"text":"👑 Roi Zombie","color":"red","bold":true},{"text":"  (tape-le !)","color":"gray"}]',
                      'execute store result bossbar mg:ev value run data get entity @e[tag=mg.evb,limit=1] Health',
                      'scoreboard players operation $evm mg.st = $evt mg.st', 'scoreboard players operation $evm mg.st %= #ev10 mg.st',
                      'execute if score $evm mg.st matches 0 if score $evt mg.st matches 1..170 at @e[tag=mg.evb,limit=1] run function mg:lobby/ev/e1_minions'])
w('lobby/ev/e1_minions', ['execute if entity @e[type=minecraft:husk,tag=mg.evm,limit=6] run return 0',
                          'summon minecraft:husk ~1 ~ ~ {Tags:["mg.evx","mg.evm","mg.mob"],IsBaby:1b,PersistenceRequired:1b,attributes:[{id:"minecraft:attack_damage",base:1}]}',
                          'summon minecraft:husk ~-1 ~ ~ {Tags:["mg.evx","mg.evm","mg.mob"],IsBaby:1b,PersistenceRequired:1b,attributes:[{id:"minecraft:attack_damage",base:1}]}',
                          'playsound minecraft:entity.zombie.ambient hostile @a ~ ~ ~ 2 0.5',
                          'particle minecraft:large_smoke ~ ~2 ~ 1 1 1 0.05 30'])
w('lobby/ev/e1_dead', ['tellraw @a {"text":"👑 Le Roi Zombie est tombé !","color":"red","bold":true}',
                       'function mg:lobby/ev/e1_end', 'function mg:lobby/ev/stop'])
w('lobby/ev/e1_end', ['execute if entity @e[tag=mg.evb] run tellraw @a {"text":"👑 Le Roi Zombie retourne dans son trou...","color":"gray"}',
                      'scoreboard players set $evbest mg.st 0', f'execute as {L} run scoreboard players operation $evbest mg.st > @s mg.evd',
                      f'execute if score $evbest mg.st matches 1.. as {L} if score @s mg.evd = $evbest mg.st run tag @s add mg.evwin',
                      'execute as @a[tag=mg.evwin,limit=1,sort=random] run function mg:lobby/ev/win', 'tag @a remove mg.evwin'])

# ---------------------------------------------------------------- 💰 Pluie de pièces (60 s), habillée selon $theme
def coin(n, model):
    comps = '"minecraft:custom_data":{mg_ev:1b},"minecraft:item_name":' + js({'text': n, 'color': 'gold'})
    return 'components:{' + comps + (f',"minecraft:item_model":"{model}"' if model else '') + '}'


SK = list(E2_SKINS.values())
w('lobby/ev/e2_start', ['scoreboard players set $evt mg.st 60', 'bossbar set mg:ev max 60'] +
  [f'execute {s[0]} run bossbar set mg:ev color {"red" if s[2] == "red" else "yellow"}' for s in SK] +
  [f'execute {s[0]} run title {L} title ' + js({'text': s[1].upper(), 'color': s[2], 'bold': True}) for s in SK] +
  [f'title {L} subtitle {{"text":"Ramasse tout ce qui tombe !","color":"gray"}}'])
w('lobby/ev/e2_sec', [f'execute {s[0]} run bossbar set mg:ev name ' + js({'text': s[1], 'color': s[2], 'bold': True}) for s in SK] +
  ['execute store result bossbar mg:ev value run scoreboard players get $evt mg.st'] +
  ['execute in minecraft:overworld run function mg:lobby/ev/e2_coin'] * 6 +
  [f'execute as {L} run function mg:lobby/ev/e2_count'])
w('lobby/ev/e2_coin', ['summon minecraft:marker 0 64 0 {Tags:["mg.evx","mg.evp"]}',
                       'spreadplayers 0 0 0 40 under 85 false @e[type=minecraft:marker,tag=mg.evp]',
                       'execute store result score $evr mg.st run random value 1..8'] +
  [f'execute {s[0]} at @e[type=minecraft:marker,tag=mg.evp] if score $evr mg.st matches 1 run summon minecraft:item ~ ~14 ~ '
   '{Tags:["mg.evx","mg.keep"],Glowing:1b,Item:{id:"minecraft:gold_ingot",count:1,' + coin(*s[5]) + '}}' for s in SK] +
  [f'execute {s[0]} at @e[type=minecraft:marker,tag=mg.evp] unless score $evr mg.st matches 1 run summon minecraft:item ~ ~14 ~ '
   '{Tags:["mg.evx","mg.keep"],Item:{id:"minecraft:gold_nugget",count:1,' + coin(*s[4]) + '}}' for s in SK] +
  [f'execute {s[0]} at @e[type=minecraft:marker,tag=mg.evp] run particle minecraft:{s[7]} ~ ~14 ~ 0.3 0.3 0.3 0 5' for s in SK] +
  ['kill @e[type=minecraft:marker,tag=mg.evp]'])
w('lobby/ev/e2_count', [f'execute store result score @s mg.evc run clear @s minecraft:gold_nugget{EVI} 0',
                        f'execute store result score #evi mg.st run clear @s minecraft:gold_ingot{EVI} 0',
                        'scoreboard players operation #evi mg.st *= #ev5 mg.st', 'scoreboard players operation @s mg.evc += #evi mg.st'] +
  [f'execute {s[0]} run title @s actionbar ' + js([{'text': s[1].split()[0] + ' ', 'color': 'gold'}, {'score': {'name': '@s', 'objective': 'mg.evc'}, 'color': 'yellow', 'bold': True},
                                                   {'text': ' ' + s[6], 'color': 'gold'}]) for s in SK])
w('lobby/ev/e2_end', [f'execute as {L} run function mg:lobby/ev/e2_count',
                      'scoreboard players set $evbest mg.st 0', f'execute as {L} run scoreboard players operation $evbest mg.st > @s mg.evc',
                      f'execute if score $evbest mg.st matches 1.. as {L} if score @s mg.evc = $evbest mg.st run tag @s add mg.evwin'] +
  [f'execute {s[0]} as @a[tag=mg.evwin,limit=1,sort=random] run tellraw @a ' + js([{'text': s[8], 'color': 'gold'}, {'selector': '@s', 'color': 'yellow'}, {'text': ' (', 'color': 'gray'},
                                                                                   {'score': {'name': '$evbest', 'objective': 'mg.st'}, 'color': 'yellow'}, {'text': ' ' + s[6] + ')', 'color': 'gray'}]) for s in SK] +
  ['execute as @a[tag=mg.evwin,limit=1,sort=random] run function mg:lobby/ev/win', 'tag @a remove mg.evwin'])

# ---------------------------------------------------------------- 🗝 Chasse au trésor
w('lobby/ev/e3_start', ['bossbar set mg:ev color blue',
                        'execute in minecraft:overworld run summon minecraft:marker 0 64 0 {Tags:["mg.evx","mg.evt"]}',
                        'execute in minecraft:overworld run spreadplayers 0 0 0 45 under 75 false @e[type=minecraft:marker,tag=mg.evt]',
                        'execute in minecraft:overworld at @e[type=minecraft:marker,tag=mg.evt] align xz positioned ~0.5 ~ ~0.5 run function mg:lobby/ev/e3_place',
                        f'title {L} title {{"text":"🗝 CHASSE AU TRÉSOR","color":"aqua","bold":true}}',
                        f'title {L} subtitle {{"text":"Un coffre est caché sur l\'île","color":"gray"}}'])
w('lobby/ev/e3_place', ['summon minecraft:item_display ~ ~0.5 ~ {Tags:["mg.evx","mg.evtc"],item:{id:"minecraft:chest",count:1},item_display:"none"}',
                        'summon minecraft:interaction ~ ~ ~ {Tags:["mg.evx","mg.evti"],width:1.1f,height:1.1f,response:1b}'])
w('lobby/ev/e3_sec', ['bossbar set mg:ev name {"text":"🗝 Chasse au trésor","color":"aqua","bold":true}',
                      'execute store result bossbar mg:ev value run scoreboard players get $evt mg.st',
                      f'execute as {L} run title @s actionbar {{"text":"❄ Froid","color":"blue"}}',
                      f'execute at @e[type=minecraft:marker,tag=mg.evt] as @a[tag=mg.evl,distance=..45] run title @s actionbar {{"text":"🌡 Tiède","color":"yellow"}}',
                      f'execute at @e[type=minecraft:marker,tag=mg.evt] as @a[tag=mg.evl,distance=..22] run title @s actionbar {{"text":"🔥 Chaud !","color":"gold"}}',
                      f'execute at @e[type=minecraft:marker,tag=mg.evt] as @a[tag=mg.evl,distance=..9] run title @s actionbar {{"text":"🔥🔥 Brûlant !!","color":"red","bold":true}}',
                      'execute if score $evt mg.st matches 90 run data merge entity @e[type=minecraft:item_display,tag=mg.evtc,limit=1] {Glowing:1b,glow_color_override:16766720}',
                      'execute if score $evt mg.st matches 90 run tellraw @a[tag=mg.evl] {"text":"🗝 Indice : le coffre brille maintenant !","color":"aqua"}',
                      'execute if score $evt mg.st matches 45 at @e[type=minecraft:marker,tag=mg.evt] run summon minecraft:firework_rocket ~ ~1 ~ {LifeTime:25,FireworksItem:{id:"minecraft:firework_rocket",count:1,components:{"minecraft:fireworks":{flight_duration:2,explosions:[{shape:"burst",colors:[I;65535]}]}}}}',
                      'execute if score $evt mg.st matches 45 run tellraw @a[tag=mg.evl] {"text":"🗝 Indice : regarde la fusée !","color":"aqua"}',
                      'execute at @e[type=minecraft:marker,tag=mg.evt] run particle minecraft:end_rod ~ ~0.5 ~ 0.3 0.3 0.3 0.01 2'])
w('lobby/ev/e3_click', ['# @s : le coffre, quelqu\'un a cliqué', 'execute on target if entity @s[tag=mg.evl] run tag @s add mg.evwin',
                        'data remove entity @s interaction',
                        'execute unless entity @a[tag=mg.evwin] run return 0',
                        'tellraw @a [{"text":"🗝 ","color":"aqua"},{"selector":"@a[tag=mg.evwin,limit=1]","color":"yellow"},{"text":" a trouvé le trésor !","color":"aqua"}]',
                        'execute at @s run particle minecraft:totem_of_undying ~ ~0.5 ~ 0.4 0.4 0.4 0.4 60',
                        'execute as @a[tag=mg.evwin,limit=1] run function mg:lobby/ev/win', 'tag @a remove mg.evwin',
                        'function mg:lobby/ev/stop'])

# ---------------------------------------------------------------- câblage
C.objectives([('mg.evd', 'minecraft.custom:minecraft.damage_dealt'), ('mg.evc', 'dummy'), ('mg.evw', 'dummy')])
C.patch('core/load', 'scoreboard objectives add mg.evw dummy', ['scoreboard players set #ev5 mg.st 5', 'scoreboard players set #ev10 mg.st 10'])
C.patch('core/tick', 'execute if score $setup mg.st matches 1 run function mg:lobby/armory_tick',
        ['execute if score $setup mg.st matches 1 run function mg:lobby/ev/tick'])
print('ok')

# Les notes des joueurs remplacent les étoiles dans les menus : à refaire après chaque régénération des menus
import runpy
runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rating', 'gen_rating.py'), run_name='__main__')
