#execute positioned -12384 123 355 run playsound minecraft:block.bell.use master @a ~ ~ ~ 5 0.5

playsound minecraft:item.armor.equip_diamond hostile @a[tag=mg.flw] -12384 123 355 5 1
execute as @e[tag=wv_model_sword,tag=finger,distance=0..] run data modify entity @s block_state.Name set value "minecraft:warped_wart_block"


schedule function floaty:sched/boss/final/cutscene/26 2s replace

#","color":"white"},{"text":"
