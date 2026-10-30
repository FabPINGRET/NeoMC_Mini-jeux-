execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 0.8
execute if score traded_with_6 bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ unless items entity @p[tag=mg.flw] weapon.mainhand minecraft:clay_ball[minecraft:custom_model_data={strings:['6']}] run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Twisty Stewie","color":"aqua"},{"text":"> I've been packing boxes and barrels for weeks, and I just realized my lucky","color":"white"},{"text":" Skull Coin","color":"yellow"},{"text":" has gone missing! Could you help me find it? I'll ","color":"white"},{"text":"trade","color":"yellow"},{"text":" you something nice for it as a reward!","color":"white"}]

execute if score traded_with_6 bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Twisty Stewie","color":"aqua"},{"text":"> My","color":"white"},{"text":" Skull Coin","color":"yellow"},{"text":" has improved my luck a lot, thanks again! Did you figure out what the deal with that ","color":"white"},{"text":"Tiny Chest","color":"gold"},{"text":" is? The chest has carvings of ","color":"white"},{"text":"really tall trees","color":"green"},{"text":" on it, unlike any I've ever seen.","color":"white"}]

execute if score traded_with_6 bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ if items entity @p[tag=mg.flw] weapon.mainhand minecraft:clay_ball[minecraft:custom_model_data={strings:['6']}] run tag @p[tag=mg.flw] add trade_complete

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @p[tag=mg.flw] if entity @s[tag=trade_complete] run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Twisty Stewie","color":"aqua"},{"text":"> My lucky","color":"white"},{"text":" Skull Coin","color":"yellow"},{"text":", you found it! You're a real one, hero, you're a real one. Here, I found this ","color":"white"},{"text":"Tiny Chest","color":"gold"},{"text":" among the boxes and barrels that definitely isn't ours. The chest has carvings of ","color":"white"},{"text":"really tall trees ","color":"green"},{"text":"on it, unlike any I've ever seen.","color":"white"}]
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @p[tag=mg.flw] if entity @s[tag=trade_complete] run item replace entity @s weapon.mainhand from block -53 56 -250 container.0
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @p[tag=mg.flw] if entity @s[tag=trade_complete] run playsound minecraft:zelda.itemget master @p[tag=mg.flw] ~ ~ ~ 1 1
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @p[tag=mg.flw] if entity @s[tag=trade_complete] run scoreboard players set traded_with_6 bool 1

tag @a[tag=mg.flw] remove trade_complete

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
