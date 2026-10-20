# Terra Nova : dinosaures (exec de tv_dino_fn.py inclus) et armes ; exécuté par gen_terranova.py (exec), à la place exacte de ce bloc.
# Tranche contiguë de l'ancien gen_terranova.py : mêmes globals que la façade, aucun import, aucune copie de w/js/patch.
# Utilise : SPAWN, __file__, js, os, part, w

# ================================================================ dinosaures
INVIS = 'active_effects:[{id:"minecraft:invisibility",duration:-1,amplifier:0,show_particles:0b}]'


def attrs(**a):
    names = {'hp': 'max_health', 'spd': 'movement_speed', 'fol': 'follow_range', 'dmg': 'attack_damage', 'scale': 'scale',
             'step': 'step_height', 'kb': 'knockback_resistance', 'akb': 'attack_knockback', 'jump': 'jump_strength', 'armor': 'armor'}
    return 'attributes:[' + ','.join(f'{{id:"minecraft:{names[k]}",base:{v}}}' for k, v in a.items()) + ']'


TVD = dict(globals())
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tv_dino_fn.py'), encoding='utf-8').read(), TVD)
w('terra/pack', ['# Meute de 2 ou 3 slashers ici, lancée sur le colon le plus proche hors de la colonie',
                 'tag @e[tag=mg.tvpk] remove mg.tvpk', 'execute store result score $tvn mg.st run random value 2..4', 'function mg:terra/pack_one',
                 'execute as @e[tag=mg.tvpk] at @s run damage @s 0.01 minecraft:generic by @p[tag=mg.tvout,gamemode=adventure,distance=..70]',
                 'tag @e[tag=mg.tvpk] remove mg.tvpk'])
w('terra/pack_one', ['function mg:terra/dino/raptor', 'tag @e[tag=mg.tvlast] add mg.tvpk', 'scoreboard players remove $tvn mg.st 1',
                     'execute if score $tvn mg.st matches 1.. run function mg:terra/pack_one'])
w('terra/pack_try', ['# Une meute sur un point d\'apparition entre 24 et 64 blocs d\'un colon (aucun à moins de 22)',
                     'scoreboard players set $tvpk mg.st 5', 'tag @e[tag=mg.trok] remove mg.trok',
                     'execute as @e[type=minecraft:marker,tag=mg.tvsp] at @s if entity @a[tag=mg.tvout,gamemode=adventure,distance=24..64] unless entity @a[tag=mg.tvw,distance=..22] run tag @s add mg.trok',
                     '# un seul point tiré parmi les points possibles (une condition « if score » serait évaluée pour tous avant la première apparition)',
                     'execute as @e[tag=mg.trok,sort=random,limit=1] at @s run function mg:terra/pack_at', 'tag @e[tag=mg.trok] remove mg.trok'])
w('terra/pack_at', ['scoreboard players set $tvf mg.st 1', 'function mg:terra/pack'])
w('terra/carno_try', ['# Une chance sur 90 par seconde : un carnotaure sauvage apparaît loin des colons',
                      'execute store result score $tvr mg.st run random value 0..89', 'execute unless score $tvr mg.st matches 0 run return 0',
                      'tag @e[tag=mg.trok] remove mg.trok',
                      'execute as @e[type=minecraft:marker,tag=mg.tvsp] at @s if entity @a[tag=mg.tvout,gamemode=adventure,distance=36..80] unless entity @a[tag=mg.tvw,distance=..30] run tag @s add mg.trok',
                      'execute as @e[tag=mg.trok,sort=random,limit=1] at @s run function mg:terra/carno_at', 'tag @e[tag=mg.trok] remove mg.trok'])
w('terra/carno_at', ['scoreboard players set $tvf mg.st 1', 'scoreboard players set $tvcc mg.st 240', 'function mg:terra/dino/carno',
                     'tellraw @a[tag=mg.tvw] {"text":"🦖 Un rugissement résonne dans la jungle… un carnotaure rôde.","color":"red"}',
                     'execute as @a[tag=mg.tvw] at @s run playsound minecraft:entity.ravager.roar hostile @s ~ ~ ~ 0.6 0.55'])
