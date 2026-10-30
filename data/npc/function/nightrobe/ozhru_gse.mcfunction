execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.strider.happy neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Ozhru-Gse","color":"light_purple"},{"text":"> Space is a malleable thing, like clay on a wheel. A vessel that can take any shape we need it to. And it leaves sharp edges when it breaks. These ","color":"white"},{"text":"scourges","color":"light_purple"},{"text":" have shredded the spacial undergirding of the Isles, hero.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
