execute positioned -269 39 7 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -269 39 7 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Grompumpud","color":"dark_aqua"},{"text":"> I'm looking for an unlicensed quack doctor in the","color":"white"},{"text":" Magma Kingdom","color":"red"},{"text":". Rumor is that somewhere hidden low, he runs an illegal clinic and can do an experimental ","color":"white"},{"text":"leg-altering surgery","color":"light_purple"},{"text":". That would take me from a 3.5 to a 5 at least with the Dwarf ladies!","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