w('terra/brach_saddle', ['# @s : brachiosaure monté sans selle → sellé (sinon on ne peut pas le diriger)',
                         'item replace entity @s saddle with minecraft:saddle',
                         'execute on passengers run title @s actionbar ' + js({'text': '🦕 Brachiosaure sellé : Z/Q/S/D pour le diriger, espace = élan', 'color': 'yellow'})])
w('terra/herb_fill', ['# Toutes les 20 s : 3 brachiosaures et 4 pachycéphalosaures dans la jungle',
                      'execute store result score $tvn mg.st if entity @e[tag=mg.tvbrach]',
                      'execute if score $tvn mg.st matches ..2 as @e[type=minecraft:marker,tag=mg.tvhp,sort=random,limit=1] at @s unless entity @a[tag=mg.tvw,distance=..30] run function mg:terra/dino/brachio',
                      'execute store result score $tvn mg.st if entity @e[tag=mg.tvpachy]',
                      'execute if score $tvn mg.st matches ..3 as @e[type=minecraft:marker,tag=mg.tvhp,sort=random,limit=1] at @s unless entity @a[tag=mg.tvw,distance=..30] run function mg:terra/dino/pachy'])
w('terra/zap', ['# @s (prédateur entré dans la colonie) : les tourelles du périmètre le frappent et le repoussent',
                'damage @s 10 minecraft:lightning_bolt', 'particle minecraft:electric_spark ~ ~1 ~ 0.4 0.8 0.4 0.3 30',
                'playsound minecraft:entity.lightning_bolt.impact hostile @a ~ ~ ~ 0.5 1.6',
                'execute facing 0 65 0 rotated ~180 -20 positioned 0.0 0.0 0.0 summon minecraft:marker run function mg:terra/vec {d:1.2}',
                'function mg:terra/push'])
w('terra/vec', ['# Marqueur placé au bout du vecteur (contexte : origine, orientation voulue)', '$tp @s ^ ^ ^$(d)', 'tag @s add mg.tvv'])
w('terra/push', ['# @s : élan = vecteur du marqueur mg.tvv', 'data modify entity @s Motion set from entity @e[type=minecraft:marker,tag=mg.tvv,limit=1] Pos',
                 'kill @e[type=minecraft:marker,tag=mg.tvv]'])
w('terra/carno_smash', ['# @s (carnotaure) : casse les structures légères autour de lui (outposts)',
                        'execute store result score $tvb2 mg.st run fill ~-2 ~ ~-2 ~2 ~3 ~2 minecraft:air replace #mg:tv_light',
                        'execute if score $tvb2 mg.st matches 1.. run playsound minecraft:entity.zombie.break_wooden_door hostile @a ~ ~ ~ 1 0.7',
                        'execute if score $tvb2 mg.st matches 1.. run particle minecraft:block{block_state:"minecraft:oak_planks"} ~ ~1 ~ 1 1 1 0 30'])
w('terra/carno_bar', ['# @s (carnotaure) : barre de vie pour les colons proches',
                      'execute store result bossbar mg:tvcarno value run data get entity @s Health',
                      'bossbar set mg:tvcarno players @a[tag=mg.tvw,distance=..48]'])
w('terra/unnet', ['# @s : fin d\'immobilisation (filet, piège)', 'data merge entity @s {NoAI:0b}', 'tag @s remove mg.tvnetted',
                  'scoreboard players operation $tvi mg.st = @s mg.tvid',
                  'execute as @e[type=minecraft:block_display,tag=mg.tvnetd] if score @s mg.tvid = $tvi mg.st run kill @s'])
