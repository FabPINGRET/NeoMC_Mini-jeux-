execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.bee.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute if score traded_with_5 bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ unless items entity @p[tag=mg.flw] weapon.mainhand minecraft:clay_ball[minecraft:custom_model_data={strings:['5']}] run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Milkweed","color":"green"},{"text":"> Hey there, I'm down here looking for a ","color":"white"},{"text":"Green Mushroom","color":"green"},{"text":". I overheard someone saying it's the best thing they've ever eaten, but I can't find one anywhere. If you ever find a ","color":"white"},{"text":"Green Mushroom","color":"green"},{"text":" on your travels, please bring it to me! I'll","color":"white"},{"text":" trade","color":"yellow"},{"text":" you something interesting for it.","color":"white"}]

execute if score traded_with_5 bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Milkweed","color":"green"},{"text":"> That ","color":"white"},{"text":"Green Mushroom","color":"green"},{"text":" was so yummy I'm gonna have a conniption. Did you find who the","color":"white"},{"text":" Skull Coin","color":"yellow"},{"text":" belongs to? My buggish intuition tells me ","color":"white"},{"text":"someone loading ships nearby","color":"aqua"},{"text":" is probably looking for it.","color":"white"}]

execute if score traded_with_5 bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ if items entity @p[tag=mg.flw] weapon.mainhand minecraft:clay_ball[minecraft:custom_model_data={strings:['5']}] run tag @p[tag=mg.flw] add trade_complete

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @p[tag=mg.flw] if entity @s[tag=trade_complete] run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Milkweed","color":"green"},{"text":"> Whoa, a ","color":"white"},{"text":"Green Mushroom","color":"green"},{"text":"! You got it for me? This is great! Here, I'd be happy if you took this","color":"white"},{"text":" Skull Coin","color":"yellow"},{"text":" in return. My buggish intuition tells me ","color":"white"},{"text":"someone loading ships nearby","color":"aqua"},{"text":" is probably looking for it.","color":"white"}]
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @p[tag=mg.flw] if entity @s[tag=trade_complete] run item replace entity @s weapon.mainhand from block 121 37 -241 container.0
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @p[tag=mg.flw] if entity @s[tag=trade_complete] run playsound minecraft:zelda.itemget master @p[tag=mg.flw] ~ ~ ~ 1 1
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @p[tag=mg.flw] if entity @s[tag=trade_complete] run scoreboard players set traded_with_5 bool 1

tag @a[tag=mg.flw] remove trade_complete


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
