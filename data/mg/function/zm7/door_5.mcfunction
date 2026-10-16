# Porte Carrière → Atelier haut ouverte
fill -14 87 40215 -12 89 40215 minecraft:air
kill @e[tag=mg.zd5]
tag @e[tag=mg.zr_e] add mg.zon
particle minecraft:poof -12.5 88 40215.5 1 1 1 0.05 40
playsound minecraft:block.wooden_door.open master @a -13.0 88 40215.0 1 0.6
tellraw @a[tag=mg.play] [{"text":"🚪 ","color":"gold"},{"selector":"@a[tag=mg.zbuyer]","color":"yellow"},{"text":" a ouvert la porte Carrière → Atelier haut.","color":"gray"}]
