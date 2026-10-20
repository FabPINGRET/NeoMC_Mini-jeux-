# Tube de lave : l'alpha dort encore (salles nettoyées = état / 2)
scoreboard players operation $trwn mg.st = $trds3 mg.st
scoreboard players operation $trwn mg.st /= #2 mg.st
execute positioned -23.5 90 186.5 as @a[tag=mg.tvw,gamemode=adventure,distance=..12] run title @s actionbar [{"text":"🔒 L'alpha dort encore : salles nettoyées ","color":"gray"},{"score":{"name":"$trwn","objective":"mg.st"},"color":"yellow","bold":true},{"text":" / 3","color":"gray"}]
execute positioned -23.5 90 186.5 run scoreboard players set @a[tag=mg.tvw,gamemode=adventure,distance=..12] mg.tval 30
