# Tableau du marché : prix du moment (tas de 64 pour les pierres) et tendance
scoreboard players set #pp mg.st 2
scoreboard players operation #pp mg.st *= #fn64 mg.st
scoreboard players operation #pp mg.st *= $fm0 mg.st
scoreboard players operation #pp mg.st /= #fn100 mg.st
scoreboard players operation #pd mg.st = #pp mg.st
scoreboard players operation #pp mg.st /= #fn10 mg.st
scoreboard players operation #pd mg.st %= #fn10 mg.st
execute store result storage mg:filon b.s int 1 run scoreboard players get #pp mg.st
execute store result storage mg:filon b.sd int 1 run scoreboard players get #pd mg.st
data modify storage mg:filon b.sc set value "green"
execute if score $fm0 mg.st < $fo0 mg.st run data modify storage mg:filon b.sc set value "red"
scoreboard players set #pp mg.st 40
scoreboard players operation #pp mg.st *= $fm10 mg.st
scoreboard players operation #pp mg.st /= #fn100 mg.st
scoreboard players operation #pd mg.st = #pp mg.st
scoreboard players operation #pp mg.st /= #fn10 mg.st
scoreboard players operation #pd mg.st %= #fn10 mg.st
execute store result storage mg:filon b.p10 int 1 run scoreboard players get #pp mg.st
execute store result storage mg:filon b.d10 int 1 run scoreboard players get #pd mg.st
data modify storage mg:filon b.a10 set value "▲"
data modify storage mg:filon b.c10 set value "green"
execute if score $fm10 mg.st < $fo10 mg.st run data modify storage mg:filon b.a10 set value "▼"
execute if score $fm10 mg.st < $fo10 mg.st run data modify storage mg:filon b.c10 set value "red"
execute if score $fm10 mg.st = $fo10 mg.st run data modify storage mg:filon b.a10 set value "="
execute if score $fm10 mg.st = $fo10 mg.st run data modify storage mg:filon b.c10 set value "gray"
scoreboard players set #pp mg.st 10
scoreboard players operation #pp mg.st *= $fm11 mg.st
scoreboard players operation #pp mg.st /= #fn100 mg.st
scoreboard players operation #pd mg.st = #pp mg.st
scoreboard players operation #pp mg.st /= #fn10 mg.st
scoreboard players operation #pd mg.st %= #fn10 mg.st
execute store result storage mg:filon b.p11 int 1 run scoreboard players get #pp mg.st
execute store result storage mg:filon b.d11 int 1 run scoreboard players get #pd mg.st
data modify storage mg:filon b.a11 set value "▲"
data modify storage mg:filon b.c11 set value "green"
execute if score $fm11 mg.st < $fo11 mg.st run data modify storage mg:filon b.a11 set value "▼"
execute if score $fm11 mg.st < $fo11 mg.st run data modify storage mg:filon b.c11 set value "red"
execute if score $fm11 mg.st = $fo11 mg.st run data modify storage mg:filon b.a11 set value "="
execute if score $fm11 mg.st = $fo11 mg.st run data modify storage mg:filon b.c11 set value "gray"
scoreboard players set #pp mg.st 70
scoreboard players operation #pp mg.st *= $fm12 mg.st
scoreboard players operation #pp mg.st /= #fn100 mg.st
scoreboard players operation #pd mg.st = #pp mg.st
scoreboard players operation #pp mg.st /= #fn10 mg.st
scoreboard players operation #pd mg.st %= #fn10 mg.st
execute store result storage mg:filon b.p12 int 1 run scoreboard players get #pp mg.st
execute store result storage mg:filon b.d12 int 1 run scoreboard players get #pd mg.st
data modify storage mg:filon b.a12 set value "▲"
data modify storage mg:filon b.c12 set value "green"
execute if score $fm12 mg.st < $fo12 mg.st run data modify storage mg:filon b.a12 set value "▼"
execute if score $fm12 mg.st < $fo12 mg.st run data modify storage mg:filon b.c12 set value "red"
execute if score $fm12 mg.st = $fo12 mg.st run data modify storage mg:filon b.a12 set value "="
execute if score $fm12 mg.st = $fo12 mg.st run data modify storage mg:filon b.c12 set value "gray"
scoreboard players set #pp mg.st 140
scoreboard players operation #pp mg.st *= $fm13 mg.st
scoreboard players operation #pp mg.st /= #fn100 mg.st
scoreboard players operation #pd mg.st = #pp mg.st
scoreboard players operation #pp mg.st /= #fn10 mg.st
scoreboard players operation #pd mg.st %= #fn10 mg.st
execute store result storage mg:filon b.p13 int 1 run scoreboard players get #pp mg.st
execute store result storage mg:filon b.d13 int 1 run scoreboard players get #pd mg.st
data modify storage mg:filon b.a13 set value "▲"
data modify storage mg:filon b.c13 set value "green"
execute if score $fm13 mg.st < $fo13 mg.st run data modify storage mg:filon b.a13 set value "▼"
execute if score $fm13 mg.st < $fo13 mg.st run data modify storage mg:filon b.c13 set value "red"
execute if score $fm13 mg.st = $fo13 mg.st run data modify storage mg:filon b.a13 set value "="
execute if score $fm13 mg.st = $fo13 mg.st run data modify storage mg:filon b.c13 set value "gray"
scoreboard players set #pp mg.st 20
scoreboard players operation #pp mg.st *= $fm14 mg.st
scoreboard players operation #pp mg.st /= #fn100 mg.st
scoreboard players operation #pd mg.st = #pp mg.st
scoreboard players operation #pp mg.st /= #fn10 mg.st
scoreboard players operation #pd mg.st %= #fn10 mg.st
execute store result storage mg:filon b.p14 int 1 run scoreboard players get #pp mg.st
execute store result storage mg:filon b.d14 int 1 run scoreboard players get #pd mg.st
data modify storage mg:filon b.a14 set value "▲"
data modify storage mg:filon b.c14 set value "green"
execute if score $fm14 mg.st < $fo14 mg.st run data modify storage mg:filon b.a14 set value "▼"
execute if score $fm14 mg.st < $fo14 mg.st run data modify storage mg:filon b.c14 set value "red"
execute if score $fm14 mg.st = $fo14 mg.st run data modify storage mg:filon b.a14 set value "="
execute if score $fm14 mg.st = $fo14 mg.st run data modify storage mg:filon b.c14 set value "gray"
scoreboard players set #pp mg.st 30
scoreboard players operation #pp mg.st *= $fm15 mg.st
scoreboard players operation #pp mg.st /= #fn100 mg.st
scoreboard players operation #pd mg.st = #pp mg.st
scoreboard players operation #pp mg.st /= #fn10 mg.st
scoreboard players operation #pd mg.st %= #fn10 mg.st
execute store result storage mg:filon b.p15 int 1 run scoreboard players get #pp mg.st
execute store result storage mg:filon b.d15 int 1 run scoreboard players get #pd mg.st
data modify storage mg:filon b.a15 set value "▲"
data modify storage mg:filon b.c15 set value "green"
execute if score $fm15 mg.st < $fo15 mg.st run data modify storage mg:filon b.a15 set value "▼"
execute if score $fm15 mg.st < $fo15 mg.st run data modify storage mg:filon b.c15 set value "red"
execute if score $fm15 mg.st = $fo15 mg.st run data modify storage mg:filon b.a15 set value "="
execute if score $fm15 mg.st = $fo15 mg.st run data modify storage mg:filon b.c15 set value "gray"
scoreboard players set #pp mg.st 500
scoreboard players operation #pp mg.st *= $fm16 mg.st
scoreboard players operation #pp mg.st /= #fn100 mg.st
scoreboard players operation #pd mg.st = #pp mg.st
scoreboard players operation #pp mg.st /= #fn10 mg.st
scoreboard players operation #pd mg.st %= #fn10 mg.st
execute store result storage mg:filon b.p16 int 1 run scoreboard players get #pp mg.st
execute store result storage mg:filon b.d16 int 1 run scoreboard players get #pd mg.st
data modify storage mg:filon b.a16 set value "▲"
data modify storage mg:filon b.c16 set value "green"
execute if score $fm16 mg.st < $fo16 mg.st run data modify storage mg:filon b.a16 set value "▼"
execute if score $fm16 mg.st < $fo16 mg.st run data modify storage mg:filon b.c16 set value "red"
execute if score $fm16 mg.st = $fo16 mg.st run data modify storage mg:filon b.a16 set value "="
execute if score $fm16 mg.st = $fo16 mg.st run data modify storage mg:filon b.c16 set value "gray"
scoreboard players set #pp mg.st 700
scoreboard players operation #pp mg.st *= $fm17 mg.st
scoreboard players operation #pp mg.st /= #fn100 mg.st
scoreboard players operation #pd mg.st = #pp mg.st
scoreboard players operation #pp mg.st /= #fn10 mg.st
scoreboard players operation #pd mg.st %= #fn10 mg.st
execute store result storage mg:filon b.p17 int 1 run scoreboard players get #pp mg.st
execute store result storage mg:filon b.d17 int 1 run scoreboard players get #pd mg.st
data modify storage mg:filon b.a17 set value "▲"
data modify storage mg:filon b.c17 set value "green"
execute if score $fm17 mg.st < $fo17 mg.st run data modify storage mg:filon b.a17 set value "▼"
execute if score $fm17 mg.st < $fo17 mg.st run data modify storage mg:filon b.c17 set value "red"
execute if score $fm17 mg.st = $fo17 mg.st run data modify storage mg:filon b.a17 set value "="
execute if score $fm17 mg.st = $fo17 mg.st run data modify storage mg:filon b.c17 set value "gray"
scoreboard players set #pp mg.st 50
scoreboard players operation #pp mg.st *= $fm18 mg.st
scoreboard players operation #pp mg.st /= #fn100 mg.st
scoreboard players operation #pd mg.st = #pp mg.st
scoreboard players operation #pp mg.st /= #fn10 mg.st
scoreboard players operation #pd mg.st %= #fn10 mg.st
execute store result storage mg:filon b.p18 int 1 run scoreboard players get #pp mg.st
execute store result storage mg:filon b.d18 int 1 run scoreboard players get #pd mg.st
data modify storage mg:filon b.a18 set value "▲"
data modify storage mg:filon b.c18 set value "green"
execute if score $fm18 mg.st < $fo18 mg.st run data modify storage mg:filon b.a18 set value "▼"
execute if score $fm18 mg.st < $fo18 mg.st run data modify storage mg:filon b.c18 set value "red"
execute if score $fm18 mg.st = $fo18 mg.st run data modify storage mg:filon b.a18 set value "="
execute if score $fm18 mg.st = $fo18 mg.st run data modify storage mg:filon b.c18 set value "gray"
scoreboard players set #pp mg.st 1400
scoreboard players operation #pp mg.st *= $fm20 mg.st
scoreboard players operation #pp mg.st /= #fn100 mg.st
scoreboard players operation #pd mg.st = #pp mg.st
scoreboard players operation #pp mg.st /= #fn10 mg.st
scoreboard players operation #pd mg.st %= #fn10 mg.st
execute store result storage mg:filon b.p20 int 1 run scoreboard players get #pp mg.st
execute store result storage mg:filon b.d20 int 1 run scoreboard players get #pd mg.st
data modify storage mg:filon b.a20 set value "▲"
data modify storage mg:filon b.c20 set value "green"
execute if score $fm20 mg.st < $fo20 mg.st run data modify storage mg:filon b.a20 set value "▼"
execute if score $fm20 mg.st < $fo20 mg.st run data modify storage mg:filon b.c20 set value "red"
execute if score $fm20 mg.st = $fo20 mg.st run data modify storage mg:filon b.a20 set value "="
execute if score $fm20 mg.st = $fo20 mg.st run data modify storage mg:filon b.c20 set value "gray"
scoreboard players set #pp mg.st 3000
scoreboard players operation #pp mg.st *= $fm22 mg.st
scoreboard players operation #pp mg.st /= #fn100 mg.st
scoreboard players operation #pd mg.st = #pp mg.st
scoreboard players operation #pp mg.st /= #fn10 mg.st
scoreboard players operation #pd mg.st %= #fn10 mg.st
execute store result storage mg:filon b.p22 int 1 run scoreboard players get #pp mg.st
execute store result storage mg:filon b.d22 int 1 run scoreboard players get #pd mg.st
data modify storage mg:filon b.a22 set value "▲"
data modify storage mg:filon b.c22 set value "green"
execute if score $fm22 mg.st < $fo22 mg.st run data modify storage mg:filon b.a22 set value "▼"
execute if score $fm22 mg.st < $fo22 mg.st run data modify storage mg:filon b.c22 set value "red"
execute if score $fm22 mg.st = $fo22 mg.st run data modify storage mg:filon b.a22 set value "="
execute if score $fm22 mg.st = $fo22 mg.st run data modify storage mg:filon b.c22 set value "gray"
scoreboard players set #pp mg.st 5000
scoreboard players operation #pp mg.st *= $fm23 mg.st
scoreboard players operation #pp mg.st /= #fn100 mg.st
scoreboard players operation #pd mg.st = #pp mg.st
scoreboard players operation #pp mg.st /= #fn10 mg.st
scoreboard players operation #pd mg.st %= #fn10 mg.st
execute store result storage mg:filon b.p23 int 1 run scoreboard players get #pp mg.st
execute store result storage mg:filon b.d23 int 1 run scoreboard players get #pd mg.st
data modify storage mg:filon b.a23 set value "▲"
data modify storage mg:filon b.c23 set value "green"
execute if score $fm23 mg.st < $fo23 mg.st run data modify storage mg:filon b.a23 set value "▼"
execute if score $fm23 mg.st < $fo23 mg.st run data modify storage mg:filon b.c23 set value "red"
execute if score $fm23 mg.st = $fo23 mg.st run data modify storage mg:filon b.a23 set value "="
execute if score $fm23 mg.st = $fo23 mg.st run data modify storage mg:filon b.c23 set value "gray"
function mg:filon/board_set with storage mg:filon b
