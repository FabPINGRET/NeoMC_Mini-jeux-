# @s : 📡 localisateur vers l'objectif de la campagne (sauf mission en cours)
execute if score @s mg.tvm matches 1.. run return 0
execute if score @s mg.trch matches 0 run return run function mg:terra/loc {x:14,y:65,z:-15}
execute if score @s mg.trch matches 15 run return run function mg:terra/loc {x:14,y:65,z:-15}
execute if score @s mg.trch matches 20 run return run function mg:terra/loc {x:15,y:65,z:-7}
execute if score @s mg.trch matches 28 run return run function mg:terra/loc {x:15,y:65,z:-7}
execute if score @s mg.trch matches 30 run return run function mg:terra/loc {x:-62,y:64,z:-168}
execute if score @s mg.trch matches 32 run return run function mg:terra/loc {x:-62,y:64,z:-168}
execute if score @s mg.trch matches 35 run return run function mg:terra/loc {x:15,y:65,z:-7}
execute if score @s mg.trch matches 40 run return run function mg:terra/loc {x:10,y:65,z:-196}
execute if score @s mg.trch matches 45 run return run function mg:terra/loc {x:14,y:65,z:-15}
execute if score @s mg.trch matches 50 run return run function mg:terra/loc {x:128,y:71,z:6}
execute if score @s mg.trch matches 52 run return run function mg:terra/loc {x:128,y:71,z:6}
execute if score @s mg.trch matches 55 run return run function mg:terra/loc {x:190,y:70,z:0}
execute if score @s mg.trch matches 58 run return run function mg:terra/loc {x:128,y:71,z:6}
execute if score @s mg.trch matches 60 run return run function mg:terra/loc {x:-200,y:65,z:4}
execute if score @s mg.trch matches 62 run return run function mg:terra/loc {x:-200,y:65,z:4}
execute if score @s mg.trch matches 64 run return run function mg:terra/loc {x:-190,y:65,z:14}
execute if score @s mg.trch matches 66 run return run function mg:terra/loc {x:14,y:65,z:-15}
execute if score @s mg.trch matches 70 run return run function mg:terra/loc {x:15,y:65,z:-7}
execute if score @s mg.trch matches 72 run return run function mg:terra/loc {x:58,y:86,z:176}
execute if score @s mg.trch matches 75 run return run function mg:terra/loc {x:0,y:99,z:186}
execute if score @s mg.trch matches 80 run return run function mg:terra/loc {x:0,y:99,z:186}
execute if score @s mg.trch matches 85 run return run function mg:terra/loc {x:0,y:99,z:177}
execute if score @s mg.trch matches 90 run return run function mg:terra/loc {x:14,y:65,z:-15}
function mg:terra/loc {x:0,y:65,z:0}
scoreboard players set @s mg.tron 0
