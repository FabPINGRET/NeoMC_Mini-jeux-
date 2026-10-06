scoreboard players add $bpc mg.st 1
execute if score $bpc mg.st matches 100 run function mg:mobarena/cathedral/vexes
execute if score $bpc mg.st matches 200 run function mg:mobarena/cathedral/vexes
execute if score $bpc mg.st matches 200 run title @a actionbar [{"text":"Le Comte de Sang réapparaît !","color":"dark_red","bold":true}]
execute if score $bpc mg.st matches 200 run scoreboard players set $bpc mg.st 0
execute if score $bpc mg.st matches 0 run bossbar set mg:boss color red
