execute positioned 125 193 -2080 run playsound minecraft:entity.goat.milk neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute positioned 125 193 -2080 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Yoruth of the Gravel Law","color":"green"},{"text":"> The primary art of a Cobblemancer is a magic of dominion: the magic of animating stone. The power of the ","color":"white"},{"text":"Bell of Life","color":"gold"},{"text":" is greater by far. It is to devote ourselves to studying this pure spirit magic that we've come to this land.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
