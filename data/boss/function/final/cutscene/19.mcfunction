execute positioned -12384 123 355 run playsound minecraft:block.bell.use master @a[tag=mg.flw] ~ ~ ~ 5 0.5
particle minecraft:dust_pillar{block_state:"diamond_block"} -12384 123 355 0.8 0 0.8 2 1000

#item replace entity @n[tag=lord_morbex_stand] armor.legs with leather_leggings[dyed_color=1121057,trim={material:"minecraft:diamond",pattern:"minecraft:vex"}] 1

summon block_display -12384 131.2 354 {NoGravity:1b,Silent:1b,Tags:["wv_morbex_tumor"],brightness:{sky:15,block:15},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1f,0.9f,1.2f]},block_state:{Name:"minecraft:end_gateway"}}

schedule function floaty:sched/boss/final/cutscene/20 2s replace

#","color":"white"},{"text":"
