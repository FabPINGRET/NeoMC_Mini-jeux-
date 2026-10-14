# Outpost Charlie tenu : récompenses, outpost réparé
scoreboard players set $tvo3 mg.st 0
bossbar set mg:tvo3 players
execute as @a[tag=mg.tvw,x=30.5,y=66,z=72.5,distance=..40] unless entity @s[scores={mg.tvm=2,mg.tvmo=3}] run function mg:terra/m2_help
execute as @a[tag=mg.tvw,scores={mg.tvm=2,mg.tvmo=3},x=30.5,y=66,z=72.5,distance=..40] run function mg:terra/m2_done
execute as @a[tag=mg.tvw,scores={mg.tvm=2,mg.tvmo=3}] run function mg:terra/m2_late
function mg:terra/out_build_3
execute positioned 30.5 66 72.5 run playsound minecraft:ui.toast.challenge_complete player @a[tag=mg.tvw,distance=..48] ~ ~ ~ 0.6 1
