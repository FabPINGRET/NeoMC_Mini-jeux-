"""🔫 Armes de Neo GTA à l'Armurerie du spawn : python tools/lobby/gen_lobby_guns.py .

Six armes (mg:gun, tools/arcade/guns.py) exposées côté nord de l'Armurerie ; clic droit sur l'une = elle va dans la case 2.
Au lobby, une balle touche le Roi Zombie des événements (mg.gtg) et les autres joueurs du lobby (un demi-cœur) : aucun bloc cassé.
Le railgun du socle 1 ne part plus quand on tire avec une arme (même clic droit sur warped_fungus_on_a_stick).
Indicateur de recharge / cadence du Sniper : barre de durabilité de l'objet (mg:gun/bar), pas use_cooldown (le tir au clic gauche n'est pas un « use » ;
use_cooldown reste réservé à Zombies et Infection, voir gun/cd_*). Le bazooka (lrpg) n'a pas de chargeur : pas de barre.
La barre est gérée avant le garde « minijeu en cours » ($state) ; gun/bar_clear remet à zéro une arme qui n'est plus en main (bazooka compris).
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'arcade'))
import common as C

C.init(sys.argv[1] if len(sys.argv) > 1 else '.')
w, js = C.w, C.js
GUNS = [(1, 'Pistolet', 'pistol', 'gray'), (2, 'Mitraillette', 'smg', 'aqua'), (3, 'Fusil à pompe', 'shotgun', 'gold'),
        (4, 'Fusil M14', 'rifle', 'yellow'), (5, 'Sniper', 'sniper', 'light_purple'), (6, 'Ray Gun', 'raygun', 'green'),
        (7, 'Bazooka', 'rpg', 'red')]
Z = -6.5
XS = [-47.5 + 1.6 * i for i in range(len(GUNS))]
LOB = '@a[tag=!mg.play,tag=!mg.surv,tag=!mg.gtw]'


def lob(extra):
    return LOB[:-1] + ',' + extra + ']'
T = 'transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[%sf,%sf,%sf]}'

B = ['# Armes de Neo GTA à l\'Armurerie (généré par tools/lobby/gen_lobby_guns.py)', 'kill @e[tag=mg.lgun]',
     f'summon minecraft:text_display -42.95 67.4 {Z} {{Tags:["mg.lgun"],billboard:"center",background:0,'
     'text:[{"text":"🔫 Armes de Neo GTA","color":"gold","bold":true},{"text":"\\nmarche dessus pour en prendre une","color":"gray"}],' + T % (1, 1, 1) + '}']
for (n, nm, mdl, col), x in zip(GUNS, XS):
    for cond, model in (('if', f'mg:gun_{mdl}'), ('unless', 'minecraft:crossbow')):
        B.append(f'execute {cond} score $rp mg.st matches 1 run summon minecraft:item_display {x:.1f} 65.3 {Z} {{Tags:["mg.lgun","mg.lspin"],billboard:"fixed",'
                 f'item:{{id:"minecraft:warped_fungus_on_a_stick",count:1,components:{{"minecraft:item_model":"{model}"}}}},' + T % (0.9, 0.9, 0.9) + '}')
    B.append(f'summon minecraft:text_display {x:.1f} 66.1 {Z} {{Tags:["mg.lgun"],billboard:"center",background:0,text:{{"text":"{nm}","color":"{col}"}},' + T % (0.6, 0.6, 0.6) + '}')
    B.append(f'summon minecraft:interaction {x:.1f} 64.5 {Z} {{Tags:["mg.lgun","mg.lgi"],width:1.0f,height:1.4f,response:1b}}')
    B.append(f'scoreboard players set @e[type=minecraft:interaction,tag=mg.lgi,x={x:.1f},y=64.5,z={Z},distance=..0.1] mg.st {n}')
w('lobby/guns_build', B)
LGBOX = f'x={min(XS) - 2:.0f},y=63,z={Z - 2},dx={max(XS) - min(XS) + 4:.0f},dy=3,dz=4'      # les 7 socles : sélecteurs bornés (chaque tick)

w('lobby/guns_tick', ['# Armes de Neo GTA au lobby (chaque tick, avant lobby/armory_tick)',
                      f'execute if score $lan mg.t matches 5 unless entity @e[type=minecraft:interaction,tag=mg.lgi,scores={{mg.st=7}},{LGBOX}] run function mg:lobby/guns_build',
                      f'execute as @e[type=minecraft:interaction,tag=mg.lgi,{LGBOX}] if data entity @s interaction run function mg:lobby/guns_take',
                      f'execute as @e[type=minecraft:interaction,tag=mg.lgi,{LGBOX}] if data entity @s attack run function mg:lobby/guns_take',
                      'tag @a remove mg.lgn2', f'execute as @e[type=minecraft:interaction,tag=mg.lgi,{LGBOX}] at @s run function mg:lobby/guns_near',
                      'tag @a[tag=mg.lgn,tag=!mg.lgn2] remove mg.lgn', 'tag @a[tag=mg.lgn2] add mg.lgn',
                      'execute as @e[type=minecraft:item_display,tag=mg.lrkt] at @s run function mg:lobby/rkt_tick',
                      f'execute as {LOB} if items entity @s weapon.mainhand *[custom_data~{{mg_gun:1b}}] unless items entity @s weapon.mainhand *[custom_data~{{lrpg:1b}}] run function mg:gun/bar',
                      f'execute as {LOB} unless items entity @s weapon.mainhand *[custom_data~{{mg_gun:1b}}] run function mg:gun/bar_clear',
                      f'execute as {LOB} if items entity @s weapon.mainhand *[custom_data~{{lrpg:1b}}] run function mg:gun/bar_clear',
                      'execute unless score $state mg.st matches 0 run return 0',
                      f'scoreboard players remove {lob('scores={mg.lrc=1..}')} mg.lrc 1',
                      f'execute as {lob('scores={mg.qs=1..}')} if items entity @s weapon.mainhand *[custom_data~{{lrpg:1b}}] at @s run function mg:lobby/rpg_fire',
                      f'execute as {lob('scores={mg.qs=1..}')} if items entity @s weapon.mainhand *[custom_data~{{mg_gun:1b}}] at @s run function mg:lobby/gun_shot',
                      f'scoreboard players reset {lob('scores={mg.gqs=1..}')} mg.gqs',
                      f'scoreboard players remove {lob('scores={mg.gcd=1..}')} mg.gcd 1',
                      f'execute as {lob('scores={mg.grl=1..}')} at @s run function mg:gun/reload_tick',
                      f'execute as {lob('scores={mg.gsn=1..}')} if items entity @s weapon.mainhand *[custom_data~{{mg_gun:1b}}] at @s run function mg:gun/sneak',
                      f'scoreboard players reset {lob('scores={mg.gsn=1..}')} mg.gsn',
                      f'execute as {LOB} if items entity @s weapon.mainhand *[custom_data~{{mg_gun:1b}}] unless items entity @s weapon.mainhand *[custom_data~{{lrpg:1b}}] run function mg:gun/hud'])
w('lobby/gun_shot', ['# @s tire au lobby : les autres joueurs du lobby deviennent des cibles le temps du tir (un demi-cœur, voir gun/hit_player)',
                      f'tag {lob("gamemode=!spectator,gamemode=!creative,tag=!mg.gtg")} add mg.lgt', 'tag @a[tag=mg.lgt] add mg.gtg',
                      'tag @s add mg.lsh', 'tag @s add mg.ghd', 'function mg:gun/use',
                      'tag @s remove mg.lsh', 'tag @s remove mg.ghd', 'tag @a[tag=mg.lgt] remove mg.gtg', 'tag @a remove mg.lgt'])
w('lobby/guns_take', ['# @s : présentoir cliqué', 'scoreboard players operation $lgn mg.st = @s mg.st',
                      f'execute on target if entity @s{LOB[2:]} run function mg:lobby/guns_give',
                      f'execute if data entity @s attack on attacker if entity @s{LOB[2:]} run function mg:lobby/guns_give',
                      'data remove entity @s interaction', 'data remove entity @s attack'])
w('lobby/guns_near', ['# @s : présentoir ; un joueur qui marche dessus prend l\'arme (une fois par passage)',
                      'scoreboard players operation $lgn mg.st = @s mg.st',
                      f'execute as {lob("distance=..1.1,tag=!mg.lgn")} run function mg:lobby/guns_give',
                      f'tag {lob("distance=..1.1")} add mg.lgn2'])
RPG = ('minecraft:warped_fungus_on_a_stick[custom_data={rpg:1b,lrpg:1b,mg_gun:1b},unbreakable={},'
       'custom_name={"text":"🚀 Bazooka (feu d\'artifice)","color":"red","bold":true,"italic":false},'
       'lore=[{"text":"Clic gauche : roquette (aucun dégât au spawn)","color":"gray","italic":false}],item_model="%s"]')
w('lobby/rpg_give', ['# @s : bazooka du lobby, case 2',
                     'execute if score $rp mg.st matches 1 run item replace entity @s hotbar.1 with ' + RPG % 'mg:gun_rpg',
                     'execute unless score $rp mg.st matches 1 run item replace entity @s hotbar.1 with ' + RPG % 'minecraft:crossbow'])
w('lobby/rpg_fire', ['# @s tire une roquette inoffensive (recharge 1 s)', 'scoreboard players reset @s mg.qs',
                     'execute if score @s mg.lrc matches 1.. run return 0', 'scoreboard players set @s mg.lrc 20',
                     'execute anchored eyes positioned ^-0.2 ^-0.1 ^1 run summon minecraft:item_display ~ ~ ~ {Tags:["mg.lrkt","mg.lrkn"],'
                     'item:{id:"minecraft:firework_rocket",count:1},teleport_duration:1,'
                     'transformation:{left_rotation:[0.5f,0.5f,-0.5f,0.5f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.4f,1.4f,1.4f]}}',
                     'execute anchored eyes positioned ^-0.2 ^-0.1 ^1 rotated as @s run tp @e[type=minecraft:item_display,tag=mg.lrkn] ~ ~ ~ ~ ~',
                     'scoreboard players set @e[type=minecraft:item_display,tag=mg.lrkn] mg.gpc 0', 'tag @e[tag=mg.lrkn] remove mg.lrkn',
                     'playsound minecraft:entity.firework_rocket.launch player @a ~ ~ ~ 1.5 0.6',
                     'playsound minecraft:entity.blaze.shoot player @a ~ ~ ~ 1 0.5', 'particle minecraft:cloud ~ ~1.4 ~ 0.2 0.2 0.2 0.05 10'])
w('lobby/rkt_tick', ['# @s : roquette du lobby en vol (3 pas de 0,7 bloc par tick, 3 s au plus)',
                     'scoreboard players add @s mg.gpc 1',
                     'execute if score @s mg.gpc matches 60.. run return run function mg:lobby/rkt_boom',
                     'function mg:lobby/rkt_step', 'execute if entity @s at @s run function mg:lobby/rkt_step', 'execute if entity @s at @s run function mg:lobby/rkt_step',
                     'execute if entity @s run particle minecraft:flame ~ ~ ~ 0.05 0.05 0.05 0.02 3'])
w('lobby/rkt_step', ['execute unless block ^ ^ ^0.7 #mg:ray_pass positioned ^ ^ ^0.4 run return run function mg:lobby/rkt_boom',
                     'execute if score @s mg.gpc matches 3.. positioned ^ ^ ^0.7 positioned ~ ~-0.9 ~ if entity @a[distance=..1.2,gamemode=!spectator] run return run function mg:lobby/rkt_boom',
                     'tp @s ^ ^ ^0.7'])
w('lobby/rkt_boom', ['# Explosion pour le spectacle : aucun bloc cassé, aucun dégât (petit saut pour ceux qui sont tout près)',
                     'execute at @s run particle minecraft:explosion_emitter ~ ~ ~ 0 0 0 0 1 force',
                     'execute at @s run particle minecraft:firework ~ ~ ~ 0.5 0.5 0.5 0.2 40 force',
                     'execute at @s run playsound minecraft:entity.generic.explode player @a ~ ~ ~ 2 1.1',
                     f'execute at @s as {lob("distance=..3")} run effect give @s minecraft:levitation 1 3 true',
                     'kill @s'])
w('lobby/guns_give', ['# @s : joueur du lobby, prend l\'arme $lgn (case 2)', 'function mg:gun/reset'] +
  [f'execute if score $lgn mg.st matches {n} run function mg:gun/put_{n} {{slot:"hotbar.1"}}' for n, *_ in GUNS if n < 7] +
  ['execute if score $lgn mg.st matches 7 run function mg:lobby/rpg_give'] +
  ['title @s actionbar [{"text":"🔫 Arme prise (case 2) : ","color":"gold"},{"text":"clic gauche tirer, clic droit viser, accroupi recharger","color":"gray"}]',
   'execute at @s run playsound minecraft:item.armor.equip_iron player @s ~ ~ ~ 1 1.2'])

C.objectives([('mg.lrc', 'dummy')])
C.patch('core/tick', 'execute if score $setup mg.st matches 1 run function mg:lobby/armory_tick',
        ['execute if score $setup mg.st matches 1 run function mg:lobby/guns_tick'], where='before')
LASER_OLD = 'execute if score $state mg.st matches 0 as @a[scores={mg.qs=1..},tag=!mg.surv] at @s run function mg:lobby/laser'
LASER_NEW = 'execute if score $state mg.st matches 0 as @a[scores={mg.qs=1..},tag=!mg.surv] unless items entity @s weapon.mainhand *[custom_data~{mg_gun:1b}] at @s run function mg:lobby/laser'
for p in (os.path.join(C.F, 'lobby', 'armory_tick.mcfunction'), os.path.join(C.R, 'tools', 'lobby', 'gen_lobby.py')):
    s = open(p, encoding='utf-8', newline='').read()
    if LASER_OLD in s:
        open(p, 'w', encoding='utf-8', newline='').write(s.replace(LASER_OLD, LASER_NEW))
print('ok')
