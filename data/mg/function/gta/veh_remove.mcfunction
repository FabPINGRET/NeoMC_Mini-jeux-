# @s : véhicule (cheval ou ghast) retiré sans explosion : sa carrosserie aussi
scoreboard players operation $gv mg.st = @s mg.gvid
execute as @e[type=minecraft:block_display] if score @s mg.gvid = $gv mg.st run kill @s
tp @s ~ -300 ~
