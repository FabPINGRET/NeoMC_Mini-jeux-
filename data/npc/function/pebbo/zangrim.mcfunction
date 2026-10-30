execute positioned 10109 188 1334 run playsound minecraft:entity.goat.milk neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute positioned 10109 188 1334 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Zangrim the Trusted","color":"red"},{"text":"> The Petrified Kingdom is the center of the largest empire in all the world. Anywhere there is stone, there are Pebbos, and the King rules them all. The Wee-Keepers assist his majesty to lead the Pebbos without stretching himself too thin.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
