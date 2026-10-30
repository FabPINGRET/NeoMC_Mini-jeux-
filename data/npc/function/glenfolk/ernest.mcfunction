execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 0.8
execute if block 512 90 -80 air at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Ernest P. Worrell","color":"aqua"},{"text":"> Hey Vern, it's Ernest. We were in the middle of filming ","color":"white"},{"text":"Ernest Goes to the Floaty Isles","color":"gold"},{"text":", and I got myself trapped in here! If you could unlock this here door, I'd ","color":"white"},{"text":"really, really appreciate ","color":"red"},{"text":"it. Knowwhatimean?","color":"white"}]
execute unless block 512 90 -80 air at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Ernest P. Worrell","color":"aqua"},{"text":"> Well, golly Bob howdy! The door's been unlocked! We can keep filming now thanks to you! You've made me a ","color":"white"},{"text":"very, very happy","color":"red"},{"text":" man. Knowwhatimean?","color":"white"}]
execute unless block 512 90 -80 air run setblock 514 90 -81 minecraft:redstone_block
execute unless block 512 90 -80 air at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1.75 ~ run particle minecraft:heart ~ ~ ~ 0.3 0.3 0.3 0 10 force 

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
