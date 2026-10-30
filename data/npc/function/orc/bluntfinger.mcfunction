execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.hoglin.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @a[distance=..10,tag=mg.flw] unless items entity @s weapon.* blaze_rod run tellraw @s [{"text":"<"},{"text":"Bluntfinger","color":"green"},{"text":"> Oog! Ug ug bubgo groh grahhh bah bah gru gru. Ook! Ooook!! Brub grud guhhhhhhhhhhhhhh.","color":"white"}]
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @a[distance=..10,tag=mg.flw] unless items entity @s weapon.* blaze_rod run tellraw @s [{"text":"<"},{"text":"Aerithra","color":"#D47453"},{"text":"> What my knobby, green friend is trying to tell you is that the Orcs are friendly to our cause. They liked things a whole lot better when the ","color":"white"},{"text":"Seven Lords","color":"gold"},{"text":" were still in charge.","color":"white"}]

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @a[distance=..10,tag=mg.flw] if items entity @s weapon.* blaze_rod run tellraw @s [{"text":"<"},{"text":"Bluntfinger","color":"green"},{"text":"> The ","color":"white"},{"text":"Seven Lords","color":"gold"},{"text":" have ever been fair and just in their dealings with us Orcs. To withhold our aid in their hour of need would be naught but the basest cowardice. I come forth as a representative of my kin to that noble end.","color":"white"}]



#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
