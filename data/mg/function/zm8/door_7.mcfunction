# Porte Galerie est → Caveau ouverte
fill 14 84 42111 16 86 42111 minecraft:air
kill @e[tag=mg.zd7]
tag @e[tag=mg.zr_h] add mg.zon
particle minecraft:poof 15.5 85 42111.5 1 1 1 0.05 40
playsound minecraft:block.wooden_door.open master @a 15.0 85 42111.0 1 0.6
tellraw @a[tag=mg.play] [{"text":"🚪 ","color":"gold"},{"selector":"@a[tag=mg.zbuyer]","color":"yellow"},{"text":" a ouvert la porte Galerie est → Caveau.","color":"gray"}]
