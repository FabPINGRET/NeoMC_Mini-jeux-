# Vers l'anneau 5/20 (@s, n) : passage, plancher, traînée (généré)
execute if entity @s[x=148,y=196,z=27878,dx=4,dy=4,dz=4] run return run function mg:sky/pass
execute unless entity @s[y=166,dy=400] run return run function mg:sky/rescue
execute if score $skp mg.st matches 0 anchored eyes facing 150.5 198.5 27880.5 run function mg:sky/trail
execute if score $skp mg.st matches 0 run particle minecraft:end_rod 150.5 198.5 27880.5 1.0 1.0 1.0 0.01 4 force @s
