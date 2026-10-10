# TP général → lobby (@s = admin) : chacun quitte proprement son activité (sauvegardes comprises), puis remise à zéro au spawn
execute as @a[tag=!mg.play,tag=!mg.out,tag=!mg.mpp,tag=mg.gtw] run function mg:gta/leave
execute as @a[tag=!mg.play,tag=!mg.out,tag=!mg.mpp,tag=mg.surv,tag=!mg.gtw] run function mg:survie/leave
execute as @a[tag=!mg.play,tag=!mg.out,tag=!mg.mpp,tag=mg.inplot] run function mg:plot/leave
execute as @a[tag=!mg.play,tag=!mg.out,tag=!mg.mpp,tag=mg.visit] run function mg:plot/leave
execute as @a[tag=!mg.play,tag=!mg.out,tag=!mg.mpp,tag=mg.lk] run function mg:lobkart/leave
execute as @a[tag=!mg.play,tag=!mg.out,tag=!mg.mpp,tag=mg.pkr] run function mg:parkour/quit
execute as @a[tag=!mg.play,tag=!mg.out,tag=!mg.mpp,tag=mg.ely] run function mg:elytra/stop_quiet
execute as @a[tag=!mg.play,tag=!mg.out,tag=!mg.mpp,tag=mg.elyf] run function mg:elytra/free_stop
execute as @a[tag=!mg.play,tag=!mg.out,tag=!mg.mpp] if predicate mg:coaster_riding run ride @s dismount
execute as @a[tag=!mg.play,tag=!mg.out,tag=!mg.mpp] run function mg:core/reset_player
tellraw @a [{"text":"🌍 ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" a ramené tout le monde au lobby.","color":"gray"}]
