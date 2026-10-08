# Vers l'anneau 15/20 (@s, n) : passage, plancher, traînée (généré)
execute if entity @s[x=58,y=137,z=28188,dx=4,dy=4,dz=4] run return run function mg:sky/pass
execute unless entity @s[y=107,dy=400] run return run function mg:sky/rescue
execute if score $skp mg.st matches 0 anchored eyes facing 60.5 139.5 28190.5 run function mg:sky/trail
execute if score $skp mg.st matches 0 run particle minecraft:end_rod 60.5 139.5 28190.5 1.0 1.0 1.0 0.01 4 force @s
