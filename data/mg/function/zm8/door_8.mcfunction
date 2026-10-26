# Porte Crypte → Caveau ouverte
fill 8 84 42118 8 86 42120 minecraft:air
kill @e[tag=mg.zd8]
tag @e[tag=mg.zr_h] add mg.zon
particle minecraft:poof 8.5 85 42119.5 1 1 1 0.05 40
playsound minecraft:block.wooden_door.open master @a 8.0 85 42119.0 1 0.6
tellraw @a[tag=mg.play] [{"text":"🚪 ","color":"gold"},{"selector":"@a[tag=mg.zbuyer]","color":"yellow"},{"text":" a ouvert la porte Crypte → Caveau.","color":"gray"}]
