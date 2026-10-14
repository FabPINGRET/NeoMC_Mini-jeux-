# Porte Hall → Réacteur ouverte
fill -1 81 39408 1 83 39408 minecraft:air
kill @e[tag=mg.zd7]
tag @e[tag=mg.zr_g] add mg.zon
particle minecraft:poof 0.5 82 39408.5 1 1 1 0.05 40
playsound minecraft:block.wooden_door.open master @a 0.0 82 39408.0 1 0.6
tellraw @a[tag=mg.play] [{"text":"🚪 ","color":"gold"},{"selector":"@a[tag=mg.zbuyer]","color":"yellow"},{"text":" a ouvert la porte Hall → Réacteur.","color":"gray"}]
