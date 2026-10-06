# Retour à la base (@s) : touches remises à zéro, encre pleine, 2 s d'invincibilité
scoreboard players set @s mg.deaths 0
scoreboard players set @s mg.ph 0
scoreboard players set @s mg.pt 0
scoreboard players set @s mg.pi 200
scoreboard players set @s mg.cd 0
function mg:paintball/base_tp
tag @s add mg.prot
scoreboard players set @s mg.qp 40
