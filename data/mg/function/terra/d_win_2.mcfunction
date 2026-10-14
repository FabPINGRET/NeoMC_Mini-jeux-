# Outpost Bravo tenu : récompenses, outpost réparé
scoreboard players set $tvo2 mg.st 0
bossbar set mg:tvo2 players
execute as @a[tag=mg.tvw,x=-71.5,y=70,z=6.5,distance=..40] unless entity @s[scores={mg.tvm=2,mg.tvmo=2}] run function mg:terra/m2_help
execute as @a[tag=mg.tvw,scores={mg.tvm=2,mg.tvmo=2},x=-71.5,y=70,z=6.5,distance=..40] run function mg:terra/m2_done
execute as @a[tag=mg.tvw,scores={mg.tvm=2,mg.tvmo=2}] run function mg:terra/m2_late
function mg:terra/out_build_2
execute positioned -71.5 70 6.5 run playsound minecraft:ui.toast.challenge_complete player @a[tag=mg.tvw,distance=..48] ~ ~ ~ 0.6 1
