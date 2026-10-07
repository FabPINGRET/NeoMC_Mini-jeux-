# Lancer d'un mouton (@s = joueur ; $ty = type : 0 normal, 1 espace, 2 nausée, 3 glace, 4 ténèbres, 5 feu, 6 super explosif, 7 ultra explosif, 8 mitraillette)
scoreboard players set $sw mg.st 0
execute if score $game mg.st matches 5 run scoreboard players set $sw mg.st 1
execute if score $game mg.st matches 7 run scoreboard players set $sw mg.st 1
execute unless score $state mg.st matches 2 run return 0
execute unless score $sw mg.st matches 1 run return 0
execute unless entity @s[tag=mg.play] run return 0

# Micro-délai d'1 s entre deux lancers : le mouton « consommé » trop tôt est rendu
execute if score @s mg.cd matches 1.. run return run function mg:sheepwar/refund

scoreboard players set @s mg.cd 10
execute at @s anchored eyes run function mg:sheepwar/launch
