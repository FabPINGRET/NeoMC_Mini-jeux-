execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.dolphin.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Scalebert","color":"yellow"},{"text":"> Gotta organize these reports, gotta file these claims away properly... What's this? A note about strange whispering from the","color":"white"},{"text":" Water Factory","color":"blue"},{"text":"? A note about a magic shrine in ","color":"white"},{"text":"Blue's basement","color":"blue"},{"text":"? A note about the Gill Guild finding a ","color":"white"},{"text":"passage locked with a riddle","color":"blue"},{"text":" down by the lake? Gotta file them away!","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
