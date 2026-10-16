# Pic du Nid : l'alpha se réveille
execute positioned 228.5 114 24.5 run function mg:terra/dino/ptera
tag @e[tag=mg.tvlast] add mg.trboss
tag @e[tag=mg.tvlast] add mg.trdg_pic
execute as @e[tag=mg.tvlast] run attribute @s minecraft:max_health base set 90
execute as @e[tag=mg.tvlast] run attribute @s minecraft:attack_damage modifier add mg:tralpha 0.5 add_multiplied_base
execute as @e[tag=mg.tvlast] run data merge entity @s {Health:90f,CustomName:{"text":"Alpha : Pic du Nid","color":"dark_red","bold":true}}
scoreboard players operation $tvi mg.st = @e[tag=mg.tvlast,limit=1] mg.tvid
execute as @e[tag=mg.tvp] if score @s mg.tvid = $tvi mg.st run data merge entity @s {Glowing:1b,glow_color_override:16729156}
scoreboard players set $trda1 mg.st 1
scoreboard players set $trdr1 mg.st 0
bossbar set mg:trdg1 max 90
execute positioned 228.5 114 24.5 run title @a[tag=mg.tvw,distance=..30] title {"text":"ALPHA","color":"dark_red","bold":true}
execute positioned 228.5 114 24.5 run title @a[tag=mg.tvw,distance=..30] subtitle {"text":"Pic du Nid","color":"gray"}
execute positioned 228.5 114 24.5 as @a[tag=mg.tvw,distance=..30] at @s run playsound minecraft:entity.ravager.roar hostile @s ~ ~ ~ 1 0.8
