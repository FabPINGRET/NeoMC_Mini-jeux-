# @s : marqueur — court terminé
kill @e[type=minecraft:item_display,tag=mg.tnball,tag=mg.tnk]
scoreboard players set @s mg.tnph 4
tag @e[type=minecraft:mannequin,tag=mg.tnrob,tag=mg.tnk] remove mg.tnchase
execute if entity @e[type=minecraft:marker,tag=mg.tncm,scores={mg.tnph=0..3}] run title @a[tag=mg.tnk] actionbar {"text":"🎾 Match terminé — attente des autres courts…","color":"gray"}
