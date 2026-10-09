# @s : véhicule (cheval ou ghast) retiré sans explosion : sa carrosserie et sa zone cliquable aussi
scoreboard players operation $gv mg.st = @s mg.gvid
execute as @e[type=minecraft:block_display] if score @s mg.gvid = $gv mg.st run kill @s
execute as @e[type=minecraft:interaction] if score @s mg.gvid = $gv mg.st run kill @s
tp @s ~ -300 ~
