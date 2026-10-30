execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.8
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Norply","color":"aqua"},{"text":"> There are lots of enemies out in the Floa'y Isles these days. Oi 'eard somewhere that","color":"white"},{"text":" monsters wif shields take almost no damage from arrows","color":"green"},{"text":" and that ","color":"white"},{"text":"monsters wif axes can disable your shield wif their attacks","color":"gold"},{"text":". Scary!","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
