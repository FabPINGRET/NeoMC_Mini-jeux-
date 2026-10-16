# @s a participé à la victoire sur le Spinosaure
scoreboard players add @s mg.trec 3
function mg:terra/rpg/xp {n:400}
tellraw @s {"text":"  +3 écailles de spinosaure (forge de Jo)","color":"dark_aqua"}
execute if score @s mg.trch matches 40 run function mg:terra/rpg/ch {n:45}
execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.8 0.9
