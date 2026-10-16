# Porte Accueil → Couloir ouverte
fill 9 81 39799 9 83 39801 minecraft:air
kill @e[tag=mg.zd1]
tag @e[tag=mg.zr_b] add mg.zon
particle minecraft:poof 9.5 82 39800.5 1 1 1 0.05 40
playsound minecraft:block.wooden_door.open master @a 9.0 82 39800.0 1 0.6
tellraw @a[tag=mg.play] [{"text":"🚪 ","color":"gold"},{"selector":"@a[tag=mg.zbuyer]","color":"yellow"},{"text":" a ouvert la porte Accueil → Couloir.","color":"gray"}]
