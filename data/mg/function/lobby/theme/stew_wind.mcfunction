# 🎃 Ragoût : coup de vent sous les pieds, instantané (@s = joueur) ; rot si stew_wind_ok refuse
execute store result score $thw mg.st at @s run function mg:lobby/theme/stew_wind_ok
execute if score $thw mg.st matches 0 run return run function mg:lobby/theme/stew_burp
execute at @s run summon minecraft:wind_charge ~ ~0.05 ~ {Tags:["mg.thwind"],Motion:[0d,-1d,0d]}
data modify entity @e[type=minecraft:wind_charge,tag=mg.thwind,limit=1] Owner set from entity @s UUID
tag @e[type=minecraft:wind_charge,tag=mg.thwind] remove mg.thwind
