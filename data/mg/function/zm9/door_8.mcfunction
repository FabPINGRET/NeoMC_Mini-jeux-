# Porte Bassin → Piscine ouverte
fill -1 81 42489 1 83 42489 minecraft:air
kill @e[tag=mg.zd8]
tag @e[tag=mg.zr_g] add mg.zon
particle minecraft:poof 0.5 82 42489.5 1 1 1 0.05 40
playsound minecraft:block.wooden_door.open master @a 0.0 82 42489.0 1 0.6
tellraw @a[tag=mg.play] [{"text":"🚪 ","color":"gold"},{"selector":"@a[tag=mg.zbuyer]","color":"yellow"},{"text":" a ouvert la porte Bassin → Piscine.","color":"gray"}]
