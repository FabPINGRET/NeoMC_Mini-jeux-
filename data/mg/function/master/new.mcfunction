# Nouvel ordre ($mso = ordre, $msv = 1 vrai / 0 piège, délai $msw)
scoreboard players add $msr mg.st 1
execute store result score $mso mg.st run random value 1..10
scoreboard players set $msv mg.st 1
execute store result score $r mg.st run random value 1..100
execute if score $mso mg.st matches 1..3 if score $r mg.st matches ..35 run scoreboard players set $msv mg.st 0
scoreboard players set $msw mg.st 60
scoreboard players operation $r mg.st = $msr mg.st
scoreboard players operation $r mg.st *= #2 mg.st
scoreboard players operation $msw mg.st -= $r mg.st
execute if score $msw mg.st matches ..19 run scoreboard players set $msw mg.st 20
scoreboard players operation $mst mg.st = $msw mg.st
scoreboard players set $msp mg.st 1
tag @a[tag=mg.play] remove mg.mso
tag @a[tag=mg.play] remove mg.msf
execute store result storage mg:ms t.d int 1 run scoreboard players get $msw mg.st
execute if score $mso mg.st matches 1 if score $msv mg.st matches 1 run function mg:master/say {t:"Sautez !",m:"👑 Master dit : "}
execute if score $mso mg.st matches 1 if score $msv mg.st matches 0 run function mg:master/say {t:"Sautez !",m:""}
execute if score $mso mg.st matches 2 if score $msv mg.st matches 1 run function mg:master/say {t:"Accroupissez-vous !",m:"👑 Master dit : "}
execute if score $mso mg.st matches 2 if score $msv mg.st matches 0 run function mg:master/say {t:"Accroupissez-vous !",m:""}
execute if score $mso mg.st matches 3 if score $msv mg.st matches 1 run function mg:master/say {t:"Sprintez !",m:"👑 Master dit : "}
execute if score $mso mg.st matches 3 if score $msv mg.st matches 0 run function mg:master/say {t:"Sprintez !",m:""}
execute if score $mso mg.st matches 4 if score $msv mg.st matches 1 run function mg:master/say {t:"Regardez le ciel !",m:"👑 Master dit : "}
execute if score $mso mg.st matches 5 if score $msv mg.st matches 1 run function mg:master/say {t:"Regardez le sol !",m:"👑 Master dit : "}
execute if score $mso mg.st matches 6 if score $msv mg.st matches 1 run function mg:master/say {t:"Ne bougez plus !",m:"👑 Master dit : "}
execute if score $mso mg.st matches 7 if score $msv mg.st matches 1 run function mg:master/say {t:"Sur le ROUGE !",m:"👑 Master dit : "}
execute if score $mso mg.st matches 8 if score $msv mg.st matches 1 run function mg:master/say {t:"Sur le BLEU !",m:"👑 Master dit : "}
execute if score $mso mg.st matches 9 if score $msv mg.st matches 1 run function mg:master/say {t:"Sur le VERT !",m:"👑 Master dit : "}
execute if score $mso mg.st matches 10 if score $msv mg.st matches 1 run function mg:master/say {t:"Sur le JAUNE !",m:"👑 Master dit : "}
