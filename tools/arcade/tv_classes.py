"""🎖 Terra Nova RPG : classes (Soldat, Éclaireur, Scientifique, Ingénieur) et donjons (alphas).
Exécuté par tv_rpg.py (même espace de noms) : utilise w, js, P, TEXT, nm, lo, WF, dlg, show, chfn, DIM, DUNGEONS, bit_test.

Classe : score mg.trcl (0 aucune, 1..4), choisie et changeable auprès de la Commandante Varga.
Capacité active (objet case 5, clic droit, recharge mg.trcd en ticks) ; rangs selon le niveau : I (1), II (5), III (10), IV (15).
"""
CLASSES = {
    1: ('soldat', '🎖 Soldat', 'red', 'minecraft:nether_star',
        'Endurant : +3 cœurs, +2 armure, le fusil chauffe 30 % moins vite.',
        '💥 Onde de choc : repousse et blesse les dinosaures proches (6 blocs), résistance 5 s. Recharge 15 s.',
        ['II (niv. 5) : dégâts +50 %', 'III (niv. 10) : portée 9 blocs', 'IV (niv. 15) : recharge 10 s']),
    2: ('eclaireur', '🏹 Éclaireur', 'green', 'minecraft:feather',
        'Agile : +15 % de vitesse, sauts plus hauts, chutes amorties, +2 dégâts en mêlée.',
        '💨 Sprint du chasseur : vitesse et saut 6 s. Recharge 15 s.',
        ['II (niv. 5) : 9 s', 'III (niv. 10) : invisible 4 s (les dinosaures te perdent)', 'IV (niv. 15) : recharge 10 s']),
    3: ('scientifique', '🔬 Scientifique', 'aqua', 'minecraft:end_crystal',
        'Soigneur : régénère lentement les colons proches, +50 % d\'XP au scanner.',
        '✨ Fusée de détection : les dinosaures à 40 blocs brillent 10 s, colons proches régénérés. Recharge 20 s.',
        ['II (niv. 5) : régénération plus forte', 'III (niv. 10) : absorption (cœurs dorés)', 'IV (niv. 15) : recharge 14 s']),
    4: ('ingenieur', '⚙ Ingénieur', 'gold', 'minecraft:dispenser',
        'Bricoleur : lance-filets et 3 filets offerts, +3 pièges, 8 pièges posés au plus.',
        '🔫 Tourelle : une tourelle automatique tire sur les prédateurs (16 blocs) pendant 20 s. Recharge 25 s.',
        ['II (niv. 5) : dégâts +50 %', 'III (niv. 10) : 30 s', 'IV (niv. 15) : recharge 18 s']),
}
CD = {1: (300, 200), 2: (300, 200), 3: (400, 280), 4: (500, 360)}          # recharge (ticks) avant / à partir du rang IV


def ability_item(n):
    key, name, col, model, passive, active, ranks = CLASSES[n]
    return (f'{WF}[custom_data={{tv:14}},item_model="{model}",unbreakable={{}},custom_name={nm(active.split(" :")[0], col)},'
            f'lore={lo(active, "Rangs : " + " · ".join(r.split(" :")[0] for r in ranks))}]')


# ---------------------------------------------------------------- choix de la classe (Varga)
CL_D = dlg('🎖 Classe de colon', 'gold', 'Chaque classe a un talent permanent et une capacité (objet en case 5, clic droit), '
           'qui se renforce aux niveaux 5, 10 et 15. Tu peux en changer quand tu veux en revenant me voir.',
           [(CLASSES[n][1], CLASSES[n][2], f'{CLASSES[n][4]}\n{CLASSES[n][5]}\nRangs : ' + ' · '.join(CLASSES[n][6]), 600 + n) for n in CLASSES])
w(f'{P}/cl/menu', [f'# @s : choix de la classe'] + show(CL_D))
for n, (key, name, col, model, passive, active, ranks) in CLASSES.items():
    w(f'{P}/cl/pick_{n}', [f'# @s devient {name}', 'execute if score @s mg.trcl matches ' + str(n) + ' run return run tellraw @s ' + js(TEXT('Tu es déjà ' + name + '.', 'gray')),
                           f'scoreboard players set @s mg.trcl {n}', 'scoreboard players set @s mg.trcd 0', f'function mg:{P}/stats', 'clear @s *[custom_data~{tv:14}]', f'function mg:{P}/kit', f'function mg:{P}/cl/bonus',
                           'title @s times 5 50 15', f'title @s title {js(TEXT(name.upper(), col, bold=True))}', f'title @s subtitle {js(TEXT(passive, "gray"))}',
                           'tellraw @s ' + js([TEXT('🎖 Classe : ', 'gold'), TEXT(name, col, bold=True), TEXT(' — ' + active, 'gray')]),
                           'execute at @s run playsound minecraft:item.armor.equip_netherite player @s ~ ~ ~ 1 1'])

