execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.turtle.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 0.5
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Time Nexus","color":"green"},{"text":"> Ah, missing the Virus already? If you have any ","color":"white"},{"text":"unfinished business","color":"gold"},{"text":", I can send you back in time, back to the Isles, to the point before you killed him. To reach this place again, you'd have to defeat the World Virus once more. Walk down the ","color":"white"},{"text":"passage behind me","color":"light_purple"},{"text":" and I will rewind your clock...","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
