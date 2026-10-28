"""Commandes des armes à Neo GTA et au lobby : clic gauche = tirer, clic droit = viser, accroupi = recharger.

    python tools/arcade/gen_gunclick.py .

Le clic gauche dans le vide ne se détecte pas : tant qu'un joueur tient une arme, une entité interaction (tag mg.gci,
numéro du propriétaire mg.gcid) est recalée sur ses yeux à chaque tick. Ses yeux étant dedans, ses deux clics la touchent :
  attack      → tir : mg.qs / mg.gqs = 1, les boucles existantes (gta/tick, lobby/guns_tick) tirent comme avant ;
  interaction → visée (tag mg.gads) : zoom selon l'arme (vitesse réduite = champ de vision réduit), viseur au lobby, lunette au sniper à Neo GTA.
Un clic droit qui passe à côté de la boîte (déplacement rapide) compte aussi comme visée, jamais comme tir.
Le sniper du duel (mg_dl) et du TDM (mg_tm) passe aussi par là : clic gauche = tir (duel/shoot, tdm/shoot), clic droit = lunette
(mg.gads lu par duel/scope, tdm/scope). Un coup de couteau d'un autre joueur sur la boîte (2,6 blocs) est renvoyé à gun/cl_foreign.
Zombies et Infection gardent le clic droit pour tirer (ils ne passent pas par ici).
"""
import sys
import common as C

C.init(sys.argv[1] if len(sys.argv) > 1 else '.')
w = C.w
GUN = '*[custom_data~{mg_gun:1b}]'
RPG = '*[custom_data~{rpg:1b}]'
DLSN = 'minecraft:warped_fungus_on_a_stick[custom_data~{mg_dl:1b}]'     # sniper du duel (tools/duel)
TMSN = 'minecraft:warped_fungus_on_a_stick[custom_data~{mg_tm:1b}]'     # sniper du TDM (tools/tdm)
LOB = 'tag=!mg.play,tag=!mg.surv,tag=!mg.gtw,tag=!mg.out'
# zoom en visée (modificateur de vitesse : le champ de vision suit) : plus fort pour les armes de loin
ZOOM = [('gun:1', -0.3), ('gun:2', -0.35), ('gun:3', -0.25), ('gun:4', -0.6), ('gun:5', -0.9), ('gun:6', -0.45), ('rpg:1b', -0.5)]
VIS = 'tag=mg.gads,tag=!mg.gtw,tag=!mg.dl,tag=!mg.play'       # joueurs qui visent et reçoivent le viseur du lobby
RET = {'text': '', 'font': 'mg:gta', 'color': 'white', 'shadow_color': 0}

w('gun/cl_tick', ['# Clic gauche / clic droit des armes (Neo GTA, lobby) : chaque tick, avant gta/pre_tick',
                  'tag @a remove mg.gcw',
                  f'execute as @a[tag=mg.gtw,gamemode=!spectator] if items entity @s weapon.mainhand {GUN} run tag @s add mg.gcw',
                  f'execute as @a[tag=mg.gtw,gamemode=!spectator] if items entity @s weapon.mainhand {RPG} run tag @s add mg.gcw',
                  f'execute if score $state mg.st matches 0 as @a[{LOB},gamemode=!spectator] if items entity @s weapon.mainhand {GUN} run tag @s add mg.gcw',
                  '# sniper du duel et du TDM (le couteau porte aussi mg_dl / mg_tm : seul le sniper arme la boîte)',
                  f'execute as @a[tag=mg.dl,gamemode=!spectator] if items entity @s weapon.mainhand {DLSN} run tag @s add mg.gcw',
                  f'execute as @a[tag=mg.play,gamemode=adventure] if items entity @s weapon.mainhand {TMSN} run tag @s add mg.gcw',
                  'execute as @a[tag=mg.gads,tag=!mg.gcw] run function mg:gun/cl_unaim',
                  '# personne n\'a d\'arme en main : les boîtes ne sont balayées qu\'une fois ($gcib, posé par cl_new et au chargement), pas à chaque tick',
                  'execute unless entity @a[tag=mg.gcw] unless score $gcib mg.st matches 1 run return 0',
                  'execute unless entity @a[tag=mg.gcw] run scoreboard players set $gcib mg.st 0',
                  'execute unless entity @a[tag=mg.gcw] run return run kill @e[type=minecraft:interaction,tag=mg.gci]',
                  'execute as @a[tag=mg.gcw] unless score @s mg.gcid matches 1.. run function mg:gun/cl_id',
                  '# un clic droit passé à côté de la boîte : visée',
                  'execute as @a[tag=mg.gcw,scores={mg.qs=1..}] run function mg:gun/cl_right',
                  'execute as @e[type=minecraft:interaction,tag=mg.gci] run function mg:gun/cl_follow',
                  '# rafale de la mitraillette (un clic gauche maintenu ne se répète pas dans Minecraft)',
                  'scoreboard players remove @a[scores={mg.gbu=1..}] mg.gbu 1',
                  'execute as @a[tag=mg.gcw,scores={mg.gbu=1..}] if items entity @s weapon.mainhand *[custom_data~{gun:2}] run function mg:gun/cl_burst',
                  'execute as @a[tag=mg.gcw,tag=!mg.gchas] at @s anchored eyes positioned ^ ^ ^ run function mg:gun/cl_new',
                  'tag @a remove mg.gchas',
                  'execute as @a[tag=mg.gads] run function mg:gun/cl_zoom',
                  'scoreboard players add $gcret mg.st 1', 'execute if score $gcret mg.st matches 2.. run function mg:gun/cl_ret'])
