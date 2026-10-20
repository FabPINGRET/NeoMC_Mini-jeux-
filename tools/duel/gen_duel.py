"""Duel sniper 1v1 : démarrage, fin et câblage dans le datapack.

    python tools/duel/gen_duel.py .        (depuis la racine du dépôt ; idempotent ; APRÈS tools/admin/gen_tp_general.py, tools/arcade/gen_gta.py,
    gen_terranova.py et tools/elyrace/gen_elyrace.py : il ajoute des lignes à tpg/lobby, gta/menu_go, terra/menu_go
    et elyrace/solo/start, qu'ils réécrivent en entier ; aussi après gen_duel_maps.py, par convention)

Les arènes sont posées par gen_duel_maps.py ; la liste et les invitations viennent de duel_invite.py ; le combat
(tick, lunette, tir, manches) de duel_play.py.
Flux : bouton « Défier en duel » (trigger mg.duel 1) -> liste cliquable (trigger 1000 + id du joueur) -> invitation
de 30 s (2 = accepter, 3 = refuser, 4 = annuler ; 5 = abandonner pendant le duel) -> duel dans une arène libre au hasard, premier à 3 manches.
Armes : le sniper (clic gauche = tir, clic droit = lunette) et un couteau (clic gauche, advancement mg:duel_melee, 1 dégât).
Aucun jeu n'est lancé : le duelliste est en « pause » (mg.spectate) tant que dure le duel (s'il y était déjà, le tag
mg.dlpz le mémorise). Occupé = un des tags de la fonction duel/busy (partie, plot, parcours, élytres, kart...).
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'arcade'))
sys.path.insert(0, HERE)
import common as C
import duel_invite
import duel_play
from duel_invite import tx, say
from duel_play import sniper_kill
from gen_duel_maps import MAPS

w, js = C.w, C.js
BUSY = ['mg.play', 'mg.out', 'mg.surv', 'mg.inplot', 'mg.visit', 'mg.xso', 'mg.ely', 'mg.elyf', 'mg.pkr', 'mg.lk',
        'mg.mpp', 'mg.gtw', 'mg.tvw', 'mg.pvpc', 'mg.dl']
OBJ = [('mg.duel', 'trigger'), ('mg.dlid', 'dummy'), ('mg.dlto', 'dummy'), ('mg.dlx', 'dummy'), ('mg.dli', 'dummy'),
       ('mg.dlhp', 'dummy'), ('mg.dlr', 'dummy'), ('mg.dlcd', 'dummy'), ('mg.dlkc', 'dummy'),
       ('mg.dlw', 'dummy ' + js({'text': '⚔ Duels gagnés', 'color': 'gold'}))]
TAGS = ['mg.dl', 'mg.dla', 'mg.dlp', 'mg.dlsc', 'mg.dlcr', 'mg.dlsh', 'mg.dlvc', 'mg.dlwn', 'mg.dlsp', 'mg.dlrq', 'mg.dlca',
        'mg.dltg', 'mg.dlt2', 'mg.dlq', 'mg.dlfl', 'mg.dlpz']
NO_REPLY = 'execute if entity @s[tag=mg.dl] run return run ' + say('@s', tx('⚔ Duel en cours : termine-le (ou abandonne-le) avant.', 'red'))


def edit_line(rel, old, new):
    """Remplace une ligne entière d'un fichier du datapack (exactement une occurrence ; idempotent)."""
    p = os.path.join(C.F, rel + '.mcfunction')
    lines = open(p, encoding='utf-8').read().split('\n')
    if new in lines and old not in lines:
        return
    idx = [i for i, l in enumerate(lines) if l == old]
    if len(idx) != 1:
        raise SystemExit(f'{rel} : ligne {old!r} trouvée {len(idx)} fois')
    lines[idx[0]] = new
    with open(p, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(lines))


def edit_sub(rel, old, new, count):
    """Remplace `old` par `new` dans le fichier, qui doit le contenir exactement `count` fois (idempotent)."""
    p = os.path.join(C.F, rel + '.mcfunction')
    t = open(p, encoding='utf-8').read()
    if old not in t and t.count(new) >= count:
        return
    if t.count(old) != count:
        raise SystemExit(f'{rel} : {old!r} trouvé {t.count(old)} fois (attendu {count})')
    with open(p, 'w', encoding='utf-8', newline='\n') as f:
        f.write(t.replace(old, new))


