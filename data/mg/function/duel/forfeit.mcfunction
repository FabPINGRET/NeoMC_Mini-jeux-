# Abandon ou chute hors de l'arène (@s = le perdant) : l'adversaire gagne
# (déjà sorti du duel par un forfait plus tôt dans le même tick : rien)
execute unless entity @s[tag=mg.dl] run return 0
scoreboard players operation $dli mg.st = @s mg.dli
tag @s add mg.dlfl
execute as @a[tag=mg.dl,tag=!mg.dlfl] if score @s mg.dli = $dli mg.st run tag @s add mg.dlwn
tellraw @a[tag=mg.dlwn] [{"selector":"@s","color":"red"},{"text":" abandonne le duel : victoire par forfait.","color":"green"}]
tellraw @s [{"text":"⚔ Tu perds le duel par forfait.","color":"gray"}]
tag @s remove mg.dlfl
function mg:duel/end
