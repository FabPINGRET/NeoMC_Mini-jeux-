# Porte Hall → Entrepôt ouverte
fill 9 81 39099 9 83 39101 minecraft:air
kill @e[tag=mg.zd3]
tag @e[tag=mg.zr_d] add mg.zon
particle minecraft:poof 9.5 82 39100.5 1 1 1 0.05 40
playsound minecraft:block.wooden_door.open master @a 9.0 82 39100.0 1 0.6
tellraw @a[tag=mg.play] [{"text":"🚪 ","color":"gold"},{"selector":"@a[tag=mg.zbuyer]","color":"yellow"},{"text":" a ouvert la porte Hall → Entrepôt.","color":"gray"}]
