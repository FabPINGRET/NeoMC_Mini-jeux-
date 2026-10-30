execute positioned 10071 187 1245 run playsound minecraft:entity.goat.milk neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute positioned 10071 187 1245 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Baskgrok the Hardsoul","color":"blue"},{"text":"> I'm practicing my sling skills. The ladies love when you can hurl a rock so fast at a wall.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
