# Vers l'anneau 8/20 (@s, n) : passage, plancher, traînée (généré)
execute if entity @s[x=-7,y=180,z=27973,dx=4,dy=4,dz=4] run return run function mg:sky/pass
execute unless entity @s[y=150,dy=400] run return run function mg:sky/rescue
execute if score $skp mg.st matches 0 anchored eyes facing -4.5 182.5 27975.5 run function mg:sky/trail
execute if score $skp mg.st matches 0 run particle minecraft:end_rod -4.5 182.5 27975.5 1.0 1.0 1.0 0.01 4 force @s
