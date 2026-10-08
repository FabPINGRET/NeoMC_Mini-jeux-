"""Fonctions de la Course d'elytres qui choisissent ou relient les parcours : preparation (controle du parcours $xc),
tirage au hasard, annonce, drapeaux de construction, desinstallation et petits repartiteurs (respawn, hud, place_tp,
fl_remove, gate_off) qui renvoient vers mg:elyrace/c<N>/<nom> selon $xc.
$xc (faux joueur de mg.st, distinct de l'objectif mg.xc) : 0 = au hasard parmi les parcours construits (pick, appele par
prepare), N = parcours NUM = N. mg:core/request le pose (id de lancement 81.. -> $xc = id - menus.ID_BASE, puis $game = 66) ;
pour tout autre lancement (66, Mini Party) request le remet a 0 : la course tire un parcours au hasard.
Python stdlib uniquement (compatible 3.8).
"""
import course_common as CC
import game as G

N_ROUTES = 2             # nombre de parcours prevus (NUM 1..N_ROUTES) ; un parcours pas encore ecrit est « pas construit »
RED = '{"text":"%s","color":"red"}'
XC = '{"score":{"name":"$xc","objective":"mg.st"},"color":"red"}'     # numero du parcours demande, lu dans un message


def dispatcher(specs, comment, name):
    """Repartiteur : appelle c<N>/<name> pour le parcours $xc (@s conserve)."""
    return [comment] + ['execute if score $xc mg.st matches %d run function %s' % (s.NUM, CC.fn(s, name)) for s in specs]


def lcm_upto(n):
    out = 1
    for k in range(2, n + 1):
        a, b = out, k
        while b:
            a, b = b, a % b
        out = out * k // a
    return out


def pick_lines(specs):
    flag = lambda s: 'data storage mg:elyrace ' + s.FLAG
    out = ['# Parcours au hasard parmi les parcours construits (appelé par prepare quand $xc vaut 0) ; $xc reste à 0 si aucun n\'est construit',
           'scoreboard players set #n mg.st 0']
    out += ['execute if %s run scoreboard players add #n mg.st 1' % flag(s) for s in specs]
    size = lcm_upto(len(specs))
    size = size if size > 1 else 2              # « random value » refuse un intervalle d'une seule valeur
    out += ['execute if score #n mg.st matches 0 run return 0',
            '# #r = rang tiré (0..#n-1) : le tirage couvre un multiple commun de 1..%d pour rester équitable' % len(specs),
            'execute store result score #r mg.st run random value 0..%d' % (size - 1),
            'scoreboard players operation #r mg.st %= #n mg.st']
    for s in specs:
        out.append('execute if %s if score #r mg.st matches 0 run scoreboard players set $xc mg.st %d' % (flag(s), s.NUM))
        out.append('execute if %s run scoreboard players remove #r mg.st 1' % flag(s))
    return out


def announce_lines(specs):
    head = ('tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance la ","color":"gray"},'
            '{"text":"🪽 COURSE D\'ÉLYTRES","color":"aqua","bold":true},{"text":" : %s","color":"gray"}]')
    out = ['# Annonce du lancement (appelée par mg:core/request, avant prepare : en mode « au hasard » le parcours n\'est pas encore tiré)',
           'execute if score $xc mg.st matches 0 run ' + head % 'un parcours au hasard parmi ceux qui sont construits (le premier arrivé gagne) !']
    by_num = {s.NUM: s for s in specs}
    for k in range(1, N_ROUTES + 1):
        what = ('%s (%d anneaux, le premier arrivé gagne) !' % (by_num[k].NAME, len(by_num[k].RINGS)) if k in by_num
                else 'le parcours %d, qui n\'est pas encore construit !' % k)
        out.append('execute if score $xc mg.st matches %d run %s' % (k, head % what))
    return out


def forget_lines(specs):
    return ['# Oublie les drapeaux de construction : tous les parcours seront reconstruits (appelé par build et core/setup_build)'] + [
        'data remove storage mg:elyrace ' + s.FLAG for s in specs]


CANCEL = ['# partie annulée ; $xc remis à 0 d\'abord : cleanup (fl_remove) ne doit rien libérer, la zone d\'un parcours en construction reste chargée',
          'scoreboard players set $xc mg.st 0', 'function mg:core/draw']


def not_built_lines(specs):
    """Parcours dont le drapeau est absent ($xc = son numéro, ou 0 = aucun parcours n'est construit). Jamais elyrace/build :
    il reconstruit tout depuis zéro ; c<k>/build ne reconstruit que le parcours demandé."""
    pre = 'tellraw @a[tag=mg.admin] [' + RED % '[Mini-Jeux] Course d\'élytres : '
    out = ['# Parcours pas (entièrement) construit : on n\'envoie personne dedans, partie annulée']
    for k, text in [(0, 'aucun parcours n\'est construit')] + [(s.NUM, 'le parcours %d (%s) n\'est pas (entièrement) construit' % (s.NUM, s.NAME)) for s in specs]:
        cmd = 'function mg:elyrace/c%d/build' % (k or specs[0].NUM)
        out.append('execute if score $xc mg.st matches %d run %s,%s]' % (k, pre, RED % (text + ' : construction en cours, ou lance /' + cmd)))
    return out + ['tellraw @a[tag=mg.play] [' + RED % '🪽 Le parcours n\'est pas encore construit : partie annulée.' + ']'] + CANCEL


