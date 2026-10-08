# Vers l'anneau 19/20 (@s, n) : passage, plancher, traînée (généré)
execute if entity @s[x=53,y=112,z=28358,dx=4,dy=4,dz=4] run return run function mg:sky/pass
execute unless entity @s[y=88,dy=400] run return run function mg:sky/rescue
execute if score $skp mg.st matches 0 anchored eyes facing 55.5 114.5 28360.5 run function mg:sky/trail
execute if score $skp mg.st matches 0 run particle minecraft:end_rod 55.5 114.5 28360.5 1.0 1.0 1.0 0.01 4 force @s
