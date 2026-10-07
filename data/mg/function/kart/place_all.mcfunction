# Dès que la zone est chargée (vérifié toutes les 0,5 s) : portillon, boîtes, un kart par pilote, vue installée
execute unless score $game mg.st matches 61 run return 0
execute unless score $state mg.st matches 1..2 run return 0
execute unless function mg:kart/loaded_all run return run schedule function mg:kart/place_all 10t
function mg:kart/gate_on
function mg:kart/boxes
function mg:kart/hazards
execute as @a[tag=mg.play] at @s run function mg:kart/kart_new
execute as @a[tag=mg.play] run function mg:kart/grid_face
execute as @a[tag=mg.play] run function mg:kart/place_seat
execute if score $kbat mg.st matches 1 as @a[tag=mg.play] run function mg:kart/bat_init
schedule function mg:kart/pre_tick 5t
tellraw @a[tag=mg.play] [{"text":"🏎 ","color":"gold"},{"text":"Vue assise : clic droit = objet, F5 = 3e personne. ","color":"gray"},{"text":"[Vue assise]","color":"yellow","click_event":{"action":"run_command","command":"trigger mg.kv set 2"}},{"text":" ","color":"gray"},{"text":"[Caméra de poursuite]","color":"yellow","click_event":{"action":"run_command","command":"trigger mg.kv set 1"}}]
