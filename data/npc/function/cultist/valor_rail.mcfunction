execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.squid.death neutral @a[tag=mg.flw] ~ ~ ~ 1 2

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Germ Eater","color":"dark_aqua"},{"text":"> The ","color":"white"},{"text":"Virus ","color":"dark_aqua"},{"text":"is ravenous for an alien artifact called the ","color":"white"},{"text":"Bell of Life","color":"gold"},{"text":". He begins to siphon power from it as we speak! Oh, glory, he can finally taste its ringing light!","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
