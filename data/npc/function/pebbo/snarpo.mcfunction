execute positioned 10103 187 1255 run playsound minecraft:entity.goat.milk neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute positioned 10103 187 1255 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Snarpo Smudgehand","color":"dark_purple"},{"text":"> Hey, I watched you shrink! Welcome to the kingdom of the ","color":"white"},{"text":"Pebbos","color":"red"},{"text":", Big One. If you need to grow again, you can go in the ","color":"white"},{"text":"middle of the magic circle and jump","color":"green"},{"text":"!","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
