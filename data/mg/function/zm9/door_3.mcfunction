# Porte Frigidarium → Bassin ouverte
fill -7 84 42484 -7 86 42486 minecraft:air
kill @e[tag=mg.zd3]
tag @e[tag=mg.zr_d] add mg.zon
particle minecraft:poof -6.5 85 42485.5 1 1 1 0.05 40
playsound minecraft:block.wooden_door.open master @a -7.0 85 42485.0 1 0.6
tellraw @a[tag=mg.play] [{"text":"🚪 ","color":"gold"},{"selector":"@a[tag=mg.zbuyer]","color":"yellow"},{"text":" a ouvert la porte Frigidarium → Bassin.","color":"gray"}]
