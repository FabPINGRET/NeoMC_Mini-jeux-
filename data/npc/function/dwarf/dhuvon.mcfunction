execute positioned -297 35 -120 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -297 35 -120 if score Inventory Bonestride matches 0 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Dhuvon","color":"dark_aqua"},{"text":"> My adopted son must be kept safe from the","color":"white"},{"text":" bone contagion","color":"gray"},{"text":"! I can trust you, hero.","color":"white"}]
execute positioned -297 35 -120 if score Inventory Bonestride matches 1 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Dhuvon","color":"dark_aqua"},{"text":"> My adopted son can't eat rocks, so I don't know what to feed him. He finds his own food I think. I hope I'm a good parent! I love Tinky so much.","color":"white"}]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
