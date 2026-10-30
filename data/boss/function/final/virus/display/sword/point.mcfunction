execute unless entity @e[tag=wv_model_sword,tag=pointwise,distance=0..] run kill @e[tag=wv_model_sword,distance=0..]
execute unless entity @e[tag=wv_model_sword,tag=pointwise,distance=0..] at @n[tag=wv_wrist,distance=0..] run function boss:final/virus/model/sword_pointwise
