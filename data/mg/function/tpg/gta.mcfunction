# TP général → Neo GTA (@s = admin)
execute unless data storage mg:gta built run return run function mg:gta/not_ready
execute as @a[tag=!mg.play,tag=!mg.out,tag=!mg.mpp,tag=mg.surv,tag=!mg.gtw] run function mg:survie/leave
execute as @a[tag=!mg.play,tag=!mg.out,tag=!mg.mpp,tag=mg.inplot] run function mg:plot/leave
execute as @a[tag=!mg.play,tag=!mg.out,tag=!mg.mpp,tag=!mg.gtw] run function mg:gta/enter
tellraw @a [{"text":"🌍 ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" a envoyé tout le monde à Neo GTA.","color":"gray"}]
