# @s : marque sa balle (tag mg.gfmy)
tag @e[tag=mg.gfmy] remove mg.gfmy
scoreboard players operation $cur mg.st = @s mg.gfi
execute as @e[type=minecraft:item_display,tag=mg.gfb] if score @s mg.gfi = $cur mg.st run tag @s add mg.gfmy
