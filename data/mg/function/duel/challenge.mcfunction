# Défi (@s = défieur ; #dlv = 1000 + id de l'adversaire)
scoreboard players operation $dlt mg.st = #dlv mg.st
scoreboard players remove $dlt mg.st 1000
execute as @a if score @s mg.dlid = $dlt mg.st run tag @s add mg.dltg
function mg:duel/challenge_chk
tag @a remove mg.dltg
