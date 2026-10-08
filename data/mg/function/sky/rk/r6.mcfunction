# Vers l'anneau 7/20 (@s, n) : passage, plancher, traînée (généré)
execute if entity @s[x=53,y=185,z=27952,dx=4,dy=6,dz=6] run return run function mg:sky/pass
execute unless entity @s[y=156,dy=400] run return run function mg:sky/rescue
execute if score $skp mg.st matches 0 anchored eyes facing 55.5 188.5 27955.5 run function mg:sky/trail
execute if score $skp mg.st matches 0 run particle minecraft:end_rod 55.5 188.5 27955.5 1.5 1.5 1.5 0.01 4 force @s
