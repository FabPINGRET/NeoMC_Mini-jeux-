# Lancement par un admin (@s) : tout le monde est appelé, même en survie ou dans un monde ; les joueurs en pause restent où ils sont ([Ne pas rejoindre] pendant le compte à rebours)
tag @a[tag=mg.gtw] add mg.pullg
tag @a[tag=mg.tvw] add mg.pullt
tag @a[tag=mg.olw] add mg.pullo
tag @a[tag=mg.fnw] add mg.pullf
tag @a[tag=mg.flw] add mg.pullw
tag @a[tag=mg.surv,tag=!mg.gtw,tag=!mg.tvw,tag=!mg.olw,tag=!mg.fnw,tag=!mg.flw] add mg.pulls
# Les joueurs en pause ne sont pas rappelés, où qu'ils soient
tag @a[tag=mg.spectate] remove mg.pullg
tag @a[tag=mg.spectate] remove mg.pullt
tag @a[tag=mg.spectate] remove mg.pullo
tag @a[tag=mg.spectate] remove mg.pullf
tag @a[tag=mg.spectate] remove mg.pullw
tag @a[tag=mg.spectate] remove mg.pulls
execute as @a[tag=mg.pullg] in minecraft:overworld run function mg:gta/leave
execute as @a[tag=mg.pullt] in minecraft:overworld run function mg:terra/leave
execute as @a[tag=mg.pullo] in minecraft:overworld run function mg:ombre/leave
execute as @a[tag=mg.pullf] in minecraft:overworld run function mg:filon/leave
execute as @a[tag=mg.pullw] in minecraft:overworld run function mg:floaty/leave
execute as @a[tag=mg.pulls] in minecraft:overworld run function mg:survie/leave
scoreboard players set $pull mg.st 1
