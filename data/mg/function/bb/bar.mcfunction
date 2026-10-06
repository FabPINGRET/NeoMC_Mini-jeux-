# Barre d'action : thème + temps restant
scoreboard players set $bbsec mg.st 4800
scoreboard players operation $bbsec mg.st -= $bbt mg.st
scoreboard players operation $bbsec mg.st /= $bbc20 mg.st
scoreboard players operation $bbmm mg.st = $bbsec mg.st
scoreboard players operation $bbmm mg.st /= $bbc60 mg.st
scoreboard players operation $bbss mg.st = $bbsec mg.st
scoreboard players operation $bbss mg.st %= $bbc60 mg.st
execute if score $bbss mg.st matches 10.. run title @a[tag=mg.play] actionbar [{"text":"✎ ","color":"gold"},{"nbt":"word","storage":"mg:bb","color":"yellow","bold":true},{"text":"   ⏱ ","color":"gray"},{"score":{"name":"$bbmm","objective":"mg.st"},"color":"white"},{"text":":","color":"white"},{"score":{"name":"$bbss","objective":"mg.st"},"color":"white"}]
execute if score $bbss mg.st matches ..9 run title @a[tag=mg.play] actionbar [{"text":"✎ ","color":"gold"},{"nbt":"word","storage":"mg:bb","color":"yellow","bold":true},{"text":"   ⏱ ","color":"gray"},{"score":{"name":"$bbmm","objective":"mg.st"},"color":"white"},{"text":":0","color":"white"},{"score":{"name":"$bbss","objective":"mg.st"},"color":"white"}]
