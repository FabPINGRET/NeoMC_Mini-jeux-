# Décompte avant l'ouverture des sols (3 s)
scoreboard players remove $dtm mg.st 1
execute if score $dtm mg.st matches 40 run title @a[tag=mg.play] actionbar [{"text":"3","color":"yellow","bold":true}]
execute if score $dtm mg.st matches 20 run title @a[tag=mg.play] actionbar [{"text":"2","color":"gold","bold":true}]
execute if score $dtm mg.st matches 1 run title @a[tag=mg.play] actionbar [{"text":"1","color":"red","bold":true}]
execute if score $dtm mg.st matches ..0 run function mg:dropper/start_round
