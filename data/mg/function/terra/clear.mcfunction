# Retire tout ce que Terra Nova a posé (entités, objets au sol, barres)
kill @e[tag=mg.tv]
execute in mg:terranova run kill @e[type=minecraft:item,x=-100,y=40,z=-100,dx=200,dy=80,dz=200]
execute in mg:terranova run kill @e[type=minecraft:experience_orb,x=-100,y=40,z=-100,dx=200,dy=80,dz=200]
bossbar remove mg:tvcarno
bossbar remove mg:tvo1
bossbar remove mg:tvo2
bossbar remove mg:tvo3
scoreboard players set $tvo1 mg.st 0
scoreboard players set $tvo2 mg.st 0
scoreboard players set $tvo3 mg.st 0
