execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 0.8
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Zalvorn the Puppet Guy","color":"gold"},{"text":"> Ah, most unfortunate timing, my friend! I am deep in rehearsal for my ","color":"white"},{"text":"grand performance","color":"green"},{"text":". Would you desire to take the stage yourself? Perhaps as one of my dear, delightful puppets? Haha! But I jest, of course.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
