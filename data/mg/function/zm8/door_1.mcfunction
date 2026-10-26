# Porte Crypte → Chapelle ouverte
fill -8 83 42118 -8 85 42120 minecraft:air
kill @e[tag=mg.zd1]
tag @e[tag=mg.zr_b] add mg.zon
particle minecraft:poof -7.5 84 42119.5 1 1 1 0.05 40
playsound minecraft:block.wooden_door.open master @a -8.0 84 42119.0 1 0.6
tellraw @a[tag=mg.play] [{"text":"🚪 ","color":"gold"},{"selector":"@a[tag=mg.zbuyer]","color":"yellow"},{"text":" a ouvert la porte Crypte → Chapelle.","color":"gray"}]
