# Vers l'anneau 6/20 (@s, n) : passage, plancher, traînée (généré)
execute if entity @s[x=108,y=191,z=27928,dx=4,dy=4,dz=4] run return run function mg:sky/pass
execute unless entity @s[y=161,dy=400] run return run function mg:sky/rescue
execute if score $skp mg.st matches 0 anchored eyes facing 110.5 193.5 27930.5 run function mg:sky/trail
execute if score $skp mg.st matches 0 run particle minecraft:end_rod 110.5 193.5 27930.5 1.0 1.0 1.0 0.01 4 force @s
