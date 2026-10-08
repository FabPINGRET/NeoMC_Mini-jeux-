# Vers l'anneau 20/20 (@s, f) : passage, plancher, traînée (généré)
execute if entity @s[x=-12,y=105,z=28347,dx=4,dy=6,dz=6] run return run function mg:sky/pass
execute unless entity @s[y=88,dy=400] run return run function mg:sky/rescue
execute if score $skp mg.st matches 0 anchored eyes facing -9.5 108.5 28350.5 run function mg:sky/trail
execute if score $skp mg.st matches 0 run particle minecraft:end_rod -9.5 108.5 28350.5 1.5 1.5 1.5 0.01 4 force @s
