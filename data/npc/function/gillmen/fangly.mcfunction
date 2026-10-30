execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.dolphin.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute if block -22 129 104 air at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Fangly","color":"yellow"},{"text":"> Could you check on my secret treasure trove for me? The entrance is ","color":"white"},{"text":"under a bit of fake gravel between four blue tube coral","color":"aqua"},{"text":". I would ","color":"white"},{"text":"really, really love","color":"red"},{"text":" if you could check it and make sure everything is still there!","color":"white"}]
execute unless block -22 129 104 air at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Fangly","color":"yellow"},{"text":"> My collection of old tires and car batteries thrown into the lake is still there? That's amazing news, thank you so much! You've made me ","color":"white"},{"text":"very happy","color":"red"},{"text":", hero.","color":"white"}]
execute unless block -22 129 104 air run setblock -19 132 101 minecraft:redstone_block
execute unless block -22 129 104 air at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1.75 ~ run particle minecraft:heart ~ ~ ~ 0.3 0.3 0.3 0 10 force

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
