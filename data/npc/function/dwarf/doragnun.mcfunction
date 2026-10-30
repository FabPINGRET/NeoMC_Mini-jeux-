execute positioned -256 34 -203 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -256 34 -203 if score Inventory Bonestride matches 0 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Doragnun","color":"dark_aqua"},{"text":"> The Dwarf Legion is supposed to protect us and the Grand Court is supposed to absolve us, but I still don't trust that my neighbors are real dwarves. What if these bone monsters are playing a long con?","color":"white"}]
execute positioned -256 34 -203 if score Inventory Bonestride matches 1 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Doragnun","color":"dark_aqua"},{"text":"> I count you as one of our own, hero. If I squint really hard, I can imagine you being squat and dense, just like how a true dwarf should be!","color":"white"}]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
