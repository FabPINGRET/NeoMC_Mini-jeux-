# Porte Bureaux → Salle des machines ouverte
fill -13 81 39065 -13 83 39067 minecraft:air
kill @e[tag=mg.zd8]
tag @e[tag=mg.zr_e] add mg.zon
particle minecraft:poof -12.5 82 39066.5 1 1 1 0.05 40
playsound minecraft:block.wooden_door.open master @a -13.0 82 39066.0 1 0.6
tellraw @a[tag=mg.play] [{"text":"🚪 ","color":"gold"},{"selector":"@a[tag=mg.zbuyer]","color":"yellow"},{"text":" a ouvert la porte Bureaux → Salle des machines.","color":"gray"}]