w('terra/net_on', ['# @s (dinosaure) : pris dans un filet (5 s, carnotaure 2,5 s, brachiosaure 3 s)',
                   'scoreboard players set @s mg.tvst 100', 'execute if entity @s[tag=mg.tvcarno] run scoreboard players set @s mg.tvst 50',
                   'execute if entity @s[tag=mg.tvbig] run scoreboard players set @s mg.tvst 60',
                   'data merge entity @s {NoAI:1b}', 'tag @s add mg.tvnetted', 'scoreboard players operation $tvi mg.st = @s mg.tvid',
                   'execute as @e[type=minecraft:block_display,tag=mg.tvnetd] if score @s mg.tvid = $tvi mg.st run kill @s',
                   'execute unless entity @s[tag=mg.tvcarno] unless entity @s[tag=mg.tvbig] run ' + part('"mg.tv","mg.tvp","mg.tvnetd","mg.tvn"', 'cobweb', -0.8, 0, -0.8, 1.6, 1.8, 1.6),
                   'execute if entity @s[tag=mg.tvcarno] run ' + part('"mg.tv","mg.tvp","mg.tvnetd","mg.tvn"', 'cobweb', -1.4, 0, -1.4, 2.8, 3.4, 2.8),
                   'execute if entity @s[tag=mg.tvbig] run ' + part('"mg.tv","mg.tvp","mg.tvnetd","mg.tvn"', 'cobweb', -2.0, 0, -2.0, 4.0, 5.0, 4.0),
                   'scoreboard players operation @e[tag=mg.tvn] mg.tvid = $tvi mg.st', 'tag @e[tag=mg.tvn] remove mg.tvn',
                   'playsound minecraft:block.wool.place hostile @a ~ ~ ~ 1 0.6', 'particle minecraft:block{block_state:"minecraft:cobweb"} ~ ~1 ~ 0.5 0.6 0.5 0 25'])

# ================================================================ armes
def gain(n, why, col='green'):
    return [f'scoreboard players add @s mg.tvc {n}', f'function mg:terra/rpg/xp {{n:{max(5, n // 2)}}}', 'scoreboard players set @s mg.tval 40',
            f'title @s actionbar [{{"text":"+{n} ₵ ","color":"{col}","bold":true}},{{"text":"{why}","color":"gray"}}]',
            'execute at @s run playsound minecraft:entity.experience_orb.pickup player @s ~ ~ ~ 0.6 1.2']


def say(msg, col='gray'):
    return ['scoreboard players set @s mg.tval 40', f'title @s actionbar {js({"text": msg, "color": col})}']


w('terra/use', ['# @s : clic droit avec un objet de Terra Nova',
                'execute if items entity @s weapon.mainhand *[custom_data~{tv:2}] run return run function mg:terra/fire2',
                'execute if items entity @s weapon.mainhand *[custom_data~{tv:3}] run return run function mg:terra/fire3',
                'execute if items entity @s weapon.mainhand *[custom_data~{tv:4}] run return run function mg:terra/sonic',
                'execute if items entity @s weapon.mainhand *[custom_data~{tv:5}] run return run function mg:terra/net_fire',
                'execute if items entity @s weapon.mainhand *[custom_data~{tv:6}] run return run function mg:terra/trap_use',
                'execute if items entity @s weapon.mainhand *[custom_data~{tv:9}] run return run function mg:terra/home',
                'execute if items entity @s weapon.mainhand *[custom_data~{tv:7}] run return run function mg:terra/fire7',
                'execute if items entity @s weapon.mainhand *[custom_data~{tv:8}] run return run function mg:terra/fire8',
                'execute if items entity @s weapon.mainhand *[custom_data~{tv:10}] run return run function mg:terra/rpg/scan',
                'execute if items entity @s weapon.mainhand *[custom_data~{tv:11}] run return run function mg:terra/rpg/whistle',
                'execute if items entity @s weapon.mainhand *[custom_data~{tv:14}] run return run function mg:terra/rpg/cl/use',
                'execute if items entity @s weapon.mainhand *[custom_data~{tv:15}] run return run function mg:terra/rpg/sheet'])
