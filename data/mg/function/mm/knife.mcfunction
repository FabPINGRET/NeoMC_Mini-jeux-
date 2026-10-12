# 10 s : le tueur est armé
execute as @a[tag=mg.play,tag=mg.mmm] run function mg:mm/knife_give
title @a[tag=mg.mmm] actionbar {"text":"🔪 Tu as ton couteau !","color":"red","bold":true}
tellraw @a[tag=mg.play] [{"text":"🔪 Le tueur est armé… méfiez-vous de tout le monde.","color":"red"}]
execute as @a[tag=mg.play] at @s run playsound minecraft:entity.wither.ambient master @s ~ ~ ~ 0.4 1.6
