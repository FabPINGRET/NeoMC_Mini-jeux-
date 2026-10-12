# @s (marqueur) suit sa grenade ; grenade disparue = elle s'est posée ici
scoreboard players operation $zq mg.st = @s mg.zmi
scoreboard players set $zf mg.st 0
tag @s add mg.zme
execute as @e[type=minecraft:snowball,tag=mg.zms] if score @s mg.zmi = $zq mg.st at @s run function mg:zx/mk_pos
tag @s remove mg.zme
execute if score $zf mg.st matches 0 at @s run function mg:zx/mk_land
