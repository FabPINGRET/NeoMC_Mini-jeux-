# @s : scanner (clic droit) : rayon de 16 blocs vers un dinosaure
execute if score @s mg.trsc matches 1.. run return 0
scoreboard players set @s mg.trsc 10
scoreboard players set $tvr mg.st 0
tag @s add mg.trsh
scoreboard players set $tvsp mg.st -1
execute anchored eyes positioned ^ ^ ^0.6 run function mg:terra/rpg/scan_ray
tag @s remove mg.trsh
execute if score $tvsp mg.st matches -1 run return run title @s actionbar {"text":"🔬 Aucun dinosaure visé","color":"gray"}
execute at @s run playsound minecraft:block.beacon.power_select player @s ~ ~ ~ 0.5 2
execute if score $tvsp mg.st matches 0 run function mg:terra/rpg/scan/raptor
execute if score $tvsp mg.st matches 1 run function mg:terra/rpg/scan/compy
execute if score $tvsp mg.st matches 2 run function mg:terra/rpg/scan/dilo
execute if score $tvsp mg.st matches 3 run function mg:terra/rpg/scan/galli
execute if score $tvsp mg.st matches 4 run function mg:terra/rpg/scan/pachy
execute if score $tvsp mg.st matches 5 run function mg:terra/rpg/scan/trike
execute if score $tvsp mg.st matches 6 run function mg:terra/rpg/scan/stego
execute if score $tvsp mg.st matches 7 run function mg:terra/rpg/scan/ankylo
execute if score $tvsp mg.st matches 8 run function mg:terra/rpg/scan/brachio
execute if score $tvsp mg.st matches 9 run function mg:terra/rpg/scan/ptera
execute if score $tvsp mg.st matches 10 run function mg:terra/rpg/scan/carno
execute if score $tvsp mg.st matches 11 run function mg:terra/rpg/scan/spino
execute if score $tvsp mg.st matches 12 run function mg:terra/rpg/scan/rex
