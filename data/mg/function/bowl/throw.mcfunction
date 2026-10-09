# @s : lancer — position latérale, angle (±8°), puissance de la jauge, effet si accroupi
scoreboard players operation #ln mg.st = @s mg.bln
execute store result score #lx mg.st run data get entity @s Pos[0] 1000
scoreboard players operation #lx mg.st -= @s mg.bcx
execute if score #lx mg.st matches 1300.. run scoreboard players set #lx mg.st 1300
execute if score #lx mg.st matches ..-1300 run scoreboard players set #lx mg.st -1300
execute store result score #yw mg.st run data get entity @s Rotation[0] 100
execute if score #yw mg.st matches 18001.. run scoreboard players remove #yw mg.st 36000
execute if score #yw mg.st matches ..-18001 run scoreboard players add #yw mg.st 36000
execute if score #yw mg.st matches 800.. run scoreboard players set #yw mg.st 800
execute if score #yw mg.st matches ..-800 run scoreboard players set #yw mg.st -800
scoreboard players operation #vz mg.st = @s mg.bpw
scoreboard players set #k mg.st 19
scoreboard players operation #vz mg.st *= #k mg.st
scoreboard players set #k mg.st 10
scoreboard players operation #vz mg.st /= #k mg.st
scoreboard players add #vz mg.st 150
scoreboard players operation #vx mg.st = #yw mg.st
scoreboard players operation #vx mg.st *= #km1 mg.st
scoreboard players operation #vx mg.st *= #vz mg.st
scoreboard players set #k mg.st 5730
scoreboard players operation #vx mg.st /= #k mg.st
scoreboard players set #sp mg.st 0
execute if predicate mg:sneak run function mg:bowl/spin
scoreboard players operation #cx mg.st = @s mg.bcx
execute positioned ~ 65.32 35160.2 run summon minecraft:item_display ~ ~ ~ {Tags:["mg.bowl","mg.bball","mg.bnew"],item:{id:"minecraft:ender_pearl",count:1},billboard:"center",teleport_duration:1,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
execute as @e[type=minecraft:item_display,tag=mg.bnew] run function mg:bowl/ball_init
scoreboard players set #pc mg.st 0
execute as @e[type=minecraft:block_display,tag=mg.bpin,tag=!mg.bpdn] if score @s mg.bln = #ln mg.st run scoreboard players add #pc mg.st 1
scoreboard players operation @s mg.bk = #pc mg.st
clear @s minecraft:warped_fungus_on_a_stick[minecraft:custom_data={mg_bowl:1b}]
scoreboard players set @s mg.bph 1
scoreboard players set @s mg.btm 0
scoreboard players reset @s mg.blu
playsound minecraft:entity.player.attack.sweep master @s ~ ~ ~ 0.8 0.6
execute if score #sp mg.st matches 0 run title @s actionbar {"text":"🎳 Lancer droit !","color":"aqua"}
execute unless score #sp mg.st matches 0 run title @s actionbar {"text":"🎳 Lancer avec effet !","color":"light_purple"}
