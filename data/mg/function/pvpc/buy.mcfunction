# @s achète l'article mg.pshop
scoreboard players operation $b mg.st = @s mg.pshop
scoreboard players reset @s mg.pshop
scoreboard players enable @s mg.pshop
execute if score $b mg.st matches 1 run return run function mg:pvpc/buy_1
execute if score $b mg.st matches 2 run return run function mg:pvpc/buy_2
execute if score $b mg.st matches 3 run return run function mg:pvpc/buy_3
execute if score $b mg.st matches 4 run return run function mg:pvpc/buy_4
execute if score $b mg.st matches 5 run return run function mg:pvpc/buy_5
execute if score $b mg.st matches 6 run return run function mg:pvpc/buy_6
execute if score $b mg.st matches 7 run return run function mg:pvpc/buy_7
execute if score $b mg.st matches 8 run return run function mg:pvpc/buy_8
execute if score $b mg.st matches 9 run return run function mg:pvpc/buy_9
execute if score $b mg.st matches 10 run return run function mg:pvpc/buy_10
execute if score $b mg.st matches 11 run return run function mg:pvpc/buy_11
execute if score $b mg.st matches 12 run return run function mg:pvpc/buy_12
