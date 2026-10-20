"""🔪 Murder Mystery — id 227. Un tueur caché, un détective armé, des innocents. Joue sur les 4 cartes de Prop Hunt.

    python tools/arcade/gen_murder.py .

- Rôles secrets : 1 tueur (couteau = un coup, après 10 s), 1 détective (arc, une flèche toutes les 5 s), le reste innocents.
  À 2 joueurs : tueur contre détective. Seul : entraînement (détective, ramasse l'or, tire), pas de victoire.
- Les pièces d'or apparaissent dans la carte : 10 pièces → un arc (ou une flèche si on en a déjà un).
- Le détective (ou tout porteur d'arc) meurt → l'arc tombe là où il est mort, brillant ; un innocent peut le ramasser.
- Tuer un innocent quand on n'est pas le tueur = éliminé aussi (et l'arc tombe).
- Les innocents gagnent si le tueur meurt ou s'il en reste à la fin (4 min 30) ; le tueur gagne s'il élimine tout le monde.
  Les 45 dernières secondes, les innocents brillent (le tueur les voit à travers les murs).
"""
import sys
import common as C

C.init(sys.argv[1] if len(sys.argv) > 1 else '.')
w, js = C.w, C.js
GID = 227
KNIFE_AT = 200                # couteau du tueur après 10 s
LIMIT = 5400                  # 4 min 30
GLOW_AT = LIMIT - 900         # les 45 dernières secondes
GOLD_EVERY, GOLD_MAX, GOLD_BOW = 60, 14, 10
ARROW_CD = 100
# cartes de Prop Hunt (tools/arcade/gen_prophunt.py) : (n°, nom, z, y de la cage, hauteur max d'apparition, rayon, fonction)
MAPS = [(1, '🏚 Manoir', 23600, 89, 85, 13, 'ph/build'), (2, '⚓ Entrepôt du port', 23700, 94, 90, 14, 'ph/build2'),
        (3, '🛒 Supermarché', 23800, 88, 84, 12, 'ph/build3'), (4, '🌿 Serre', 23900, 90, 87, 13, 'ph/build4')]

PL = '@a[tag=mg.play]'
INNO = '@a[tag=mg.play,tag=!mg.mmm]'
KILLER = '@a[tag=mg.play,tag=mg.mmm]'
KNIFE = ('minecraft:iron_sword[unbreakable={},custom_data={mg_mmk:1b},custom_name={"text":"🔪 Couteau","color":"red","italic":false},'
         'attribute_modifiers=[{type:"minecraft:attack_damage",id:"mg:mmk",amount:50.0,operation:"add_value",slot:"mainhand"},'
         '{type:"minecraft:attack_speed",id:"mg:mmks",amount:100.0,operation:"add_value",slot:"mainhand"}]]')
# use_cooldown = ARROW_CD : la flèche achetée avec l'or attend la fin du verrou vanilla de l'arc (<= 5 s) avant de pouvoir tirer
BOW = f'minecraft:bow[unbreakable={{}},use_cooldown={{seconds:{ARROW_CD / 20:g}f,cooldown_group:"mg:mmbow"}},custom_data={{mg_mm:1b}},custom_name={{"text":"🏹 Arc du détective","color":"aqua","italic":false}}]'
BOW_ENT = ('{Tags:["mg.mmb","mg.keep"],PickupDelay:40s,Age:-32768s,Glowing:1b,Invulnerable:1b,Item:{id:"minecraft:bow",count:1,components:{'
           f'"minecraft:unbreakable":{{}},"minecraft:use_cooldown":{{seconds:{ARROW_CD / 20:g}f,cooldown_group:"mg:mmbow"}},'
           '"minecraft:custom_data":{mg_mm:1b},"minecraft:custom_name":{"text":"🏹 Arc du détective","color":"aqua","italic":false}}}}')


def per_map(fmt):
    return [f'execute if score $mmm mg.st matches {n} run ' + fmt.format(z=z, cy=cy, u=u, r=r, py=cy + 6, f=f)
            for (n, _, z, cy, u, r, f) in MAPS]


def say(sel, parts):
    return f'tellraw {sel} ' + js(parts)


