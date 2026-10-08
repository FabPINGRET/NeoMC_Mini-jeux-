# Vers l'anneau 1/20 (@s, n) : passage, plancher, traînée (généré)
execute if entity @s[x=-3,y=223,z=27698,dx=6,dy=6,dz=4] run return run function mg:sky/pass
execute unless entity @s[y=194,dy=400] run return run function mg:sky/rescue
execute if score $skp mg.st matches 0 anchored eyes facing 0.5 226.5 27700.5 run function mg:sky/trail
execute if score $skp mg.st matches 0 run particle minecraft:end_rod 0.5 226.5 27700.5 1.5 1.5 1.5 0.01 4 force @s
