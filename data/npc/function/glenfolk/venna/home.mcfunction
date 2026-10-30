execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute if block 238 35 -114 air at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Venna","color":"aqua"},{"text":"> I'm a druid, and my heart hurts for these poor plants being blighted by the dust. If I could get another soul to have empathy for plants, it would make me ","color":"white"},{"text":"so, so happy","color":"red"},{"text":". I want to show you some ","color":"white"},{"text":"lonely plants around the Isles","color":"green"},{"text":" and hopefully, something inside you will stir. Wait for a few seconds by the ","color":"white"},{"text":"lonliest dead bush on this island","color":"aqua"},{"text":" for starters...","color":"white"}]
execute unless block 238 35 -114 air at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Venna","color":"aqua"},{"text":"> You understand! You care! I'm ","color":"white"},{"text":"so, so happy ","color":"red"},{"text":"you're on this plant-love journey with me. You've made me feel like I'm able to make a difference, hero.","color":"white"}]
execute if block 238 35 -114 air run setblock 239 55 -214 minecraft:redstone_block
execute unless block 238 35 -114 air run setblock 232 36 -116 minecraft:redstone_block
execute unless block 238 35 -114 air at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1.75 ~ run particle minecraft:heart ~ ~ ~ 0.3 0.3 0.3 0 10 force 
#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 

#reset home
#setblock 238 35 -116 minecraft:redstone_block
#start bush timer
#setblock 239 55 -214 minecraft:redstone_block
#reset bush
#setblock 243 54 -213 minecraft:redstone_block
#start tulip timer
#setblock 56 49 -47 minecraft:redstone_block
#reset tulip
#setblock 48 50 -49 minecraft:redstone_block
#start pitcher timer
#setblock -104 50 -169 minecraft:redstone_block
#reset pitcher
#setblock -102 50 -167 minecraft:redstone_block
#start sapling timer
#setblock 58 54 46 minecraft:redstone_block
#reset sapling
#setblock 51 54 46 minecraft:redstone_block
#return to home
#setblock 238 35 -114 minecraft:redstone_block

#command tree

#start bush timer
#setblock -9773 268 430 minecraft:redstone_block
#leave home
#setblock -9761 252 430 minecraft:redstone_block
#start tulip timer
#setblock -9761 252 418 minecraft:redstone_block
#leave bush
#setblock -9761 252 416 minecraft:redstone_block
#start pitcher timer
#setblock -9761 252 422 minecraft:redstone_block
#leave tulip
#setblock -9761 252 420 minecraft:redstone_block
#start sapling timer
#setblock -9761 252 426 minecraft:redstone_block
#leave pitcher
#setblock -9761 252 424 minecraft:redstone_block
#return to home
#setblock -9761 252 428 minecraft:redstone_block
