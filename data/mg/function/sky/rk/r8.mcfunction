# Vers l'anneau 9/20 (@s, b) : passage, plancher, traînée (généré)
execute if entity @s[x=-72,y=173,z=27987,dx=4,dy=6,dz=6] run return run function mg:sky/pass
execute unless entity @s[y=144,dy=400] run return run function mg:sky/rescue
execute if score $skp mg.st matches 0 anchored eyes facing -69.5 176.5 27990.5 run function mg:sky/trail
execute if score $skp mg.st matches 0 run particle minecraft:wax_on -69.5 176.5 27990.5 1.5 1.5 1.5 0.01 4 force @s
