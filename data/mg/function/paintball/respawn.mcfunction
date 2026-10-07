# Retour à la base (@s) : touches remises à zéro, encre pleine, 3 s d'attente (immobilisé, tir bloqué) puis 2 s d'invincibilité
scoreboard players set @s mg.deaths 0
scoreboard players set @s mg.ph 0
scoreboard players set @s mg.pt 0
scoreboard players set @s mg.pi 200
# mg.cd = 20 (cadence) + 60 ticks d'attente : le tir est bloqué tant que mg.cd >= 1
scoreboard players set @s mg.cd 80
function mg:paintball/base_tp
tag @s add mg.prot
scoreboard players set @s mg.qp 100
