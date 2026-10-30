execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.armadillo.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.5
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Nemoris","color":"#D47453"},{"text":"> I've never been to the ","color":"white"},{"text":"Isle of Silence","color":"gray"},{"text":", but the","color":"white"},{"text":" Monks of Shh","color":"red"},{"text":" who live there interest and unsettle me. If you watch one for long enough, it will just puff away into dust.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
