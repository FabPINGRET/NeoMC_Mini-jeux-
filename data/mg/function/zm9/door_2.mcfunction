# Porte Vestiaire → Frigidarium ouverte
fill -15 84 42503 -13 86 42503 minecraft:air
kill @e[tag=mg.zd2]
tag @e[tag=mg.zr_c] add mg.zon
particle minecraft:poof -13.5 85 42503.5 1 1 1 0.05 40
playsound minecraft:block.wooden_door.open master @a -14.0 85 42503.0 1 0.6
tellraw @a[tag=mg.play] [{"text":"🚪 ","color":"gold"},{"selector":"@a[tag=mg.zbuyer]","color":"yellow"},{"text":" a ouvert la porte Vestiaire → Frigidarium.","color":"gray"}]
