# @s = balle dans le trou !
tag @s remove mg.gfmv
tag @s add mg.gfin
scoreboard players set @s mg.gfu 0
scoreboard players set @s mg.gfv 0
scoreboard players set @s mg.gfw 0
tp @s @e[tag=mg.gftg,limit=1]
execute at @s run tp @s ~ ~-0.55 ~
execute at @s run particle minecraft:firework ~ ~0.8 ~ 0.3 0.6 0.3 0.08 40 force
execute at @s run particle minecraft:happy_villager ~ ~0.5 ~ 0.6 0.3 0.6 0 15 force
execute at @s run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 1 0.8
scoreboard players operation $cur mg.st = @s mg.gfi
execute as @a[tag=mg.play] if score @s mg.gfi = $cur mg.st run function mg:golf/in
