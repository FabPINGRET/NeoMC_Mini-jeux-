# Porte Entrepôt → Quai ouverte
fill 23 81 39085 25 83 39085 minecraft:air
kill @e[tag=mg.zd6]
tag @e[tag=mg.zr_g] add mg.zon
particle minecraft:poof 24.5 82 39085.5 1 1 1 0.05 40
playsound minecraft:block.wooden_door.open master @a 24.0 82 39085.0 1 0.6
tellraw @a[tag=mg.play] [{"text":"🚪 ","color":"gold"},{"selector":"@a[tag=mg.zbuyer]","color":"yellow"},{"text":" a ouvert la porte Entrepôt → Quai.","color":"gray"}]
