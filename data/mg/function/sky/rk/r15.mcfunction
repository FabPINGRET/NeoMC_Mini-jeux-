# Vers l'anneau 16/20 (@s, n) : passage, plancher, traînée (généré)
execute if entity @s[x=118,y=130,z=28218,dx=4,dy=4,dz=4] run return run function mg:sky/pass
execute unless entity @s[y=100,dy=400] run return run function mg:sky/rescue
execute if score $skp mg.st matches 0 anchored eyes facing 120.5 132.5 28220.5 run function mg:sky/trail
execute if score $skp mg.st matches 0 run particle minecraft:end_rod 120.5 132.5 28220.5 1.0 1.0 1.0 0.01 4 force @s
