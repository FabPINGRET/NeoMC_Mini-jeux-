execute positioned 10101 187 1342 run playsound minecraft:entity.goat.milk neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute positioned 10101 187 1342 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Omoth of the Hollow Psalm","color":"green"},{"text":"> I, Omoth, am the sole ","color":"white"},{"text":"Cobblemancer","color":"green"},{"text":" left in the Petrified Kingdom. It is my sacred duty and honor to act as advisor to the king. Though strong magic from beyond the edges of our world calls to me like the ringing of a bell, here I will remain.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
