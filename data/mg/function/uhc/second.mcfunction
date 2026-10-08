# Chaque seconde : zone (40 → 5 entre 2:30 et 5:00) et affichage
scoreboard players operation $uhs mg.st = $uht mg.st
scoreboard players operation $uhs mg.st /= #20 mg.st
execute if score $uhs mg.st matches 150.. run scoreboard players set $zr mg.st 40
execute if score $uhs mg.st matches 150.. run scoreboard players operation $uhz mg.st = $uhs mg.st
execute if score $uhs mg.st matches 150.. run scoreboard players remove $uhz mg.st 150
execute if score $uhs mg.st matches 150.. run scoreboard players operation $uhz mg.st *= #7 mg.st
execute if score $uhs mg.st matches 150.. run scoreboard players operation $uhz mg.st /= #30 mg.st
execute if score $uhs mg.st matches 150.. run scoreboard players operation $zr mg.st -= $uhz mg.st
execute if score $zr mg.st matches ..4 run scoreboard players set $zr mg.st 5
execute if score $uhs mg.st matches 150.. run function mg:uhc/zone
scoreboard players set $uhl mg.st 150
scoreboard players operation $uhl mg.st -= $uhs mg.st
execute if score $uhs mg.st matches ..149 run title @a[tag=mg.play] actionbar [{"text":"⛏ Farm — PvP dans ","color":"green"},{"score":{"name":"$uhl","objective":"mg.st"},"color":"yellow","bold":true},{"text":" s","color":"green"}]
execute if score $uhs mg.st matches 150.. run title @a[tag=mg.play,tag=!mg.zout] actionbar [{"text":"⚔ PvP — zone ","color":"red"},{"score":{"name":"$zr","objective":"mg.st"},"color":"yellow","bold":true},{"text":" blocs du centre — en vie : ","color":"red"},{"score":{"name":"$alive","objective":"mg.st"},"color":"yellow"}]
