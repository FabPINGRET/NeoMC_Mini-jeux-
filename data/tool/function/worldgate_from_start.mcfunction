summon item_display ~ ~1.5 ~ {billboard:"vertical",Tags:["worldgate_from"],brightness:{sky:15,block:15},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.1f,0.1f,0.1f]},item:{id:"minecraft:ender_pearl",count:1,components:{"minecraft:custom_model_data":{strings:['2']}}}}
summon marker ~ ~ ~ {NoGravity:1b,Silent:1b,Invulnerable:1b,Tags:["worldgate_from_marker"]}
schedule function floaty:sched/tool/worldgate_from_grow 2t replace
