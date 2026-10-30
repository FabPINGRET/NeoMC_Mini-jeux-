execute positioned 134 193 -2071 run playsound minecraft:entity.goat.milk neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute positioned 134 193 -2071 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Elen of the Folded Echo","color":"green"},{"text":"> There are 6 of these statues total in the Dark Isles. One by a","color":"white"},{"text":" Valorforge ","color":"red"},{"text":"fountain, one near the ","color":"white"},{"text":"Pygmy ","color":"dark_green"},{"text":"village, one in the ","color":"white"},{"text":"Brain Mesa","color":"gold"},{"text":", one by the","color":"white"},{"text":" Moldsap","color":"light_purple"},{"text":" sugar house, and two in the ","color":"white"},{"text":"Dark Wilds","color":"dark_purple"},{"text":". It might help to write that down somewhere.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
