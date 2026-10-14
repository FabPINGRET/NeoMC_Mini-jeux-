# Outpost Alpha tenu : récompenses, outpost réparé
scoreboard players set $tvo1 mg.st 0
bossbar set mg:tvo1 players
execute as @a[tag=mg.tvw,x=62.5,y=65,z=-73.5,distance=..40] unless entity @s[scores={mg.tvm=2,mg.tvmo=1}] run function mg:terra/m2_help
execute as @a[tag=mg.tvw,scores={mg.tvm=2,mg.tvmo=1},x=62.5,y=65,z=-73.5,distance=..40] run function mg:terra/m2_done
execute as @a[tag=mg.tvw,scores={mg.tvm=2,mg.tvmo=1}] run function mg:terra/m2_late
function mg:terra/out_build_1
execute positioned 62.5 65 -73.5 run playsound minecraft:ui.toast.challenge_complete player @a[tag=mg.tvw,distance=..48] ~ ~ ~ 0.6 1