# ------------------------------------------------------------------ préparation et départ
w('mm/prepare', ['# 🔪 Murder Mystery — préparation : une carte de Prop Hunt au hasard, rôles secrets',
                 'execute store result score $mmm mg.st run random value 1..4'] + per_map('function mg:{f}') + [
                 'function mg:mm/kill_all', 'scoreboard players set $px mg.st 0'] +
  per_map('scoreboard players set $py mg.st {py}') + per_map('scoreboard players set $pz mg.st {z}') + [
                 f'clear {PL}', f'effect clear {PL}', f'gamemode adventure {PL}', f'tag {PL} add mg.mmx', f'team join mg_mm {PL}',
                 'execute if score $n0 mg.st matches 2.. as @a[tag=mg.play,sort=random,limit=1] run tag @s add mg.mmm',
                 'execute as @a[tag=mg.play,tag=!mg.mmm,sort=random,limit=1] run tag @s add mg.mmd'] +
  per_map(f'spreadplayers 0 {{z}} 3 {{r}} under {{u}} false {PL}') + [f'execute as {PL} at @s run spawnpoint @s ~ ~ ~'])
w('mm/go', ['# Départ : rôles annoncés en secret ; le couteau arrive dans 10 s',
            'scoreboard players set $mmt mg.st 0', 'scoreboard players set $mmc mg.st 0', 'scoreboard players set @a mg.deaths 0',
            'scoreboard players set @a mg.mmk 0', f'scoreboard players set {PL} mg.mma 0', f'scoreboard players set {PL} mg.mmo 0',
            f'effect give {PL} minecraft:saturation infinite 0 true', 'execute as @a[tag=mg.mmd] run function mg:mm/det_kit'] +
  [f'execute if score $mmm mg.st matches {n} run ' + say(PL, [{'text': '🗺 Carte : ', 'color': 'gray'}, {'text': nm, 'color': 'aqua', 'bold': True}])
   for (n, nm, *_) in MAPS] + [
            'title @a[tag=mg.mmm] title {"text":"🔪 TUEUR","color":"red","bold":true}',
            'title @a[tag=mg.mmm] subtitle {"text":"Élimine tout le monde sans te faire prendre","color":"gray"}',
            'title @a[tag=mg.mmd] title {"text":"🏹 DÉTECTIVE","color":"aqua","bold":true}',
            'title @a[tag=mg.mmd] subtitle {"text":"Trouve le tueur et abats-le","color":"gray"}',
            'title @a[tag=mg.play,tag=!mg.mmm,tag=!mg.mmd] title {"text":"😇 INNOCENT","color":"green","bold":true}',
            'title @a[tag=mg.play,tag=!mg.mmm,tag=!mg.mmd] subtitle {"text":"Survis ; 10 pièces d\'or = un arc","color":"gray"}',
            say('@a[tag=mg.mmm]', [{'text': '🔪 Tu es le TUEUR. ', 'color': 'red', 'bold': True},
                                   {'text': 'Ton couteau arrive dans 10 s : un coup suffit. Personne ne connaît ton rôle, reste discret. '
                                            'Attention au détective et à son arc. Dans les 45 dernières secondes, les innocents brillent.', 'color': 'gray'}]),
            say('@a[tag=mg.mmd]', [{'text': '🏹 Tu es le DÉTECTIVE. ', 'color': 'aqua', 'bold': True},
                                   {'text': 'Une flèche toutes les 5 s, tir chargé = mortel. Si tu tues un innocent, tu es éliminé ! '
                                            'Si tu meurs, ton arc tombe : un innocent pourra le ramasser.', 'color': 'gray'}]),
            say('@a[tag=mg.play,tag=!mg.mmm,tag=!mg.mmd]', [{'text': '😇 Tu es INNOCENT. ', 'color': 'green', 'bold': True},
                                                            {'text': 'Survis jusqu\'à la fin. Ramasse 10 pièces d\'or pour un arc, ou récupère celui du détective s\'il tombe. '
                                                                     'Tuer un innocent = éliminé.', 'color': 'gray'}]),
            'execute unless score $n0 mg.st matches 2.. run ' + say(PL, [{'text': '🔪 Mode entraînement (seul) : tu es détective, entraîne-toi au tir et '
                                                                                   'ramasse l\'or. Pas de victoire ; il faut au moins 2 joueurs pour une vraie partie.', 'color': 'yellow'}])])
