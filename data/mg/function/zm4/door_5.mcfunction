# Porte Atelier → Bureaux ouverte
fill -23 81 39087 -21 83 39087 minecraft:air
kill @e[tag=mg.zd5]
tag @e[tag=mg.zr_f] add mg.zon
particle minecraft:poof -21.5 82 39087.5 1 1 1 0.05 40
playsound minecraft:block.wooden_door.open master @a -22.0 82 39087.0 1 0.6
tellraw @a[tag=mg.play] [{"text":"🚪 ","color":"gold"},{"selector":"@a[tag=mg.zbuyer]","color":"yellow"},{"text":" a ouvert la porte Atelier → Bureaux.","color":"gray"}]