def guard(rel, needle, new_lines, where='after'):
    """Insère des lignes à côté de l'unique ligne du fichier qui contient `needle`."""
    p = os.path.join(C.F, rel + '.mcfunction')
    hits = [l for l in open(p, encoding='utf-8').read().split('\n') if needle in l and l not in new_lines]
    if len(hits) != 1:
        raise SystemExit(f'{rel} : motif {needle!r} trouvé {len(hits)} fois')
    C.patch(rel, hits[0], new_lines, where)


def basics():
    w('duel/load', ['# Duel sniper : objectifs (à appeler depuis core/load)'] + [f'scoreboard objectives add {n} {c}' for n, c in OBJ])
    w('duel/remove', ['# Duel sniper : désinstallation (à appeler depuis mg:desinstaller)',
                      'execute as @a[tag=mg.dl] run function mg:duel/stop',
                      'kill @e[type=minecraft:marker,tag=mg.dlend]',
                      'function mg:duel/build_clear',
                      'data remove storage mg:duel built',
                      'data remove storage mg:duel m']
      + [f'tag @a remove {t}' for t in TAGS if t != 'mg.dl']
      + [f'scoreboard objectives remove {n}' for n, c in OBJ]
      + ['# objectif d\'une version de développement antérieure (absent d\'un monde neuf : sans effet)',
         'scoreboard objectives remove mg.dlsp0'])
    w('duel/cmd', [
        '# Trigger mg.duel (@s = joueur) : 1 = liste des adversaires, 2 = accepter, 3 = refuser, 4 = annuler son invitation (sans effet pendant un duel),',
        '# 5 = abandonner le duel (sans effet hors duel),',
        '# 1000 + id = défier le joueur d\'id mg.dlid (liste cliquable). Remis à zéro d\'abord (core/tick le réactive)',
        'scoreboard players operation #dlv mg.st = @s mg.duel',
        'scoreboard players reset @s mg.duel',
        'execute if score #dlv mg.st matches 1 run function mg:duel/list',
        'execute if score #dlv mg.st matches 2 run function mg:duel/accept',
        'execute if score #dlv mg.st matches 3 run function mg:duel/refuse',
        'execute if score #dlv mg.st matches 4 run function mg:duel/cancel',
        'execute if score #dlv mg.st matches 5 if entity @s[tag=mg.dl] run function mg:duel/forfeit',
        'execute if score #dlv mg.st matches 1000.. run function mg:duel/challenge',
    ])
    w('duel/busy', ['# @s occupé ? -> $dlb = 1 (partie, plot, parcours, élytres, kart, duel...) ; l\'invitation en cours (mg.dlrq) est testée à part',
                    'scoreboard players set $dlb mg.st 0',
                    'execute unless entity @s[tag=mg.init] run scoreboard players set $dlb mg.st 1',
                    'execute if entity @s[gamemode=spectator] run scoreboard players set $dlb mg.st 1']
      + [f'execute if entity @s[tag={t}] run scoreboard players set $dlb mg.st 1' for t in BUSY])
    w('duel/new_id', ['# Numéro de joueur pour les liens de la liste (1, 2, 3...)',
                      'scoreboard players add $dlseq mg.st 1',
                      'scoreboard players operation @s mg.dlid = $dlseq mg.st'])
    w('duel/reconnect', ['# Joueur reconnecté (core/reconnect, @s = joueur) : duel périmé et invitations effacés',
                         'execute if entity @s[tag=mg.dl] run function mg:duel/stop',
                         'tag @s remove mg.dlrq',
                         'scoreboard players reset @s mg.dlto',
                         'scoreboard players reset @s mg.dlx'])


