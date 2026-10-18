# ⚽ Terrain de foot : chaque tick tant qu'un joueur est sur le terrain, au vestiaire ou dans le puits (core/tick)
execute as @a[x=-17,y=46,z=-41,dx=38,dy=17,dz=27,tag=!mg.ftin,gamemode=!spectator] run function mg:foot/enter
# socles du vestiaire : rouge et bleu = équipe (une fois), blanc = quitter, or = retour au spawn (pas les spectateurs)
execute as @a[tag=!mg.play,tag=!mg.out,tag=!mg.ftr,gamemode=!spectator,x=-2.7,y=48,z=-18.7,dx=0.4,dy=0.5,dz=0.4] run function mg:foot/pad_red
execute as @a[tag=!mg.play,tag=!mg.out,tag=!mg.ftb,gamemode=!spectator,x=2.3,y=48,z=-18.7,dx=0.4,dy=0.5,dz=0.4] run function mg:foot/pad_blue
execute as @a[tag=!mg.play,tag=!mg.out,tag=mg.ftr,gamemode=!spectator,x=-2.7,y=48,z=-15.7,dx=0.4,dy=0.5,dz=0.4] run function mg:foot/pad_white
execute as @a[tag=!mg.play,tag=!mg.out,tag=mg.ftb,gamemode=!spectator,x=-2.7,y=48,z=-15.7,dx=0.4,dy=0.5,dz=0.4] run function mg:foot/pad_white
execute as @a[tag=!mg.play,tag=!mg.out,gamemode=!spectator,x=2.3,y=48,z=-15.7,dx=0.4,dy=0.5,dz=0.4] run function mg:foot/leave
# buts : la balle, même en partie, dans un renfoncement
execute if entity @e[type=minecraft:sulfur_cube,tag=mg.ball,x=-16,y=48,z=-33,dx=1,dy=2,dz=4] run function mg:foot/goal_w
execute if entity @e[type=minecraft:sulfur_cube,tag=mg.ball,x=19,y=48,z=-33,dx=1,dy=2,dz=4] run function mg:foot/goal_e
