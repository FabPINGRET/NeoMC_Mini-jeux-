execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 0.8
execute if score Inventory ThornBow matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Commander Murray","color":"aqua"},{"text":"> My men take pride in our defense of this castle and our lands. Robbo, one of our best, is currently stationed by the ","color":"white"},{"text":"bloom contagion ","color":"light_purple"},{"text":"while the rest of us keep the peace here and diligently train.","color":"white"}]
execute if score Inventory ThornBow matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Commander Murray","color":"aqua"},{"text":"> My men take pride in our defense of this castle and our lands. We all look up to you, hero! I pray we can achieve your level of skill with nothing but diligent training and performance-enhancing drugs.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
