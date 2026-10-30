execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.frog.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.7

#PRE MEMORY RESTORATION
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Quibbint","color":"#44BBFF"},{"text":"> Welcome to Quibbint's Secret Store! Don't tell anyone about it or I will make you frown like you've never frowned before in your entire","color":"white"},{"text":" LIFE","color":"white","bold":true,"italic":true},{"text":". Kapeesh?","color":"white","bold":false,"italic":false}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
