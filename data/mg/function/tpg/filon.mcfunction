# TP général → Filon (@s = admin)
execute unless data storage mg:filon {built:1} run return run tellraw @s {"text":"🚧 L'île du Filon n'est pas encore construite : réessaie dans une minute.","color":"yellow"}
execute as @a[tag=!mg.play,tag=!mg.out,tag=!mg.mpp,tag=mg.surv,tag=!mg.fnw] run function mg:survie/leave
execute as @a[tag=!mg.play,tag=!mg.out,tag=!mg.mpp,tag=mg.inplot] run function mg:plot/leave
execute as @a[tag=!mg.play,tag=!mg.out,tag=!mg.mpp,tag=!mg.fnw,tag=!mg.dl] run function mg:filon/enter
tellraw @a [{"text":"🌍 ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" a envoyé tout le monde au Filon.","color":"gray"}]