RCOL = {2: '0.35,0.75,1.0', 3: '1.0,0.7,0.2', 7: '0.8,0.3,1.0', 8: '1.0,1.0,0.4'}
for n, heat, cd, dmg in [(2, 140, 4, 5), (3, 90, 3, 7), (7, 60, 3, 11), (8, 45, 3, 16)]:
    w(f'terra/fire{n}', [f'# @s tire ({ {2: "fusil à impulsions", 3: "fusil Mk2", 7: "fusil à plasma Mk3", 8: "lance-foudre"}[n]}) : +{heat} de chaleur, surchauffe à 1000',
                         'execute if entity @s[tag=mg.tvoh] run return run playsound minecraft:block.dispenser.fail player @s ~ ~ ~ 0.5 1.6',
                         'execute if score @s mg.tvcd matches 1.. run return 0',
                         f'scoreboard players set @s mg.tvcd {cd}', f'scoreboard players add @s mg.tvh {heat}',
                         f'execute if score @s mg.trcl matches 1 run scoreboard players remove @s mg.tvh {heat * 3 // 10}',
                         'execute if score @s mg.tvh matches 1000.. run function mg:terra/overheat',
                         f'playsound minecraft:entity.breeze.shoot player @a ~ ~ ~ 0.7 {1.9 if n == 2 else 1.6}' if n < 8 else
                         'playsound minecraft:item.trident.thunder player @a ~ ~ ~ 0.5 1.8',
                         'scoreboard players set $tvr mg.st 0', 'tag @s add mg.tvsh',
                         f'execute anchored eyes positioned ^ ^ ^0.6 run function mg:terra/ray{n}', 'tag @s remove mg.tvsh', 'tag @e[tag=mg.tvhitn] remove mg.tvhitn'])
    w(f'terra/ray{n}', ['# Un pas (0,5 bloc) du tir à impulsions',
                        f'particle minecraft:dust{{color:[{RCOL[n]}],scale:{0.7 if n < 7 else 1.0}}} ~ ~ ~ 0 0 0 0 1 force',
                        'scoreboard players add $tvr mg.st 1',
                        f'execute positioned ~-0.5 ~-0.5 ~-0.5 as @e[tag=mg.tvtg,tag=!mg.tvhitn,dx=0,dy=0,dz=0,limit=1] positioned ~0.5 ~0.5 ~0.5 run {"" if n == 7 else "return run "}function mg:terra/hit{n}',
                        'execute unless block ~ ~ ~ #mg:tv_pass run return run particle minecraft:electric_spark ~ ~ ~ 0.1 0.1 0.1 0.2 6',
                        f'execute if score $tvr mg.st matches ..80 positioned ^ ^ ^0.5 run function mg:terra/ray{n}'])
    w(f'terra/hit{n}', ['# @s (dinosaure) touché par une impulsion' + (' (plasma : traverse)' if n == 7 else ''),
                        '# précision du tireur : +1 dégât tous les 2 points (chiffre affiché au-dessus de la cible)',
                        f'execute if entity @a[tag=mg.tvsh,scores={{mg.trs4=8..}}] run function mg:terra/hitd {{d:{dmg + 4}}}',
                        f'execute if entity @a[tag=mg.tvsh,scores={{mg.trs4=6..7}}] run function mg:terra/hitd {{d:{dmg + 3}}}',
                        f'execute if entity @a[tag=mg.tvsh,scores={{mg.trs4=4..5}}] run function mg:terra/hitd {{d:{dmg + 2}}}',
                        f'execute if entity @a[tag=mg.tvsh,scores={{mg.trs4=2..3}}] run function mg:terra/hitd {{d:{dmg + 1}}}',
                        f'execute unless entity @a[tag=mg.tvsh,scores={{mg.trs4=2..}}] run function mg:terra/hitd {{d:{dmg}}}', 'tag @s add mg.tvhitn',
                        'particle minecraft:electric_spark ~ ~1 ~ 0.3 0.6 0.3 0.5 30' if n == 8 else 'particle minecraft:crit ~ ~ ~ 0 0 0 0 1',
                        'particle minecraft:electric_spark ~ ~ ~ 0.2 0.2 0.2 0.3 10',
                        'execute as @a[tag=mg.tvsh] at @s run playsound minecraft:entity.arrow.hit_player player @s ~ ~ ~ 0.4 1.5'])
