# Paintball — tick de jeu

# Cadence de tir
execute as @a[tag=mg.play,scores={mg.cd=1..}] run scoreboard players remove @s mg.cd 1

# Attente au respawn (3 s immobilisé)
execute as @a[tag=mg.play,scores={mg.cd=21..}] run function mg:paintball/respawn_wait

# Tirs
execute as @a[tag=mg.play,scores={mg.qs=1..}] run function mg:paintball/shoot

# Encre, peinture sous les pieds, récupération des touches
execute as @a[tag=mg.play] at @s run function mg:paintball/ink_tick

# Invincibilité après réapparition
execute as @a[tag=mg.prot] run function mg:quake/prot_tick

# Mort accidentelle → retour à la base
execute as @a[tag=mg.play,scores={mg.deaths=1..}] run function mg:paintball/respawn

# Affichage : pourcentage de terrain peint et temps restant
scoreboard players operation Orange mg.pb = $pa mg.st
scoreboard players operation Orange mg.pb *= $c100 mg.st
scoreboard players operation Orange mg.pb /= $pt mg.st
scoreboard players operation Bleu mg.pb = $pb mg.st
scoreboard players operation Bleu mg.pb *= $c100 mg.st
scoreboard players operation Bleu mg.pb /= $pt mg.st
scoreboard players operation Temps mg.pb = $tl mg.st
scoreboard players operation Temps mg.pb /= $c20 mg.st

# Minuteur
scoreboard players remove $tl mg.st 1
execute if score $tl mg.st matches 1200 run tellraw @a[tag=mg.play] [{"text":"▓ Plus qu'une minute !","color":"gold"}]
execute if score $tl mg.st matches 200 run tellraw @a[tag=mg.play] [{"text":"▓ 10 secondes !","color":"red"}]

# Fin : le plus de terrain peint gagne
execute if score $state mg.st matches 2 if score $tl mg.st matches ..0 if score $pa mg.st > $pb mg.st run return run function mg:paintball/win_orange
execute if score $state mg.st matches 2 if score $tl mg.st matches ..0 if score $pb mg.st > $pa mg.st run return run function mg:paintball/win_blue
execute if score $state mg.st matches 2 if score $tl mg.st matches ..0 run return run function mg:core/draw
