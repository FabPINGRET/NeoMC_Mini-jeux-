# Porte Chapelle → Galerie des os ouverte
fill -16 83 42111 -14 85 42111 minecraft:air
kill @e[tag=mg.zd2]
tag @e[tag=mg.zr_c] add mg.zon
particle minecraft:poof -14.5 84 42111.5 1 1 1 0.05 40
playsound minecraft:block.wooden_door.open master @a -15.0 84 42111.0 1 0.6
tellraw @a[tag=mg.play] [{"text":"🚪 ","color":"gold"},{"selector":"@a[tag=mg.zbuyer]","color":"yellow"},{"text":" a ouvert la porte Chapelle → Galerie des os.","color":"gray"}]
