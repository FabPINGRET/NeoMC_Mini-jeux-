# Le lieutenant Varek sort de son QG avec sa garde
summon minecraft:evoker -208.5 65 13.5 {Tags:["mg.tv","mg.tvhos","mg.tvtg","mg.trvarek","mg.trboss"],PersistenceRequired:1b,CanJoinRaid:0b,DeathLootTable:"minecraft:empty",CustomName:{"text":"Lieutenant Varek","color":"dark_red","bold":true},CustomNameVisible:1b,attributes:[{id:"minecraft:max_health",base:140},{id:"minecraft:follow_range",base:40}],Health:140f}
scoreboard players set $trva mg.st 1
scoreboard players set $trvr mg.st 0
execute positioned -206 65 8 run function mg:terra/rpg/sixer
execute positioned -206 65 18 run function mg:terra/rpg/sixer
execute positioned -198 65 13 run function mg:terra/rpg/sixer
execute positioned -202 65 16 run function mg:terra/rpg/sixer
tellraw @a[tag=mg.tvw,x=-230,y=0,z=-30,dx=60,dy=200,dz=70] {"text":"⚔ Lieutenant Varek : « Encore un colon ? Personne ne repart du fort ! »","color":"dark_red"}
execute positioned -200 65 4 as @a[tag=mg.tvw,gamemode=adventure,distance=..40] run function mg:terra/rpg/cs/boss_varek
execute as @e[tag=mg.trvarek] run data merge entity @s {NoAI:1b}
schedule function mg:terra/rpg/boss/wake 90t