w('terra/hitd', ['# @s (cible) : dégâts du tir ($(d)) et chiffre flottant', '$damage @s $(d) minecraft:player_attack by @a[tag=mg.tvsh,limit=1]',
                 '$execute at @s run function mg:terra/rpg/dmgnum {d:$(d)}'])
w('terra/overheat', ['# @s : surchauffe, plus de tir avant refroidissement complet', 'tag @s add mg.tvoh', 'scoreboard players set @s mg.tvh 1000',
                     'playsound minecraft:block.fire.extinguish player @s ~ ~ ~ 0.8 1.2', 'scoreboard players set @s mg.tval 0'])
w('terra/cooled', ['# @s : fusil refroidi', 'tag @s remove mg.tvoh', 'playsound minecraft:block.beacon.power_select player @s ~ ~ ~ 0.4 1.8'])
w('terra/sonic', ['# @s : canon sonique, onde en cône (sphère de 4,5 blocs centrée 4 blocs devant)',
                  'execute if score @s mg.tvsc matches 1.. run return run playsound minecraft:block.dispenser.fail player @s ~ ~ ~ 0.5 1.4',
                  'scoreboard players set @s mg.tvsc 80', 'playsound minecraft:entity.warden.sonic_boom player @a ~ ~ ~ 1 1.3',
                  'execute anchored eyes positioned ^ ^ ^1.5 run particle minecraft:sonic_boom ~ ~ ~ 0 0 0 0 1 force',
                  'execute anchored eyes positioned ^ ^ ^3.5 run particle minecraft:sonic_boom ~ ~ ~ 0.4 0.3 0.4 0 2 force',
                  'execute anchored eyes positioned ^ ^ ^6 run particle minecraft:sonic_boom ~ ~ ~ 0.9 0.5 0.9 0 3 force',
                  'tag @s add mg.tvsrc',
                  'execute anchored eyes positioned ^ ^ ^4 as @e[tag=mg.tvtg,distance=..4.5] at @s run function mg:terra/sonic_hit',
                  'tag @s remove mg.tvsrc'])
w('terra/sonic_hit', ['# @s (dinosaure) pris dans l\'onde : dégâts, ralenti, repoussé (sauf les géants)',
                      'damage @s 3 minecraft:sonic_boom by @a[tag=mg.tvsrc,limit=1]', 'effect give @s minecraft:slowness 4 2 true',
                      'execute if entity @s[tag=mg.tvbig] run return 0',
                      'execute if entity @s[tag=mg.tvcarno] facing entity @a[tag=mg.tvsrc,limit=1] feet rotated ~180 -20 positioned 0.0 0.0 0.0 summon minecraft:marker run function mg:terra/vec {d:0.9}',
                      'execute unless entity @s[tag=mg.tvcarno] facing entity @a[tag=mg.tvsrc,limit=1] feet rotated ~180 -25 positioned 0.0 0.0 0.0 summon minecraft:marker run function mg:terra/vec {d:1.8}',
                      'function mg:terra/push'])
w('terra/prod_hit', ['# @s a frappé avec le bâton électrique : le dinosaure visé est étourdi',
                     'execute anchored eyes positioned ^ ^ ^1.8 as @e[tag=mg.tvtg,distance=..2.4,sort=nearest,limit=1] at @s run function mg:terra/stun'])
