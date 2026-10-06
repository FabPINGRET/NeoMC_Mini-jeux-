# Spleef — préparation (appelé au lancement)
function mg:spleef/build

# Nombre d'étages selon les joueurs : solo 1, 2-3 → 2, 4-5 → 3, 6+ → 4
scoreboard players set $nf mg.st 4
execute if score $n0 mg.st matches ..5 run scoreboard players set $nf mg.st 3
execute if score $n0 mg.st matches ..3 run scoreboard players set $nf mg.st 2
execute if score $n0 mg.st matches ..1 run scoreboard players set $nf mg.st 1
function mg:spleef/trim

# Hauteur d'élimination = 4 blocs sous le dernier étage (80, 73, 66, 59)
scoreboard players set $yd mg.st 55
execute if score $nf mg.st matches 3 run scoreboard players set $yd mg.st 62
execute if score $nf mg.st matches 2 run scoreboard players set $yd mg.st 69
execute if score $nf mg.st matches 1 run scoreboard players set $yd mg.st 76

# Perchoir spectateur
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 88
scoreboard players set $pz mg.st 300

gamemode adventure @a[tag=mg.play]
execute as @a[tag=mg.play] run spawnpoint @s 0 88 300
spreadplayers 0 300 4 13 under 82 false @a[tag=mg.play]
