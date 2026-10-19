# Fin de session : barres des boss, invocations (vex) retirées
bossbar remove mg:trspino
bossbar remove mg:trrex
bossbar remove mg:trvarek
execute in mg:terranova run kill @e[type=minecraft:vex,x=-260,y=-64,z=-260,dx=520,dy=400,dz=520]
scoreboard players set $trspa mg.st 0
scoreboard players set $trva mg.st 0
scoreboard players set $trra mg.st 0
function mg:terra/rpg/dg_clear
