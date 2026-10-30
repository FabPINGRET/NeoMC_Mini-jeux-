execute positioned -11544 199 -181 run playsound minecraft:entity.strider.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 2
execute positioned -11544 199 -181 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Dark Eebo","color":"blue"},{"text":"> Ayo, sorry about that stuff downstairs, I had just done a line of fish food in a painting of a club bathroom and was absolutely not in my right mind if you know what I'm sayin. We're cool, right? Yeah, put it here friendo.","color":"white"},{"text":" *daps you up*","color":"gray","italic":true}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
