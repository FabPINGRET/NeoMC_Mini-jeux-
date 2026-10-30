function game:increment_heart_container
particle effect{color:[0.000,1.000,1.000],power:0.5} ~ ~1 ~ 0.5 0.5 0.5 0.1 100
playsound minecraft:entity.glow_squid.ambient master @a[tag=mg.flw] ~ ~1 ~ 1 1
playsound minecraft:entity.glow_squid.squirt master @a[tag=mg.flw] ~ ~1 ~ 1 1
playsound minecraft:zelda.heart_container master @a[tag=mg.flw] ~ ~1 ~ 1 1
setblock ~ ~1 ~ minecraft:amethyst_cluster[facing=up,waterlogged=false]
setblock ~ ~2 ~ air

scoreboard players set nacre_5 bool 1
setblock ~ ~ ~ ice

execute if score nacre_1 bool matches 1 if score nacre_2 bool matches 1 if score nacre_3 bool matches 1 if score nacre_4 bool matches 1 if score nacre_5 bool matches 1 if score nacre_6 bool matches 1 if score nacre_7 bool matches 1 if score nacre_8 bool matches 1 if score nacre_9 bool matches 1 if score nacre_10 bool matches 1 run advancement grant @a[tag=mg.flw] only sidequest_2:nacre
execute if score nacre_1 bool matches 1 if score nacre_2 bool matches 1 if score nacre_3 bool matches 1 if score nacre_4 bool matches 1 if score nacre_5 bool matches 1 if score nacre_6 bool matches 1 if score nacre_7 bool matches 1 if score nacre_8 bool matches 1 if score nacre_9 bool matches 1 if score nacre_10 bool matches 1 run scoreboard players set $fla27 mg.fla 1
