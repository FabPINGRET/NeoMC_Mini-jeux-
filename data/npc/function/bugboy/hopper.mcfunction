execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.bee.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Hopper","color":"green"},{"text":"> So, you've come to me for jumping advice, eh? Shhh sh sh it's alright, I'll teach ya. My secret is, ready for this? My secret is pressing ","color":"white"},{"keybind":"key.jump"},{"text":". Pretty cool right? Try it!"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
