execute positioned 10100 188 1346 run playsound minecraft:entity.goat.milk neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute positioned 10100 188 1346 if score Inventory DominionRod matches 0 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Wee-Witto King","color":"red"},{"text":"> It isn't every day that a","color":"white"},{"text":" Big One","color":"red"},{"text":" enters my courts. We are in a crisis, so unless you are here to offer aid, I do not have time for you. The","color":"white"},{"text":" Shrunken Temple","color":"green"},{"text":", our holiest site, was stolen with the ","color":"white"},{"text":"Lord of Stone ","color":"gray"},{"text":"imprisoned inside. The ","color":"white"},{"text":"Cobblemancers","color":"green"},{"text":" would be able to locate it, but their entire order went to another dimension, called the ","color":"white"},{"text":"Floaty Isles","color":"gold"},{"text":", long ago through a tiny crack in space.","color":"white"}]

execute positioned 10100 188 1346 if score Inventory DominionRod matches 1 unless score lord_of_valor Story matches 1 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Wee-Witto King","color":"red"},{"text":"> It isn't every day that a","color":"white"},{"text":" Big One","color":"red"},{"text":" enters my courts. Thank you for offering your aid. The","color":"white"},{"text":" Shrunken Temple","color":"green"},{"text":" is restored to us and the ","color":"white"},{"text":"Lord of Stone ","color":"gray"},{"text":"walks free once more. You are legally a beast, give me five. Not gonna down-low-too-slow you. You earned it.","color":"white"}]

execute positioned 10100 188 1346 if score Inventory DominionRod matches 1 if score lord_of_valor Story matches 1 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Wee-Witto King","color":"red"},{"text":"> Me? The seventh Lord? Surely, you jest! My station as king of the Pebbos is as high as any living thing could hope to reach. To become a Lord would be to lower myself.","color":"white"}]

kill @n[tag=quest_marker,distance=..3]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
