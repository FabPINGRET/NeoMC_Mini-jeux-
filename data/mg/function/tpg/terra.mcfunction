# TP général → Terra Nova (@s = admin)
execute unless data storage mg:terra built run return run function mg:terra/not_ready
execute as @a[tag=!mg.play,tag=!mg.out,tag=!mg.mpp,tag=mg.surv,tag=!mg.tvw] run function mg:survie/leave
execute as @a[tag=!mg.play,tag=!mg.out,tag=!mg.mpp,tag=mg.inplot] run function mg:plot/leave
execute as @a[tag=!mg.play,tag=!mg.out,tag=!mg.mpp,tag=!mg.tvw,tag=!mg.dl] run function mg:terra/enter
tellraw @a [{"text":"🌍 ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" a envoyé tout le monde à Terra Nova.","color":"gray"}]