w('gun/cl_zoom', ['# @s vise : zoom selon l\'arme en main', 'attribute @s minecraft:movement_speed modifier remove mg:aim'] +
  [f'execute if items entity @s weapon.mainhand *[custom_data~{{{c}}}] run return run attribute @s minecraft:movement_speed modifier add mg:aim {z} add_multiplied_total' for c, z in ZOOM])
w('gun/cl_ret', ['# Viseur au centre de l\'écran pour ceux qui visent au lobby (Neo GTA a le sien : gta/aim)', 'scoreboard players set $gcret mg.st 0',
                 '# sauf le duel et le TDM : leur lunette (duel/scope, tdm/scope) pose son propre cache',
                 f'title @a[{VIS}] times 0 5 2',
                 f'execute if score $rp mg.st matches 1 run title @a[{VIS}] title ' + C.js(RET),
                 f'execute unless score $rp mg.st matches 1 run title @a[{VIS}] title {{"text":"+","color":"white"}}'])
w('gun/cl_burst', ['scoreboard players set @s mg.qs 1', 'scoreboard players set @s mg.gqs 1'])
w('gun/cl_id', ['scoreboard players add $gcidn mg.st 1', 'scoreboard players operation @s mg.gcid = $gcidn mg.st'])
w('gun/cl_new', ['# @s : tient une arme, pas encore de boîte (position = ses yeux)', 'scoreboard players set $gcib mg.st 1',
                 'summon minecraft:interaction ~ ~-1.3 ~ {Tags:["mg.gci","mg.gcin"],width:2.6f,height:2.6f,response:0b}',
                 'scoreboard players operation @e[type=minecraft:interaction,tag=mg.gcin] mg.gcid = @s mg.gcid',
                 'tag @e[tag=mg.gcin] remove mg.gcin', 'tag @s add mg.gchas'])
w('gun/cl_follow', ['# @s : boîte d\'un joueur armé ; propriétaire parti ou plus armé : supprimée',
                    'scoreboard players operation $gcid mg.st = @s mg.gcid',
                    'execute as @a[tag=mg.gcw] if score @s mg.gcid = $gcid mg.st run tag @s add mg.gcme',
                    'execute unless entity @a[tag=mg.gcme] run return run kill @s',
                    'execute if entity @a[tag=mg.gchas,tag=mg.gcme] run return run function mg:gun/cl_dup',
                    'execute if data entity @s attack on attacker if entity @s[tag=mg.gcme] run function mg:gun/cl_left',
                    'execute if data entity @s interaction on target if entity @s[tag=mg.gcme] run function mg:gun/cl_right',
                    '# un autre joueur que le propriétaire touche la boîte : armé (ses yeux sont aussi dans cette boîte, proche) = son propre clic ;',
                    '# sinon (couteau du duel / TDM sur l\'adversaire armé du sniper) = gun/cl_foreign',
                    'execute if data entity @s attack on attacker unless entity @s[tag=mg.gcme] run function mg:gun/cl_foreign',
                    'execute if data entity @s interaction on target unless entity @s[tag=mg.gcme] if entity @s[tag=mg.gcw] run function mg:gun/cl_right',
                    'data remove entity @s attack', 'data remove entity @s interaction',
                    'execute at @a[tag=mg.gcme,limit=1] anchored eyes positioned ^ ^ ^ run tp @s ~ ~-1.3 ~',
                    'tag @a[tag=mg.gcme] add mg.gchas', 'tag @a remove mg.gcme'])
w('gun/cl_dup', ['kill @s', 'tag @a remove mg.gcme'])
w('gun/cl_foreign', ['# @s = attaquant (pas le propriétaire de la boîte) ; la victime est @a[tag=mg.gcme], propriétaire de la boîte frappée',
                     '# attaquant armé (mg.gcw) : le ciblage a pris la boîte adverse au lieu de la sienne, son clic gauche est un tir',
                     'execute if entity @s[tag=mg.gcw] run return run function mg:gun/cl_left',
                     'execute if entity @s[tag=mg.dl] run return run function mg:duel/box_knife',
                     'execute if entity @s[tag=mg.play] if score $game mg.st matches 246 run return run function mg:tdm/box_knife'])
w('gun/cl_left', ['# @s : clic gauche avec une arme → tir (boucles existantes) ; mitraillette : rafale de 8 ticks',
                  'scoreboard players set @s mg.qs 1', 'scoreboard players set @s mg.gqs 1',
                  'execute if items entity @s weapon.mainhand *[custom_data~{gun:2}] run scoreboard players set @s mg.gbu 8'])
w('gun/cl_right', ['# @s : clic droit avec une arme → viser / arrêter de viser',
                   'scoreboard players reset @s mg.qs', 'scoreboard players reset @s mg.gqs',
                   'execute if entity @s[tag=mg.gads] run return run function mg:gun/cl_unaim',
                   'tag @s add mg.gads', 'function mg:gun/cl_zoom',
                   'execute at @s run playsound minecraft:item.spyglass.use player @s ~ ~ ~ 0.6 1.4'])
w('gun/cl_unaim', ['tag @s remove mg.gads', 'attribute @s minecraft:movement_speed modifier remove mg:aim', 'title @s[tag=!mg.gtw] clear',
                   'execute if entity @s[tag=mg.gscope] run function mg:gta/unscope'])

C.objectives([('mg.gcid', 'dummy'), ('mg.gbu', 'dummy')])
C.patch('core/tick', 'function mg:gta/pre_tick', ['execute if score $setup mg.st matches 1 run function mg:gun/cl_tick'], where='before')
C.patch('desinstaller', 'scoreboard objectives remove mg.bw', ['kill @e[type=minecraft:interaction,tag=mg.gci]'])
C.patch('core/load', 'scoreboard objectives add mg.bw trigger', ['scoreboard players set $gcib mg.st 1'])
print('ok')
