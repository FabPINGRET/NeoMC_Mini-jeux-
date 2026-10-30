execute positioned 10095 187 1304 run playsound minecraft:entity.goat.milk neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute if score Inventory DominionRod matches 0 positioned 10095 187 1304 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Zanos the Vigil","color":"red"},{"text":"> Welcome to Wee-Witto Castle, Big One. The future of the Petrified Kingdom is uncertain.","color":"white"}]
execute if score Inventory DominionRod matches 1 positioned 10095 187 1304 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Zanos the Vigil","color":"red"},{"text":"> Welcome to Wee-Witto Castle, Big One. The future of the Petrified Kingdom is secure thanks to you.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
