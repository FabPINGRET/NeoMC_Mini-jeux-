# @s = joueur qui vient de heurter un mur (avancement mg:elyrace_wall ou chute de vitesse) : -1 coeur ; plus de coeur : reprise (why/ko)
execute if score @s mg.xk matches 1.. run return 0
execute if score @s mg.xg matches 1.. run return 0
execute if score @s mg.xf matches 1.. run return 0
execute if score @s mg.xx matches ..32 run return 0
scoreboard players set @s mg.xk 12
scoreboard players remove @s mg.xh 1
execute at @s run playsound minecraft:entity.player.hurt master @s ~ ~ ~ 1 0.8
execute if score @s mg.xh matches ..0 run return run function mg:elyrace/why/ko
# encore en vie : sous-titre du choc, puis le HUD
title @s times 5 50 15
title @s subtitle [{"text":"💥 Choc ! -1 ♥","color":"red"}]
title @s title ""
function mg:elyrace/hud
