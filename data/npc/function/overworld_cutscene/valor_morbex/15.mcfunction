advancement grant @a[tag=mg.flw] only main_quest:quest_4
scoreboard players set $fla46 mg.fla 1

execute positioned 10020 94 -98 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.shulker.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned 10020 94 -98 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Slime Man","color":"green"},{"text":"> Leaving a slick trail of justice, Slime Man out!","color":"white"}]
execute positioned 10020 94 -98 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:item.chorus_fruit.teleport neutral @a[tag=mg.flw] ~ ~ ~ 1 0.5
execute positioned 10020 94 -98 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run particle minecraft:sneeze ~ ~ ~ 0.1 0.1 0.1 0.05 100 force @a[tag=mg.flw]

function music:end
tp @n[tag=slime_man_valor_tower_1,distance=0..] 10020 90 -98 -45 0
setblock 10018 91 -105 air
scoreboard players set @a[tag=mg.flw] SoundtrackOverride 0
tag @a[tag=mg.flw] remove cutscene
tag @a[tag=mg.flw] remove no_warp
setblock 10022 93 -86 minecraft:ladder[facing=south,waterlogged=false]

#unlock ember depot
setblock -9765 252 428 minecraft:redstone_block

#unlock valor tower
setblock -9769 248 420 minecraft:redstone_block

#defendly leave basement
setblock -9765 252 430 minecraft:redstone_block
#defendly return to noparentunnels
setblock -9769 252 416 minecraft:redstone_block


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
