execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.creaking.step neutral @a[tag=mg.flw] ~ ~ ~ 1 2
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.axolotl.idle_air neutral @a[tag=mg.flw] ~ ~ ~ 1 1

execute if score Inventory TomeOfTongues matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Driku-Kani","color":"#C29D62"},{"text":"> ","color":"white"},{"text":"*nuk-tuk* ","color":"gray","italic":true},{"text":"What did that ","color":"white"},{"text":"scary guy","color":"dark_aqua"},{"text":" want with the ","color":"white"},{"text":"Lord of Forest","color":"green"},{"text":"? We're built to dance, not to fight. I hope the other six Lords are ok.","color":"white","italic":false},{"text":" *tuk-nuk* ","color":"gray","italic":true}]

execute if score Inventory TomeOfTongues matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Driku-Kani","color":"#C29D62"},{"text":"> ","color":"white"},{"text":"*nuk-tuk* ","color":"gray","italic":true},{"text":"We foresaw pieces of recent events through our dances, but we never guessed how drastic they would be. I hope the other six Lords are ok.","color":"white","italic":false},{"text":" *tuk-nuk* ","color":"gray","italic":true}]

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run function npc:pygmy/pose/repose

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
