execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.bee.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=!vendor_arrow_0,tag=mg.flw] [{"text":"<"},{"text":"Mawth","color":"green"},{"text":"> Arrows for you! Even if you don't have a bow, they're great for picking your teeth.","color":"white"}]
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=vendor_arrow_0,tag=mg.flw] [{"text":"<"},{"text":"Mawth","color":"green"},{"text":"> I can only make these arrows so fast. If you need something else to pick your teeth with in the meantime, maybe try a stick or something.","color":"white"}]

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run give @a[distance=..10,tag=!vendor_arrow_0,tag=mg.flw] arrow 12
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tag @a[distance=..10,tag=!vendor_arrow_0,tag=mg.flw] add vendor_arrow_0


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
