execute if function mg:dropadv/loaded_all run return run function mg:dropadv/build_1
scoreboard players add $daw mg.st 1
execute if score $daw mg.st matches 120.. run return run tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] Dropper Aventure : zone pas chargée.","color":"red"}]
schedule function mg:dropadv/build_wait 20t
