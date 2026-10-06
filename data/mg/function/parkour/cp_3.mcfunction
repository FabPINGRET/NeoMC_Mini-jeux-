# Checkpoint 3/3 atteint (@s = coureur)
scoreboard players set @s mg.ppc 3
tellraw @s [{"text":"✔ Checkpoint 3/3","color":"aqua","bold":true}]
execute at @s run playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 1 1.2
execute at @s run particle minecraft:happy_villager ~ ~1 ~ 0.5 0.5 0.5 0.1 20
