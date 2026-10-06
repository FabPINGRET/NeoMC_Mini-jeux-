# Course de bateaux sur glace — tick de jeu

# Les joueurs restent dans leur bateau
execute as @a[tag=mg.play] run function mg:icerace/ride_check

# Points de passage / tours
execute as @a[tag=mg.play] run function mg:icerace/cp_check

# Hors piste → dernier point de passage
execute as @a[tag=mg.play] store result score @s mg.t run data get entity @s Pos[1]
execute as @a[tag=mg.play,scores={mg.t=..72}] run function mg:icerace/rescue

# Limite de temps : 4 minutes
scoreboard players add $rt mg.st 1
execute if score $state mg.st matches 2 if score $rt mg.st matches 4800 run function mg:icerace/timeout
execute if score $rt mg.st matches 3600 run tellraw @a[tag=mg.play] [{"text":"⛵ Plus qu'une minute !","color":"gold"}]

# Plus personne → égalité
execute if score $state mg.st matches 2 unless entity @a[tag=mg.play] run function mg:core/draw
