# @s (présentoir) : le joueur le plus proche achète (ou prend, si c'est gratuit)
scoreboard players operation $gpt mg.st = @s mg.gpt
scoreboard players set $gok mg.st 0
execute as @a[tag=mg.gtw,tag=!mg.gbuy,gamemode=!spectator,distance=..1.6,sort=nearest,limit=1] at @s run function mg:gta/pad_buy
execute unless score $gok mg.st matches 1 run return 0
scoreboard players set @s mg.gpc 600
execute if entity @s[tag=mg.garm] run scoreboard players set @s mg.gpc 40
kill @e[type=minecraft:item_display,tag=mg.gpdi,distance=..1.5]
kill @e[type=minecraft:text_display,tag=mg.gpdt,distance=..2.5]
playsound minecraft:entity.villager.yes player @a ~ ~ ~ 0.6 1.2
