# Porte Quai → Salle des machines ouverte
fill 15 81 39058 15 83 39060 minecraft:air
kill @e[tag=mg.zd7]
tag @e[tag=mg.zr_e] add mg.zon
particle minecraft:poof 15.5 82 39059.5 1 1 1 0.05 40
playsound minecraft:block.wooden_door.open master @a 15.0 82 39059.0 1 0.6
tellraw @a[tag=mg.play] [{"text":"🚪 ","color":"gold"},{"selector":"@a[tag=mg.zbuyer]","color":"yellow"},{"text":" a ouvert la porte Quai → Salle des machines.","color":"gray"}]
