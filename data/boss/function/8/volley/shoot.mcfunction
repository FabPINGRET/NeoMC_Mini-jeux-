execute as @n[tag=frostbyte_head,distance=0..] at @s run summon marker ~ ~1.8 ~ {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Invisible:1b,PersistenceRequired:1b,Tags:["frostbyte_volley_pos","beam"],DisabledSlots:4144959,Rotation:[-90F,0F]}

execute store result score state Value run random value -120..-60
execute if score boss:fs BossHealth matches 0..4 store result score state Value run random value -110..-70

#execute store result entity @n[tag=frostbyte_volley_pos] Rotation[0] int 1 run random value -120..-60
execute store result entity @n[tag=frostbyte_volley_pos,distance=0..] Rotation[0] int 1 run scoreboard players get state Value
execute store result entity @n[tag=frostbyte_head,distance=0..] Rotation[0] int 1 run scoreboard players get state Value
