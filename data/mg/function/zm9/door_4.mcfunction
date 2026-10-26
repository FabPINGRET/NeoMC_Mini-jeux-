# Porte Bassin → Caldarium ouverte
fill 7 83 42484 7 85 42486 minecraft:air
kill @e[tag=mg.zd4]
tag @e[tag=mg.zr_e] add mg.zon
particle minecraft:poof 7.5 84 42485.5 1 1 1 0.05 40
playsound minecraft:block.wooden_door.open master @a 7.0 84 42485.0 1 0.6
tellraw @a[tag=mg.play] [{"text":"🚪 ","color":"gold"},{"selector":"@a[tag=mg.zbuyer]","color":"yellow"},{"text":" a ouvert la porte Bassin → Caldarium.","color":"gray"}]
