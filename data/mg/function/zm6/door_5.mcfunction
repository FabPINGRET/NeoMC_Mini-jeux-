# Porte Escalier → Bloc opératoire ouverte
fill -17 87 39792 -17 89 39794 minecraft:air
kill @e[tag=mg.zd5]
tag @e[tag=mg.zr_e] add mg.zon
particle minecraft:poof -16.5 88 39793.5 1 1 1 0.05 40
playsound minecraft:block.wooden_door.open master @a -17.0 88 39793.0 1 0.6
tellraw @a[tag=mg.play] [{"text":"🚪 ","color":"gold"},{"selector":"@a[tag=mg.zbuyer]","color":"yellow"},{"text":" a ouvert la porte Escalier → Bloc opératoire.","color":"gray"}]
