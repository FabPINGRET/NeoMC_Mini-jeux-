# Nyxar, dragon de la Lune Noire est vaincu
scoreboard players set $ob8 mg.st 0
scoreboard players set $obc8 mg.st 300
bossbar set mg:olb8 players
kill @e[tag=mg.olminion_nyxar]
kill @e[tag=mg.oljar]
execute positioned -171.5 102 178.5 as @a[tag=mg.olw,distance=..53] run function mg:ombre/boss/nyxar_rw
execute positioned -171.5 102 178.5 run particle minecraft:totem_of_undying ~ ~2 ~ 3 2 3 0.5 200 force
execute positioned -171.5 102 178.5 run playsound minecraft:ui.toast.challenge_complete master @a[distance=..80] ~ ~ ~ 1 0.8
