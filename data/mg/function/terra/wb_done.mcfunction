# Terra Nova prête : murs du bord, drapeau, plus de chargement forcé si personne ne joue
execute in mg:terranova run kill @e[type=minecraft:item,x=-100,y=40,z=-100,dx=200,dy=80,dz=200]
execute in mg:terranova run function mg:terra/walls
execute in mg:terranova if block 0 64 0 minecraft:chiseled_stone_bricks run data modify storage mg:terra built set value 1b
execute unless score $tvw mg.st matches 1 in mg:terranova run forceload remove -112 -112 111 111
execute if data storage mg:terra built run tellraw @a[tag=mg.admin] {"text":"🦖 Terra Nova est construite.","color":"green"}
