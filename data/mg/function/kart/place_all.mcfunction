# Dès que la zone est chargée (vérifié toutes les 0,5 s) : portillon, boîtes, un kart par pilote, vue installée
execute unless score $game mg.st matches 61 run return 0
execute unless score $state mg.st matches 1..2 run return 0
execute unless function mg:kart/loaded_all run return run schedule function mg:kart/place_all 10t
function mg:kart/gate_on
function mg:kart/boxes
execute as @a[tag=mg.play] at @s run function mg:kart/kart_new
execute as @a[tag=mg.play] run function mg:kart/place_seat
tellraw @a[tag=mg.play] [{"text":"🏎 ","color":"gold"},{"text":"Vue : 3e personne (Ctrl = objet). ","color":"gray"},{"text":"[1re personne]","color":"yellow","click_event":{"action":"run_command","command":"trigger mg.kv set 2"}},{"text":" ","color":"gray"},{"text":"[3e personne]","color":"yellow","click_event":{"action":"run_command","command":"trigger mg.kv set 1"}}]
