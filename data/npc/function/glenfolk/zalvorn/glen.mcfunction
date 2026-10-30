execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 0.8
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Zalvorn the Puppet Guy","color":"gold"},{"text":"> I've a ","color":"white"},{"text":"puppet show","color":"green"},{"text":" in the desert, a sight you simply must see. I came to the castle seeking new inspirations; fresh material for my little darlings. But alas, the road home was destroyed, ","color":"white"},{"text":"torn asunder by a meteor","color":"gold"},{"text":". No matter! I will find a way. Nothing shall keep me from my puppets.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
