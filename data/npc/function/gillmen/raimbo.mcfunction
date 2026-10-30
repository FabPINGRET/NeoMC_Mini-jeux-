execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.dolphin.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Raimbo","color":"yellow"},{"text":"> We followed you through the portal but got caught snooping and were arrested by weirdos. After you freed the ","color":"white"},{"text":"Lord","color":"red"},{"text":", he came and broke everyone out! Now the ","color":"white"},{"text":"Gill Guild","color":"blue"},{"text":" will be able to help you find secrets in the ","color":"white"},{"text":"Dark Isles","color":"light_purple"},{"text":"! There is so much treaure hunting to be done here...","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
