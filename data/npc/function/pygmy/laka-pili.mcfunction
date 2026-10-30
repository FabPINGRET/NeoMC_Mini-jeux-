execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.creaking.step neutral @a[tag=mg.flw] ~ ~ ~ 1 2
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.axolotl.idle_air neutral @a[tag=mg.flw] ~ ~ ~ 1 1

execute if score zalvorn Story matches 0..1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Laka-Pili","color":"#C29D62"},{"text":"> ","color":"white"},{"text":"*nuk-tuk* ","color":"gray","italic":true},{"text":"I don't know you, fleshy one. Are you here to trade? Hunt? Trap? If not, do you at least carry a message? A gift? A plea? Whatever the reason, it had better be good.","color":"white"},{"text":" Tanglevine","color":"green"},{"text":" is not kind to tourists.","color":"white","italic":false},{"text":" *tuk-nuk* ","color":"gray","italic":true}]

execute if score zalvorn Story matches 2 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Laka-Pili","color":"#C29D62"},{"text":"> ","color":"white"},{"text":"*nuk-tuk* ","color":"gray","italic":true},{"text":"Pupu-Nini? Ah, that's who I must have seen! She went down the path to where the","color":"white"},{"text":" Worldgate ","color":"yellow"},{"text":"is. My intuition tells me she went through it and is","color":"white"},{"text":" somewhere on the other side","color":"yellow"},{"text":". She's too curious for her own good.","color":"white","italic":false},{"text":" *tuk-nuk* ","color":"gray","italic":true}]

execute if score zalvorn Story matches 3.. at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Laka-Pili","color":"#C29D62"},{"text":"> ","color":"white"},{"text":"*nuk-tuk* ","color":"gray","italic":true},{"text":"Surely, you are welcome in","color":"white"},{"text":" Tanglevine","color":"green"},{"text":" all the days of your life.","color":"white","italic":false},{"text":" *tuk-nuk* ","color":"gray","italic":true}]


execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run function npc:pygmy/pose/repose

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
