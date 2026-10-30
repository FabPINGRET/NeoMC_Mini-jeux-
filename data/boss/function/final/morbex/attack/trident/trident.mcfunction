summon trident ~ ~ ~ {NoGravity:1b,pickup:2b,damage:10d,shake:1b,crit:1b,Motion:[0.0,-2.0,0.0],Tags:["morbex_trident","new"],SoundEvent:"block.sculk.break"}
execute store result entity @n[tag=morbex_trident,tag=new,distance=0..] Motion[0] float 0.01 run random value -100..100
execute store result entity @n[tag=morbex_trident,tag=new,distance=0..] Motion[2] float 0.01 run random value -100..100
data modify entity @n[tag=morbex_trident,tag=new,distance=0..] Owner set from entity @n[tag=l_morbex_2,distance=0..] UUID
tag @e[tag=morbex_trident,distance=0..] remove new
