execute at @n[tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.wither_skeleton.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute at @n[tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Kethqenthi","color":"dark_aqua"},{"text":"> Do not address Kethqenthi as \"you,\" that is a mistake. Kethqenthi is a Qessk, a construct, a fabrication. A Qessk is an \"it,\" made by and for the","color":"white"},{"text":" Doctor","color":"yellow"},{"text":", and nothing more and nothing else.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
