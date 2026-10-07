# Spawn (chaque tick après le setup) : socles de l'armurerie, armes, portail des plots, animation du décor
execute as @a[tag=!mg.play,x=-53,y=63,z=-9,dx=2.99,dy=2.5,dz=2.99] run function mg:lobby/pad_1
execute as @a[tag=!mg.play,x=-53,y=63,z=-5,dx=2.99,dy=2.5,dz=2.99] run function mg:lobby/pad_2
execute as @a[tag=!mg.play,x=-53,y=63,z=3,dx=2.99,dy=2.5,dz=2.99] run function mg:lobby/pad_3
execute as @a[tag=!mg.play,x=-53,y=63,z=7,dx=2.99,dy=2.5,dz=2.99] run function mg:lobby/pad_4

# Recharge de la baguette et du railgun
scoreboard players remove @a[scores={mg.wd=1..}] mg.wd 1
scoreboard players remove @a[scores={mg.lcd=1..}] mg.lcd 1

# Utilisation (seulement dans le lobby, hors partie)
execute if score $state mg.st matches 0 as @a[scores={mg.qs=1..},tag=!mg.surv] at @s run function mg:lobby/laser
execute if score $state mg.st matches 0 as @a[scores={mg.fw=1..},tag=!mg.surv] at @s run function mg:lobby/wand
execute as @a[scores={mg.wc=1..},tag=!mg.surv] run function mg:lobby/wind_used
execute if score $state mg.st matches 0 as @e[type=minecraft:snowball,tag=mg.sn] at @s run function mg:lobby/snow_tick
execute if score $state mg.st matches 0 as @a[scores={mg.us=1..},tag=!mg.surv] at @s run function mg:lobby/snow_thrown
execute unless score $state mg.st matches 0 run scoreboard players reset @a mg.fw

# Portail des plots : le traverser envoie sur son plot (une fois par passage)
execute as @a[tag=mg.lpz] unless entity @s[x=-4,y=64,z=-48,dx=8,dy=3,dz=1] run tag @s remove mg.lpz
execute as @a[tag=!mg.lpz,tag=!mg.play,tag=!mg.out,tag=!mg.surv,tag=!mg.inplot,gamemode=adventure,x=-4,y=64,z=-48,dx=8,dy=3,dz=1] run function mg:lobby/portal

# Décor : animation toutes les 2 s, particules toutes les 0,5 s
scoreboard players add $lan mg.t 1
execute if score $lan mg.t matches 40.. run function mg:lobby/anim
execute if score $lan mg.t matches 40.. run scoreboard players set $lan mg.t 0
scoreboard players operation $lfx mg.t = $lan mg.t
scoreboard players set $l10 mg.t 10
scoreboard players operation $lfx mg.t %= $l10 mg.t
execute if score $lfx mg.t matches 0 if entity @a[x=0,y=64,z=0,distance=..160] run function mg:lobby/fx

# Secrets du spawn
execute if score $lfx mg.t matches 0 run function mg:secrets/tick
execute as @a[tag=!mg.play,tag=!mg.surv,tag=!mg.lk,x=0,y=64,z=0,distance=..15] run function mg:secrets/dance
