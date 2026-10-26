# Porte Galerie des os → Puits ouverte
fill -16 84 42089 -14 86 42089 minecraft:air
kill @e[tag=mg.zd3]
tag @e[tag=mg.zr_d] add mg.zon
particle minecraft:poof -14.5 85 42089.5 1 1 1 0.05 40
playsound minecraft:block.wooden_door.open master @a -15.0 85 42089.0 1 0.6
tellraw @a[tag=mg.play] [{"text":"🚪 ","color":"gold"},{"selector":"@a[tag=mg.zbuyer]","color":"yellow"},{"text":" a ouvert la porte Galerie des os → Puits.","color":"gray"}]
