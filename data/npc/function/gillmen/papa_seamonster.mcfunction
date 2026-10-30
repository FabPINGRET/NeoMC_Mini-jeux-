execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.dolphin.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Papa Seamonster","color":"yellow"},{"text":"> Most of my noble Gill Guild is fighting for their lives down in the ","color":"white"},{"text":"Lake","color":"blue"},{"text":", trying to hunt down every last monster and make it safe for us to return. Our division up here is focused on exploring every corner of the Floaty Isles looking for secrets.","color":"white"},{"text":" Talk to Gylvester ","color":"yellow"},{"text":"if you want to hear about any of the interesting things we've found!","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
