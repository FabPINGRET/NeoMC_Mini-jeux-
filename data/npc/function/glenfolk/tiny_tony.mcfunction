execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.8
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Tiny Tony","color":"aqua"},{"text":"> My parents gave themselves a little promotion from mayor and mayoress to king and queen! But, it's ok, they said they got elected. The","color":"white"},{"text":" Bell of Life","color":"gold"},{"text":" is right up that ladder if you want to go see it!","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
