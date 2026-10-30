execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.strider.happy neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Nynngrizh-Ao","color":"light_purple"},{"text":"> The Floaty Isles used to have a wormhole system called the Buh' Tween, but we closed it after suspecting the", "color":"white"},{"text":" three scourges ", "color":"light_purple"},{"text":"might have broken in that way. Space is thin in places; it's best to not risk intruders. Plenty of other worlds have Buh' Tweens of their own!","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
