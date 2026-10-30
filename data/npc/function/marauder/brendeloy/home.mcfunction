execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run advancement grant @a[distance=..10,tag=mg.flw] only sidequest_2:bard_start

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ if score Inventory BardSongTotal matches 7.. if block -43 41 -237 air run tag @p[tag=mg.flw] add bard_reward_1
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ if score Inventory BardSongTotal matches 17 if block -45 41 -234 air unless entity @p[tag=bard_reward_1,tag=mg.flw] run tag @p[tag=mg.flw] add bard_reward_2

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 0.8

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ unless score Inventory BardSongTotal matches 17 unless entity @p[tag=bard_reward_1,tag=mg.flw] unless entity @p[tag=bard_reward_2,tag=mg.flw] run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Brendeloy","color":"aqua"},{"text":"> Ah, hero. Are you here to read the songs of an old man? I'm trying to write a ","color":"white"},{"text":"song about each culture in the Isles","color":"aqua"},{"text":". Seeing as you've talked to people from many different lands, could you help me with this? If you find me writing a song somewhere, please ","color":"white"},{"text":"tell me what you know of that culture","color":"aqua"},{"text":". I will surely reward you if you assist me in writing many songs.","color":"white"}]

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ if score Inventory BardSongTotal matches 17 unless entity @p[tag=bard_reward_1,tag=mg.flw] unless entity @p[tag=bard_reward_2,tag=mg.flw] run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Brendeloy","color":"aqua"},{"text":"> Thank you for your assistance, hero. This song library is my legacy, please look after it when I'm gone.","color":"white"}]

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ if entity @p[tag=bard_reward_1,tag=mg.flw] run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Brendeloy","color":"aqua"},{"text":"> You've helped me write","color":"white"},{"text":" 7 songs","color":"aqua"},{"text":"! As promised, you're entitled to a reward. I'll let you take a ","color":"white"},{"text":"curious little fruit","color":"yellow"},{"text":" I found...","color":"white"}]

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ if entity @p[tag=bard_reward_2,tag=mg.flw] run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Brendeloy","color":"aqua"},{"text":"> You've helped me write","color":"white"},{"text":" a song about every culture","color":"aqua"},{"text":"! You've made this old man's life richer with the joys of creating art. As promised, you're entitled to a reward. I'll let you take a ","color":"white"},{"text":"curious lullaby ","color":"light_purple"},{"text":"I found...","color":"white"}]


execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ if entity @p[tag=bard_reward_1,tag=mg.flw] run setblock -43 41 -237 minecraft:redstone_torch[lit=true]
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ if entity @p[tag=bard_reward_2,tag=mg.flw] run setblock -45 41 -234 minecraft:redstone_torch[lit=true]

tag @a[tag=mg.flw] remove bard_reward_1
tag @a[tag=mg.flw] remove bard_reward_2

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
