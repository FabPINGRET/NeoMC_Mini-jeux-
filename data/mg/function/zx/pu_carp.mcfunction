scoreboard players set @e[type=minecraft:marker,tag=mg.zwin] mg.zws 6
execute as @e[type=minecraft:marker,tag=mg.zwin] at @s run function mg:zx/win_set
scoreboard players add @a[tag=mg.play] mg.zpt 200
execute as @a[tag=mg.play] at @s run playsound minecraft:block.anvil.use master @s ~ ~ ~ 0.6 1.2
