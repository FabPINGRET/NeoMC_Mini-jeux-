# Porte B → D ouverte
fill 11 81 35777 11 83 35779 minecraft:air
kill @e[tag=mg.zd3]
tag @e[tag=mg.zr_d] add mg.zon
particle minecraft:poof 11.5 82 35778.5 1 1 1 0.05 40
playsound minecraft:block.wooden_door.open master @a 11.0 82 35778.0 1 0.6
tellraw @a[tag=mg.play] [{"text":"🚪 ","color":"gold"},{"selector":"@a[tag=mg.zbuyer]","color":"yellow"},{"text":" a ouvert la porte B → D.","color":"gray"}]
