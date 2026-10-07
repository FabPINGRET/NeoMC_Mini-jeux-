# Pilote sorti de son kart (touche Maj) : il y remonte, ou un kart neuf est créé au dernier point de passage
scoreboard players operation $me mg.st = @s mg.ri
tag @e[tag=mg.mine] remove mg.mine
execute as @e[type=minecraft:block_display,tag=mg.kart] if score @s mg.ri = $me mg.st run tag @s add mg.mine
execute if entity @e[type=minecraft:block_display,tag=mg.mine] run ride @s mount @e[type=minecraft:block_display,tag=mg.mine,limit=1]
tag @e[tag=mg.mine] remove mg.mine
scoreboard players set $rd mg.st 0
execute on vehicle run scoreboard players set $rd mg.st 1
execute if score $rd mg.st matches 0 at @s run function mg:kart/kart_new
