# Adversaire touché (@s = victime ; le tireur porte le tag mg.qsh, $st = son équipe)
scoreboard players add @s mg.ph 1
scoreboard players set @s mg.pt 0
execute as @a[tag=mg.qsh,limit=1] at @s run playsound minecraft:entity.arrow.hit_player master @s ~ ~ ~ 0.8 1.6
execute at @s run playsound minecraft:entity.slime.squish master @a ~ ~ ~ 1 1.2
execute at @s run particle minecraft:poof ~ ~1 ~ 0.2 0.3 0.2 0.05 8
execute if score @s mg.ph matches 3.. run function mg:paintball/splatted
