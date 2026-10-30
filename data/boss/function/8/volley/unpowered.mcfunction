tag @n[tag=frostbyte_volley_pos,distance=0..] remove beam
tag @n[tag=frostbyte_volley_pos,distance=0..] add unpowered

execute as @n[tag=frostbyte_volley_pos,distance=0..] at @s run summon block_display ~ ~ ~ {NoGravity:1b,Silent:1b,Glowing:1b,Tags:["frostbyte_volley","unpowered"],glow_color_override:3847130,brightness:{sky:15,block:15},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[-0.375f,-0.375f,-0.375f],scale:[0.75f,0.75f,0.75f]},block_state:{Name:"minecraft:deepslate_lapis_ore"}}

execute at @n[tag=frostbyte_volley_pos,distance=0..] run particle block{block_state:"deepslate_lapis_ore"} ~ ~ ~ 0.5 0.5 0.5 0 50
execute at @n[tag=frostbyte_volley_pos,distance=0..] run playsound minecraft:entity.evoker.cast_spell master @a[tag=mg.flw] ~ ~ ~ 1 2
