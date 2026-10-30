execute positioned -342 57 -147 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -342 57 -147 if score Inventory Bonestride matches 0 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Tromglubglin","color":"dark_aqua"},{"text":"> The ","color":"white"},{"text":"bone contagion " ,"color":"gray"},{"text":"is through here. We've tried to shut the gate, but those bone tentacles keep forcing it open. We in the Dwarf Legion keep constant watch so that no more bone monsters sneak in here.","color":"white"}]
execute positioned -342 57 -147 if score Inventory Bonestride matches 1 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Tromglubglin","color":"dark_aqua"},{"text":"> You returned with your life! Incredible.","color":"white"}]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