# ---------------------------------------------------------------- talents permanents (attributs), appliqués par rpg/stats
w(f'{P}/cl/passive', ['# @s : talents de sa classe (modificateurs mg:trcl*), retirés puis remis',
                      'attribute @s minecraft:max_health modifier remove mg:trcl', 'attribute @s minecraft:armor modifier remove mg:trcl',
                      'attribute @s minecraft:movement_speed modifier remove mg:trcl', 'attribute @s minecraft:jump_strength modifier remove mg:trcl',
                      'attribute @s minecraft:safe_fall_distance modifier remove mg:trcl', 'attribute @s minecraft:attack_damage modifier remove mg:trcl',
                      'execute if score @s mg.trcl matches 1 run attribute @s minecraft:max_health modifier add mg:trcl 6 add_value',
                      'execute if score @s mg.trcl matches 1 run attribute @s minecraft:armor modifier add mg:trcl 2 add_value',
                      'execute if score @s mg.trcl matches 2 run attribute @s minecraft:movement_speed modifier add mg:trcl 0.15 add_multiplied_base',
                      'execute if score @s mg.trcl matches 2 run attribute @s minecraft:jump_strength modifier add mg:trcl 0.1 add_value',
                      'execute if score @s mg.trcl matches 2 run attribute @s minecraft:safe_fall_distance modifier add mg:trcl 6 add_value',
                      'execute if score @s mg.trcl matches 2 run attribute @s minecraft:attack_damage modifier add mg:trcl 2 add_value'])
w(f'{P}/cl/remove', ['# @s quitte Terra Nova : talents retirés'] + [f'attribute @s minecraft:{a} modifier remove mg:trcl' for a in
                                                                  ('max_health', 'armor', 'movement_speed', 'jump_strength', 'safe_fall_distance', 'attack_damage')])
KITC = ['# @s : objet de capacité et bonus d\'équipement de la classe']
for n in CLASSES:
    KITC.append(f'execute if score @s mg.trcl matches {n} run item replace entity @s hotbar.4 with {ability_item(n)}')
# kit rappelé sans `clear` (achats, forge) : les objets de l'ingénieur ne sont donnés que s'il ne les a pas (même garde que le dépôt)
KITC += ['execute if score @s mg.trcl matches 4 unless items entity @s container.* *[custom_data~{tv:5}] run give @s ' + NETL_ITEM,
         'execute if score @s mg.trcl matches 4 unless items entity @s container.* *[custom_data~{tv:6}] run give @s ' + TRAP_ITEM]
w(f'{P}/cl/kit', KITC)
# +3 filets et +3 pièges offerts à l'ingénieur : une seule fois par visite (tag mg.trkb, retiré et compteurs remis à 0 par terra/enter)
w(f'{P}/cl/bonus', ['# @s : bonus de départ de l\'ingénieur (une fois par visite)', 'execute unless score @s mg.trcl matches 4 run return 0',
                    'execute if entity @s[tag=mg.trkb] run return 0', 'tag @s add mg.trkb',
                    'scoreboard players add @s mg.tvnet 3', 'scoreboard players add @s mg.tvtr 3'])

# ---------------------------------------------------------------- capacité active
USE = ['# @s : clic droit sur l\'objet de capacité',
       'execute if score @s mg.trcd matches 1.. run return run function mg:terra/rpg/cl/wait',
       'scoreboard players set $rk mg.st 1', 'execute if score @s mg.trlv matches 5.. run scoreboard players set $rk mg.st 2',
       'execute if score @s mg.trlv matches 10.. run scoreboard players set $rk mg.st 3', 'execute if score @s mg.trlv matches 15.. run scoreboard players set $rk mg.st 4']
for n, (a, b) in CD.items():
    USE += [f'execute if score @s mg.trcl matches {n} run scoreboard players set @s mg.trcd {a}',
            f'execute if score @s mg.trcl matches {n} if score $rk mg.st matches 4 run scoreboard players set @s mg.trcd {b}',
            f'execute if score @s mg.trcl matches {n} run function mg:{P}/cl/act_{CLASSES[n][0]}']
w(f'{P}/cl/use', USE)
w(f'{P}/cl/wait', ['scoreboard players operation $s mg.st = @s mg.trcd', 'scoreboard players add $s mg.st 19', 'scoreboard players set #20 mg.st 20',
                   'scoreboard players operation $s mg.st /= #20 mg.st', 'scoreboard players set @s mg.tval 20',
                   'title @s actionbar [{"text":"⏳ Capacité prête dans ","color":"gray"},{"score":{"name":"$s","objective":"mg.st"},"color":"yellow","bold":true},{"text":" s","color":"gray"}]',
                   'playsound minecraft:block.dispenser.fail player @s ~ ~ ~ 0.4 1.6'])
