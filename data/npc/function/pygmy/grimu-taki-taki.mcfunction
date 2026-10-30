execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.creaking.step neutral @a[tag=mg.flw] ~ ~ ~ 1 2
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.axolotl.idle_air neutral @a[tag=mg.flw] ~ ~ ~ 1 1

execute if score zalvorn Story matches 0..2 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Grimu-Taki-Taki","color":"#C29D62"},{"text":"> ","color":"white"},{"text":"*nuk-tuk* ","color":"gray","italic":true},{"text":"Our noble jungle is being choked by chaos. The","color":"white"},{"text":" Lord of Forest","color":"green"},{"text":" has been sealed within the ","color":"white"},{"text":"Serpent King's Tomb","color":"green"},{"text":", and Pupu-Nini, the only Pygmy who knows the chant of unsealing, has ","color":"white"},{"text":"gone missing","color":"gold"},{"text":"! Our ritual dancers ","color":"white"},{"text":"beneath the Tangleweb","color":"dark_green"},{"text":" have been working on a ","color":"white"},{"text":"magic dance to discover where Pupu-Nini is","color":"gold"},{"text":". If you want to help, go see if their dance is ready.","color":"white","italic":false},{"text":" *tuk-nuk* ","color":"gray","italic":true}]

execute if score zalvorn Story matches 3 if score Inventory TomeOfTongues matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Grimu-Taki-Taki","color":"#C29D62"},{"text":"> ","color":"white"},{"text":"*nuk-tuk* ","color":"gray","italic":true},{"text":"Our noble jungle is being choked by chaos. The","color":"white"},{"text":" Lord of Forest","color":"green"},{"text":" has been sealed within the ","color":"white"},{"text":"Serpent King's Tomb","color":"green"},{"text":", but at least Pupu-Nini, the only Pygmy who knows the chant of unsealing, has been returned to us.","color":"white","italic":false},{"text":" *tuk-nuk* ","color":"gray","italic":true}]

execute if score Inventory TomeOfTongues matches 1 unless score lord_of_valor Story matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Grimu-Taki-Taki","color":"#C29D62"},{"text":"> ","color":"white"},{"text":"*nuk-tuk* ","color":"gray","italic":true},{"text":"Thank you for rescuing our","color":"white"},{"text":" Lord","color":"green"},{"text":"! You are a forever-friend to the Pygmies for all your days.","color":"white","italic":false},{"text":" *tuk-nuk* ","color":"gray","italic":true}]

execute if score Inventory TomeOfTongues matches 1 if score lord_of_valor Story matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Grimu-Taki-Taki","color":"#C29D62"},{"text":"> ","color":"white"},{"text":"*nuk-tuk* ","color":"gray","italic":true},{"text":"You want me to be the seventh Lord? Hah! No, I have tons of crazy medical conditions that would disqualify me from service. Tons of horrible diseases.","color":"white","italic":false},{"text":" *tuk-nuk* ","color":"gray","italic":true}]

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run function npc:pygmy/pose/repose

execute if score zalvorn Story matches 0 run scoreboard players set zalvorn Story 1

execute positioned 10468 58.2 158 run kill @n[tag=quest_marker,distance=..3]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
