# Outpost Charlie perdu
scoreboard players set $tvo3 mg.st 0
bossbar set mg:tvo3 players
particle minecraft:explosion_emitter 30.5 67 72.5 0 0 0 0 1 force
playsound minecraft:entity.generic.explode hostile @a 30.5 66 72.5 2 0.8
tellraw @a[tag=mg.tvw,x=30.5,y=66,z=72.5,distance=..64] {"text":"💥 Le générateur de l’outpost Charlie est détruit !","color":"red","bold":true}
execute as @a[tag=mg.tvw,scores={mg.tvm=2,mg.tvmo=3}] run function mg:terra/m2_fail
function mg:terra/out_build_3
