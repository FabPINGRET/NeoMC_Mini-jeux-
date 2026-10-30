execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.creaking.step neutral @a[tag=mg.flw] ~ ~ ~ 1 2
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.axolotl.idle_air neutral @a[tag=mg.flw] ~ ~ ~ 1 1

execute if score Inventory TomeOfTongues matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Snabu-Paku","color":"#C29D62"},{"text":"> ","color":"white"},{"text":"*nuk-tuk* ","color":"gray","italic":true},{"text":"The net of thick vines to the south is what we Pygmies call the","color":"white"},{"text":" Tangleweb","color":"dark_green"},{"text":". It is an ancient feature of the jungle the ","color":"white"},{"text":"Lord of Forest","color":"green"},{"text":" always loved. I pray he is able to escape the ","color":"white"},{"text":"tomb ","color":"green"},{"text":"so he can see it once again...","color":"white","italic":false},{"text":" *tuk-nuk* ","color":"gray","italic":true}]

execute if score Inventory TomeOfTongues matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Snabu-Paku","color":"#C29D62"},{"text":"> ","color":"white"},{"text":"*nuk-tuk* ","color":"gray","italic":true},{"text":"The net of thick vines to the south is what we Pygmies call the","color":"white"},{"text":" Tangleweb","color":"dark_green"},{"text":". It is an ancient feature of the jungle.","color":"white","italic":false},{"text":" *tuk-nuk* ","color":"gray","italic":true}]

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run function npc:pygmy/pose/repose

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
