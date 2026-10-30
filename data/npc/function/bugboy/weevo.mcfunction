execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.bee.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute if score BetterEconomy bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=!vendor_golden_carrot_0,tag=mg.flw] [{"text":"<"},{"text":"Weevo","color":"green"},{"text":"> I usually would have golden carrots for you, but times have been tough, so I haven't been able to gild them. Here are some embarassingly regular carrots. Sorry.","color":"white"}]
execute if score BetterEconomy bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=vendor_golden_carrot_0,tag=mg.flw] [{"text":"<"},{"text":"Weevo","color":"green"},{"text":"> I'll probably not be able to afford the signature gilding for my carrots tomorrow. Though, I wouldn't be opposed to you stopping by and saying hello!","color":"white"}]

execute if score BetterEconomy bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=!vendor_golden_carrot_0,tag=mg.flw] [{"text":"<"},{"text":"Weevo","color":"green"},{"text":"> I have some niiiiice golden carrots for you today! One look at the radiant gleam of a freshly gilded carrot in the moonlight is enough to make a bug forget about all the monsters stomping around above ground.","color":"white"}]
execute if score BetterEconomy bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=vendor_golden_carrot_0,tag=mg.flw] [{"text":"<"},{"text":"Weevo","color":"green"},{"text":"> I'm working on gilding carrots right now! It's a bit of a process though, lots of fine brushwork and intermittent cursing, so I won't have more ready for you until tomorrow.","color":"white"}]

execute if score BetterEconomy bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run give @a[distance=..10,tag=!vendor_golden_carrot_0,tag=mg.flw] carrot 8
execute if score BetterEconomy bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run give @a[distance=..10,tag=!vendor_golden_carrot_0,tag=mg.flw] golden_carrot 8
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tag @a[distance=..10,tag=!vendor_golden_carrot_0,tag=mg.flw] add vendor_golden_carrot_0


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
