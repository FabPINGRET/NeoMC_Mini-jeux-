execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.bee.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Mayor Skeeter","color":"green"},{"text":"> It's good to see you again, Hero. These giant tree stumps above us used to be our homes. They sheltered us from the rain, and kept us warm and dry. Now that we're underground, we can start to return the favor and nurture these beautiful trees back to their former splendor. We've made the best of bad situation, and I'm proud of my Bugboys for doing it.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
