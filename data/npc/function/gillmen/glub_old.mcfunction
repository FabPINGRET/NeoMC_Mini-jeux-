execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.dolphin.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute if score traded_with_1 bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ unless items entity @p[tag=mg.flw] weapon.mainhand minecraft:clay_ball[minecraft:custom_model_data={strings:['1']}] run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Glub","color":"yellow"},{"text":"> I've been looking for a","color":"white"},{"text":" Seawater Orb","color":"blue"},{"text":" for many months; they're exceedingly rare. If you ever find one, please give it to me! I'll","color":"white"},{"text":" trade","color":"yellow"},{"text":" you something bizarre I found for it.","color":"white"}]

execute if score traded_with_1 bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Glub","color":"yellow"},{"text":"> Thanks for the","color":"white"},{"text":" Seawater Orb","color":"blue"},{"text":"! Have you found someone to give the","color":"white"},{"text":" Weird Ring","color":"light_purple"},{"text":" to yet? It must belong to someone ","color":"white"},{"text":"otherworldly","color":"light_purple"},{"text":"...","color":"white"}]

execute if score traded_with_1 bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ if items entity @p[tag=mg.flw] weapon.mainhand minecraft:clay_ball[minecraft:custom_model_data={strings:['1']}] run tag @p[tag=mg.flw] add trade_complete

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @p[tag=mg.flw] if entity @s[tag=trade_complete] run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Glub","color":"yellow"},{"text":"> A","color":"white"},{"text":" Seawater Orb","color":"blue"},{"text":"! Wow, thanks for giving it to me! Here, have this","color":"white"},{"text":" Weird Ring","color":"light_purple"},{"text":" I found. It must belong to someone ","color":"white"},{"text":"otherworldly","color":"light_purple"},{"text":"...","color":"white"}]
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @p[tag=mg.flw] if entity @s[tag=trade_complete] run item replace entity @s weapon.mainhand from block 16 70 139 container.0
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @p[tag=mg.flw] if entity @s[tag=trade_complete] run playsound minecraft:zelda.itemget master @p[tag=mg.flw] ~ ~ ~ 1 1
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @p[tag=mg.flw] if entity @s[tag=trade_complete] run scoreboard players set traded_with_1 bool 1

tag @a[tag=mg.flw] remove trade_complete

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
