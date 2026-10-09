# Porte A → B ouverte
fill -1 81 36089 1 83 36089 minecraft:air
kill @e[tag=mg.zd1]
tag @e[tag=mg.zr_b] add mg.zon
particle minecraft:poof 0.5 82 36089.5 1 1 1 0.05 40
playsound minecraft:block.wooden_door.open master @a 0.0 82 36089.0 1 0.6
tellraw @a[tag=mg.play] [{"text":"🚪 ","color":"gold"},{"selector":"@a[tag=mg.zbuyer]","color":"yellow"},{"text":" a ouvert la porte A → B.","color":"gray"}]
