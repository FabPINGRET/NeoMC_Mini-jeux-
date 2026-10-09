# @s : balle — rebond au sol (amorti) ; arbitrage si l'échange est en cours
scoreboard players set @s mg.tny 65100
execute if score @s mg.tnvy matches ..-60 at @s run particle minecraft:dust{color:[0.75,0.55,0.35],scale:1.2} ~ ~-0.1 ~ 0.15 0 0.15 0 5
execute if score @s mg.tnvy matches ..-60 at @s run playsound minecraft:entity.slime.jump_small master @a[tag=!mg.surv,distance=..40] ~ ~ ~ 0.7 1.7
scoreboard players operation @s mg.tnvy *= #tnm7 mg.st
scoreboard players operation @s mg.tnvy /= #tn10 mg.st
execute if score @s mg.tnvy matches ..40 run scoreboard players set @s mg.tnvy 0
scoreboard players operation @s mg.tnvx *= #tn3 mg.st
scoreboard players operation @s mg.tnvx /= #tn4 mg.st
scoreboard players operation @s mg.tnvz *= #tn3 mg.st
scoreboard players operation @s mg.tnvz /= #tn4 mg.st
execute if entity @s[tag=mg.tnlive] run function mg:tennis/judge
