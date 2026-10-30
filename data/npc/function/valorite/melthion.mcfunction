execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.armadillo.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.5
execute if score traded_with_8 bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ unless items entity @p[tag=mg.flw] weapon.mainhand minecraft:clay_ball[minecraft:custom_model_data={strings:['8']}] run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Dr. Melthion","color":"#D47453"},{"text":"> My-y jaw-aw is coming-ing loose! I need-eed a ","color":"white"},{"text":"Screw","color":"gray"},{"text":" or some-omething to bolt it back-ack onto my face-ce. I'd ","color":"white"},{"text":"trade-ade","color":"yellow"},{"text":" you for one if you-ou had one-ne for me!","color":"white"}]

execute if score traded_with_8 bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Dr. Melthion","color":"#D47453"},{"text":"> My jaw feels good as new, thanks again. My friends are actually having a curb-biting competition later if you want to join. They said I have a good chance of winning if I can open my mouth wide enough! Haha, I love those guys. You ever do anything with that ","color":"white"},{"text":"Juice Chalice","color":"red"},{"text":"? I heard it's real popular among","color":"white"},{"text":" people with no parents","color":"green"},{"text":".","color":"white"}]

execute if score traded_with_8 bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ if items entity @p[tag=mg.flw] weapon.mainhand minecraft:clay_ball[minecraft:custom_model_data={strings:['8']}] run tag @p[tag=mg.flw] add trade_complete

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @p[tag=mg.flw] if entity @s[tag=trade_complete] run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Dr. Melthion","color":"#D47453"},{"text":"> A screw-ew! Please, let me-e secure my jaw-aw with it... There! That's so much better! Let me tell ya, that's the last time I'm falling for letting my buddies curb stomp me as a prank haha. Here, you can have this ","color":"white"},{"text":"Juice Chalice","color":"red"},{"text":" one of my patients left here. I heard it's real popular among","color":"white"},{"text":" people with no parents","color":"green"},{"text":".","color":"white"}]
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @p[tag=mg.flw] if entity @s[tag=trade_complete] run item replace entity @s weapon.mainhand from block 9919 56 -126 container.0
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @p[tag=mg.flw] if entity @s[tag=trade_complete] run playsound minecraft:zelda.itemget master @p[tag=mg.flw] ~ ~ ~ 1 1
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @p[tag=mg.flw] if entity @s[tag=trade_complete] run scoreboard players set traded_with_8 bool 1

tag @a[tag=mg.flw] remove trade_complete

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
