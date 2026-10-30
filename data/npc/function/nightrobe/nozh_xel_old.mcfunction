execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.strider.happy neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute if score traded_with_2 bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ unless items entity @p[tag=mg.flw] weapon.mainhand minecraft:clay_ball[minecraft:custom_model_data={strings:['2']}] run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Nozh-Xel","color":"light_purple"},{"text":"> My ","color":"white"},{"text":"Weird Ring","color":"light_purple"},{"text":" slipped off my weird finger, and I can't find it anywhere! It might have fallen through a crack in space, who knows. If you find it on your travels, return it to me and I'll happily ","color":"white"},{"text":"trade","color":"yellow"},{"text":" you something for it!","color":"white"}]

execute if score traded_with_2 bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Nozh-Xel","color":"light_purple"},{"text":"> Thanks for recovering my","color":"white"},{"text":" Weird Ring","color":"light_purple"},{"text":", Have you found someone to give the","color":"white"},{"text":" Ink Jar","color":"gray"},{"text":" to yet? It must belong to someone who ","color":"white"},{"text":"spends time around large animals","color":"green"},{"text":"...","color":"white"}]

execute if score traded_with_2 bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ if items entity @p[tag=mg.flw] weapon.mainhand minecraft:clay_ball[minecraft:custom_model_data={strings:['2']}] run tag @p[tag=mg.flw] add trade_complete

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @p[tag=mg.flw] if entity @s[tag=trade_complete] run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Nozh-Xel","color":"light_purple"},{"text":"> That's my","color":"white"},{"text":" Weird Ring","color":"light_purple"},{"text":"! Thank you for returning it to me! Here, have this","color":"white"},{"text":" Ink Jar","color":"gray"},{"text":" I picked up. It smells like it belongs to someone who ","color":"white"},{"text":"spends time around large animals","color":"green"},{"text":"...","color":"white"}]
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @p[tag=mg.flw] if entity @s[tag=trade_complete] run item replace entity @s weapon.mainhand from block 339 74 1587 container.0
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @p[tag=mg.flw] if entity @s[tag=trade_complete] run playsound minecraft:zelda.itemget master @p[tag=mg.flw] ~ ~ ~ 1 1
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @p[tag=mg.flw] if entity @s[tag=trade_complete] run scoreboard players set traded_with_2 bool 1

tag @a[tag=mg.flw] remove trade_complete

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
