# Habillage des animaux tourné comme eux (chaque tick), puis cycle des chutes et ambiance du thème (chaque seconde)
execute as @e[type=minecraft:item_display,tag=mg.thrid,x=-80,y=30,z=-80,dx=160,dy=120,dz=160] on vehicle rotated as @s on passengers if entity @s[tag=mg.thrid] run rotate @s ~ 0
execute as @e[type=minecraft:interaction,tag=mg.thnpci,x=21,y=63,z=21,dx=3,dy=3,dz=3,limit=1] if data entity @s interaction run function mg:lobby/theme/npc_use
execute as @e[type=minecraft:interaction,tag=mg.thnpci,x=21,y=63,z=21,dx=3,dy=3,dz=3,limit=1] if data entity @s attack run function mg:lobby/theme/npc_use
execute as @a[tag=mg.thbun] at @s run function mg:lobby/theme/stew_rabbit_tp
execute as @a[tag=mg.thzap] at @s run particle minecraft:electric_spark ~ ~0.2 ~ 0.2 0.1 0.2 0 2 normal
# patinoire de Noël : entrée dans la piste (dy = 1 : la grotte PvP est dessous), sortie, glisse (le ragoût patin prime : tag mg.thsk)
execute if score $theme mg.st matches 2 in minecraft:overworld if block 41 63 24 minecraft:packed_ice as @a[x=35,y=64,z=15,dx=13,dy=1,dz=19,gamemode=!spectator,gamemode=!creative,tag=!mg.surv,tag=!mg.play,tag=!mg.out,tag=!mg.inplot,tag=!mg.visit,tag=!mg.pkr,tag=!mg.lk,tag=!mg.ely,tag=!mg.elyf,tag=!mg.xso,tag=!mg.dl,tag=!mg.gtw,tag=!mg.tvw,tag=!mg.mpp,tag=!mg.pvpc,tag=!mg.thbun,tag=!mg.thmini,tag=!mg.thrk] run function mg:lobby/theme/rink_on
execute unless score $theme mg.st matches 2 as @a[tag=mg.thrk] run function mg:lobby/theme/rink_off
execute in minecraft:overworld unless block 41 63 24 minecraft:packed_ice as @a[tag=mg.thrk] run function mg:lobby/theme/rink_off
execute as @a[tag=mg.thrk] at @s unless dimension minecraft:overworld run function mg:lobby/theme/rink_off
execute in minecraft:overworld as @a[tag=mg.thrk] unless entity @s[x=35,y=64,z=15,dx=13,dy=1,dz=19,gamemode=!spectator,gamemode=!creative,tag=!mg.surv,tag=!mg.play,tag=!mg.out,tag=!mg.inplot,tag=!mg.visit,tag=!mg.pkr,tag=!mg.lk,tag=!mg.ely,tag=!mg.elyf,tag=!mg.xso,tag=!mg.dl,tag=!mg.gtw,tag=!mg.tvw,tag=!mg.mpp,tag=!mg.pvpc,tag=!mg.thbun,tag=!mg.thmini] run function mg:lobby/theme/rink_off
execute as @a[tag=mg.thrk,tag=mg.thsk,tag=mg.thrkm] run function mg:lobby/theme/rink_unset
execute as @a[tag=mg.thrk,tag=!mg.thsk,tag=!mg.thrkm] run function mg:lobby/theme/rink_set
scoreboard players add $tht mg.st 1
execute if score $tht mg.st matches ..19 run return 0
scoreboard players set $tht mg.st 0
function mg:lobby/theme/npc_second
function mg:lobby/theme/banner
function mg:lobby/theme/fall_tick
execute if score $theme mg.st matches 1 run function mg:lobby/theme/halloween/fx
execute if score $theme mg.st matches 2 run function mg:lobby/theme/noel/fx
