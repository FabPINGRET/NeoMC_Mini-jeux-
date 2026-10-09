# @s : requilleur — balaye les quilles tombées, remet un jeu complet si besoin, rend la boule
scoreboard players operation #ln mg.st = @s mg.bln
execute if score @s mg.btm matches 20 as @e[type=minecraft:block_display,tag=mg.bpdn] if score @s mg.bln = #ln mg.st at @s run particle minecraft:poof ~ ~0.2 ~ 0.1 0.1 0.1 0.01 2
execute if score @s mg.btm matches 20 as @e[type=minecraft:block_display,tag=mg.bpdn] if score @s mg.bln = #ln mg.st run kill @s
execute if score @s mg.btm matches 20 at @s run playsound minecraft:block.piston.contract master @s ~ ~ ~ 0.4 0.8
execute if score @s mg.btm matches 28 if entity @s[tag=mg.bnr] unless score @s mg.brl matches 4 run function mg:bowl/rack
execute if score @s mg.btm matches 40.. if score @s mg.brl matches 4 run return run function mg:bowl/done
execute if score @s mg.btm matches 40.. run function mg:bowl/to_aim
