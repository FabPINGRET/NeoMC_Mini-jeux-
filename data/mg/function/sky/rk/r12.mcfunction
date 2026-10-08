# Vers l'anneau 13/20 (@s, n) : passage, plancher, traînée (généré)
execute if entity @s[x=-62,y=149,z=28158,dx=4,dy=4,dz=4] run return run function mg:sky/pass
execute unless entity @s[y=119,dy=400] run return run function mg:sky/rescue
execute if score $skp mg.st matches 0 anchored eyes facing -59.5 151.5 28160.5 run function mg:sky/trail
execute if score $skp mg.st matches 0 run particle minecraft:end_rod -59.5 151.5 28160.5 1.0 1.0 1.0 0.01 4 force @s
