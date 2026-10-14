# Porte Couloir → Quai est ouverte
fill 26 81 39399 26 83 39401 minecraft:air
kill @e[tag=mg.zd4]
tag @e[tag=mg.zr_e] add mg.zon
particle minecraft:poof 26.5 82 39400.5 1 1 1 0.05 40
playsound minecraft:block.wooden_door.open master @a 26.0 82 39400.0 1 0.6
tellraw @a[tag=mg.play] [{"text":"🚪 ","color":"gold"},{"selector":"@a[tag=mg.zbuyer]","color":"yellow"},{"text":" a ouvert la porte Couloir → Quai est.","color":"gray"}]
