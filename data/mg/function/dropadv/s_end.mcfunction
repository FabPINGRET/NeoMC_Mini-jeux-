# Fin : le moins d'essais parmi ceux qui ont fini ; personne n'a fini → le plus avancé (Aventure)
execute if score $dat mg.st matches 36000.. run tellraw @a[tag=!mg.surv] [{"text":"⏱ Temps écoulé !","color":"gold"}]
scoreboard players set $dbest mg.st 999999
execute as @a[tag=mg.play,tag=mg.ddone] if score @s mg.dtt < $dbest mg.st run scoreboard players operation $dbest mg.st = @s mg.dtt
execute if score $dbest mg.st matches 999999 run return run function mg:dropadv/timeout
execute as @a[tag=mg.play,tag=mg.ddone] if score @s mg.dtt = $dbest mg.st run tag @s add mg.dwin
execute as @a[tag=mg.dwin,limit=1] run function mg:core/win_player
tag @a remove mg.dwin
