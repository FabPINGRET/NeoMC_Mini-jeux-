# Sethkar, le pharaon-liche est vaincu
scoreboard players set $ob4 mg.st 0
scoreboard players set $obc4 mg.st 300
bossbar set mg:olb4 players
kill @e[tag=mg.olminion_sethkar]
kill @e[tag=mg.oljar]
execute positioned 198.5 65 -27.5 as @a[tag=mg.olw,distance=..50] run function mg:ombre/boss/sethkar_rw
execute positioned 198.5 65 -27.5 run particle minecraft:totem_of_undying ~ ~2 ~ 3 2 3 0.5 200 force
execute positioned 198.5 65 -27.5 run playsound minecraft:ui.toast.challenge_complete master @a[distance=..80] ~ ~ ~ 1 0.8
