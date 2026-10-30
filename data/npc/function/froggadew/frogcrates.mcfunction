execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.frog.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.7

#PRE MEMORY RESTORATION
execute if score memory_contagion bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Frogcrates","color":"#44BBFF"},{"text":"> What happened to the ","color":"white"},{"text":"Lord of Water","color":"blue"},{"text":"? I think... I can't remember... oh, gods, I'm supposed to know but I can't remember...","color":"white"}]

#POST MEMORY RESTORATION, PRE DUNGEON
execute if score memory_contagion bool matches 1 if score Inventory SoaringTrident matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Frogcrates","color":"#44BBFF"},{"text":"> You, the Oracle told me I would meet a hero who looks just like you! I need your help, I've just remembered where the ","color":"white"},{"text":"Lord of Water","color":"blue"},{"text":" is. He's deep in my mind, in a manor I built to house my memories. Oh, but a foul ","color":"white"},{"text":"Contagion","color":"green"},{"text":" discovered our plan and forced a ","color":"white"},{"text":"Dreadwarden","color":"aqua"},{"text":" into my mind as well. I pray the ","color":"white"},{"text":"Lord","color":"blue"},{"text":" is safe. Would you follow him deep into my psyche?","color":"white"}]

#POST DUNGEON
execute if score Inventory SoaringTrident matches 1 unless score lord_of_valor Story matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Frogcrates","color":"#44BBFF"},{"text":"> The","color":"white"},{"text":" Lord of Water","color":"blue"},{"text":" is safe, and you've helped me confront my own suppressed memories as well. Not to mention that ","color":"white"},{"text":"mind-barnacle","color":"aqua"},{"text":" you scraped off the hull of my thoughts! You are truly a ","color":"white"},{"text":"Hero of the Dark Isles","color":"dark_purple"},{"text":".","color":"white"}]

execute if score Inventory SoaringTrident matches 1 if score lord_of_valor Story matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Frogcrates","color":"#44BBFF"},{"text":"> You would consider me as a candidate for the seventh Lord? You make me smile, hero. No, I am far too old. That job needs to be done by someone young and full of strength.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
