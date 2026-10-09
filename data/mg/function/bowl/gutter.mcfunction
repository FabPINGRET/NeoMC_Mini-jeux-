# @s : boule dans la gouttière (plus d'effet, plus de quilles)
tag @s add mg.bgut
execute if score @s mg.bx matches 1.. run scoreboard players set @s mg.bx 2000
execute if score @s mg.bx matches ..0 run scoreboard players set @s mg.bx -2000
scoreboard players set @s mg.bvx 0
data modify entity @s Pos[1] set value 64.3d
execute at @s run playsound minecraft:block.note_block.didgeridoo master @a[tag=!mg.surv,distance=..30] ~ ~ ~ 1 0.6
