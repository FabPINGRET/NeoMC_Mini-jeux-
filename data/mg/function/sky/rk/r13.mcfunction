# Vers l'anneau 14/20 (@s, b) : passage, plancher, traînée (généré)
execute if entity @s[x=-2,y=142,z=28172,dx=4,dy=6,dz=6] run return run function mg:sky/pass
execute unless entity @s[y=113,dy=400] run return run function mg:sky/rescue
execute if score $skp mg.st matches 0 anchored eyes facing 0.5 145.5 28175.5 run function mg:sky/trail
execute if score $skp mg.st matches 0 run particle minecraft:wax_on 0.5 145.5 28175.5 1.5 1.5 1.5 0.01 4 force @s