w('mm/det_kit', ['# @s : détective', f'item replace entity @s hotbar.1 with {BOW}', 'item replace entity @s hotbar.2 with minecraft:arrow'])
w('mm/knife', ['# 10 s : le tueur est armé', 'execute as @a[tag=mg.play,tag=mg.mmm] run function mg:mm/knife_give',
               'title @a[tag=mg.mmm] actionbar {"text":"🔪 Tu as ton couteau !","color":"red","bold":true}',
               say(PL, [{'text': '🔪 Le tueur est armé… méfiez-vous de tout le monde.', 'color': 'red'}]),
               f'execute as {PL} at @s run playsound minecraft:entity.wither.ambient master @s ~ ~ ~ 0.4 1.6'])
w('mm/knife_give', [f'give @s {KNIFE}'])

# ------------------------------------------------------------------ arc, flèches, or
w('mm/arrow', ['# @s : flèche rechargée', 'give @s minecraft:arrow 1', 'scoreboard players set @s mg.mma 0',
               'execute at @s run playsound minecraft:item.crossbow.loading_end player @s ~ ~ ~ 0.6 1.2'])
w('mm/drop_here', ['# @s : son arc tombe à ses pieds', 'clear @s minecraft:bow', 'clear @s minecraft:arrow',
                   f'execute at @s run summon minecraft:item ~ ~1 ~ {BOW_ENT}', 'function mg:mm/bow_news'])
w('mm/drop_death', ['# @s vient de mourir : son arc tombe là où il est mort', 'data modify storage mg:mm d set value {x:0,y:0,z:0}',
                    'execute store result storage mg:mm d.x int 1 run data get entity @s LastDeathLocation.pos[0]',
                    'execute store result storage mg:mm d.y int 1 run data get entity @s LastDeathLocation.pos[1]',
                    'execute store result storage mg:mm d.z int 1 run data get entity @s LastDeathLocation.pos[2]',
                    'clear @s minecraft:bow', 'clear @s minecraft:arrow', 'function mg:mm/drop_at with storage mg:mm d', 'function mg:mm/bow_news'])
w('mm/drop_at', ['# Arc à la position de la mort (macro : $(x) $(y) $(z))', f'$summon minecraft:item $(x).5 $(y).5 $(z).5 {BOW_ENT}'])
w('mm/bow_news', [say('@a[tag=mg.mmx]', [{'text': '🏹 L\'arc est tombé ! ', 'color': 'aqua', 'bold': True},
                                          {'text': 'Il brille : le premier innocent qui le ramasse peut abattre le tueur.', 'color': 'gray'}]),
                  'execute as @a[tag=mg.mmx] at @s run playsound minecraft:block.bell.use master @s ~ ~ ~ 0.6 0.8'])
w('mm/gold_spawn', ['# Une pièce d\'or au hasard dans la carte (14 au plus)',
                    'execute store result score $mmq mg.st if entity @e[type=minecraft:item,tag=mg.mmg]',
                    f'execute if score $mmq mg.st matches {GOLD_MAX}.. run return 0'] +
  per_map('summon minecraft:marker 0 {u} {z} {{Tags:["mg.mmp"]}}') +
  per_map('spreadplayers 0 {z} 0 {r} under {u} false @e[type=minecraft:marker,tag=mg.mmp]') + [
                    'execute at @e[type=minecraft:marker,tag=mg.mmp] run summon minecraft:item ~ ~0.3 ~ {Tags:["mg.mmg","mg.keep"],Age:-32768s,'
                    'Item:{id:"minecraft:gold_ingot",count:1,components:{"minecraft:custom_name":{"text":"🪙 Pièce d\'or","color":"gold","italic":false}}}}',
                    'kill @e[type=minecraft:marker,tag=mg.mmp]'])
w('mm/gold', ['# @s (innocent) : compte ses pièces d\'or', 'execute store result score @s mg.mmo run clear @s minecraft:gold_ingot 0',
              f'execute if score @s mg.mmo matches {GOLD_BOW}.. run function mg:mm/gold_bow'])
