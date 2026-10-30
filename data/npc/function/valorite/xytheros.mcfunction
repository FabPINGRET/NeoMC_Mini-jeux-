execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.armadillo.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.5

execute if score simpletoid bool matches 1 run setblock 9947 35 -70 redstone_block

execute if score simpletoid bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Xytheros","color":"#D47453"},{"text":"> I keep trying to place a winning bet in the Simpletoid Race, but","color":"white"},{"text":" no matter who I bet on, I lose","color":"gold"},{"text":". I don't know what's going on, either the Moon Queen has cursed me with bad luck, or there's some ","color":"white"},{"text":"foul play","color":"green"},{"text":" happening. If I could place a winning bet, I'd be ","color":"white"},{"text":"so, so happy","color":"red"},{"text":".","color":"white"}]

execute if score simpletoid bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Xytheros","color":"#D47453"},{"text":"> I did it, I placed a winning bet! I'm ","color":"white"},{"text":"so, so happy","color":"red"},{"text":", thanks for the recommendation! Now I can finally pay off my debts to these crooked swindlers and get a fresh start on my life as a Simpletoid Rights activist.","color":"white"}]

execute if score simpletoid bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1.75 ~ run particle minecraft:heart ~ ~ ~ 0.3 0.3 0.3 0 10 force


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
