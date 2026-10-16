# Porte Puits → Wagonnets ouverte
fill 38 87 40189 40 89 40189 minecraft:air
kill @e[tag=mg.zd6]
tag @e[tag=mg.zr_f] add mg.zon
particle minecraft:poof 39.5 88 40189.5 1 1 1 0.05 40
playsound minecraft:block.wooden_door.open master @a 39.0 88 40189.0 1 0.6
tellraw @a[tag=mg.play] [{"text":"🚪 ","color":"gold"},{"selector":"@a[tag=mg.zbuyer]","color":"yellow"},{"text":" a ouvert la porte Puits → Wagonnets.","color":"gray"}]
