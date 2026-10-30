execute if score Inventory Time matches 4 run advancement grant @a[tag=mg.flw] only sidequest_2:bard_start
execute if score Inventory Time matches 4 run scoreboard players set $fla42 mg.fla 1
execute if score Inventory Time matches 4 if score Inventory BardSongTotal matches 16 run advancement grant @a[tag=mg.flw] only sidequest_2:bard_finish
execute if score Inventory Time matches 4 if score Inventory BardSongTotal matches 16 run scoreboard players set $fla43 mg.fla 1

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 0.8
execute unless score Inventory Time matches 4 if score bard_3 bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Brendeloy","color":"aqua"},{"text":"> Ah, hero. I'm working on writing a song about the ","color":"white"},{"text":"Orphans","color":"aqua"},{"text":". Though, I'm not feeling very inspired at the moment... If you could come back here in the","color":"white"},{"text":" dead of night ","color":"aqua"},{"text":"and tell me what you know about the ","color":"white"},{"text":"Orphans","color":"aqua"},{"text":", that would be good. Yes, that's when my creative juices start really flowing...","color":"white"}]
execute if score Inventory Time matches 4 if score bard_3 bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Brendeloy","color":"aqua"},{"text":"> Yes... that's it! Inspiration strikes! My song about the ","color":"white"},{"text":"Orphans","color":"aqua"},{"text":" is finished! Thank you for your help, hero.","color":"white"}]
execute if score Inventory Time matches 4 if score bard_3 bool matches 0 if score Inventory BardSongTotal matches 6 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"Now that you've helped me finish ","color":"white"},{"text":"7 songs","color":"aqua"},{"text":", I want to give you something. Meet me back at my ","color":"white"},{"text":"song library","color":"aqua"},{"text":".","color":"white"}]
execute if score Inventory Time matches 4 if score bard_3 bool matches 0 if score Inventory BardSongTotal matches 16 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"Now that you've helped me finish ","color":"white"},{"text":"all 17 songs","color":"aqua"},{"text":", I want to give you something. Meet me back at my ","color":"white"},{"text":"song library","color":"aqua"},{"text":".","color":"white"}]

execute if score bard_3 bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Brendeloy","color":"aqua"},{"text":"> I think this is a fine song about the ","color":"white"},{"text":"Orphans","color":"aqua"},{"text":". It will be a worthy addition to my ","color":"white"},{"text":"song library","color":"aqua"},{"text":". Come visit sometime! I live near my kin the","color":"white"},{"text":" Marauders","color":"aqua"},{"text":".","color":"white"}]
execute if score bard_3 bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1.75 ~ run particle minecraft:note ~ ~ ~ 0.3 0.3 0.3 0 10 force 

execute if score Inventory Time matches 4 if score bard_3 bool matches 0 run scoreboard players add Inventory BardSongTotal 1
execute if score Inventory Time matches 4 run setblock -228 66 -1209 minecraft:redstone_block

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
