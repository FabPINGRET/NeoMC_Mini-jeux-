# @s : mission « Récupération de matériel » : une caisse sur un point au hasard
execute store result score $tvr mg.st run random value 0..13
execute if score $tvr mg.st matches 0 run return run function mg:terra/m1_at {x:-11,y:64,z:58}
execute if score $tvr mg.st matches 1 run return run function mg:terra/m1_at {x:-58,y:67,z:-18}
execute if score $tvr mg.st matches 2 run return run function mg:terra/m1_at {x:82,y:65,z:80}
execute if score $tvr mg.st matches 3 run return run function mg:terra/m1_at {x:-75,y:66,z:-33}
execute if score $tvr mg.st matches 4 run return run function mg:terra/m1_at {x:81,y:68,z:-8}
execute if score $tvr mg.st matches 5 run return run function mg:terra/m1_at {x:-76,y:68,z:-81}
execute if score $tvr mg.st matches 6 run return run function mg:terra/m1_at {x:-64,y:64,z:48}
execute if score $tvr mg.st matches 7 run return run function mg:terra/m1_at {x:55,y:65,z:48}
execute if score $tvr mg.st matches 8 run return run function mg:terra/m1_at {x:-77,y:65,z:30}
execute if score $tvr mg.st matches 9 run return run function mg:terra/m1_at {x:61,y:66,z:3}
execute if score $tvr mg.st matches 10 run return run function mg:terra/m1_at {x:82,y:65,z:51}
execute if score $tvr mg.st matches 11 run return run function mg:terra/m1_at {x:68,y:65,z:-50}
execute if score $tvr mg.st matches 12 run return run function mg:terra/m1_at {x:-10,y:66,z:-75}
execute if score $tvr mg.st matches 13 run return run function mg:terra/m1_at {x:-52,y:65,z:-60}
