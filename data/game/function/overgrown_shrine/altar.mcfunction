execute if score love_19 bool matches 0 run tag @p[tag=mg.flw] add overgrown_shrine_complete
tellraw @p[tag=mg.flw] [{"text":"A name congeals in your mind...","color":"gray","italic":true},{"text":" Intercession","color":"dark_aqua","italic":true},{"text":"...","color":"gray","italic":true}]
playsound minecraft:ambient.warped_forest.mood master @p[tag=mg.flw] ~ ~1 ~ 1 2
