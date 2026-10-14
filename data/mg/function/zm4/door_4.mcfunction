# Porte Couloir → Salle des machines ouverte
fill -1 81 39069 1 83 39069 minecraft:air
kill @e[tag=mg.zd4]
tag @e[tag=mg.zr_e] add mg.zon
particle minecraft:poof 0.5 82 39069.5 1 1 1 0.05 40
playsound minecraft:block.wooden_door.open master @a 0.0 82 39069.0 1 0.6
tellraw @a[tag=mg.play] [{"text":"🚪 ","color":"gold"},{"selector":"@a[tag=mg.zbuyer]","color":"yellow"},{"text":" a ouvert la porte Couloir → Salle des machines.","color":"gray"}]
