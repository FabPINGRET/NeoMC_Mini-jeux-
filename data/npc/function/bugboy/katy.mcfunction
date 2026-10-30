execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.bee.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 1

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ if entity @p[tag=overgrown_shrine_complete,tag=mg.flw] run setblock 200 49 -367 minecraft:redstone_block

execute if block 200 49 -367 minecraft:air at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Katy","color":"green"},{"text":"> This shrine continues down those vines. I'm convinced there is a ","color":"white"},{"text":"fourth goddess","color":"dark_aqua"},{"text":" whose name we have forgotten but whose role in the forest is equally critical. If you could find the","color":"white"},{"text":" name of the forgotten goddess","color":"dark_aqua"},{"text":" so that I could worship her, it would make me","color":"white"},{"text":" wonderfully happy","color":"red"},{"text":".","color":"white"}]


execute if block 200 49 -367 minecraft:redstone_block at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Katy","color":"green"},{"text":"> ","color":"white"},{"text":"Intercession","color":"dark_aqua"},{"text":"... Yes, that must be her name. After all, hers is the role we ","color":"white"},{"text":"Bugboys ","color":"green"},{"text":"play! When all seems lost for some poor tree, we intercede for it, nurturing it back to life. Hero, I believe that intercession is your role in the Isles as well. When all seemed lost, you arrived from the void. You've made me ","color":"white"},{"text":"wonderfully happy","color":"red"},{"text":", thank you!","color":"white"}]
execute if block 200 49 -367 minecraft:redstone_block at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1.75 ~ run particle minecraft:heart ~ ~ ~ 0.3 0.3 0.3 0 10 force


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
