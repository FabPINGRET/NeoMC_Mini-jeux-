# 🎃 Ragoût : rot de sorcière, instantané (@s = joueur) ; aussi le repli du coup de vent et du ragoût sans place
execute at @s run playsound minecraft:entity.player.burp neutral @a[distance=..16] ~ ~ ~ 2 0.5
execute at @s run particle minecraft:dust{color:[0.35,0.8,0.2],scale:1.2} ~ ~1.5 ~ 0.3 0.2 0.3 0.02 14 normal
execute at @s run title @a[distance=..10,tag=!mg.play] actionbar [{"selector":"@s"}," a roté comme une sorcière !"]
