# Survie en vol, chaque tick (@s = participant, positionné)
scoreboard players add @s mg.skg 1
execute if score @s mg.skg matches 1.. if predicate mg:gliding run scoreboard players set @s mg.skg 0
execute if score $skpo mg.st matches 1 if entity @s[x=-8,y=195,z=28992,dx=16,dy=6,dz=16] run scoreboard players set @s mg.skg -40
execute if score @s mg.skl matches 101.. run scoreboard players set @s mg.skg -20
execute unless entity @s[y=96,dy=400] run return run function mg:sky/s_elim {why:"est tombé dans le vide"}
execute if score @s mg.skg matches 20.. run return run function mg:sky/s_elim {why:"s'est posé"}
execute if score @s mg.sko matches 60.. run return run function mg:sky/s_elim {why:"est resté hors de la zone"}
execute if score @s mg.sko matches 1.. run return run title @s actionbar [{"text":"⚠ HORS DE LA ZONE — reviens vers le centre ! ","color":"red","bold":true},{"score":{"name":"@s","objective":"mg.sko"},"color":"yellow"},{"text":"/60","color":"gray"}]
execute if score @s mg.skl matches 101.. run return run title @s actionbar [{"text":"💨 Colonne de vent !","color":"aqua","bold":true}]
execute if score $skt mg.st matches ..3599 run title @s actionbar [{"text":"🪽 En vol : ","color":"aqua"},{"score":{"name":"$skn","objective":"mg.st"},"color":"white"},{"text":"   ◯ zone ","color":"gray"},{"score":{"name":"$skzr","objective":"mg.st"},"color":"red"},{"text":" blocs   🚀 dans ","color":"gray"},{"score":{"name":"$skfs","objective":"mg.st"},"color":"gold"},{"text":" s","color":"gray"}]
execute if score $skt mg.st matches 3600.. run title @s actionbar [{"text":"🌪 MORT SUBITE","color":"red","bold":true},{"text":"   🪽 En vol : ","color":"aqua","bold":false},{"score":{"name":"$skn","objective":"mg.st"},"color":"white","bold":false}]
