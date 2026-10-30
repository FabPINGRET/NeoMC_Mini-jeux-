execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.8
execute if score traded_with_9 bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ unless items entity @p[tag=mg.flw] weapon.mainhand minecraft:clay_ball[minecraft:custom_model_data={strings:['9']}] run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Squaninki","color":"aqua"},{"text":"> Oi'm so thirsty. Ain't had a drop o' juice in ages! I've yew've got a","color":"white"},{"text":" Juice Chalice","color":"red"},{"text":" Oi could sip from, Oi'd ","color":"white"},{"text":"trade ","color":"yellow"},{"text":"ya me most proized possession, honest!","color":"white"}]

execute if score traded_with_9 bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Squaninki","color":"aqua"},{"text":"> That juice yew gave me was the best Oi ever 'ad. Roight 'eavenly that was. Oi can't stop havin dreams about it to be honest. S'pose Oi wasn't gonna be able to resell that","color":"white"},{"text":" Royal Gem","color":"aqua"},{"text":" Oi nicked off a ","color":"white"},{"text":"Sand Dragon","color":"gold"},{"text":" anyhow.","color":"white"}]

execute if score traded_with_9 bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ if items entity @p[tag=mg.flw] weapon.mainhand minecraft:clay_ball[minecraft:custom_model_data={strings:['9']}] run tag @p[tag=mg.flw] add trade_complete

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @p[tag=mg.flw] if entity @s[tag=trade_complete] run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Squaninki","color":"aqua"},{"text":"> Blimey, that juice! Tastes amazin! And the cup's dead fancy too. Hit the spot roight proper, that did. Like I promised, here's a","color":"white"},{"text":" Royal Gem","color":"aqua"},{"text":" Oi nicked off a ","color":"white"},{"text":"Sand Dragon","color":"gold"},{"text":".","color":"white"}]
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @p[tag=mg.flw] if entity @s[tag=trade_complete] run item replace entity @s weapon.mainhand from block -196 54 -1214 container.0
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @p[tag=mg.flw] if entity @s[tag=trade_complete] run playsound minecraft:zelda.itemget master @p[tag=mg.flw] ~ ~ ~ 1 1
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @p[tag=mg.flw] if entity @s[tag=trade_complete] run scoreboard players set traded_with_9 bool 1

tag @a[tag=mg.flw] remove trade_complete

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
