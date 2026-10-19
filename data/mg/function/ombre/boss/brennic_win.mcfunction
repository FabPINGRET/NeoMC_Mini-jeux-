# Brennic, seigneur des brigands est vaincu
scoreboard players set $ob0 mg.st 0
scoreboard players set $obc0 mg.st 300
bossbar set mg:olb0 players
kill @e[tag=mg.olminion_brennic]
kill @e[tag=mg.oljar]
execute positioned -204.5 71 -41.5 as @a[tag=mg.olw,distance=..58] run function mg:ombre/boss/brennic_rw
execute positioned -204.5 71 -41.5 run particle minecraft:totem_of_undying ~ ~2 ~ 3 2 3 0.5 200 force
execute positioned -204.5 71 -41.5 run playsound minecraft:ui.toast.challenge_complete master @a[distance=..80] ~ ~ ~ 1 0.8
