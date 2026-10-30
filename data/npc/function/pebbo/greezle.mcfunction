execute positioned 10135 187 1209 run playsound minecraft:entity.goat.milk neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute positioned 10135 187 1209 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Greezle Tiptap","color":"dark_purple"},{"text":"> I'm a Pebbo, alright? Of course I love making art out of stone! Hey, don't touch it though.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
