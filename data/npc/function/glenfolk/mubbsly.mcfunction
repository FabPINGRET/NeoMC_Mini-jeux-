execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 0.8
execute if block 90 45 46 air at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Mubbsly","color":"aqua"},{"text":"> When we started digging the foundation for this castle, we were surprised to find these existing ruins beneath it! It's the Undercroft of a long-forgotten citadel, and we think it might continue even deeper. My wife has been especially interested in some ","color":"white"},{"text":"mysterious vaults","color":"light_purple"},{"text":" we've unearthed. Who knows how ancient these chambers are...","color":"white"}]

execute if score beat_sealed_citadel bool matches 0 unless block 90 45 46 air at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Mubbsly","color":"aqua"},{"text":"> When we started digging the foundation for this castle, we were surprised to find these existing ruins beneath it! It's the Undercroft of a long-forgotten citadel, and it looks like it continues even deeper...","color":"white"}]

execute if score beat_sealed_citadel bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Mubbsly","color":"aqua"},{"text":"> There was an ancient deity in the last vault you say? I believe it. This world is full to bursting with that sort of crazy thing. Well, I suppose now that our excavation here is complete, I can get back to my old day job digging graves. And smiling at my beautiful Quarsheesha!","color":"white"}]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