w('mm/gold_bow', [f'# @s : {GOLD_BOW} pièces → un arc, ou une flèche si on en a déjà un', f'clear @s minecraft:gold_ingot {GOLD_BOW}',
                  f'scoreboard players remove @s mg.mmo {GOLD_BOW}',
                  'execute at @s run playsound minecraft:entity.player.levelup player @s ~ ~ ~ 0.6 1.4',
                  'execute unless items entity @s container.* minecraft:bow run return run function mg:mm/gold_newbow',
                  'give @s minecraft:arrow 1', 'title @s actionbar {"text":"🪙 10 pièces → +1 flèche","color":"gold"}'])
w('mm/gold_newbow', [f'give @s {BOW}', 'give @s minecraft:arrow 1',
                     'title @s actionbar {"text":"🪙 10 pièces → un arc ! Ne te trompe pas de cible…","color":"gold","bold":true}'])

# ------------------------------------------------------------------ morts
w('mm/hero', ['# @s a abattu le tueur', 'tag @s add mg.mmhero', 'scoreboard players set @s mg.mmk 0',
              say('@a[tag=mg.mmx]', [{'text': '🏹 ', 'color': 'aqua'}, {'selector': '@s', 'color': 'aqua', 'bold': True},
                                     {'text': ' a abattu le tueur !', 'color': 'gray'}])])
w('mm/bad_kill', ['# @s (pas le tueur) a tué un innocent : il est éliminé aussi',
                  say('@s', [{'text': '🔪 Tu as tué un innocent… et tu le paies de ta vie !', 'color': 'red'}]),
                  'execute if items entity @s container.* minecraft:bow run function mg:mm/drop_here',
                  'clear @s', 'effect clear @s minecraft:glowing', 'function mg:core/eliminate'])
w('mm/die', ['# @s est mort : son arc tombe, puis il est éliminé (seul : il continue)',
             'execute unless score $n0 mg.st matches 2.. run return run scoreboard players set @s mg.deaths 0',
             'execute if items entity @s container.* minecraft:bow run function mg:mm/drop_death',
             'clear @s', 'effect clear @s minecraft:glowing', 'function mg:core/eliminate'])
w('mm/bow_spit', ['# @s (tueur) a ramassé l\'arc : il retombe', 'function mg:mm/drop_here',
                  'title @s actionbar {"text":"🔪 Le tueur ne peut pas porter l\'arc","color":"red"}'])
w('mm/glow', ['# 45 dernières secondes : les innocents brillent', f'effect give {INNO} minecraft:glowing infinite 0 true',
              say(PL, [{'text': '⏳ 45 secondes ! ', 'color': 'gold', 'bold': True}, {'text': 'Les innocents brillent : le tueur les voit à travers les murs.', 'color': 'gray'}])])

