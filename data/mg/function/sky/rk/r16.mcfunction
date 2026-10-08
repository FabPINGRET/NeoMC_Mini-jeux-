# Vers l'anneau 17/20 (@s, n) : passage, plancher, traînée (généré)
execute if entity @s[x=147,y=123,z=28278,dx=6,dy=6,dz=4] run return run function mg:sky/pass
execute unless entity @s[y=94,dy=400] run return run function mg:sky/rescue
execute if score $skp mg.st matches 0 anchored eyes facing 150.5 126.5 28280.5 run function mg:sky/trail
execute if score $skp mg.st matches 0 run particle minecraft:end_rod 150.5 126.5 28280.5 1.5 1.5 1.5 0.01 4 force @s
