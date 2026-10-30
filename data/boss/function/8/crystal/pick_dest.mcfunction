#This function picks the final location of each crystal for them to move to

kill @e[tag=frostbyte_crystal_loc,distance=0..]

execute at @e[tag=frostbyte_crystal_dest,tag=1,sort=random,limit=1,distance=0..] run summon marker ~ 106 ~ {NoGravity:1b,Silent:1b,Tags:["frostbyte_crystal_loc","1"]}
execute at @e[tag=frostbyte_crystal_dest,tag=2,sort=random,limit=1,distance=0..] run summon marker ~ 106 ~ {NoGravity:1b,Silent:1b,Tags:["frostbyte_crystal_loc","2"]}
execute at @e[tag=frostbyte_crystal_dest,tag=3,sort=random,limit=1,distance=0..] run summon marker ~ 106 ~ {NoGravity:1b,Silent:1b,Tags:["frostbyte_crystal_loc","3"]}
execute at @e[tag=frostbyte_crystal_dest,tag=4,sort=random,limit=1,distance=0..] run summon marker ~ 106 ~ {NoGravity:1b,Silent:1b,Tags:["frostbyte_crystal_loc","4"]}

execute as @e[tag=frostbyte_crystal_loc,distance=0..] at @s run function boss:8/crystal/vary
