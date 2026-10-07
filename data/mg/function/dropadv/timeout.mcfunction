# Temps écoulé : le plus avancé gagne (à égalité, le moins d'échecs)
execute as @a[tag=mg.play] run scoreboard players operation @s mg.t = @s mg.dlv
execute as @a[tag=mg.play] run scoreboard players operation @s mg.t *= #k1000 mg.st
execute as @a[tag=mg.play] run scoreboard players operation @s mg.t -= @s mg.dfl
scoreboard players set $dbest mg.st -999999
execute as @a[tag=mg.play] if score @s mg.t > $dbest mg.st run scoreboard players operation $dbest mg.st = @s mg.t
tellraw @a[tag=!mg.surv] [{"text":"⏱ Temps écoulé !","color":"gold"}]
execute as @a[tag=mg.play] if score @s mg.t = $dbest mg.st run tag @s add mg.dwin
execute as @a[tag=mg.dwin,limit=1] run function mg:core/win_player
tag @a remove mg.dwin
