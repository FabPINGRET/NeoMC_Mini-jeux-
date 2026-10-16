# Porte Entrée → Carrière ouverte
fill -9 81 40196 -9 83 40198 minecraft:air
kill @e[tag=mg.zd2]
tag @e[tag=mg.zr_d] add mg.zon
particle minecraft:poof -8.5 82 40197.5 1 1 1 0.05 40
playsound minecraft:block.wooden_door.open master @a -9.0 82 40197.0 1 0.6
tellraw @a[tag=mg.play] [{"text":"🚪 ","color":"gold"},{"selector":"@a[tag=mg.zbuyer]","color":"yellow"},{"text":" a ouvert la porte Entrée → Carrière.","color":"gray"}]