# ------------------------------------------------------------------ tick
w('mm/tick', ['# 🔪 Murder Mystery — tick', 'scoreboard players add $mmt mg.st 1',
              f'execute if score $n0 mg.st matches 2.. if score $mmt mg.st matches {KNIFE_AT} run function mg:mm/knife',
              '# couteau : au tueur seulement ; arc : jamais au tueur',
              f'clear {INNO} minecraft:iron_sword', 'execute as @e[type=minecraft:item] if items entity @s contents minecraft:iron_sword run kill @s',
              f'execute if score $mmt mg.st matches {KNIFE_AT + 1}.. as {KILLER} unless items entity @s container.* minecraft:iron_sword run function mg:mm/knife_give',
              f'execute as {KILLER} if items entity @s container.* minecraft:bow run function mg:mm/bow_spit',
              f'clear {KILLER} minecraft:arrow', f'clear {KILLER} minecraft:gold_ingot',
              '# flèches : un tir chargé tue, pas de ramassage',
              'execute as @e[type=minecraft:arrow,tag=!mg.mmar] run data merge entity @s {damage:20.0d,pickup:0b,Tags:["mg.mmar"]}',
              f'execute as {INNO} if items entity @s container.* minecraft:bow unless items entity @s container.* minecraft:arrow run scoreboard players add @s mg.mma 1',
              f'execute as @a[tag=mg.play,scores={{mg.mma={ARROW_CD}..}}] run function mg:mm/arrow',
              '# or',
              f'scoreboard players operation $mmq mg.st = $mmt mg.st', f'scoreboard players set #{GOLD_EVERY} mg.st {GOLD_EVERY}',
              f'scoreboard players operation $mmq mg.st %= #{GOLD_EVERY} mg.st',
              'execute if score $mmq mg.st matches 0 run function mg:mm/gold_spawn',
              f'execute as {INNO} run function mg:mm/gold',
              '# morts : le tueur abattu → héros ; un innocent qui tue un innocent → éliminé',
              f'execute as @a[tag=mg.mmm] run scoreboard players operation $mmc mg.st += @s mg.mmk',
              f'execute if entity @a[tag=mg.play,tag=mg.mmm,scores={{mg.deaths=1..}}] as @a[tag=mg.play,tag=!mg.mmm,scores={{mg.mmk=1..}}] run function mg:mm/hero',
              'execute if score $n0 mg.st matches 2.. as @a[tag=mg.play,tag=!mg.mmm,scores={mg.mmk=1..,mg.deaths=0}] run function mg:mm/bad_kill',
              f'execute as @a[tag=mg.play,scores={{mg.deaths=1..}}] run function mg:mm/die',
              'scoreboard players set @a[tag=mg.mmx] mg.mmk 0',
              f'execute if score $n0 mg.st matches 2.. if score $mmt mg.st matches {GLOW_AT} run function mg:mm/glow',
              'scoreboard players operation $mmq mg.st = $mmt mg.st', 'scoreboard players set #20 mg.st 20', 'scoreboard players operation $mmq mg.st %= #20 mg.st',
              f'execute store result score $mmn mg.st if entity {INNO}', f'execute store result score $mmk mg.st if entity {KILLER}',
              'execute if score $mmq mg.st matches 0 run function mg:mm/second',
              'execute if score $state mg.st matches 2 if score $n0 mg.st matches 2.. if score $mmk mg.st matches 0 run return run function mg:mm/innocents_win',
              'execute if score $state mg.st matches 2 if score $n0 mg.st matches 2.. if score $mmn mg.st matches 0 run return run function mg:mm/murderer_win',
              f'execute if score $state mg.st matches 2 if score $mmt mg.st matches {LIMIT}.. run function mg:mm/timeout'])
w('mm/second', [f'scoreboard players set $mml mg.st {LIMIT // 20}', 'scoreboard players operation $mmq mg.st = $mmt mg.st',
                'scoreboard players operation $mmq mg.st /= #20 mg.st', 'scoreboard players operation $mml mg.st -= $mmq mg.st',
                f'execute if score $mmt mg.st matches ..{KNIFE_AT} run title @a[tag=mg.mmm] actionbar {{"text":"🔪 Ton couteau arrive dans quelques secondes…","color":"red"}}',
                f'execute if score $mmt mg.st matches {KNIFE_AT + 1}.. run title {KILLER} actionbar [{{"text":"🔪 Innocents restants : ","color":"red"}},{{"score":{{"name":"$mmn","objective":"mg.st"}},"color":"yellow","bold":true}},{{"text":" — ","color":"gray"}},{{"score":{{"name":"$mml","objective":"mg.st"}},"color":"yellow"}},{{"text":" s","color":"gray"}}]',
                f'execute as {INNO} run title @s actionbar [{{"text":"🪙 Or : ","color":"gold"}},{{"score":{{"name":"@s","objective":"mg.mmo"}},"color":"yellow","bold":true}},{{"text":"/{GOLD_BOW} — ","color":"gray"}},{{"score":{{"name":"$mml","objective":"mg.st"}},"color":"yellow"}},{{"text":" s","color":"gray"}}]'])

# ------------------------------------------------------------------ fins
w('mm/reveal', [say('@a[tag=mg.mmx]', [{'text': '🔪 Le tueur était : ', 'color': 'red'}, {'selector': '@a[tag=mg.mmm]', 'color': 'yellow', 'bold': True},
                                        {'text': ' (', 'color': 'gray'}, {'score': {'name': '$mmc', 'objective': 'mg.st'}, 'color': 'red'},
                                        {'text': ' victime(s))', 'color': 'gray'}]),
                 'execute if entity @a[tag=mg.mmd] run ' + say('@a[tag=mg.mmx]', [{'text': '🏹 Le détective : ', 'color': 'aqua'}, {'selector': '@a[tag=mg.mmd]', 'color': 'yellow'}])])
