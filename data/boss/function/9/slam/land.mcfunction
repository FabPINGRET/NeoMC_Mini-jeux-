playsound minecraft:item.mace.smash_ground hostile @a[tag=mg.flw] ~ ~ ~ 2 0.7
execute as @a[distance=..3,tag=mg.flw] run damage @s 26 minecraft:dragon_breath
setblock ~ ~ ~ water
particle minecraft:explosion ~ ~ ~ 0.8 0 0.8 0 4
scoreboard players set @a[gamemode=!spectator,tag=mg.flw] ScreenShake 1
schedule function floaty:sched/game/screenshake_end 0.5s replace
kill @s
