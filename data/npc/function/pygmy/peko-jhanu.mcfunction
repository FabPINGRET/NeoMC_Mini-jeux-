execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.creaking.step neutral @a[tag=mg.flw] ~ ~ ~ 1 2
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.axolotl.idle_air neutral @a[tag=mg.flw] ~ ~ ~ 1 1

execute if score traded_with_7 bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ unless items entity @p[tag=mg.flw] weapon.mainhand minecraft:clay_ball[minecraft:custom_model_data={strings:['7']}] run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Peko-Jhanu","color":"#C29D62"},{"text":"> ","color":"white"},{"text":"*nuk-tuk* ","color":"gray","italic":true},{"text":"I'm down here looking for a ","color":"white"},{"text":"Tiny Chest","color":"gold"},{"text":" that I lost some time ago. If you ever happen to recover it for me, I will","color":"white"},{"text":" trade ","color":"yellow"},{"text":"an interesting thing I found during my search for it.","color":"white","italic":false},{"text":" *tuk-nuk* ","color":"gray","italic":true}]

execute if score traded_with_7 bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Peko-Jhanu","color":"#C29D62"},{"text":"> ","color":"white"},{"text":"*nuk-tuk* ","color":"gray","italic":true},{"text":"Thanks for returning my ","color":"white"},{"text":"Tiny Chest","color":"gold"},{"text":" full of Lord of Forest funko pops! I wonder who might need that","color":"white"},{"text":" Important-Looking Screw","color":"gray"},{"text":" I found. It looks like it could be useful to a","color":"white"},{"text":" person made of copper","color":"gold"},{"text":".","color":"white","italic":false},{"text":" *tuk-nuk* ","color":"gray","italic":true}]

execute if score traded_with_7 bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ if items entity @p[tag=mg.flw] weapon.mainhand minecraft:clay_ball[minecraft:custom_model_data={strings:['7']}] run tag @p[tag=mg.flw] add trade_complete

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @p[tag=mg.flw] if entity @s[tag=trade_complete] run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Peko-Jhanu","color":"#C29D62"},{"text":"> ","color":"white"},{"text":"*nuk-tuk* ","color":"gray","italic":true},{"text":"You found my ","color":"white"},{"text":"Tiny Chest","color":"gold"},{"text":"! Thanks so much, this chest contains all of my Lord of Forest funko pops! As promised, here's an","color":"white"},{"text":" Important-Looking Screw","color":"gray"},{"text":" I found. It looks like it could be useful to a","color":"white"},{"text":" person made of copper","color":"gold"},{"text":".","color":"white","italic":false},{"text":" *tuk-nuk* ","color":"gray","italic":true}]
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @p[tag=mg.flw] if entity @s[tag=trade_complete] run item replace entity @s weapon.mainhand from block 10329 33 157 container.0
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @p[tag=mg.flw] if entity @s[tag=trade_complete] run playsound minecraft:zelda.itemget master @p[tag=mg.flw] ~ ~ ~ 1 1
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @p[tag=mg.flw] if entity @s[tag=trade_complete] run scoreboard players set traded_with_7 bool 1

tag @a[tag=mg.flw] remove trade_complete

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run function npc:pygmy/pose/repose

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
