# Porte Caldarium → Palestre ouverte
fill 13 83 42503 15 85 42503 minecraft:air
kill @e[tag=mg.zd5]
tag @e[tag=mg.zr_f] add mg.zon
particle minecraft:poof 14.5 84 42503.5 1 1 1 0.05 40
playsound minecraft:block.wooden_door.open master @a 14.0 84 42503.0 1 0.6
tellraw @a[tag=mg.play] [{"text":"🚪 ","color":"gold"},{"selector":"@a[tag=mg.zbuyer]","color":"yellow"},{"text":" a ouvert la porte Caldarium → Palestre.","color":"gray"}]
