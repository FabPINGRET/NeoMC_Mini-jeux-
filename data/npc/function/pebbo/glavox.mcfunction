execute positioned 10091 188 1334 run playsound minecraft:entity.goat.milk neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute positioned 10091 188 1334 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Glavox the Stonesworn","color":"red"},{"text":"> The goings-on in the world of the ","color":"white"},{"text":"Big Ones","color":"red"},{"text":" don't concern us most days. When we need to converse with them, we send the ","color":"white"},{"text":"Lord of Stone","color":"gray"},{"text":" as our representative. He is able to change his stature at will and can grow to their size. The","color":"white"},{"text":" Big Ones","color":"red"},{"text":" don't even know we exist, they think the Monks of Shh are who the Lord speaks for.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
