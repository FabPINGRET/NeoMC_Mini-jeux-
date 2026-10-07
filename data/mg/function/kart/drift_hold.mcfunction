# Virage forcé dans le sens du dérapage, la direction le resserre ou l'élargit
scoreboard players add @s mg.kdr 1
scoreboard players operation $kt mg.st = @s mg.kdd
scoreboard players operation $kt mg.st *= #k5 mg.st
execute if score @s mg.kdd matches -1 if score $kl mg.st matches 1 run scoreboard players remove $kt mg.st 2
execute if score @s mg.kdd matches -1 if score $kr mg.st matches 1 run scoreboard players add $kt mg.st 3
execute if score @s mg.kdd matches 1 if score $kr mg.st matches 1 run scoreboard players add $kt mg.st 2
execute if score @s mg.kdd matches 1 if score $kl mg.st matches 1 run scoreboard players remove $kt mg.st 3
execute if score @s mg.kdr matches 25 at @s run playsound minecraft:block.amethyst_block.chime master @s ~ ~ ~ 1 1.2
execute if score @s mg.kdr matches 55 at @s run playsound minecraft:block.amethyst_block.chime master @s ~ ~ ~ 1 1.8
