execute positioned 9780 57 24 run playsound minecraft:item.armor.equip_iron neutral @a[tag=mg.flw] ~ ~ ~ 1 2
execute positioned 9780 57 24 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Garden Gnome","color":"red"},{"text":"> ","color":"white"},{"text":"...\nHere, people appreciate me for my intellect rather than just my cute little funny body.","color":"gray","italic":true}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
