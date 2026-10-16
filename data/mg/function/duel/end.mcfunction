# Fin de duel de l'arène $dli (le gagnant porte mg.dlwn) : +1 victoire, retour au lobby des deux joueurs
execute as @a[tag=mg.dl] if score @s mg.dli = $dli mg.st run tag @s add mg.dlsp
scoreboard players add @a[tag=mg.dlwn,limit=1] mg.dlw 1
tellraw @a[tag=mg.dlwn,limit=1] [{"text":"⚔ Victoire ! Duels gagnés : ","color":"green"},{"score":{"name":"@s","objective":"mg.dlw"},"color":"gold"}]
execute as @a[tag=mg.dlwn,limit=1] at @s run playsound minecraft:entity.player.levelup master @s ~ ~ ~ 1 1.2
execute as @a[tag=mg.dlsp] run function mg:duel/stop
tag @a remove mg.dlwn
