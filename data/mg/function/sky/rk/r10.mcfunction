# Vers l'anneau 11/20 (@s, n) : passage, plancher, traînée (généré)
execute if entity @s[x=-157,y=161,z=28088,dx=4,dy=4,dz=4] run return run function mg:sky/pass
execute unless entity @s[y=131,dy=400] run return run function mg:sky/rescue
execute if score $skp mg.st matches 0 anchored eyes facing -154.5 163.5 28090.5 run function mg:sky/trail
execute if score $skp mg.st matches 0 run particle minecraft:end_rod -154.5 163.5 28090.5 1.0 1.0 1.0 0.01 4 force @s
