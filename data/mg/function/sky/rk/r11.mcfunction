# Vers l'anneau 12/20 (@s, n) : passage, plancher, traînée (généré)
execute if entity @s[x=-122,y=154,z=28137,dx=4,dy=6,dz=6] run return run function mg:sky/pass
execute unless entity @s[y=125,dy=400] run return run function mg:sky/rescue
execute if score $skp mg.st matches 0 anchored eyes facing -119.5 157.5 28140.5 run function mg:sky/trail
execute if score $skp mg.st matches 0 run particle minecraft:end_rod -119.5 157.5 28140.5 1.5 1.5 1.5 0.01 4 force @s
