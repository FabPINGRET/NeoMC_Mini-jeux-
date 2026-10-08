# Vers l'anneau 3/20 (@s, n) : passage, plancher, traînée (généré)
execute if entity @s[x=83,y=211,z=27773,dx=4,dy=4,dz=4] run return run function mg:sky/pass
execute unless entity @s[y=181,dy=400] run return run function mg:sky/rescue
execute if score $skp mg.st matches 0 anchored eyes facing 85.5 213.5 27775.5 run function mg:sky/trail
execute if score $skp mg.st matches 0 run particle minecraft:end_rod 85.5 213.5 27775.5 1.0 1.0 1.0 0.01 4 force @s
