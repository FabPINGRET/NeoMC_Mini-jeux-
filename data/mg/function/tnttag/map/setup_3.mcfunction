# TNT Tag — préparation de la carte 3 « Village perché » (centre 0 ~ 27400), générée par tools/tnttag/gen_maps.py
function mg:tnttag/map/build_3
# Perchoir des éliminés (~15 blocs au-dessus du point le plus haut) et hauteur d'élimination
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 117
scoreboard players set $pz mg.st 27400
scoreboard players set $tty mg.st 80
kill @e[type=minecraft:item,x=-25,y=76,z=27375,dx=50,dy=44,dz=50]
gamemode adventure @a[tag=mg.play]
execute as @a[tag=mg.play] run spawnpoint @s 0 83 27396
# Placement sur 16 points de départ fixes au sol (tirés au hasard, deux passes si beaucoup de joueurs)
tag @a remove mg.tts
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:0.5,y:83,z:27396.5,fx:0.5,fz:27400.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-4.5,y:83,z:27404.5,fx:0.5,fz:27400.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:5.5,y:83,z:27402.5,fx:0.5,fz:27400.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-2.5,y:83,z:27406.5,fx:0.5,fz:27400.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-11.5,y:86,z:27393.5,fx:0.5,fz:27400.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:6.5,y:86,z:27409.5,fx:0.5,fz:27400.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:11.5,y:86,z:27391.5,fx:0.5,fz:27400.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-10.5,y:86,z:27400.5,fx:0.5,fz:27400.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:0.5,y:89,z:27386.5,fx:0.5,fz:27400.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:12.5,y:86,z:27414.5,fx:0.5,fz:27400.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-17.5,y:89,z:27417.5,fx:0.5,fz:27400.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:20.5,y:89,z:27407.5,fx:0.5,fz:27400.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:20.5,y:89,z:27388.5,fx:0.5,fz:27400.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-16.5,y:89,z:27412.5,fx:0.5,fz:27400.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-12.5,y:92,z:27379.5,fx:0.5,fz:27400.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:6.5,y:89,z:27422.5,fx:0.5,fz:27400.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:0.5,y:83,z:27396.5,fx:0.5,fz:27400.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-4.5,y:83,z:27404.5,fx:0.5,fz:27400.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:5.5,y:83,z:27402.5,fx:0.5,fz:27400.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-2.5,y:83,z:27406.5,fx:0.5,fz:27400.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-11.5,y:86,z:27393.5,fx:0.5,fz:27400.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:6.5,y:86,z:27409.5,fx:0.5,fz:27400.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:11.5,y:86,z:27391.5,fx:0.5,fz:27400.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-10.5,y:86,z:27400.5,fx:0.5,fz:27400.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:0.5,y:89,z:27386.5,fx:0.5,fz:27400.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:12.5,y:86,z:27414.5,fx:0.5,fz:27400.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-17.5,y:89,z:27417.5,fx:0.5,fz:27400.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:20.5,y:89,z:27407.5,fx:0.5,fz:27400.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:20.5,y:89,z:27388.5,fx:0.5,fz:27400.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-16.5,y:89,z:27412.5,fx:0.5,fz:27400.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-12.5,y:92,z:27379.5,fx:0.5,fz:27400.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:6.5,y:89,z:27422.5,fx:0.5,fz:27400.5}
tp @a[tag=mg.play,tag=!mg.tts] 0.5 83 27396.5
tag @a remove mg.tts
