summon block_display ~ 122 ~ {NoGravity:1b,Silent:1b,Tags:["morbex_honey"],transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]},block_state:{Name:"minecraft:honey_block"}}
particle minecraft:dust_pillar{block_state:"honey_block"} ~ 123 ~ 0.2 0 0.2 0.2 5
playsound minecraft:block.crop.break hostile @a[tag=mg.flw] ~ 123 ~ 2 1
tag @s remove honey_potential
