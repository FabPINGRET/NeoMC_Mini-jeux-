# Pendant le compte à rebours : prise en compte des choix de kart
execute unless score $game mg.st matches 61 run return 0
execute unless score $state mg.st matches 1 run return 0
scoreboard players enable @a[tag=mg.play] mg.kch
execute as @a[tag=mg.play] if score @s mg.kch matches 1.. run function mg:kart/choose
schedule function mg:kart/pre_tick 5t
