# Fin : points de chaque cacheur et meilleur cacheur
scoreboard players set $phb mg.st 0
execute as @a[tag=mg.phx] run scoreboard players operation $phb mg.st > @s mg.phpt
execute if score $phb mg.st matches ..0 run return 0
tellraw @a[tag=mg.phx] {"text":"🎭 Points des cacheurs (regardés par les chercheurs, en mouvement) :","color":"gold"}
execute as @a[tag=mg.phx,scores={mg.phpt=1..}] run tellraw @a[tag=mg.phx] [{"text":" • ","color":"gray"},{"selector":"@s","color":"yellow"},{"text":" : ","color":"gray"},{"score":{"name":"@s","objective":"mg.phpt"},"color":"aqua","bold":true}]
execute as @a[tag=mg.phx] if score @s mg.phpt = $phb mg.st run tellraw @a [{"text":"🏆 Meilleur cacheur : ","color":"gold","bold":true},{"selector":"@s","color":"yellow"},{"text":" (","color":"gray"},{"score":{"name":"$phb","objective":"mg.st"},"color":"aqua"},{"text":" points)","color":"gray"}]
