# Porte Quai ouest → Galerie ouverte
fill -37 81 39387 -35 83 39387 minecraft:air
kill @e[tag=mg.zd5]
tag @e[tag=mg.zr_f] add mg.zon
particle minecraft:poof -35.5 82 39387.5 1 1 1 0.05 40
playsound minecraft:block.wooden_door.open master @a -36.0 82 39387.0 1 0.6
tellraw @a[tag=mg.play] [{"text":"🚪 ","color":"gold"},{"selector":"@a[tag=mg.zbuyer]","color":"yellow"},{"text":" a ouvert la porte Quai ouest → Galerie.","color":"gray"}]
