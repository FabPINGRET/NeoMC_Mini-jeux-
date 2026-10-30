execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Mime","color":"white"},{"text":"> ...","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
