# Feu vert : « 1… 2… 3… » (titre + note de plus en plus aiguë) et barre de temps restant (barre d'action)
scoreboard players operation $k mg.st = $sqg mg.st
scoreboard players operation $k mg.st -= $sqt mg.st
scoreboard players operation $k mg.st *= #3 mg.st
scoreboard players operation $k mg.st /= $sqg mg.st
execute if score $k mg.st matches 3.. run scoreboard players set $k mg.st 2
execute unless score $k mg.st = $sqk mg.st run function mg:soleil/count_step
scoreboard players set #10 mg.st 10
scoreboard players operation $b mg.st = $sqt mg.st
scoreboard players operation $b mg.st *= #10 mg.st
scoreboard players operation $b mg.st /= $sqg mg.st
execute if score $b mg.st matches 0 run title @a[tag=mg.play] actionbar [{"text":"🟢 ","color":"red"},{"text":"","color":"red"},{"text":"██████████","color":"dark_gray"},{"text":" avance !","color":"red","bold":true}]
execute if score $b mg.st matches 1 run title @a[tag=mg.play] actionbar [{"text":"🟢 ","color":"red"},{"text":"█","color":"red"},{"text":"█████████","color":"dark_gray"},{"text":" avance !","color":"red","bold":true}]
execute if score $b mg.st matches 2 run title @a[tag=mg.play] actionbar [{"text":"🟢 ","color":"red"},{"text":"██","color":"red"},{"text":"████████","color":"dark_gray"},{"text":" avance !","color":"red","bold":true}]
execute if score $b mg.st matches 3 run title @a[tag=mg.play] actionbar [{"text":"🟢 ","color":"red"},{"text":"███","color":"red"},{"text":"███████","color":"dark_gray"},{"text":" avance !","color":"red","bold":true}]
execute if score $b mg.st matches 4 run title @a[tag=mg.play] actionbar [{"text":"🟢 ","color":"yellow"},{"text":"████","color":"yellow"},{"text":"██████","color":"dark_gray"},{"text":" avance !","color":"yellow","bold":true}]
execute if score $b mg.st matches 5 run title @a[tag=mg.play] actionbar [{"text":"🟢 ","color":"yellow"},{"text":"█████","color":"yellow"},{"text":"█████","color":"dark_gray"},{"text":" avance !","color":"yellow","bold":true}]
execute if score $b mg.st matches 6 run title @a[tag=mg.play] actionbar [{"text":"🟢 ","color":"yellow"},{"text":"██████","color":"yellow"},{"text":"████","color":"dark_gray"},{"text":" avance !","color":"yellow","bold":true}]
execute if score $b mg.st matches 7 run title @a[tag=mg.play] actionbar [{"text":"🟢 ","color":"green"},{"text":"███████","color":"green"},{"text":"███","color":"dark_gray"},{"text":" avance !","color":"green","bold":true}]
execute if score $b mg.st matches 8 run title @a[tag=mg.play] actionbar [{"text":"🟢 ","color":"green"},{"text":"████████","color":"green"},{"text":"██","color":"dark_gray"},{"text":" avance !","color":"green","bold":true}]
execute if score $b mg.st matches 9 run title @a[tag=mg.play] actionbar [{"text":"🟢 ","color":"green"},{"text":"█████████","color":"green"},{"text":"█","color":"dark_gray"},{"text":" avance !","color":"green","bold":true}]
execute if score $b mg.st matches 10 run title @a[tag=mg.play] actionbar [{"text":"🟢 ","color":"green"},{"text":"██████████","color":"green"},{"text":"","color":"dark_gray"},{"text":" avance !","color":"green","bold":true}]
