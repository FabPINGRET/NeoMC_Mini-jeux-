# @s : balle — dans le filet : arrêtée, point au receveur
scoreboard players set @s mg.tnz -300
execute if score @s mg.tnl matches 2 run scoreboard players set @s mg.tnz 300
scoreboard players set @s mg.tnvx 0
scoreboard players set @s mg.tnvz 0
execute if score @s mg.tnvy matches 1.. run scoreboard players set @s mg.tnvy 0
execute at @s run playsound minecraft:block.wool.hit master @a[tag=!mg.surv,distance=..40] ~ ~ ~ 1 0.8
scoreboard players set $tnwhy mg.st 1
function mg:tennis/pt_recv
