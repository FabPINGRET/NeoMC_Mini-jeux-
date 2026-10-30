execute positioned 10061 188 1271 run playsound minecraft:entity.goat.milk neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute positioned 10061 188 1271 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Zimbly So","color":"dark_purple"},{"text":"> The Monks of Shh are an ancient tradition of the Pebbos. We know the Big Ones could crush us if they knew about us, so having the Monks misdirects people to not look closer at the Isle of Silence.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
