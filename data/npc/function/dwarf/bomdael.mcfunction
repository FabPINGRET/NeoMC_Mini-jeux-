execute positioned -306 64 -159 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.8
execute positioned -306 64 -159 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Bomdael","color":"dark_aqua"},{"text":"> President Snuguki is my dad! He told me secretly that when I grow up, he's going to pass the presidency to me! He called it um, I think a \"dymasty.\" Isn't that a cool idea?","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
