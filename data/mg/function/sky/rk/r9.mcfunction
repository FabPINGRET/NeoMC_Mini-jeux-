# Vers l'anneau 10/20 (@s, n) : passage, plancher, traînée (généré)
execute if entity @s[x=-132,y=167,z=28028,dx=4,dy=4,dz=4] run return run function mg:sky/pass
execute unless entity @s[y=137,dy=400] run return run function mg:sky/rescue
execute if score $skp mg.st matches 0 anchored eyes facing -129.5 169.5 28030.5 run function mg:sky/trail
execute if score $skp mg.st matches 0 run particle minecraft:end_rod -129.5 169.5 28030.5 1.0 1.0 1.0 0.01 4 force @s
