# Laser dans le mille (cœur d'une cible)
particle minecraft:firework ~ ~ ~ 0.2 0.2 0.2 0.15 30
particle minecraft:dust{color:[1.0,0.85,0.1],scale:1.4} ~ ~ ~ 0.3 0.3 0.3 0 20
playsound minecraft:block.note_block.bell master @a ~ ~ ~ 1 1.5
playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 0.8 1.2
title @s actionbar [{"text":"★ DANS LE MILLE ! ★","color":"gold","bold":true}]
