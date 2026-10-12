# @s : joueur coiffé d'un casque de jeu → présentoir (item_display) collé à sa tête, tourné comme lui
execute unless score @s mg.hid matches 1.. run scoreboard players add $hid_n mg.st 1
execute unless score @s mg.hid matches 1.. run scoreboard players operation @s mg.hid = $hid_n mg.st
scoreboard players operation $hid mg.st = @s mg.hid
scoreboard players operation $hhn mg.st = @s mg.hat
execute as @e[type=minecraft:item_display,tag=mg.hatf] if score @s mg.hid = $hid mg.st run tag @s add mg.hatt
execute as @e[type=minecraft:item_display,tag=mg.hatt] unless score @s mg.hat = $hhn mg.st run kill @s
execute unless entity @e[type=minecraft:item_display,tag=mg.hatt,limit=1] run function mg:hat/follow_new
execute anchored eyes positioned ^ ^ ^ run tp @e[type=minecraft:item_display,tag=mg.hatt,limit=1] ~ ~ ~ ~ ~
tag @e[type=minecraft:item_display,tag=mg.hatt] remove mg.hatt
tag @s add mg.hatd