w('terra/stun', ['# @s (dinosaure) : étourdi 3 s', 'effect give @s minecraft:slowness 3 4 true', 'effect give @s minecraft:weakness 3 1 true',
                 'particle minecraft:electric_spark ~ ~1 ~ 0.3 0.6 0.3 0.25 25', 'playsound minecraft:item.trident.thunder player @a ~ ~ ~ 0.25 2'])
w('terra/net_fire', ['# @s : lance-filets (un filet par tir)',
                     'execute if score @s mg.tvnet matches ..0 run return run function mg:terra/no_net',
                     'scoreboard players remove @s mg.tvnet 1', 'playsound minecraft:entity.fishing_bobber.throw player @a ~ ~ ~ 1 0.6',
                     'scoreboard players set $tvr mg.st 0', 'execute anchored eyes positioned ^ ^ ^0.6 run function mg:terra/net_ray'])
w('terra/no_net', say('🕸 Plus de filets : achète-en au dépôt de la colonie', 'red') + ['playsound minecraft:block.dispenser.fail player @s ~ ~ ~ 0.5 1.2'])
w('terra/net_ray', ['# Un pas (0,5 bloc) du filet', 'particle minecraft:block{block_state:"minecraft:cobweb"} ~ ~ ~ 0.05 0.05 0.05 0 2',
                    'scoreboard players add $tvr mg.st 1',
                    'execute positioned ~-0.5 ~-0.5 ~-0.5 as @e[tag=mg.tvtg,tag=!mg.tvnetted,dx=0,dy=0,dz=0,limit=1] at @s run return run function mg:terra/net_on',
                    'execute unless block ~ ~ ~ #mg:tv_pass run return 0',
                    'execute if score $tvr mg.st matches ..48 positioned ^ ^ ^0.5 run function mg:terra/net_ray'])
w('terra/trap_use', ['# @s : pose un piège à ses pieds (hors de la colonie, 4 actifs au plus)',
                     'execute if score @s mg.tvtr matches ..0 run return run function mg:terra/no_trap',
                     'execute unless entity @s[tag=mg.tvout] run return run function mg:terra/trap_here',
                     'execute if block ~ ~-0.3 ~ #mg:tv_pass run return run function mg:terra/trap_air',
                     'scoreboard players operation $own mg.st = @s mg.tvpid', 'scoreboard players set $tvn mg.st 0',
                     'execute as @e[type=minecraft:marker,tag=mg.tvtrap] if score @s mg.tvo = $own mg.st run scoreboard players add $tvn mg.st 1',
                     'execute if score $tvn mg.st matches 4.. unless score @s mg.trcl matches 4 run return run function mg:terra/trap_max',
                     'execute if score $tvn mg.st matches 8.. run return run function mg:terra/trap_max',
                     'scoreboard players remove @s mg.tvtr 1', 'execute align xyz positioned ~0.5 ~ ~0.5 run function mg:terra/trap_new'])
w('terra/no_trap', say('⚙ Plus de pièges : achète-en au dépôt de la colonie', 'red'))
w('terra/trap_here', say('⚙ Pas de pièges dans la colonie : pose-les dans la jungle', 'yellow'))
w('terra/trap_air', say('⚙ Pose le piège au sol', 'yellow'))
w('terra/trap_max', say('⚙ 4 pièges posés au plus : attends qu\'ils servent', 'yellow'))
w('terra/trap_new', ['# Piège ici (propriétaire $own)', 'scoreboard players add $tvid mg.st 1',
                     'summon minecraft:marker ~ ~ ~ {Tags:["mg.tv","mg.tvtrap","mg.tvn"]}',
                     part('"mg.tv","mg.tvtrapd","mg.tvn"', 'heavy_weighted_pressure_plate', -0.45, 0, -0.45, 0.9, 1.0, 0.9),
                     part('"mg.tv","mg.tvtrapd","mg.tvn"', 'iron_bars', -0.4, 0.02, -0.38, 0.8, 0.22, 0.1),
                     part('"mg.tv","mg.tvtrapd","mg.tvn"', 'iron_bars', -0.4, 0.02, 0.28, 0.8, 0.22, 0.1),
                     'scoreboard players operation @e[tag=mg.tvn] mg.tvid = $tvid mg.st', 'scoreboard players operation @e[tag=mg.tvn] mg.tvo = $own mg.st',
                     'tag @e[tag=mg.tvn] remove mg.tvn', 'playsound minecraft:block.chain.place player @a ~ ~ ~ 0.8 0.8'])
