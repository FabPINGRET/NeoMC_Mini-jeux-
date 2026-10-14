# Porte Hall → Couloir ouest ouverte
fill -8 81 39399 -8 83 39401 minecraft:air
kill @e[tag=mg.zd1]
tag @e[tag=mg.zr_b] add mg.zon
particle minecraft:poof -7.5 82 39400.5 1 1 1 0.05 40
playsound minecraft:block.wooden_door.open master @a -8.0 82 39400.0 1 0.6
tellraw @a[tag=mg.play] [{"text":"🚪 ","color":"gold"},{"selector":"@a[tag=mg.zbuyer]","color":"yellow"},{"text":" a ouvert la porte Hall → Couloir ouest.","color":"gray"}]
