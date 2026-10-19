# Le Colosse de runes : plus personne, le combat est remis à zéro
scoreboard players set $ob6 mg.st 0
bossbar set mg:olb6 players
execute as @e[tag=mg.olb_colosse] run kill @s
kill @e[tag=mg.olminion_colosse]
kill @e[tag=mg.oljar]
function mg:ombre/boss/colosse/pill_reset
