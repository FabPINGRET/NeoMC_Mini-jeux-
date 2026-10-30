execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.dolphin.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute if score bubble_lake Story matches 0..3 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Whiskerton","color":"yellow"},{"text":"> ","color":"white"},{"text":"Bubble Lake","color":"blue"},{"text":" means everything to us. It’s our heritage and our home. One day soon, our children will swim here in peace. We just have to finish this fight.","color":"white"}]
execute if score bubble_lake Story matches 4 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Whiskerton","color":"yellow"},{"text":"> ","color":"white"},{"text":"Bubble Lake","color":"blue"},{"text":" means everything to us. It’s our heritage and our home. One day soon, our children will swim here in peace.","color":"white"}]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
