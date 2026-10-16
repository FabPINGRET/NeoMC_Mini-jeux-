# Lancement par un admin (@s) : tout le monde est appelé, même en survie, dans Neo GTA ou en pause ([Ne pas rejoindre] pendant le compte à rebours)
tag @a[tag=mg.gtw] add mg.pullg
tag @a[tag=mg.tvw] add mg.pullt
tag @a[tag=mg.surv,tag=!mg.gtw,tag=!mg.tvw] add mg.pulls
tag @a[tag=mg.spectate,tag=!mg.dl] add mg.pullp
execute as @a[tag=mg.pullg] in minecraft:overworld run function mg:gta/leave
execute as @a[tag=mg.pullt] in minecraft:overworld run function mg:terra/leave
execute as @a[tag=mg.pulls] in minecraft:overworld run function mg:survie/leave
tag @a[tag=mg.pullp] remove mg.spectate
scoreboard players set $pull mg.st 1
