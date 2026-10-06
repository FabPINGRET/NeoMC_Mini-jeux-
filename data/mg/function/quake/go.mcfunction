# Quakecraft — début de partie
scoreboard players operation $tl mg.st = $qt mg.st
tag @a remove mg.prot
tag @a remove mg.qdd
tag @a remove mg.qsh
scoreboard players reset @a mg.qs
scoreboard players reset @a mg.gi
scoreboard players set @a[tag=mg.play] mg.ks 0
scoreboard players reset @a mg.us
kill @e[type=minecraft:marker,tag=mg.grm]
scoreboard players set @a[tag=mg.play] mg.qk 0
scoreboard players set @a[tag=mg.play] mg.cd 0
scoreboard players set @a[tag=mg.play] mg.deaths 0
gamemode adventure @a[tag=mg.play]
execute as @a[tag=mg.play] run function mg:quake/kit
execute as @a[tag=mg.play] run function mg:quake/fx
scoreboard objectives setdisplay sidebar mg.qk
tellraw @a[tag=mg.play] [{"text":"⚡ QUAKECRAFT : ","color":"aqua","bold":true},{"text":"clic droit avec le railgun pour tirer un rayon instantané. Un tir qui touche = un kill (tu réapparais ailleurs en 2 s d'invincibilité). Premier à ","color":"gray"},{"score":{"name":"$qg","objective":"mg.st"},"color":"gold"},{"text":" kills gagne, sinon le meilleur quand le temps est écoulé !","color":"gray"}]
