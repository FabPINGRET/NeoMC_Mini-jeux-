# @s : la boule tombe dans la fosse
execute at @s run particle minecraft:poof ~ ~ ~ 0.2 0.2 0.2 0.02 6
execute at @s run playsound minecraft:block.wool.fall master @a[tag=!mg.surv,distance=..30] ~ ~ ~ 1 0.6
kill @s
