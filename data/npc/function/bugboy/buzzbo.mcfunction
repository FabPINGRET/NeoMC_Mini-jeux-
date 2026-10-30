execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.bee.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute if block 175 46 -220 minecraft:air at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Buzzbo","color":"yellow"},{"text":"> It's a lot harder to get honey down here than it used to be. We had some perfect spots picked out for new beehives, but... well, I guess that dream might have to wait. Unlezzzzzz you'd be willing to help us!","color":"white"}]
execute if block 175 46 -220 minecraft:redstone_block at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Buzzbo","color":"yellow"},{"text":"> I'm so exzzzzzited to finally have honey flowing once again! We're a small buzzzzzziness so the help goes a long way.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
