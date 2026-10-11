# Clic gauche / clic droit des armes (Neo GTA, lobby) : chaque tick, avant gta/pre_tick
tag @a remove mg.gcw
execute as @a[tag=mg.gtw,gamemode=!spectator] if items entity @s weapon.mainhand *[custom_data~{mg_gun:1b}] run tag @s add mg.gcw
execute as @a[tag=mg.gtw,gamemode=!spectator] if items entity @s weapon.mainhand *[custom_data~{rpg:1b}] run tag @s add mg.gcw
execute if score $state mg.st matches 0 as @a[tag=!mg.play,tag=!mg.surv,tag=!mg.gtw,tag=!mg.out,gamemode=!spectator] if items entity @s weapon.mainhand *[custom_data~{mg_gun:1b}] run tag @s add mg.gcw
execute as @a[tag=mg.gads,tag=!mg.gcw] run function mg:gun/cl_unaim
execute unless entity @a[tag=mg.gcw] run return run kill @e[type=minecraft:interaction,tag=mg.gci]
execute as @a[tag=mg.gcw] unless score @s mg.gcid matches 1.. run function mg:gun/cl_id
# un clic droit passé à côté de la boîte : visée
execute as @a[tag=mg.gcw,scores={mg.qs=1..}] run function mg:gun/cl_right
execute as @e[type=minecraft:interaction,tag=mg.gci] run function mg:gun/cl_follow
# rafale de la mitraillette (un clic gauche maintenu ne se répète pas dans Minecraft)
scoreboard players remove @a[scores={mg.gbu=1..}] mg.gbu 1
execute as @a[tag=mg.gcw,scores={mg.gbu=1..}] if items entity @s weapon.mainhand *[custom_data~{gun:2}] run function mg:gun/cl_burst
execute as @a[tag=mg.gcw,tag=!mg.gchas] at @s anchored eyes positioned ^ ^ ^ run function mg:gun/cl_new
tag @a remove mg.gchas
execute as @a[tag=mg.gads] run function mg:gun/cl_zoom
scoreboard players add $gcret mg.st 1
execute if score $gcret mg.st matches 2.. run function mg:gun/cl_ret
