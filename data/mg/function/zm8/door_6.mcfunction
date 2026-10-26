# Porte Sacristie → Galerie est ouverte
fill 14 83 42089 16 85 42089 minecraft:air
kill @e[tag=mg.zd6]
tag @e[tag=mg.zr_g] add mg.zon
particle minecraft:poof 15.5 84 42089.5 1 1 1 0.05 40
playsound minecraft:block.wooden_door.open master @a 15.0 84 42089.0 1 0.6
tellraw @a[tag=mg.play] [{"text":"🚪 ","color":"gold"},{"selector":"@a[tag=mg.zbuyer]","color":"yellow"},{"text":" a ouvert la porte Sacristie → Galerie est.","color":"gray"}]
