# Mini-Jeux Void — chargement (idempotent)

# --- Objectifs ---
scoreboard objectives add mg.st dummy
# Modèles du resource pack activés par défaut (/function mg:rp_off pour les couper)
execute unless score $rp mg.st matches 0..1 run scoreboard players set $rp mg.st 1
scoreboard objectives add mg.t dummy
scoreboard objectives add mg.wins dummy [{"text":"✦ Victoires ✦","color":"gold"}]
scoreboard objectives add mg.stp dummy
scoreboard objectives add mg.stk playerKillCount
scoreboard objectives add mg.deaths deathCount
scoreboard objectives add mg.cs minecraft.used:minecraft.carrot_on_a_stick
scoreboard objectives add mg.us minecraft.used:minecraft.snowball
scoreboard objectives add mg.menu trigger
scoreboard objectives add mg.go trigger
scoreboard objectives add mg.cd dummy
scoreboard objectives add mg.cls trigger
scoreboard objectives add mg.cl dummy
scoreboard objectives add mg.opt trigger
scoreboard objectives add mg.buy trigger
scoreboard objectives add mg.mb dummy [{"text":"☠ MOB ARENA ☠","color":"red"}]
scoreboard objectives add mg.tw dummy
scoreboard objectives add mg.ts dummy [{"text":"▮ TURF WARS ▮","color":"gold"}]
scoreboard objectives add mg.pb dummy [{"text":"▓ PAINTBALL — % peint ▓","color":"gold"}]
scoreboard objectives add mg.pi dummy
scoreboard objectives add mg.ph dummy
scoreboard objectives add mg.pt dummy
scoreboard objectives add mg.ak dummy
scoreboard objectives add mg.ag dummy
scoreboard objectives add mg.cp dummy
scoreboard objectives add mg.lp dummy
scoreboard objectives add mg.ri dummy
scoreboard objectives add mg.rp dummy [{"text":"⛵ COURSE — progression %","color":"aqua"}]
scoreboard objectives add mg.vote trigger
scoreboard objectives add mg.bb trigger
scoreboard objectives add mg.bw trigger
scoreboard objectives add mg.bi dummy
scoreboard objectives add mg.br dummy
scoreboard objectives add mg.ba dummy
scoreboard objectives add mg.vc dummy
scoreboard objectives add mg.vb dummy [{"text":"☑ VOTES — prochain jeu","color":"green"}]
scoreboard objectives add mg.fw minecraft.used:minecraft.blaze_rod
scoreboard objectives add mg.wc minecraft.used:minecraft.wind_charge
scoreboard objectives add mg.wd dummy
scoreboard objectives add mg.ok dummy [{"text":"➶ KILLS — 10 pour gagner","color":"gold"}]
scoreboard objectives add mg.qk dummy [{"text":"⚡ QUAKECRAFT ⚡","color":"aqua"}]
scoreboard objectives add mg.ppc dummy
scoreboard objectives add mg.ppt dummy
scoreboard objectives add mg.ppb dummy
scoreboard objectives add mg.ppf dummy
scoreboard objectives add mg.ks dummy
scoreboard objectives add mg.gi dummy
scoreboard objectives add mg.qp dummy
scoreboard objectives add mg.qs minecraft.used:minecraft.warped_fungus_on_a_stick
scoreboard objectives add mg.dp dummy [{"text":"★","color":"gold"}]
scoreboard objectives add mg.ln dummy
scoreboard objectives add mg.lv dummy [{"text":"♥","color":"red"}]
function mg:core/load_lg
function mg:core/load_pk
function mg:core/load_hp
scoreboard objectives add mg.pl trigger
scoreboard objectives add mg.plot dummy
scoreboard objectives add mg.pcx dummy
scoreboard objectives add mg.pcz dummy
scoreboard objectives add mg.dice trigger
scoreboard objectives add mg.dz minecraft.used:minecraft.echo_shard
scoreboard objectives add mg.mpm dummy [{"text":"● PIÈCES (★ sous le pseudo)","color":"gold"}]
scoreboard objectives add mg.mpk dummy [{"text":"★","color":"yellow"}]
scoreboard objectives add mg.mpi dummy
scoreboard objectives add mg.mpo dummy
scoreboard objectives add mg.mpz dummy
scoreboard objectives add mg.mpv dummy
scoreboard objectives add mg.mid dummy
scoreboard objectives add mg.mit dummy
scoreboard objectives add mg.mip dummy
scoreboard objectives add mg.sv trigger
scoreboard objectives add mg.kty dummy
scoreboard objectives add mg.kcol dummy
scoreboard objectives add mg.kbl dummy
scoreboard objectives add mg.kch trigger
scoreboard objectives add mg.krl dummy
scoreboard objectives add mg.ksp dummy
scoreboard objectives add mg.kdr dummy
scoreboard objectives add mg.kdd dummy
scoreboard objectives add mg.kbo dummy
scoreboard objectives add mg.khi dummy
scoreboard objectives add mg.kst dummy
scoreboard objectives add mg.kit dummy
scoreboard objectives add mg.kcp dummy
scoreboard objectives add mg.klp dummy
scoreboard objectives add mg.kvy dummy
scoreboard objectives add mg.kfp dummy
scoreboard objectives add mg.kpg dummy
scoreboard objectives add mg.krk dummy
scoreboard objectives add mg.krc dummy
scoreboard objectives add mg.khd dummy
scoreboard objectives add mg.kspr dummy
scoreboard objectives add mg.kvm dummy
scoreboard objectives add mg.kv trigger
scoreboard objectives add mg.kic dummy
scoreboard objectives add mg.kgd dummy
scoreboard objectives add mg.kbill dummy
scoreboard objectives add mg.kboo dummy
scoreboard objectives add mg.kmg dummy
scoreboard objectives add mg.kmap dummy [{"text":"🗺 Circuit Champignon","color":"gold","bold":true}]
scoreboard objectives modify mg.kmap numberformat blank
scoreboard objectives modify mg.kmap displayname [{"text":"🗺 Circuit Champignon","color":"gold","bold":true}]
scoreboard objectives add mg.kps dummy [{"text":"🏎 KART : progression %","color":"gold"}]
scoreboard objectives add mg.svid dummy
scoreboard objectives add mg.svvx dummy

