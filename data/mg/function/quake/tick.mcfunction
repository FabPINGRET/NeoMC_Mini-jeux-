# Quakecraft — tick de jeu

# Rechargement du railgun : message « prêt » puis décompte
execute as @a[tag=mg.play,scores={mg.cd=1}] run title @s actionbar [{"text":"⚡ Railgun prêt","color":"aqua"}]
execute as @a[tag=mg.play,scores={mg.cd=1}] at @s run playsound minecraft:block.note_block.hat master @s ~ ~ ~ 0.6 2
execute as @a[tag=mg.play,scores={mg.cd=1..}] run scoreboard players remove @s mg.cd 1

# Tirs
execute as @a[tag=mg.play,scores={mg.qs=1..}] run function mg:quake/shoot

# Grenades (rares) : lancer + marqueurs en vol
execute as @a[tag=mg.play,scores={mg.us=1..}] at @s run function mg:quake/gren_throw
execute as @e[type=minecraft:marker,tag=mg.grm] at @s run function mg:quake/gren_tick

# Joueurs éliminés : compte à rebours avant la réapparition
execute as @a[tag=mg.qdd] run function mg:quake/dead_tick

# Invincibilité après réapparition
execute as @a[tag=mg.prot] run function mg:quake/prot_tick

# Chute dans le vide / mort accidentelle → réapparition
execute as @a[tag=mg.play] store result score @s mg.t run data get entity @s Pos[1]
execute as @a[tag=mg.play,scores={mg.t=..70}] run function mg:quake/respawn
execute as @a[tag=mg.play,scores={mg.deaths=1..}] run function mg:quake/respawn

# Minuteur
scoreboard players remove $tl mg.st 1
execute if score $tl mg.st matches 1200 run tellraw @a[tag=mg.play] [{"text":"⚡ Plus qu'une minute !","color":"aqua"}]

# Victoire : objectif de kills atteint
execute if score $state mg.st matches 2 as @a[tag=mg.play] if score @s mg.qk >= $qg mg.st run return run function mg:core/win_player
# Fin du temps : le meilleur (égalité = match nul)
execute if score $state mg.st matches 2 if score $tl mg.st matches ..0 run return run function mg:quake/timeout
# Plus qu'un joueur
execute store result score $alive mg.st if entity @a[tag=mg.play]
execute if score $state mg.st matches 2 if score $n0 mg.st matches 2.. if score $alive mg.st matches 1 as @a[tag=mg.play,limit=1] run return run function mg:core/win_player
execute if score $state mg.st matches 2 if score $alive mg.st matches 0 run function mg:core/draw
