# Fin : le plus de niveaux réussis (mg.dok), puis le moins d'essais (mg.dtt) ; personne n'a réussi de niveau : match nul
execute unless score $state mg.st matches 2 run return 0
execute if score $dat mg.st matches 36000.. run tellraw @a[tag=!mg.surv] [{"text":"⏱ Temps écoulé !","color":"gold"}]
execute as @a[tag=mg.play] run tellraw @a[tag=!mg.surv] [{"selector":"@s","color":"yellow"},{"text":" : ","color":"gray"},{"score":{"name":"@s","objective":"mg.dok"},"color":"white","bold":true},{"text":"/13 réussis, ","color":"gray"},{"score":{"name":"@s","objective":"mg.dsk"},"color":"white"},{"text":" passé(s), ","color":"gray"},{"score":{"name":"@s","objective":"mg.dtt"},"color":"white"},{"text":" essais","color":"gray"}]
execute unless entity @a[tag=mg.play,scores={mg.dok=1..}] run return run function mg:core/draw
# score = niveaux réussis × 1 000 000 − essais (au plus 13 millions : pas de dépassement)
execute as @a[tag=mg.play] run scoreboard players operation @s mg.t = @s mg.dok
execute as @a[tag=mg.play] run scoreboard players operation @s mg.t *= #k1000 mg.st
execute as @a[tag=mg.play] run scoreboard players operation @s mg.t *= #k1000 mg.st
execute as @a[tag=mg.play] run scoreboard players operation @s mg.t -= @s mg.dtt
scoreboard players set $dbest mg.st -999999999
execute as @a[tag=mg.play] if score @s mg.t > $dbest mg.st run scoreboard players operation $dbest mg.st = @s mg.t
execute as @a[tag=mg.play] if score @s mg.t = $dbest mg.st run tag @s add mg.dwin
execute as @a[tag=mg.dwin,limit=1] run function mg:core/win_player
tag @a remove mg.dwin
