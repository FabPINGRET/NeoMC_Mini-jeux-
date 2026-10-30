execute if score golem_lycan bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.ravager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.5
execute if score golem_lycan bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.breeze.deflect neutral @a[tag=mg.flw] ~ ~ ~ 1 1

execute if score golem_lycan bool matches 0 if score moonlight_contagion bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Abbot Ognar","color":"red"},{"text":"> May the Sun watch over you, hero! We ","color":"white"},{"text":"Fire Golems","color":"red"},{"text":" have been praying more fervently than ever for the Sun, our great fertility goddess, to grant our deepest and only wish. We want to become living beings! Not just animate, but breathing, biological creatures. My monks have been taking rotating shifts worshipping at the ","color":"white"},{"text":"Great Altar of Sunfire ","color":"red"},{"text":"constantly for years now.","color":"white"}]
execute if score golem_lycan bool matches 0 if score moonlight_contagion bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Abbot Ognar","color":"red"},{"text":"> We were deceived... all these years worshipping the Sun, wasted... I feel so ashamed. I will find a grand way to humble myself before the Moon.","color":"white"}]


execute if score golem_lycan bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Abbot Ognarax","color":"red"},{"text":"> Does the Moon forgive me for all these years I spent worshipping the Sun? It must, for its blessing touches even me. I will spend every day looking forward to these beautiful nights when I can feel my lungs fill with air and blood flow through my veins.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
