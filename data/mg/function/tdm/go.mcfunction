# Départ
scoreboard players set $tmt mg.st 0
# premier pack de soin 20 s après le GO
scoreboard players set $tmhc mg.st 400
# la protection posée par spawn pendant le prepare ne court qu'à partir d'ici : on tire dès le GO
tag @a remove mg.tmp
scoreboard players reset @a mg.tmx
title @a[tag=mg.play] actionbar ""
execute as @a[tag=mg.play] run function mg:tdm/kit
# core/begin vient de retirer la résistance du compte à rebours : pas de mort hors tir (coups de poing), pas de dégâts de chute
execute as @a[tag=mg.play] run function mg:tdm/buffs
scoreboard players set @a mg.deaths 0
scoreboard players set Rouge mg.tmk 0
scoreboard players set Bleu mg.tmk 0
scoreboard objectives setdisplay sidebar mg.tmk
tellraw @a[tag=mg.play] [{"text":"🎯 TDM SNIPER : ","color":"gold","bold":true},{"text":"tête = élimination, corps = 2 touches. Clic gauche : tir · clic droit : lunette. Tu réapparais tout de suite (3 s de protection). 25 frags pour gagner l'équipe, 8 min max. Pas de tir ami.","color":"gray"}]
execute unless score $n0 mg.st matches 2.. run tellraw @a[tag=mg.play] {"text":"🎯 Mode entraînement (seul) : pas d'adversaire ni de victoire ; il faut au moins 2 joueurs pour une vraie partie.","color":"yellow"}