def not_available_lines():
    return ['# Parcours dont le module n\'existe pas encore (emplacement réservé) : partie annulée',
            'tellraw @a[tag=mg.admin] [' + RED % '[Mini-Jeux] Course d\'élytres : le parcours ' + ',' + XC + ',' + RED % ' n\'est pas encore disponible.' + ']',
            'tellraw @a[tag=mg.play] [' + RED % '🪽 Ce parcours n\'est pas encore disponible : partie annulée.' + ']'] + CANCEL


def prepare_lines(specs):
    built = {s.NUM: s for s in specs}
    out = ['# Course d\'élytres : préparation (parcours $xc : 0 = au hasard parmi les parcours construits)',
           'execute if score $xc mg.st matches 0 run function mg:elyrace/pick',
           '# parcours pas construit (ou pas encore écrit) : on n\'envoie personne dedans, partie annulée',
           'execute if score $xc mg.st matches 0 run return run function mg:elyrace/not_built']
    for k in range(1, N_ROUTES + 1):
        if k in built:
            out.append('execute if score $xc mg.st matches %d unless data storage mg:elyrace %s run return run function mg:elyrace/not_built' % (k, built[k].FLAG))
        else:
            out.append('execute if score $xc mg.st matches %d run return run function mg:elyrace/not_available' % k)
    out += ['# restes d\'une partie précédente'] + ['tag @a remove ' + t for t in G.TAGS]
    out += ['execute if score $xc mg.st matches %d run function %s' % (s.NUM, CC.fn(s, 'setup')) for s in specs]
    out += ['gamemode adventure @a[tag=mg.play]', 'clear @a[tag=mg.play]',
            'scoreboard players set @a[tag=mg.play] mg.deaths 0']
    for n, _, _ in G.OBJECTIVES:
        out.append('scoreboard players set @a[tag=mg.play] mg.%s %d' % (n, G.HEARTS if n == 'xh' else 0))
    out += ['scoreboard players set $xt mg.st 0', 'scoreboard players set $xf mg.st 0',
            'scoreboard players set $xw mg.st 0', 'scoreboard players set $xe mg.st 0',
            'scoreboard players set #k10 mg.st 10', 'scoreboard players set #k20 mg.st 20',
            'scoreboard players set #k100 mg.st 100', 'scoreboard players set #krel mg.st %d' % G.DROP_REL,
            'scoreboard players set $ri mg.st 0',
            'execute as @a[tag=mg.play] run function mg:elyrace/equip',
            'execute as @a[tag=mg.play] run function mg:elyrace/place_one',
            'scoreboard objectives setdisplay sidebar mg.xa']
    return out


def uninstall_lines(specs):
    out = ['# Désinstallation de la Course d\'élytres (appelé par mg:desinstaller)',
           '# pas de build_abort ici : il appelle core/forceloads, qui réactiverait tous les chargements forcés que desinstaller vient de retirer',
           'schedule clear mg:elyrace/build', 'schedule clear mg:elyrace/build_next']
    out += ['schedule clear ' + CC.fn(s, 'build_wait') for s in specs]
    out += ['# ancien chemin (avant 2a : construction en un seul module, sans c<N>/) : un schedule d\'une version précédente peut survivre',
            'schedule clear mg:elyrace/build_wait']
    out += ['function mg:elyrace/forget',
            'clear @a minecraft:elytra[minecraft:custom_data~{mg_elyr:1b}]',
            'clear @a minecraft:firework_rocket[minecraft:custom_data~{mg_elyr:1b}]']
    out += ['tag @a remove ' + t for t in G.TAGS]
    out.append('advancement revoke @a only mg:elyrace_wall')
    out += ['scoreboard objectives remove mg.%s' % n for n, _, _ in G.OBJECTIVES]
    return out


def functions(specs):
    return {'prepare': prepare_lines(specs), 'pick': pick_lines(specs), 'announce': announce_lines(specs),
            'forget': forget_lines(specs), 'not_built': not_built_lines(specs), 'not_available': not_available_lines(),
            'uninstall': uninstall_lines(specs),
            'respawn': dispatcher(specs, '# @s = joueur à replacer au dernier point de reprise de son parcours', 'respawn'),
            'hud': dispatcher(specs, '# @s = joueur : barre d\'action de son parcours', 'hud'),
            'place_tp': dispatcher(specs, '# @s = joueur : le met à sa place de départ (mg.ri) sur son parcours', 'place_tp'),
            'fl_remove': dispatcher(specs, '# Libère le chargement forcé de la zone de départ du parcours $xc', 'fl_remove'),
            'gate_off': dispatcher(specs, '# GO : ouvre le portillon du parcours $xc', 'gate_off')}
