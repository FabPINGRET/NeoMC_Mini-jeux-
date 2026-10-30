execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.panda.cant_breed neutral @a[tag=mg.flw] ~ ~ ~ 1 0.8
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Vizhniv","color":"gold"},{"text":"> A ","color":"white"},{"text":"weird guy ","color":"yellow"},{"text":"gave this to my dad. It's cool to look at, sure, but I don't know what it's supposed to actually ","color":"white"},{"text":"do","color":"white","italic":true},{"text":", ya know?","color":"white","italic":false}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