def start():
    w('duel/accept', [
        '# Accepter (@s = invité)',
        'execute unless score @s mg.dlto matches 1.. run return run ' + say('@s', tx('Tu n\'as aucune invitation de duel en attente.')),
        'scoreboard players operation $dlt mg.st = @s mg.dlto',
        'execute as @a[tag=mg.dlrq] if score @s mg.dlid = $dlt mg.st run tag @s add mg.dlca',
        'function mg:duel/accept_chk',
        'tag @a remove mg.dlca',
    ])
    w('duel/accept_chk', [
        '# Dernières vérifications puis départ (@s = invité ; le défieur porte mg.dlca)',
        'execute unless entity @a[tag=mg.dlca] run return run function mg:duel/fail_gone',
        'function mg:duel/busy',
        'execute if score $dlb mg.st matches 1 run return run function mg:duel/fail_busy',
        'execute if entity @s[tag=mg.dlrq] run return run function mg:duel/fail_busy',
        'execute as @a[tag=mg.dlca] run function mg:duel/busy',
        'execute if score $dlb mg.st matches 1 run return run function mg:duel/fail_gone',
        'function mg:duel/pick',
        'execute if score $dli mg.st matches 0 run return run function mg:duel/fail_map',
        'function mg:duel/start',
    ])
    w('duel/fail_gone', [say('@s', tx('⚔ Le défieur n\'est plus disponible : invitation annulée.')), 'function mg:duel/inv_end'])
    w('duel/fail_busy', [say('@s', tx('⚔ Tu es occupé (partie ou activité en cours) : tu ne peux pas accepter maintenant.')),
                         say('@a[tag=mg.dlca]', tx('⚔ Ton adversaire est occupé : invitation annulée.')), 'function mg:duel/inv_end'])
    w('duel/fail_map', [say('@s', tx('⚔ Aucune arène libre pour le moment : invitation annulée.')),
                        say('@a[tag=mg.dlca]', tx('⚔ Aucune arène libre pour le moment : invitation annulée.')), 'function mg:duel/inv_end'])
    w('duel/inv_end', ['# Ferme l\'invitation (@s = invité ; le défieur porte mg.dlca)',
                       'tag @a[tag=mg.dlca] remove mg.dlrq', 'scoreboard players reset @s mg.dlto', 'scoreboard players reset @s mg.dlx'])
    pick = ['# Arène libre au hasard -> $dli (1 Canyon, 2 Ville, 3 Glacier ; 0 = aucune ou pas encore construites ; sans duel en cours ni TDM ($tma))',
            'scoreboard players set $dli mg.st 0',
            'execute unless data storage mg:duel {built:1b} run return 0',
            'execute store result score #dlm mg.st run random value 1..3']
    for m in (1, 2, 3):
        for k in range(3):
            a = (m - 1 + k) % 3 + 1
            pick.append(f'execute if score #dlm mg.st matches {m} if score $dli mg.st matches 0 unless entity @a[tag=mg.dl,scores={{mg.dli={a}}}] '
                        f'unless score $tma mg.st matches {a} run scoreboard players set $dli mg.st {a}')
    w('duel/pick', pick)
    start_l = ['# Départ du duel (@s = invité = départ sud ; le défieur porte mg.dlca = départ nord ; $dli = arène)',
               'tag @a[tag=mg.dlca] add mg.dla',
               '# l\'invitation est fermée AVANT setup (elle remet mg.dlx à zéro, que spawn utilise pour la protection)',
               'function mg:duel/inv_end',
               'execute as @a[tag=mg.dlca] run function mg:duel/setup',
               'function mg:duel/setup']
    for i, m in enumerate(MAPS, 1):
        start_l.append(f'execute if score $dli mg.st matches {i} run ' + say(
            f'@a[tag=mg.dl,scores={{mg.dli={i}}}]', tx('⚔ Duel sniper : ', 'gold'),
            {'selector': f'@a[tag=mg.dla,scores={{mg.dli={i}}}]', 'color': 'white'}, tx(' contre '),
            {'selector': f'@a[tag=mg.dl,tag=!mg.dla,scores={{mg.dli={i}}}]', 'color': 'white'},
            tx(f' - {m["name"]} - premier à 3 manches. Tête = élimination, corps = 2 touches. Clic gauche : tir · clic droit : lunette. Abandon : trigger mg.duel 5.')))
    w('duel/start', start_l)
    w('duel/setup', [
        '# Prépare un duelliste (@s ; $dli = arène) : pause mémorisée (mg.dlpz), inventaire, kit, départ',
        'tag @s remove mg.dlpz',
        'execute if entity @s[tag=mg.spectate] run tag @s add mg.dlpz',
        'tag @s add mg.dl',
        'tag @s add mg.spectate',
        'scoreboard players operation @s mg.dli = $dli mg.st',
        'scoreboard players set @s mg.dlr 0',
        'scoreboard players reset @s mg.dlto',
        'tag @s remove mg.dlrq',
        '# son vote éventuel ne compte plus (comme elyrace/solo/start)',
        'scoreboard players reset @s mg.vc',
        'execute if score $state mg.st matches 0 run function mg:vote/refresh',
        'gamemode adventure @s',
        'effect clear @s',
        'effect give @s minecraft:saturation infinite 0 true',
        '# pas de mort hors tir : résistance maximale (coups de poing), pas de dégâts de chute (portique du Canyon)',
        'effect give @s minecraft:resistance infinite 4 true',
        'attribute @s minecraft:fall_damage_multiplier base set 0',
        'function mg:core/heal',
        'clear @s',
        'function mg:duel/kit',
        'function mg:duel/spawn',
    ])
    rest = (',unbreakable={},custom_name=' + js(tx('🎯 Sniper de duel', 'aqua', bold=True, italic=False)) + ',lore=['
            + js(tx('Clic gauche : tir (recharge 2 s)', 'gray', italic=False)) + ',' + js(tx('Clic droit : lunette — tête = élimination, corps = 2 touches', 'gray', italic=False)) + ']]')
    # icône du pack (mg:gun_sniper) si le resource pack est actif ($rp), sinon la longue-vue vanilla
    kit = [f'execute {cond} score $rp mg.st matches 1 run item replace entity @s weapon.mainhand with '
           f'minecraft:warped_fungus_on_a_stick[custom_data={{mg_dl:1b}},item_model="{model}"' + rest
           for cond, model in (('if', 'mg:gun_sniper'), ('unless', 'minecraft:spyglass'))]
    w('duel/kit', ['# Kit du duel (@s) : le sniper en main, le couteau (clic gauche) dans l\'inventaire', 'clear @s *[custom_data~{mg_dl:1b}]'] + kit
      + ['give @s ' + duel_play.knife('mg_dl')])
    sp = ['# Départ de manche (@s = duelliste) : défieur au nord, invité au sud ; 3 s de protection (mg.dlp), tir impossible',
          'scoreboard players set @s mg.dlhp 2',
          'function mg:duel/unscope',
          'execute if entity @s[tag=mg.gads] run function mg:gun/cl_unaim',
          'tag @s add mg.dlp',
          'scoreboard players set @s mg.dlx 60',
          'scoreboard players set @s mg.dlcd 0',
          'scoreboard players set @s mg.dlkc 0',
          'title @s actionbar ' + js(tx('3', 'yellow', bold=True))]
    for i, m in enumerate(MAPS, 1):
        sp.append(f'execute if entity @s[tag=mg.dla,scores={{mg.dli={i}}}] run tp @s 0.5 {m["y"]} {m["z"] - 66}.5 0 0')
        sp.append(f'execute if entity @s[tag=!mg.dla,scores={{mg.dli={i}}}] run tp @s 0.5 {m["y"]} {m["z"] + 66}.5 180 0')
    w('duel/spawn', sp)
    w('duel/next', ['# Manche suivante : les deux duellistes de l\'arène (mg.dlsp) repartent',
                    'execute as @a[tag=mg.dlsp] run function mg:duel/spawn', 'tag @a remove mg.dlsp'])
    w('duel/stop', [
        '# Fin de duel pour @s (fin normale, forfait, reconnexion, désinstallation) : état effacé, retour au lobby',
        'tag @s remove mg.dl', 'tag @s remove mg.dla', 'tag @s remove mg.dlp', 'tag @s remove mg.dlsc', 'tag @s remove mg.dlcr', 'tag @s remove mg.dlsp',
        '# lunette levée (la boîte de clic disparaît avec mg.dl : gun/cl_tick)',
        'execute if entity @s[tag=mg.gads] run function mg:gun/cl_unaim',
        'execute unless entity @s[tag=mg.dlpz] run tag @s remove mg.spectate',
        'tag @s remove mg.dlpz',
        'scoreboard players reset @s mg.dli', 'scoreboard players reset @s mg.dlhp',
        'scoreboard players reset @s mg.dlr', 'scoreboard players reset @s mg.dlcd', 'scoreboard players reset @s mg.dlx',
        'scoreboard players reset @s mg.dlkc',
        'title @s reset',
        sniper_kill([m['z'] for m in MAPS]),
        'clear @s *[custom_data~{mg_dl:1b}]',
        '# effets du duel (setup) retirés sauf si une partie a pris le joueur (ses effets sont les siens ; ailleurs, enter / reset_player les effacent)',
        'execute unless entity @s[tag=mg.play] unless entity @s[tag=mg.out] run effect clear @s minecraft:resistance',
        'execute unless entity @s[tag=mg.play] unless entity @s[tag=mg.out] run effect clear @s minecraft:saturation',
        '# retour au lobby, sauf si une activité l\'a pris entre-temps (reset_player y arracherait la survie, le plot... : garde de elyrace/solo/stop)',
        'execute unless entity @s[tag=mg.play] unless entity @s[tag=mg.out] unless entity @s[tag=mg.surv] unless entity @s[tag=mg.inplot] '
        'unless entity @s[tag=mg.visit] unless entity @s[tag=mg.gtw] unless entity @s[tag=mg.tvw] run function mg:core/reset_player',
    ])


