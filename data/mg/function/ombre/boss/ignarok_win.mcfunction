# Ignarok, dragon de feu est vaincu
scoreboard players set $ob5 mg.st 0
scoreboard players set $obc5 mg.st 300
bossbar set mg:olb5 players
kill @e[tag=mg.olminion_ignarok]
kill @e[tag=mg.oljar]
execute positioned 180.5 117 180.5 as @a[tag=mg.olw,distance=..54] run function mg:ombre/boss/ignarok_rw
execute positioned 180.5 117 180.5 run particle minecraft:totem_of_undying ~ ~2 ~ 3 2 3 0.5 200 force
execute positioned 180.5 117 180.5 run playsound minecraft:ui.toast.challenge_complete master @a[distance=..80] ~ ~ ~ 1 0.8
