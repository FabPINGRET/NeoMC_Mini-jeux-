# Porte Ossuaire → Sacristie ouverte
fill 8 83 42078 8 85 42080 minecraft:air
kill @e[tag=mg.zd5]
tag @e[tag=mg.zr_f] add mg.zon
particle minecraft:poof 8.5 84 42079.5 1 1 1 0.05 40
playsound minecraft:block.wooden_door.open master @a 8.0 84 42079.0 1 0.6
tellraw @a[tag=mg.play] [{"text":"🚪 ","color":"gold"},{"selector":"@a[tag=mg.zbuyer]","color":"yellow"},{"text":" a ouvert la porte Ossuaire → Sacristie.","color":"gray"}]
