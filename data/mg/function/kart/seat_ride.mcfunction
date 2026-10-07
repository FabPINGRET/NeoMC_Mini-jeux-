execute if entity @s[gamemode=spectator] run gamemode adventure @s
scoreboard players operation $me mg.st = @s mg.ri
execute as @e[type=minecraft:item_display,tag=mg.khead] if score @s mg.ri = $me mg.st run kill @s
scoreboard players set $rd mg.st 0
execute on vehicle run scoreboard players set $rd mg.st 1
execute if score $rd mg.st matches 0 run ride @s mount @e[type=minecraft:block_display,tag=mg.kk,limit=1]
