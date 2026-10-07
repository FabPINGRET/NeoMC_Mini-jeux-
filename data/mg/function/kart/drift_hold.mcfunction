# Le nez pivote vers l'intérieur (la trajectoire suit avec retard, voir heading) ; la direction resserre ou élargit
scoreboard players add @s mg.kdr 1
scoreboard players operation $kt mg.st = @s mg.kdd
scoreboard players operation $kt mg.st *= #k60 mg.st
execute if score @s mg.kdd matches -1 if score $kl mg.st matches 1 run scoreboard players remove $kt mg.st 30
execute if score @s mg.kdd matches -1 if score $kr mg.st matches 1 run scoreboard players add $kt mg.st 35
execute if score @s mg.kdd matches 1 if score $kr mg.st matches 1 run scoreboard players add $kt mg.st 30
execute if score @s mg.kdd matches 1 if score $kl mg.st matches 1 run scoreboard players remove $kt mg.st 35
execute if score @s mg.kdr matches 20 at @s run playsound minecraft:block.amethyst_block.chime master @s ~ ~ ~ 1 1.0
execute if score @s mg.kdr matches 45 at @s run playsound minecraft:block.amethyst_block.chime master @s ~ ~ ~ 1 1.4
execute if score @s mg.kdr matches 80 at @s run playsound minecraft:block.amethyst_block.chime master @s ~ ~ ~ 1 1.9
