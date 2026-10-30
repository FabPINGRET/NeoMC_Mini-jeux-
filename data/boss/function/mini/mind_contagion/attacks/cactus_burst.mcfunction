playsound minecraft:item.crossbow.shoot hostile @a[tag=mg.flw] ~ ~ ~ 2 1

summon arrow ~ ~ ~ {pickup:2b,damage:50d,crit:1b,Tags:["cactus_bomb_arrow"],CustomName:{"color":"light_purple","text":"Brain Cactus"},SoundEvent:"item.spear.hit"}
summon arrow ~ ~ ~ {pickup:2b,damage:50d,crit:1b,Tags:["cactus_bomb_arrow"],CustomName:{"color":"light_purple","text":"Brain Cactus"},SoundEvent:"item.spear.hit"}
summon arrow ~ ~ ~ {pickup:2b,damage:50d,crit:1b,Tags:["cactus_bomb_arrow"],CustomName:{"color":"light_purple","text":"Brain Cactus"},SoundEvent:"item.spear.hit"}
summon arrow ~ ~ ~ {pickup:2b,damage:50d,crit:1b,Tags:["cactus_bomb_arrow"],CustomName:{"color":"light_purple","text":"Brain Cactus"},SoundEvent:"item.spear.hit"}
summon arrow ~ ~ ~ {pickup:2b,damage:50d,crit:1b,Tags:["cactus_bomb_arrow"],CustomName:{"color":"light_purple","text":"Brain Cactus"},SoundEvent:"item.spear.hit"}
summon arrow ~ ~ ~ {pickup:2b,damage:50d,crit:1b,Tags:["cactus_bomb_arrow"],CustomName:{"color":"light_purple","text":"Brain Cactus"},SoundEvent:"item.spear.hit"}
summon arrow ~ ~ ~ {pickup:2b,damage:50d,crit:1b,Tags:["cactus_bomb_arrow"],CustomName:{"color":"light_purple","text":"Brain Cactus"},SoundEvent:"item.spear.hit"}
summon arrow ~ ~ ~ {pickup:2b,damage:50d,crit:1b,Tags:["cactus_bomb_arrow"],CustomName:{"color":"light_purple","text":"Brain Cactus"},SoundEvent:"item.spear.hit"}
summon arrow ~ ~ ~ {pickup:2b,damage:50d,crit:1b,Tags:["cactus_bomb_arrow"],CustomName:{"color":"light_purple","text":"Brain Cactus"},SoundEvent:"item.spear.hit"}
summon arrow ~ ~ ~ {pickup:2b,damage:50d,crit:1b,Tags:["cactus_bomb_arrow"],CustomName:{"color":"light_purple","text":"Brain Cactus"},SoundEvent:"item.spear.hit"}
summon arrow ~ ~ ~ {pickup:2b,damage:50d,crit:1b,Tags:["cactus_bomb_arrow"],CustomName:{"color":"light_purple","text":"Brain Cactus"},SoundEvent:"item.spear.hit"}
summon arrow ~ ~ ~ {pickup:2b,damage:50d,crit:1b,Tags:["cactus_bomb_arrow"],CustomName:{"color":"light_purple","text":"Brain Cactus"},SoundEvent:"item.spear.hit"}
summon arrow ~ ~ ~ {pickup:2b,damage:50d,crit:1b,Tags:["cactus_bomb_arrow"],CustomName:{"color":"light_purple","text":"Brain Cactus"},SoundEvent:"item.spear.hit"}
summon arrow ~ ~ ~ {pickup:2b,damage:50d,crit:1b,Tags:["cactus_bomb_arrow"],CustomName:{"color":"light_purple","text":"Brain Cactus"},SoundEvent:"item.spear.hit"}
summon arrow ~ ~ ~ {pickup:2b,damage:50d,crit:1b,Tags:["cactus_bomb_arrow"],CustomName:{"color":"light_purple","text":"Brain Cactus"},SoundEvent:"item.spear.hit"}
summon arrow ~ ~ ~ {pickup:2b,damage:50d,crit:1b,Tags:["cactus_bomb_arrow"],CustomName:{"color":"light_purple","text":"Brain Cactus"},SoundEvent:"item.spear.hit"}
summon arrow ~ ~ ~ {pickup:2b,damage:50d,crit:1b,Tags:["cactus_bomb_arrow"],CustomName:{"color":"light_purple","text":"Brain Cactus"},SoundEvent:"item.spear.hit"}
summon arrow ~ ~ ~ {pickup:2b,damage:50d,crit:1b,Tags:["cactus_bomb_arrow"],CustomName:{"color":"light_purple","text":"Brain Cactus"},SoundEvent:"item.spear.hit"}
summon arrow ~ ~ ~ {pickup:2b,damage:50d,crit:1b,Tags:["cactus_bomb_arrow"],CustomName:{"color":"light_purple","text":"Brain Cactus"},SoundEvent:"item.spear.hit"}
summon arrow ~ ~ ~ {pickup:2b,damage:50d,crit:1b,Tags:["cactus_bomb_arrow"],CustomName:{"color":"light_purple","text":"Brain Cactus"},SoundEvent:"item.spear.hit"}
summon arrow ~ ~ ~ {pickup:2b,damage:50d,crit:1b,Tags:["cactus_bomb_arrow"],CustomName:{"color":"light_purple","text":"Brain Cactus"},SoundEvent:"item.spear.hit"}
summon arrow ~ ~ ~ {pickup:2b,damage:50d,crit:1b,Tags:["cactus_bomb_arrow"],CustomName:{"color":"light_purple","text":"Brain Cactus"},SoundEvent:"item.spear.hit"}
summon arrow ~ ~ ~ {pickup:2b,damage:50d,crit:1b,Tags:["cactus_bomb_arrow"],CustomName:{"color":"light_purple","text":"Brain Cactus"},SoundEvent:"item.spear.hit"}
summon arrow ~ ~ ~ {pickup:2b,damage:50d,crit:1b,Tags:["cactus_bomb_arrow"],CustomName:{"color":"light_purple","text":"Brain Cactus"},SoundEvent:"item.spear.hit"}
summon arrow ~ ~ ~ {pickup:2b,damage:50d,crit:1b,Tags:["cactus_bomb_arrow"],CustomName:{"color":"light_purple","text":"Brain Cactus"},SoundEvent:"item.spear.hit"}
summon arrow ~ ~ ~ {pickup:2b,damage:50d,crit:1b,Tags:["cactus_bomb_arrow"],CustomName:{"color":"light_purple","text":"Brain Cactus"},SoundEvent:"item.spear.hit"}
summon arrow ~ ~ ~ {pickup:2b,damage:50d,crit:1b,Tags:["cactus_bomb_arrow"],CustomName:{"color":"light_purple","text":"Brain Cactus"},SoundEvent:"item.spear.hit"}
summon arrow ~ ~ ~ {pickup:2b,damage:50d,crit:1b,Tags:["cactus_bomb_arrow"],CustomName:{"color":"light_purple","text":"Brain Cactus"},SoundEvent:"item.spear.hit"}
summon arrow ~ ~ ~ {pickup:2b,damage:50d,crit:1b,Tags:["cactus_bomb_arrow"],CustomName:{"color":"light_purple","text":"Brain Cactus"},SoundEvent:"item.spear.hit"}
summon arrow ~ ~ ~ {pickup:2b,damage:50d,crit:1b,Tags:["cactus_bomb_arrow"],CustomName:{"color":"light_purple","text":"Brain Cactus"},SoundEvent:"item.spear.hit"}

execute as @e[tag=cactus_bomb_arrow,distance=0..] run data modify entity @s Owner set from entity @n[tag=mind_boss_name,distance=0..] UUID

execute as @e[tag=cactus_bomb_arrow,distance=0..] store result entity @s Motion[0] double 0.001 run random value -1000..1000
execute as @e[tag=cactus_bomb_arrow,distance=0..] store result entity @s Motion[1] double 0.001 run random value 200..800
execute as @e[tag=cactus_bomb_arrow,distance=0..] store result entity @s Motion[2] double 0.001 run random value -1000..1000
