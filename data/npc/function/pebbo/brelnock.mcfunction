execute positioned 10091 188 1330 run playsound minecraft:entity.goat.milk neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute positioned 10091 188 1330 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Brelnock the Measured","color":"red"},{"text":"> This counsil is vital to the everyday needs of all Pebbos. Without us, to whom would they pay taxes?\n\nThat was a poor joke. We know we're not perfect but we really do try to govern our wonderful kingdom with a gentle hand.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
