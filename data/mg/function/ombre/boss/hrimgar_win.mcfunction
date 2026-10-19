# Hrimgar, le géant du givre est vaincu
scoreboard players set $ob2 mg.st 0
scoreboard players set $obc2 mg.st 300
bossbar set mg:olb2 players
kill @e[tag=mg.olminion_hrimgar]
kill @e[tag=mg.oljar]
execute positioned 30.5 105 -204.5 as @a[tag=mg.olw,distance=..55] run function mg:ombre/boss/hrimgar_rw
execute positioned 30.5 105 -204.5 run particle minecraft:totem_of_undying ~ ~2 ~ 3 2 3 0.5 200 force
execute positioned 30.5 105 -204.5 run playsound minecraft:ui.toast.challenge_complete master @a[distance=..80] ~ ~ ~ 1 0.8
