execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.bee.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute if block 173 40 -322 tuff at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Jacquet","color":"green"},{"text":"> People are worried, I understand that, so I understand when they say things like \"","color":"white"},{"text":"hmm, nobody knows where this stone structure came from!","color":"gray","italic":true},{"text":"\" but I know what I saw, and they question me out of fear. Monsters made of flowers, bones, and dust built these in the dead of night. I know what I saw alright. Watch your back adventurer.","color":"white","italic":false}]

execute unless block 173 40 -322 tuff at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Jacquet","color":"green"},{"text":"> Ohhh that's not good. I'll do my best to protect the forest from whatever comes through that portal.","color":"white","italic":false}]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
