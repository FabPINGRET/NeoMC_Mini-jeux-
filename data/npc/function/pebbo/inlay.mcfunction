execute positioned 10085 195 1212 run playsound minecraft:entity.goat.milk neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute positioned 10085 195 1212 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Inlay Gildertwist","color":"dark_purple"},{"text":"> You can","color":"white"},{"text":" select an armor trim material using the color wall","color":"gold"},{"text":"! When you pick a pattern, we'll use whichever material is currently selected.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
