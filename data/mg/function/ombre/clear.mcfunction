# Retire ce que la session a posé (pas les entités permanentes)
execute in mg:ombrelune run kill @e[tag=mg.ol,tag=!mg.ols]
function mg:ombre/boss/clear
team remove mg_ol
team remove mg_olel
execute in mg:ombrelune run kill @e[type=minecraft:item,x=-240,y=0,z=-240,dx=480,dy=300,dz=480]
execute in mg:ombrelune run kill @e[type=minecraft:experience_orb,x=-240,y=0,z=-240,dx=480,dy=300,dz=480]
execute in mg:ombrelune run kill @e[type=minecraft:vex,x=-240,y=0,z=-240,dx=480,dy=300,dz=480]
execute in mg:ombrelune run kill @e[type=minecraft:area_effect_cloud,x=-240,y=0,z=-240,dx=480,dy=300,dz=480]
