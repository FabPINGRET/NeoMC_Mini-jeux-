# @s : mission « Défense d'outpost » : un outpost libre (tiré au sort)
execute store result score $tvr mg.st run random value 1..3
execute if score $tvr mg.st matches 1 if score $tvo1 mg.st matches 0 run return run function mg:terra/m2_set {k:1,x:62,y:65,z:-73,n:"Alpha"}
execute if score $tvr mg.st matches 2 if score $tvo2 mg.st matches 0 run return run function mg:terra/m2_set {k:2,x:-71,y:70,z:6,n:"Bravo"}
execute if score $tvr mg.st matches 3 if score $tvo3 mg.st matches 0 run return run function mg:terra/m2_set {k:3,x:30,y:66,z:72,n:"Charlie"}
execute if score $tvo1 mg.st matches 0 run return run function mg:terra/m2_set {k:1,x:62,y:65,z:-73,n:"Alpha"}
execute if score $tvo2 mg.st matches 0 run return run function mg:terra/m2_set {k:2,x:-71,y:70,z:6,n:"Bravo"}
execute if score $tvo3 mg.st matches 0 run return run function mg:terra/m2_set {k:3,x:30,y:66,z:72,n:"Charlie"}
tellraw @s {"text":"🛡 Tous les outposts sont déjà attaqués : rejoins une défense en cours (barre bleue) !","color":"aqua"}
