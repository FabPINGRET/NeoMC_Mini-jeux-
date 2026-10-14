# Outpost Bravo perdu
scoreboard players set $tvo2 mg.st 0
bossbar set mg:tvo2 players
particle minecraft:explosion_emitter -71.5 71 6.5 0 0 0 0 1 force
playsound minecraft:entity.generic.explode hostile @a -71.5 70 6.5 2 0.8
tellraw @a[tag=mg.tvw,x=-71.5,y=70,z=6.5,distance=..64] {"text":"💥 Le générateur de l’outpost Bravo est détruit !","color":"red","bold":true}
execute as @a[tag=mg.tvw,scores={mg.tvm=2,mg.tvmo=2}] run function mg:terra/m2_fail
function mg:terra/out_build_2
