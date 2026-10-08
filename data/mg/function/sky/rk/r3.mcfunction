# Vers l'anneau 4/20 (@s, b) : passage, plancher, traînée (généré)
execute if entity @s[x=132,y=202,z=27813,dx=6,dy=6,dz=4] run return run function mg:sky/pass
execute unless entity @s[y=173,dy=400] run return run function mg:sky/rescue
execute if score $skp mg.st matches 0 anchored eyes facing 135.5 205.5 27815.5 run function mg:sky/trail
execute if score $skp mg.st matches 0 run particle minecraft:wax_on 135.5 205.5 27815.5 1.5 1.5 1.5 0.01 4 force @s