w('terra/trap_fire', ['# @s (piège) : un prédateur marche dessus : bloqué 6 s (carnotaure 2,5 s), 4 dégâts',
                      'scoreboard players operation $tvti mg.st = @s mg.tvid',
                      'execute as @e[tag=mg.tvhos,tag=!mg.tvnetted,distance=..1.4,sort=nearest,limit=1] at @s run function mg:terra/trap_hit',
                      'execute as @e[type=minecraft:block_display,tag=mg.tvtrapd] if score @s mg.tvid = $tvti mg.st run kill @s',
                      'playsound minecraft:block.chain.break hostile @a ~ ~ ~ 1 0.6', 'particle minecraft:crit ~ ~0.5 ~ 0.4 0.3 0.4 0.2 15', 'kill @s'])
w('terra/trap_hit', ['damage @s 4 minecraft:generic', 'function mg:terra/net_on', 'execute unless entity @s[tag=mg.tvcarno] run scoreboard players set @s mg.tvst 120'])
w('terra/home', ['# @s : rappel à la colonie (5 s, annulé par un coup)',
                 'execute if entity @s[tag=mg.tvcar] run return run function mg:terra/home_no_crate',
                 'execute unless entity @s[tag=mg.tvout] run return run function mg:terra/home_here',
                 'execute if score @s mg.tvhm matches 1.. run return 0',
                 'scoreboard players set @s mg.tvhm 100', 'scoreboard players set @s mg.tvdt 0',
                 'tellraw @s {"text":"📡 Rappel à la colonie dans 5 s… ne prends pas de coup !","color":"green"}',
                 'playsound minecraft:block.beacon.activate player @s ~ ~ ~ 0.6 1.6'])
w('terra/home_no_crate', say('📦 Impossible avec la caisse : rapporte-la à pied !', 'red'))
w('terra/home_here', say('Tu es déjà dans la colonie.', 'gray'))
w('terra/home_tick', ['# @s attend son rappel (5 s) : un coup reçu annule',
                      'execute if score @s mg.tvdt matches 1.. run scoreboard players set @s mg.tvhm 0',
                      'execute if score @s mg.tvdt matches 1.. run return run title @s actionbar {"text":"✖ Rappel annulé : tu as pris un coup !","color":"red","bold":true}',
                      'scoreboard players remove @s mg.tvhm 1',
                      'scoreboard players operation $tvs mg.st = @s mg.tvhm', 'scoreboard players add $tvs mg.st 19', 'scoreboard players set #20 mg.st 20',
                      'scoreboard players operation $tvs mg.st /= #20 mg.st',
                      'title @s actionbar [{"text":"📡 Rappel à la colonie dans ","color":"green"},{"score":{"name":"$tvs","objective":"mg.st"},"color":"yellow","bold":true},{"text":" s","color":"green"}]',
                      'execute if score @s mg.tvhm matches 0 run function mg:terra/home_go'])
w('terra/home_go', ['# @s : de retour sur la place de la colonie', f'tp @s {SPAWN[0]} {SPAWN[1]} {SPAWN[2]}',
                    'execute at @s run playsound minecraft:entity.enderman.teleport player @a ~ ~ ~ 0.6 1.2',
                    'execute at @s run particle minecraft:reverse_portal ~ ~1 ~ 0.4 0.8 0.4 0.05 40'])