# Soldat : onde de choc
w(f'{P}/cl/act_soldat', ['# @s (soldat) : onde de choc', 'tag @s add mg.trsrc', 'effect give @s minecraft:resistance 5 1',
                         'playsound minecraft:entity.generic.explode player @a ~ ~ ~ 1 1.4', 'particle minecraft:explosion ~ ~1 ~ 2 0.4 2 0 10',
                         'particle minecraft:sweep_attack ~ ~1 ~ 3 0.3 3 0 20',
                         'execute if score $rk mg.st matches ..2 as @e[tag=mg.tvtg,distance=..6] at @s run function mg:terra/rpg/cl/shock',
                         'execute if score $rk mg.st matches 3.. as @e[tag=mg.tvtg,distance=..9] at @s run function mg:terra/rpg/cl/shock',
                         'tag @s remove mg.trsrc'])
w(f'{P}/cl/shock', ['# @s (cible) prise dans l\'onde', 'execute if score $rk mg.st matches 1 run damage @s 8 minecraft:player_explosion by @a[tag=mg.trsrc,limit=1]',
                    'execute if score $rk mg.st matches 2.. run damage @s 12 minecraft:player_explosion by @a[tag=mg.trsrc,limit=1]',
                    'execute unless entity @s[tag=mg.tvbig] facing entity @a[tag=mg.trsrc,limit=1] feet rotated ~180 -25 positioned 0.0 0.0 0.0 summon minecraft:marker run function mg:terra/vec {d:1.4}',
                    'execute unless entity @s[tag=mg.tvbig] run function mg:terra/push'])
# Éclaireur : sprint
w(f'{P}/cl/act_eclaireur', ['# @s (éclaireur) : sprint du chasseur', 'playsound minecraft:entity.breeze.wind_burst player @a ~ ~ ~ 0.8 1.4',
                            'particle minecraft:gust ~ ~0.5 ~ 0.3 0.1 0.3 0 3',
                            'execute if score $rk mg.st matches 1 run effect give @s minecraft:speed 6 2', 'execute if score $rk mg.st matches 1 run effect give @s minecraft:jump_boost 6 1',
                            'execute if score $rk mg.st matches 2.. run effect give @s minecraft:speed 9 2', 'execute if score $rk mg.st matches 2.. run effect give @s minecraft:jump_boost 9 1',
                            'execute if score $rk mg.st matches 3.. run effect give @s minecraft:invisibility 4 0',
                            'execute if score $rk mg.st matches 3.. as @e[tag=mg.tvhos,distance=..24] run function mg:terra/rpg/cl/lose'])
w(f'{P}/cl/lose', ['# @s (prédateur) perd la trace de l\'éclaireur invisible : il se tourne vers un autre colon ou erre',
                   'effect give @s minecraft:slowness 2 1 true', 'effect give @s minecraft:blindness 3 0 true'])
# Scientifique : fusée de détection
w(f'{P}/cl/act_scientifique', ['# @s (scientifique) : fusée de détection', 'playsound minecraft:entity.firework_rocket.launch player @a ~ ~ ~ 1 1',
                               'particle minecraft:firework ~ ~3 ~ 0.4 2 0.4 0.05 40 force', 'particle minecraft:glow ~ ~1 ~ 6 1 6 0 60',
                               'effect give @e[tag=mg.tvd,distance=..40] minecraft:glowing 10 0 true',
                               'execute if score $rk mg.st matches 1 run effect give @a[tag=mg.tvw,distance=..8] minecraft:regeneration 6 1',
                               'execute if score $rk mg.st matches 2.. run effect give @a[tag=mg.tvw,distance=..8] minecraft:regeneration 6 2',
                               'execute if score $rk mg.st matches 3.. run effect give @a[tag=mg.tvw,distance=..8] minecraft:absorption 20 1'])
