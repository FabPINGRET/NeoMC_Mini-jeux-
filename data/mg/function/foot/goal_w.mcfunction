# But dans le but ROUGE (ouest) : le point va aux Bleus, quel que soit le tireur (vraie règle du foot)
particle minecraft:firework -14.5 49.5 -31 0.4 0.8 1.6 0.1 40 force
function mg:foot/ball_home
scoreboard players add $but mg.ftn 1
execute unless entity @a[x=-16,y=47,z=-40,dx=36,dy=6,dz=18,tag=mg.ftr] unless entity @a[x=-16,y=47,z=-40,dx=36,dy=6,dz=18,tag=mg.ftb] run return run function mg:foot/goal_free
scoreboard players add $ftb mg.ft 1
function mg:foot/goal_show
