# Spleef — l'arène rétrécit (appelé toutes les 12 s après les 40 premières secondes)
scoreboard players add $ss mg.st 1
scoreboard players set $sk mg.st 240
execute if score $ss mg.st matches 1 run function mg:spleef/shrink_1
execute if score $ss mg.st matches 2 run function mg:spleef/shrink_2
execute if score $ss mg.st matches 3 run function mg:spleef/shrink_3
execute if score $ss mg.st matches 4 run function mg:spleef/shrink_4
execute if score $ss mg.st matches 5 run function mg:spleef/shrink_5
execute if score $ss mg.st matches 6 run function mg:spleef/shrink_6
execute if score $ss mg.st matches 7 run function mg:spleef/shrink_7
execute if score $ss mg.st matches 8 run function mg:spleef/shrink_8
execute if score $ss mg.st matches 9 run function mg:spleef/shrink_9
execute if score $ss mg.st matches 10 run function mg:spleef/shrink_10
execute as @a[tag=!mg.surv] at @s run playsound minecraft:block.snow.break master @s ~ ~ ~ 1 0.6
