# Ysh'tar, la reine-araignée est vaincu
scoreboard players set $ob1 mg.st 0
scoreboard players set $obc1 mg.st 300
bossbar set mg:olb1 players
kill @e[tag=mg.olminion_ystar]
kill @e[tag=mg.oljar]
execute positioned -204.5 72 -204.5 as @a[tag=mg.olw,distance=..53] run function mg:ombre/boss/ystar_rw
execute positioned -204.5 72 -204.5 run particle minecraft:totem_of_undying ~ ~2 ~ 3 2 3 0.5 200 force
execute positioned -204.5 72 -204.5 run playsound minecraft:ui.toast.challenge_complete master @a[distance=..80] ~ ~ ~ 1 0.8
