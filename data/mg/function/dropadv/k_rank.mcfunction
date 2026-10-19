# Aventure : classement aux niveaux réussis (puis le moins d'échecs) ; personne n'a réussi de niveau : match nul
execute unless score $state mg.st matches 2 run return 0
execute as @a[tag=mg.play] run tellraw @a[tag=!mg.surv] [{"selector":"@s","color":"yellow"},{"text":" : ","color":"gray"},{"score":{"name":"@s","objective":"mg.dok"},"color":"white","bold":true},{"text":"/13 réussis, ","color":"gray"},{"score":{"name":"@s","objective":"mg.dsk"},"color":"white"},{"text":" passé(s), ","color":"gray"},{"score":{"name":"@s","objective":"mg.dfl"},"color":"white"},{"text":" échec(s)","color":"gray"}]
execute unless entity @a[tag=mg.play,scores={mg.dok=1..}] run return run function mg:core/draw
execute as @a[tag=mg.play] run scoreboard players operation @s mg.t = @s mg.dok
execute as @a[tag=mg.play] run scoreboard players operation @s mg.t *= #k1000 mg.st
execute as @a[tag=mg.play] run scoreboard players operation @s mg.t *= #k1000 mg.st
execute as @a[tag=mg.play] run scoreboard players operation @s mg.t -= @s mg.dfl
scoreboard players set $dbest mg.st -999999999
execute as @a[tag=mg.play] if score @s mg.t > $dbest mg.st run scoreboard players operation $dbest mg.st = @s mg.t
execute as @a[tag=mg.play] if score @s mg.t = $dbest mg.st run tag @s add mg.dwin
execute as @a[tag=mg.dwin,limit=1] run function mg:core/win_player
tag @a remove mg.dwin
