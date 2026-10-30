execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.bee.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Phly","color":"green"},{"text":"> Honestly, feel free to just poop on the floor wherever you want. Yeah, um, it being good fertilizer for the trees is the only reason pretty much. Yeah, the only reason.","color":"white"},{"text":"\n\nYou hear his stomach rumbling from where you stand...","color":"gray","italic":true}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
