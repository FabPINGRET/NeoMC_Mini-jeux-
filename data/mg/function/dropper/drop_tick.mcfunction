# Manche en cours
scoreboard players remove @a[tag=mg.play,scores={mg.cd=1..}] mg.cd 1

# Réussite : les pieds dans l'eau
execute as @a[tag=mg.play] at @s if block ~ ~ ~ minecraft:water run function mg:dropper/success

# Raté : posé sur un obstacle ou sur le sol, c'est-à-dire sous le niveau du rebord de départ (y 121)
execute as @a[tag=mg.play] store result score @s mg.t run data get entity @s Pos[1]
execute if score $dph mg.st matches 1 as @a[tag=mg.play,scores={mg.cd=0,mg.t=..118}] at @s if data entity @s {OnGround:1b} unless block ~ ~ ~ minecraft:water run function mg:dropper/fail

# Nom du leader en actionbar toutes les secondes : rien (les points sont sous les pseudos)
