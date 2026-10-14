# Outpost Alpha perdu
scoreboard players set $tvo1 mg.st 0
bossbar set mg:tvo1 players
particle minecraft:explosion_emitter 62.5 66 -73.5 0 0 0 0 1 force
playsound minecraft:entity.generic.explode hostile @a 62.5 65 -73.5 2 0.8
tellraw @a[tag=mg.tvw,x=62.5,y=65,z=-73.5,distance=..64] {"text":"💥 Le générateur de l’outpost Alpha est détruit !","color":"red","bold":true}
execute as @a[tag=mg.tvw,scores={mg.tvm=2,mg.tvmo=1}] run function mg:terra/m2_fail
function mg:terra/out_build_1
