# TP général → survie (@s = admin)
execute as @a[tag=!mg.play,tag=!mg.out,tag=!mg.mpp,tag=mg.gtw] run function mg:gta/leave
execute as @a[tag=!mg.play,tag=!mg.out,tag=!mg.mpp,tag=!mg.surv] run function mg:survie/enter
tellraw @a [{"text":"🌍 ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" a envoyé tout le monde en survie.","color":"gray"}]