# --- Équipes ---
team add mg_red
team modify mg_red color red
team modify mg_red friendlyFire false
team modify mg_red prefix [{"text":"⬤ ","color":"red"}]
team add mg_blue
team modify mg_blue color blue
team modify mg_blue friendlyFire false
team modify mg_blue prefix [{"text":"⬤ ","color":"blue"}]
team add mg_green
team modify mg_green color green
team modify mg_green friendlyFire false
team modify mg_green prefix [{"text":"⬤ ","color":"green"}]
team add mg_yellow
team modify mg_yellow color yellow
team modify mg_yellow friendlyFire false
team modify mg_yellow prefix [{"text":"⬤ ","color":"yellow"}]
team add mg_party
team modify mg_party friendlyFire false
team modify mg_party collisionRule never

# --- Globals par défaut (seulement si absents) ---
execute unless score $state mg.st = $state mg.st run scoreboard players set $state mg.st 0
execute unless score $game mg.st = $game mg.st run scoreboard players set $game mg.st 0
execute unless score $timer mg.st = $timer mg.st run scoreboard players set $timer mg.st 0
execute unless score $sb mg.st = $sb mg.st run scoreboard players set $sb mg.st 0
execute unless score $setup mg.st = $setup mg.st run scoreboard players set $setup mg.st 0
execute unless score $tc mg.st = $tc mg.st run scoreboard players set $tc mg.st 0
execute unless score $pn mg.st = $pn mg.st run scoreboard players set $pn mg.st 0
execute unless score $mp mg.st = $mp mg.st run scoreboard players set $mp mg.st 0
execute unless score $svc mg.st = $svc mg.st run scoreboard players set $svc mg.st 0
# Règles du serveur (survie + mini-jeux) réappliquées à chaque chargement
execute if score $setup mg.st matches 1 run function mg:core/rules
execute if score $setup mg.st matches 1 unless data storage mg:kart built run schedule function mg:kart/build 5s
execute if score $setup mg.st matches 1 if data storage mg:kart built unless data storage mg:kart built2 run schedule function mg:kart/t2/build 8s
execute if score $setup mg.st matches 1 if data storage mg:kart built2 unless data storage mg:kart built3 run schedule function mg:kart/t3/build 10s
execute if score $setup mg.st matches 1 unless data storage mg:dropadv built run schedule function mg:dropadv/build 40s

# Zones chargées (après une mise à jour du pack, les nouvelles zones sont prises en compte)
execute if score $setup mg.st matches 1 run function mg:core/forceloads

# Plots joueurs : construits automatiquement après une mise à jour du pack sur un monde déjà installé
execute if score $setup mg.st matches 1 unless data storage mg:plot built run function mg:plot/build
execute if score $setup mg.st matches 1 unless data storage mg:party {built:3b} run schedule function mg:party/build 3s

tellraw @a [{"text":"[Mini-Jeux] ","color":"gold"},{"text":"Datapack chargé. ","color":"gray"},{"text":"Première fois ? Un OP lance ","color":"gray"},{"text":"/function mg:setup","color":"yellow"},{"text":" pour tout construire.","color":"gray"}]
