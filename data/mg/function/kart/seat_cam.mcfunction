scoreboard players set $rd mg.st 0
execute on vehicle run scoreboard players set $rd mg.st 1
execute if score $rd mg.st matches 1 run ride @s dismount
execute unless entity @s[gamemode=spectator] run gamemode spectator @s
execute unless entity @e[tag=mg.kcamc] run function mg:kart/cam_new
execute at @s unless entity @e[type=minecraft:item_display,tag=mg.kcamc,distance=..2] run spectate @e[type=minecraft:item_display,tag=mg.kcamc,limit=1] @s
