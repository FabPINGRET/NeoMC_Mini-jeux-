# @s : joueur avec un présentoir ; le sien n'est pas orphelin
scoreboard players operation $hid mg.st = @s mg.hid
execute as @e[type=minecraft:item_display,tag=mg.hato] if score @s mg.hid = $hid mg.st run tag @s remove mg.hato
