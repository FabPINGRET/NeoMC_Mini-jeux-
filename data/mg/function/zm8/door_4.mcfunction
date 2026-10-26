# Porte Puits → Ossuaire ouverte
fill -8 84 42078 -8 86 42080 minecraft:air
kill @e[tag=mg.zd4]
tag @e[tag=mg.zr_e] add mg.zon
particle minecraft:poof -7.5 85 42079.5 1 1 1 0.05 40
playsound minecraft:block.wooden_door.open master @a -8.0 85 42079.0 1 0.6
tellraw @a[tag=mg.play] [{"text":"🚪 ","color":"gold"},{"selector":"@a[tag=mg.zbuyer]","color":"yellow"},{"text":" a ouvert la porte Puits → Ossuaire.","color":"gray"}]
