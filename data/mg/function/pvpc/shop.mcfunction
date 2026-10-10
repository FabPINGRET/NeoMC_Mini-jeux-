# @s ouvre la boutique (fenêtre avec son solde)
scoreboard players enable @s mg.pshop
execute store result storage mg:pvpc s.c int 1 run scoreboard players get @s mg.pco
function mg:pvpc/shop_show with storage mg:pvpc s
