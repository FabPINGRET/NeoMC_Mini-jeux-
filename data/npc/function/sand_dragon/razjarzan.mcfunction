execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.panda.cant_breed neutral @a[tag=mg.flw] ~ ~ ~ 1 0.8
execute if score Inventory TomeOfTongues matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Viceroy Razjarzan","color":"gold"},{"text":"> Hero! I'm glad you've found your way here. We've heard that the strange stone structures around the Isles are dormant ","color":"white"},{"text":"Worldgates","color":"dark_purple"},{"text":"! There is one ","color":"white"},{"text":"inside the old shaman's house, in the giant skull","color":"gold"},{"text":", if you're curious. But first, let me give you a ","color":"white"},{"text":"gift","color":"gold"},{"text":"! I will have our ","color":"white"},{"text":"Floating Forge","color":"red"},{"text":" readied for you, it is capable of creating amazing things from all this meteoric iron.","color":"white"}]


execute if score Inventory TomeOfTongues matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Viceroy Razjarzan","color":"gold"},{"text":"> Hero! How are your adventures going? Did the sword we give you ever come in handy? If there's ever anything you need me to order my subjects to do for you, you need just ask. We're all big fans!","color":"white"}]


execute positioned 228 63 95 run kill @e[tag=quest_marker,distance=..1]

execute if block 229 56 97 air run setblock -9769 252 420 minecraft:redstone_block
setblock 229 56 97 stone

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
