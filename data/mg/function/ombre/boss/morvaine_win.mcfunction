# Morvaine, la mère-sorcière est vaincu
scoreboard players set $ob3 mg.st 0
scoreboard players set $obc3 mg.st 300
bossbar set mg:olb3 players
kill @e[tag=mg.olminion_morvaine]
kill @e[tag=mg.oljar]
execute positioned 205.5 65 -187.5 as @a[tag=mg.olw,distance=..52] run function mg:ombre/boss/morvaine_rw
execute positioned 205.5 65 -187.5 run particle minecraft:totem_of_undying ~ ~2 ~ 3 2 3 0.5 200 force
execute positioned 205.5 65 -187.5 run playsound minecraft:ui.toast.challenge_complete master @a[distance=..80] ~ ~ ~ 1 0.8
