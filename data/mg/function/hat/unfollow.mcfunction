# @s : joueur ; son présentoir est retiré
scoreboard players operation $hid mg.st = @s mg.hid
execute as @e[type=minecraft:item_display,tag=mg.hatf] if score @s mg.hid = $hid mg.st run kill @s
tag @s remove mg.hatd
