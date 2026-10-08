# Chaque seconde : zone 50 → 6 entre 3:00 et 5:00 (+10 s de compte à rebours)
scoreboard players operation $hgs mg.st = $hgt mg.st
scoreboard players operation $hgs mg.st /= #20 mg.st
execute if score $hgs mg.st matches 190.. run scoreboard players set $zr mg.st 50
execute if score $hgs mg.st matches 190.. run scoreboard players operation $hgz mg.st = $hgs mg.st
execute if score $hgs mg.st matches 190.. run scoreboard players remove $hgz mg.st 190
execute if score $hgs mg.st matches 190.. run scoreboard players operation $hgz mg.st *= #11 mg.st
execute if score $hgs mg.st matches 190.. run scoreboard players operation $hgz mg.st /= #30 mg.st
execute if score $hgs mg.st matches 190.. run scoreboard players operation $zr mg.st -= $hgz mg.st
execute if score $zr mg.st matches ..5 run scoreboard players set $zr mg.st 6
execute if score $hgs mg.st matches 190.. run function mg:hg/zone
execute if score $hgs mg.st matches 10..189 run title @a[tag=mg.play] actionbar [{"text":"🏹 En vie : ","color":"gold"},{"score":{"name":"$alive","objective":"mg.st"},"color":"yellow","bold":true}]
execute if score $hgs mg.st matches 190.. run title @a[tag=mg.play,tag=!mg.zout] actionbar [{"text":"🏹 Zone ","color":"red"},{"score":{"name":"$zr","objective":"mg.st"},"color":"yellow","bold":true},{"text":" blocs du centre — en vie : ","color":"red"},{"score":{"name":"$alive","objective":"mg.st"},"color":"yellow"}]
