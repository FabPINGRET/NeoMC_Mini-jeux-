scoreboard players set $zsc mg.st 0
scoreboard players remove $zleft mg.st 1
execute as @e[type=minecraft:marker,tag=mg.zsp,tag=mg.zon,sort=random,limit=1] at @s run function mg:zm3/spawn_one with storage mg:zm
