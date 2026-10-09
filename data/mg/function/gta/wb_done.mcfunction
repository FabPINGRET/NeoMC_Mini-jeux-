# Ville prête : murs invisibles, drapeau, plus de chargement forcé si personne ne joue
execute in mg:gta run kill @e[type=minecraft:item,x=-46,y=50,z=32222,dx=102,dy=60,dz=96]
execute in mg:gta run function mg:gta/walls
execute in mg:gta if block 0 58 32400 minecraft:stone run data modify storage mg:gta built set value 1b
execute unless score $gtw mg.st matches 1 in mg:gta run forceload remove -88 32312 88 32488
execute unless score $gtw mg.st matches 1 in mg:gta run forceload remove -44 32211 54 32312
