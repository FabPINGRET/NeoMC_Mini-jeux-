# Porte Passerelle → Galerie ouverte
fill 31 87 39799 31 89 39801 minecraft:air
kill @e[tag=mg.zd7]
tag @e[tag=mg.zr_c] add mg.zon
particle minecraft:poof 31.5 88 39800.5 1 1 1 0.05 40
playsound minecraft:block.wooden_door.open master @a 31.0 88 39800.0 1 0.6
tellraw @a[tag=mg.play] [{"text":"🚪 ","color":"gold"},{"selector":"@a[tag=mg.zbuyer]","color":"yellow"},{"text":" a ouvert la porte Passerelle → Galerie.","color":"gray"}]
