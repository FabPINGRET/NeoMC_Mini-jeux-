execute as @n[tag=threnodist_stand,distance=0..] at @s run playsound minecraft:entity.fox.spit hostile @a[tag=mg.flw] ~ ~ ~ 3 2
execute as @n[tag=threnodist_stand,distance=0..] at @s rotated ~ 0 positioned ~ ~2.8 ~ positioned ^ ^ ^-0.2 run particle minecraft:dust_plume ~ ~ ~ 0 0 0 0 2
execute as @n[tag=threnodist_stand,distance=0..] at @s run summon arrow ~ ~2.5 ~ {pickup:2b,damage:4d,PierceLevel:2b,Motion:[0.0,0.5,0.0],Tags:["thren_arrow","gravity","new"],item:{id:"minecraft:tipped_arrow",count:1,components:{"minecraft:potion_contents":{custom_color:9371791,custom_effects:[{id:"minecraft:wither",amplifier:1,duration:1600,show_particles:0b}]}}}}
execute store result entity @n[tag=thren_arrow,tag=new,distance=0..] Motion[0] float 0.001 run random value -200..200
execute store result entity @n[tag=thren_arrow,tag=new,distance=0..] Motion[2] float 0.001 run random value -200..200
tag @e[tag=thren_arrow,tag=new,distance=0..] remove new
