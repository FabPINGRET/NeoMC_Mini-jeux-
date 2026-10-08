# Un pas de rayon (0,4 bloc)
execute unless block ~ ~ ~ #mg:ray_pass run return run function mg:gun/impact
execute positioned ~-0.99 ~-0.99 ~-0.99 as @e[tag=mg.gtg,tag=!mg.ghd,dx=0,dy=0,dz=0] positioned ~0.99 ~0.99 ~0.99 if entity @s[dx=0,dy=0,dz=0] run tag @s add mg.ghit
execute if entity @e[tag=mg.ghit] run function mg:gun/hit_here
execute if score $gstop mg.st matches 1 run return 0
execute if score $gdn mg.st matches 6 run particle minecraft:dust{color:[0.3,1.0,0.4],scale:1.2} ~ ~ ~ 0 0 0 0 1
execute unless score $gdn mg.st matches 6 run particle minecraft:crit ~ ~ ~ 0 0 0 0 1
scoreboard players remove $grs mg.st 1
execute if score $grs mg.st matches 1.. positioned ^ ^ ^0.4 run function mg:gun/ray