def wire():
    C.patch('core/load', 'function mg:sky/load', ['function mg:duel/load'])
    C.patch('desinstaller', 'function mg:sky/remove', ['function mg:duel/remove'])
    C.patch('core/setup_build', 'schedule function mg:sky/build 40s', ['schedule function mg:duel/build_all 60s'])
    C.patch('core/reconnect', 'scoreboard players reset @s mg.lg', ['function mg:duel/reconnect'])
    C.patch('core/tick', 'scoreboard players enable @a mg.xs', ['scoreboard players enable @a mg.duel'])
    C.patch('core/tick', 'execute if entity @a[tag=mg.xso] run function mg:elyrace/solo/tick', [
        '# Duel sniper : commandes, puis boucle (duellistes, ou invitations en attente)',
        'execute as @a[scores={mg.duel=1..}] run function mg:duel/cmd',
        'execute if entity @a[tag=mg.dl] run function mg:duel/tick',
        'execute unless entity @a[tag=mg.dl] if entity @a[scores={mg.dlto=1..}] run function mg:duel/tick',
        'execute unless entity @a[tag=mg.dl] unless entity @a[scores={mg.dlto=1..}] if entity @a[tag=mg.dlrq] run function mg:duel/tick'])
    edit_line('core/request', 'clear @a[tag=!mg.surv] minecraft:warped_fungus_on_a_stick',
              'clear @a[tag=!mg.surv,tag=!mg.dl] minecraft:warped_fungus_on_a_stick')
    old = 'execute if score $gmt mg.t matches 40.. as @a[tag=mg.admin,tag=mg.init,tag=!mg.surv,tag=!mg.play,tag=!mg.out,tag=!mg.inplot,tag=!mg.pkr,tag=!mg.lk,tag=!mg.visit,gamemode=!spectator,gamemode=!creative] run function mg:core/give_menu_safe'
    edit_line('core/tick', old, old.replace('tag=!mg.visit,', 'tag=!mg.visit,tag=!mg.dl,'))
    # le TP général les arrête proprement (sinon reset_player sans stop = forfait arbitraire de l'adversaire)
    guard('tpg/lobby', 'run function mg:core/reset_player', ['execute as @a[tag=mg.dl] run function mg:duel/stop'], 'before')
    # pas de rappel « partie lancée sans toi (pause) » ni de bascule de pause pour un duelliste
    edit_sub('core/request', '@a[tag=mg.init,tag=mg.spectate,tag=!mg.surv]', '@a[tag=mg.init,tag=mg.spectate,tag=!mg.surv,tag=!mg.dl]', 2)
    guard('core/opt_spec', 'execute store success score @s mg.t if entity @s[tag=mg.spectate]', [NO_REPLY], 'before')
    # pas d'entrée en survie, sur un plot, en GTA / Terra Nova ni en solo d'élytres pendant un duel
    guard('survie/enter', 'execute if entity @s[tag=mg.mpp] run return run', [NO_REPLY])
    guard('gta/menu_go', 'execute if entity @s[tag=mg.out] run return run', [NO_REPLY])
    guard('terra/menu_go', 'execute if entity @s[tag=mg.out] run return run', [NO_REPLY])
    guard('elyrace/solo/start', 'execute if entity @s[tag=mg.xso] run return run', [NO_REPLY])
    # plot/cmd : le trigger est remis à zéro ici (une garde par return le laisserait réarmé)
    guard('plot/cmd', 'execute if score @s mg.pl matches 1 run function mg:plot/enter', [
        'execute if entity @s[tag=mg.dl] run ' + NO_REPLY.split(' run return run ')[1],
        'execute if entity @s[tag=mg.dl] run scoreboard players reset @s mg.pl'], 'before')


def main(root):
    C.init(root)
    basics()
    duel_invite.lists(w)
    duel_invite.invitations(w)
    start()
    duel_play.build(w, js, [m['z'] for m in MAPS])
    duel_play.write_adv(C.D, 'duel_melee', 'mg:duel/melee_adv')
    wire()


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '.')
