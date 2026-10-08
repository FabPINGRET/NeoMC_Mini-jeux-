# Vers l'anneau 2/20 (@s, n) : passage, plancher, traînée (généré)
execute if entity @s[x=33,y=217,z=27743,dx=4,dy=4,dz=4] run return run function mg:sky/pass
execute unless entity @s[y=187,dy=400] run return run function mg:sky/rescue
execute if score $skp mg.st matches 0 anchored eyes facing 35.5 219.5 27745.5 run function mg:sky/trail
execute if score $skp mg.st matches 0 run particle minecraft:end_rod 35.5 219.5 27745.5 1.0 1.0 1.0 0.01 4 force @s
