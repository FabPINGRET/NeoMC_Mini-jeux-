# Carapace lancée devant le kart (verte : tout droit, rebondit ; rouge : vise le pilote juste devant)
$execute on vehicle at @s rotated ~ 0 positioned ^ ^0.45 ^1.9 run summon minecraft:item_display ~ ~ ~ {Tags:["mg.kshell","$(t)","mg.knew","mg.fx"],teleport_duration:1,item:{id:"minecraft:leather_helmet",components:{"minecraft:dyed_color":$(c)}},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.9f,0.9f,0.9f]}}
execute on vehicle at @s rotated ~ 0 positioned ^ ^0.45 ^1.9 as @e[type=minecraft:item_display,tag=mg.knew] run tp @s ~ ~ ~ ~ 0
scoreboard players set @e[type=minecraft:item_display,tag=mg.knew] mg.t 120
scoreboard players set @e[type=minecraft:item_display,tag=mg.knew] mg.kbo 4
scoreboard players set @e[type=minecraft:item_display,tag=mg.knew] mg.kdr 0
scoreboard players set @e[type=minecraft:item_display,tag=mg.knew] mg.kdd -1
scoreboard players operation $kme mg.st = @s mg.krk
scoreboard players remove $kme mg.st 1
execute if entity @e[type=minecraft:item_display,tag=mg.knew,tag=mg.kred] as @a[tag=mg.play,tag=!mg.kfin] if score @s mg.krk = $kme mg.st run scoreboard players operation @e[type=minecraft:item_display,tag=mg.knew] mg.kdd = @s mg.ri
tag @e[type=minecraft:item_display,tag=mg.knew] remove mg.knew
execute at @s run playsound minecraft:entity.snowball.throw master @a[tag=mg.play,distance=..16] ~ ~ ~ 1 0.7