w('mm/innocents_win', ['# Le tueur est mort, ou il reste des innocents à la fin', 'function mg:mm/reveal',
                       f'tag {INNO} add mg.win', f'scoreboard players add {INNO} mg.wins 1',
                       'scoreboard players set $state mg.st 3', 'scoreboard players set $timer mg.st 120',
                       'title @a[tag=!mg.surv] title {"text":"Les INNOCENTS gagnent !","color":"green","bold":true}',
                       'tellraw @a [{"text":"★ Victoire des innocents : ","color":"gold"},{"selector":"@a[tag=mg.play,tag=!mg.mmm]","color":"green"}]',
                       'execute as @a[tag=!mg.surv] at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 1 1'])
w('mm/murderer_win', ['# Plus aucun innocent', 'function mg:mm/reveal',
                      say('@a', [{'text': '🔪 Le tueur a éliminé tout le monde !', 'color': 'red', 'bold': True}]),
                      f'execute as {KILLER} run return run function mg:core/win_player', 'function mg:core/draw'])
w('mm/timeout', ['# Fin du temps : les survivants gagnent (seul : fin de l\'entraînement)',
                 'execute unless score $n0 mg.st matches 2.. run ' + say(PL, [{'text': '🔪 Fin de l\'entraînement.', 'color': 'yellow'}]),
                 'execute unless score $n0 mg.st matches 2.. run return run function mg:core/draw',
                 say('@a', [{'text': '⏳ Le temps est écoulé : les innocents ont survécu !', 'color': 'green'}]), 'function mg:mm/innocents_win'])
w('mm/kill_all', ['kill @e[type=minecraft:item,tag=mg.mmg]', 'kill @e[type=minecraft:item,tag=mg.mmb]',
                  'kill @e[type=minecraft:marker,tag=mg.mmp]', 'kill @e[type=minecraft:arrow,tag=mg.mmar]'])
w('mm/cleanup', ['function mg:mm/kill_all', 'effect clear @a[tag=mg.mmx] minecraft:glowing', 'team leave @a[team=mg_mm]',
                 'tag @a remove mg.mmm', 'tag @a remove mg.mmd', 'tag @a remove mg.mmhero', 'tag @a remove mg.mmx',
                 'scoreboard players reset * mg.mma', 'scoreboard players reset * mg.mmo', 'title @a reset'])

C.register([GID], 'mm', [C.announce(GID, '', '🔪 MURDER MYSTERY', 'red', 'un tueur se cache parmi vous… le détective doit le démasquer !')])
C.objectives([('mg.mmk', 'playerKillCount'), ('mg.mma', 'dummy'), ('mg.mmo', 'dummy')])
C.patch('core/load', 'scoreboard objectives add mg.bw trigger', ['team add mg_mm', 'team modify mg_mm nametagVisibility never', 'team modify mg_mm deathMessageVisibility never',
                                                                 'team modify mg_mm collisionRule never', 'team modify mg_mm friendlyFire true'])
C.patch('desinstaller', 'scoreboard objectives remove mg.bw', ['team remove mg_mm', 'data remove storage mg:mm d'])
print('Murder Mystery OK')

# pas de morts ni d'éliminations dans le chat pendant la partie (les joueurs ne doivent pas savoir qui est tombé)
_el = C.lines_of('core/eliminate')
_old = 'tellraw @a [{"selector":"@s","color":"red"},{"text":" est éliminé !","color":"gray"}]'
if _old in _el:
    i = _el.index(_old)
    _el[i:i + 1] = [f'execute unless score $game mg.st matches {GID} run ' + _old,
                    f'execute if score $game mg.st matches {GID} run tellraw @s {{"text":"☠ Tu es éliminé : tu regardes la suite en silence.","color":"gray"}}']
    C.w('core/eliminate', _el[:-1] if _el[-1] == '' else _el)

