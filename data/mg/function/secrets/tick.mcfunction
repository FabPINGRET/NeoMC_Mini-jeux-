# Secrets du spawn (toutes les 0,5 s depuis lobby/armory_tick)
execute as @a[tag=!mg.play,tag=!mg.surv,tag=!mg.lk,gamemode=!spectator,x=0,y=64,z=0,distance=..140] at @s run function mg:secrets/check
scoreboard players remove $ebt mg.st 10
execute unless score $ebt mg.st matches 1.. if block 0 65 50 minecraft:polished_blackstone_button[powered=true] run function mg:secrets/button
