execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.shulker.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Slime Man","color":"green"},{"text":"> Ah, you made it! I wasn't even really looking for this spirit, but I found it before you anyway. I don't speak Fungloid though, do you? If so, could you ask this spirit to replace the","color":"white"},{"text":" red track switch","color":"red"},{"text":"? I'm gonna keep searching for this","color":"white"},{"text":" magic spell","color":"light_purple"},{"text":". I'm sure it'll make me a real, er, stronger hero!","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
