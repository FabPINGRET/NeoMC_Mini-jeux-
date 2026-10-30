execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.panda.cant_breed neutral @a[tag=mg.flw] ~ ~ ~ 1 0.8
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Nazhzaima","color":"gold"},{"text":"> The meteors were scary enough, but once monsters started appearing at night, we ripped our houses out of the ground and floated them in the air where they couldn't reach us! I see Zhaini over there just built a fence, which in retrospect would have worked fine too.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
