tellraw @a[tag=mg.mmx] [{"text":"🏹 L'arc est tombé ! ","color":"aqua","bold":true},{"text":"Il brille : le premier innocent qui le ramasse peut abattre le tueur.","color":"gray"}]
execute as @a[tag=mg.mmx] at @s run playsound minecraft:block.bell.use master @s ~ ~ ~ 0.6 0.8
