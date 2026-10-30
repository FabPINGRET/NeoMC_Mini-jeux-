tag @e[distance=0..] remove icelight_nexttarget

tag @n[tag=enemy,tag=!icelight_marked,distance=..15] add icelight_nexttarget

execute if entity @e[tag=icelight_nexttarget,distance=0..] facing entity @n[tag=icelight_nexttarget,distance=0..] feet positioned ~ ~1 ~ run function utility:icelight_ray
