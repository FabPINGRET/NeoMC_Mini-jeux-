# Porte A → C ouverte
fill 11 81 23199 11 83 23201 minecraft:air
kill @e[tag=mg.zd2]
tag @e[tag=mg.zr_c] add mg.zon
particle minecraft:poof 11.5 82 23200.5 1 1 1 0.05 40
playsound minecraft:block.wooden_door.open master @a 11.0 82 23200.0 1 0.6
tellraw @a[tag=mg.play] [{"text":"🚪 ","color":"gold"},{"selector":"@a[tag=mg.zbuyer]","color":"yellow"},{"text":" a ouvert la porte A → C.","color":"gray"}]
