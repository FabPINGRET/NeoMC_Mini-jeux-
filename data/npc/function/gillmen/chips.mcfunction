execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.dolphin.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Chips","color":"yellow"},{"text":"> Oh hey, you interested in the","color":"white"},{"text":" Trial Well ","color":"red"},{"text":"too? I'm with the ","color":"white"},{"text":"Gill Guild","color":"yellow"},{"text":", and we've been curious about this place ever since we discovered it. We think there's","color":"white"},{"text":" treasure ","color":"yellow"},{"text":"at the bottom if you can get past a few rooms full of monsters without dying. There's an ","color":"white"},{"text":"entrance at the top of the lava fall","color":"red"},{"text":" we just can't figure out how to reach yet...","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
