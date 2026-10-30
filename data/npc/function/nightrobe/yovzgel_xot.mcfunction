execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.strider.happy neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute if score Inventory FeatherBrush matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Yovzgel-Xot","color":"light_purple"},{"text":"> If you keep walking down this corridor, you'll reach the Mindczar's house. She is waiting for you, I think.","color":"white"}]
execute if score Inventory FeatherBrush matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Yovzgel-Xot","color":"light_purple"},{"text":"> Limbohold is a quick escape route for us whenever we encounter a dimension ruled by the","color":"white"},{"text":" World Virus","color":"dark_purple"},{"text":". We know its twisting paths far better than he does.","color":"white"}]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
