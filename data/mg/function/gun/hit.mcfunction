# @s = cible touchée (le tireur porte mg.gsh)
tag @s add mg.ghd
execute if score $gdn mg.st matches 1 run scoreboard players set $gdm mg.st 60
execute if score $gdn mg.st matches 2 run scoreboard players set $gdm mg.st 40
execute if score $gdn mg.st matches 3 run scoreboard players set $gdm mg.st 50
execute if score $gdn mg.st matches 4 run scoreboard players set $gdm mg.st 100
execute if score $gdn mg.st matches 5 run scoreboard players set $gdm mg.st 350
execute if score $gdn mg.st matches 6 run scoreboard players set $gdm mg.st 200
execute if entity @a[tag=mg.gsh,tag=mg.zdbl] run scoreboard players operation $gdm mg.st *= #2 mg.st
execute if entity @s[type=minecraft:player] run function mg:gun/hit_player
execute unless entity @s[type=minecraft:player] run function mg:gun/hit_mob
execute if score $zpts mg.st matches 1 run scoreboard players add @a[tag=mg.gsh,limit=1] mg.zpt 10
particle minecraft:damage_indicator ~ ~1.2 ~ 0.2 0.3 0.2 0 2
execute as @a[tag=mg.gsh,limit=1] at @s run playsound minecraft:entity.arrow.hit_player player @s ~ ~ ~ 0.5 1.6
