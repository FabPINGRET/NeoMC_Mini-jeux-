execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.creaking.step neutral @a[tag=mg.flw] ~ ~ ~ 1 2
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.axolotl.idle_air neutral @a[tag=mg.flw] ~ ~ ~ 1 1

execute if score Inventory TomeOfTongues matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Knoko-Paki","color":"#C29D62"},{"text":"> ","color":"white"},{"text":"*nuk-tuk* ","color":"gray","italic":true},{"text":"The ","color":"white"},{"text":"Lord of Forest ","color":"green"},{"text":"was always a peaceful leader. We Pygmies never needed much from the rest of the ","color":"white"},{"text":"Isles ","color":"dark_purple"},{"text":"and we never had much to offer them in return. Now, the problems of the ","color":"white"},{"text":"Isles","color":"dark_purple"},{"text":" have come to us, and we are left defenseless.","color":"white","italic":false},{"text":" *tuk-nuk* ","color":"gray","italic":true}]

execute if score Inventory TomeOfTongues matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Knoko-Paki","color":"#C29D62"},{"text":"> ","color":"white"},{"text":"*nuk-tuk* ","color":"gray","italic":true},{"text":"We Pygmies never needed much from the rest of the","color":"white"},{"text":" Isles","color":"dark_purple"},{"text":" and we never had much to offer them in return. You have come to us of your own accord to restore our","color":"white"},{"text":" Lord","color":"green"},{"text":" to us. We are grateful for that.","color":"white","italic":false},{"text":" *tuk-nuk* ","color":"gray","italic":true}]


execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run function npc:pygmy/pose/repose

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