# Ingénieur : tourelle
w(f'{P}/cl/act_ingenieur', ['# @s (ingénieur) : tourelle automatique à ses pieds (une seule par ingénieur)', 'scoreboard players operation $own mg.st = @s mg.tvpid',
                            'execute as @e[tag=mg.trtur] if score @s mg.tvo = $own mg.st run kill @s',
                            'execute align xz positioned ~0.5 ~ ~0.5 run summon minecraft:marker ~ ~ ~ {Tags:["mg.tv","mg.trtur","mg.trtm","mg.trtn"]}',
                            'execute align xz positioned ~0.5 ~ ~0.5 run summon minecraft:block_display ~ ~ ~ {Tags:["mg.tv","mg.trtur","mg.trtn"],block_state:{Name:"minecraft:dispenser",Properties:{facing:"up"}},transformation:{translation:[-0.35f,0f,-0.35f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.7f,0.7f,0.7f]}}',
                            'execute align xz positioned ~0.5 ~ ~0.5 run summon minecraft:block_display ~ ~ ~ {Tags:["mg.tv","mg.trtur","mg.trtn"],block_state:{Name:"minecraft:lightning_rod"},transformation:{translation:[-0.5f,0.7f,-0.5f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1f,0.8f,1f]}}',
                            'scoreboard players operation @e[tag=mg.trtn] mg.tvo = $own mg.st',
                            'execute if score $rk mg.st matches ..2 run scoreboard players set @e[tag=mg.trtn,tag=mg.trtm] mg.tvst 20',
                            'execute if score $rk mg.st matches 3.. run scoreboard players set @e[tag=mg.trtn,tag=mg.trtm] mg.tvst 30',
                            'execute if score $rk mg.st matches 2.. run tag @e[tag=mg.trtn,tag=mg.trtm] add mg.trtx',
                            'tag @e[tag=mg.trtn] remove mg.trtn', 'playsound minecraft:block.anvil.place player @a ~ ~ ~ 0.6 1.6'])
w(f'{P}/cl/turret', ['# @s (tourelle, chaque seconde) : tire sur le prédateur le plus proche (16 blocs), puis s\'use',
                     'scoreboard players remove @s mg.tvst 1', 'execute if score @s mg.tvst matches ..0 run return run function mg:terra/rpg/cl/turret_end',
                     'execute unless entity @e[tag=mg.tvhos,distance=..16] run return 0', 'scoreboard players set $tvr mg.st 0',
                     'execute positioned ~ ~1.2 ~ facing entity @e[tag=mg.tvhos,distance=..16,sort=nearest,limit=1] eyes run function mg:terra/rpg/cl/tray',
                     'playsound minecraft:entity.breeze.shoot player @a ~ ~ ~ 0.6 1.9'])
w(f'{P}/cl/tray', ['particle minecraft:dust{color:[1.0,0.6,0.1],scale:0.8} ~ ~ ~ 0 0 0 0 1', 'scoreboard players add $tvr mg.st 1',
                   'execute positioned ~-0.5 ~-0.5 ~-0.5 as @e[tag=mg.tvhos,dx=0,dy=0,dz=0,limit=1] positioned ~0.5 ~0.5 ~0.5 run return run function mg:terra/rpg/cl/thit',
                   'execute unless block ~ ~ ~ #mg:tv_pass run return 0', 'execute if score $tvr mg.st matches ..32 positioned ^ ^ ^0.5 run function mg:terra/rpg/cl/tray'])
w(f'{P}/cl/thit', ['# prédateur touché par la tourelle (dégâts attribués au propriétaire)', 'scoreboard players operation $own mg.st = @e[tag=mg.trcur,limit=1] mg.tvo',
                   'tag @a remove mg.trtown', 'execute as @a[tag=mg.tvw] if score @s mg.tvpid = $own mg.st run tag @s add mg.trtown',
                   'execute if entity @e[tag=mg.trcur,tag=mg.trtx] run return run damage @s 8 minecraft:player_attack by @a[tag=mg.trtown,limit=1]',
                   'damage @s 5 minecraft:player_attack by @a[tag=mg.trtown,limit=1]', 'particle minecraft:crit ~ ~1 ~ 0.3 0.3 0.3 0.2 8'])
w(f'{P}/cl/turret_end', ['scoreboard players operation $own mg.st = @s mg.tvo', 'execute as @e[tag=mg.trtur] if score @s mg.tvo = $own mg.st run kill @s',
                         'particle minecraft:smoke ~ ~0.8 ~ 0.2 0.3 0.2 0.02 15', 'playsound minecraft:block.chain.break player @a ~ ~ ~ 0.6 1'])
w(f'{P}/cl/second', ['# Chaque seconde : tourelles, soins du scientifique (toutes les 5 s)',
                     'execute as @e[type=minecraft:marker,tag=mg.trtm] at @s run function mg:terra/rpg/cl/turret_one',
                     'execute if score $trq3 mg.st matches 0 as @a[tag=mg.tvw,scores={mg.trcl=3}] at @s run effect give @a[tag=mg.tvw,distance=..6] minecraft:regeneration 3 0 true'])
w(f'{P}/cl/turret_one', ['tag @s add mg.trcur', 'function mg:terra/rpg/cl/turret', 'tag @s remove mg.trcur'])
w(f'{P}/cl/tick', ['scoreboard players remove @a[tag=mg.tvw,scores={mg.trcd=1..}] mg.trcd 1'])

# ================================================================ donjons : alphas, salles et vagues (tv_dungeons.py)
exec(open(os.path.join(os.path.dirname(os.path.abspath(C.__file__)), 'tv_dungeons.py'), encoding='utf-8').read())
