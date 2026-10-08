# Vers l'anneau 18/20 (@s, b) : passage, plancher, traînée (généré)
execute if entity @s[x=113,y=117,z=28332,dx=4,dy=6,dz=6] run return run function mg:sky/pass
execute unless entity @s[y=88,dy=400] run return run function mg:sky/rescue
execute if score $skp mg.st matches 0 anchored eyes facing 115.5 120.5 28335.5 run function mg:sky/trail
execute if score $skp mg.st matches 0 run particle minecraft:wax_on 115.5 120.5 28335.5 1.5 1.5 1.5 0.01 4 force @s
