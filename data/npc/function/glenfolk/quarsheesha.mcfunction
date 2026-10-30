execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run advancement grant @a[distance=..10,tag=mg.flw] only sidequest:undercroft_start

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute if block 90 45 46 air at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Quarsheesha","color":"aqua"},{"text":"> This Undercroft is full of mysterious, arcane treasures, I just know it! I think these vault doors can be opened if we find enough","color":"white"},{"text":" Secret Keys","color":"dark_purple"},{"text":". I've been studying them, and they appear to be found all over the world in purple boxes like the one behind me. If you find any","color":"white"},{"text":" Secret Keys","color":"dark_purple"},{"text":", put them in the recepticle!","color":"white"}]

execute if score beat_sealed_citadel bool matches 0 unless block 90 45 46 air at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Quarsheesha","color":"aqua"},{"text":"> You've found every last ","color":"white"},{"text":"Secret Key","color":"dark_purple"},{"text":"! That's amazing! But... what is that draft coming from the last vault?","color":"white"}]

execute if score beat_sealed_citadel bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Quarsheesha","color":"aqua"},{"text":"> You were in the last vault for a while! I was worried, but it would have been foolish of me to follow you into that place. I have a sweetie of a husband after all! Thanks for assisting our research, I mean it.","color":"white"}]



#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
