# Le Colosse de runes est vaincu
scoreboard players set $ob6 mg.st 0
scoreboard players set $obc6 mg.st 300
bossbar set mg:olb6 players
kill @e[tag=mg.olminion_colosse]
kill @e[tag=mg.oljar]
execute positioned 0.5 67 188.5 as @a[tag=mg.olw,distance=..56] run function mg:ombre/boss/colosse_rw
execute positioned 0.5 67 188.5 run particle minecraft:totem_of_undying ~ ~2 ~ 3 2 3 0.5 200 force
execute positioned 0.5 67 188.5 run playsound minecraft:ui.toast.challenge_complete master @a[distance=..80] ~ ~ ~ 1 0.8
