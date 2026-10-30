execute positioned 10061 188 1265 run playsound minecraft:entity.goat.milk neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute positioned 10061 188 1265 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Joobzle Pullthread","color":"dark_purple"},{"text":"> We're sewing giant cloaks for the Monks of Shh. Each one is gigantic; they have to be able to cover legions of Pebbos at a time.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
