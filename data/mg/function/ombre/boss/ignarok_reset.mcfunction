# Ignarok, dragon de feu : plus personne, le combat est remis à zéro
scoreboard players set $ob5 mg.st 0
bossbar set mg:olb5 players
execute as @e[tag=mg.olb_ignarok] run kill @s
kill @e[tag=mg.olminion_ignarok]
kill @e[tag=mg.oljar]
