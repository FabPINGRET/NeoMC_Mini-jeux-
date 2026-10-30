"""Rapport texte des commandes du terrain « Scourge of the Floaty Isles » (fonctions pures : le texte est déterministe, sans horodatage).

    text = fl_terrain_report.report_text(ctx, finds, stats, pending, after=None)     # finds / stats / pending : fl_terrain_rw.Pass
    fl_terrain_report.chunk_totals(stats, pending)                       # (chunks non lus, chunks à vérifier)
    fl_terrain_report.totals_line(unread, to_check)                      # « 1 chunk non lu, 2 a verifier » (pluriel juste à 0, 1 et n)

Deux familles de chunks, jamais mélangées : les NON LUS (fl_terrain.UNREAD : lz4, externe, inconnu, corrompu, illisible : aucune commande
n'en est sortie) et ceux À VÉRIFIER (fl_terrain.A_VERIFIER : lus, mais sans_bloc / rc_hors_panneau demandent un coup d'oeil, avec leur
position fichier + chunk (cx, cz) ; panneau_illisible : un panneau dont un run_command n'a pas pu être extrait). Seules les clés non
nulles sont affichées.
`after` (liste de fl_terrain_rw.Change, une par commande de `finds`) : le build a réécrit le terrain. Le rapport montre alors les risques
avant ET après, les réécritures par action, la liste « Non reecrits » (raison, x y z, type, commande : commandes laissées, ou réécrites
mais avec un sélecteur non borné qui reste, ou `advancement ... everything` remplacé par un NOOP, raison `eclate`) et la liste complète
APRÈS (« <= avant : ... » quand la commande a changé). Si le build a vu des chunks à commandes que le lecteur NBT strict ne lit pas
(ctx['unread_cmd'], raison `illisible_cmd`) : une section les liste (fichier, cx, cz) : leurs commandes ne sont PAS réécrites. Sans
`after` (--no-rewrite) : la liste des commandes d'origine et leurs risques.
"""
import functools
from collections import Counter

import fl_terrain

EXAMPLES, VERBS = 10, 15
_WHY = {'sans_bloc': 'command_block present mais aucun bloc de commande ni minecart trouve, ou command_block hors de tout bloc de commande '
                     '(objet de coffre, SpawnData de spawner, falling_block...)',
        'rc_hors_panneau': 'run_command hors de tout bloc de commande, minecart ou panneau (livre, coffre...)',
        'panneau_illisible': 'panneau avec plus de run_command que de commandes extraites (JSON invalide ou type inattendu) : commandes non listees'}
_FX = (('tag', '+tag=mg.flw (selecteurs joueurs)'), ('distance', '+distance=0.. (selecteurs entites)'), ('say', 'say -> tellraw'),
       ('fall', 'gamerule fall_damage -> attribut'),
       ('dim', 'dimension source -> mg:floaty'), ('revoke', 'advancement revoke'), ('imbrique', 'commandes imbriquees (Command:) reecrites'),
       ('retire', 'time / gamerule globaux retires dans une commande imbriquee'), ('last_output', 'LastOutput retires'),
       ('auteur', 'lignes de l\'auteur retirees dans une commande imbriquee'), ('setdisplay', 'setdisplay retires dans une commande imbriquee'))
_NOOPS = ('retiree', 'auteur', 'setdisplay', 'risque_dur', 'eclate')
_LEFT = ('eclate', 'non_analysable', 'trop_long', 'chaine', 'mutf8', 'taille', 'verif', 'en_tete', 'selecteur_residuel')


@functools.lru_cache(maxsize=None)
def _risks(command):
    return tuple(fl_terrain.classify(command))


@functools.lru_cache(maxsize=None)
def _sel_str(command):
    return fl_terrain.string_selectors(command)


def risky_commands(finds):
    """-> [(commande, risques, [Found])] : commandes DISTINCTES à risque, les plus graves d'abord."""
    by = {}
    for f in finds:
        by.setdefault(f.command, []).append(f)
    rows = [(c, list(_risks(c)), fs) for c, fs in by.items()]
    rows = [r for r in rows if r[1]]
    rows.sort(key=lambda r: (fl_terrain.RISK_NAMES.index(r[1][0]), -len(r[1]), -len(r[2]), r[0]))
    return rows


def verb(command):
    """Commande finale d'une chaîne « execute ... run X » (sinon la commande elle-même) -> son premier mot ('(vide)' si rien)."""
    words = command.strip().lstrip('/').rsplit(' run ', 1)[-1].split()
    return words[0] if words else '(vide)'


def _line(f, risks=(), command=None):
    x, y, z = f.pos
    return f'{x} {y} {z}\t{f.kind}\t{"auto" if f.auto else "-"}\t{",".join(risks) or "-"}\t{" ".join((f.command if command is None else command).split())}'     # une ligne, sans tabulation


def chunk_totals(stats, pending):
    """-> (chunks non lus, chunks à vérifier) : un chunk à vérifier pour plusieurs raisons ne compte qu'une fois."""
    return sum(stats[k] for k in fl_terrain.UNREAD), len({c for k in fl_terrain.A_VERIFIER for c in pending.get(k, ())})


def totals_line(unread, to_check):
    def s(n):
        return 's' if n > 1 else ''
    return f'{unread} chunk{s(unread)} non lu{s(unread)}, {to_check} a verifier'


def _counts(stats, keys):
    return ', '.join(f'{k} {stats[k]}' for k in keys if stats[k])


def _chunk_sections(stats, pending):
    out = []
    if any(stats[k] for k in fl_terrain.UNREAD):
        out += ['', f'## Chunks non lus ({_counts(stats, fl_terrain.UNREAD)}) : NON analyses, leurs commandes ne sont PAS dans ce rapport']
    if any(stats[k] for k in fl_terrain.A_VERIFIER):
        out += ['', f'## Chunks a verifier ({_counts(stats, fl_terrain.A_VERIFIER)}) : lus, mais a regarder a la main (fichier, chunk cx cz)']
        for k in fl_terrain.A_VERIFIER:
            if pending.get(k):
                out += [f'- {k} : {_WHY[k]}'] + [f'  {f} chunk ({cx}, {cz})' for f, cx, cz in sorted(pending[k])]
    return out


def _unread_cmd_lines(items):
    """[(fichier, cx, cz)] des chunks à commandes illisibles (raison illisible_cmd) -> section du rapport (vide s'il n'y en a pas)."""
    if not items:
        return []
    return ['', f'## illisible_cmd : {len(items)} chunk(s) avec command_block / run_command que le lecteur NBT strict ne lit pas : '
            'commandes NON reecrites, a traiter a la main (fichier, chunk cx cz)'] + [f'  {f} chunk ({cx}, {cz})' for f, cx, cz in sorted(items)]


def _table(commands):
    """[commande de chaque bloc] -> {risque: (blocs, commandes distinctes)}."""
    out = {}
    for cmd, n in Counter(commands).items():
        for r in _risks(cmd):
            b, d = out.get(r, (0, 0))
            out[r] = (b + n, d + 1)
    return out


def _risk_lines(before, after):
    """Tableau des risques ; avec `after` : colonne « apres » (même ordre des catégories)."""
    out = ['', '## Risques par categorie (blocs / commandes distinctes)' + (', avant -> apres reecriture' if after is not None else '')]
    a = _table(c.new for c in after) if after is not None else None
    for n in fl_terrain.RISK_NAMES:
        b, d = before.get(n, (0, 0))
        b2, d2 = a.get(n, (0, 0)) if a is not None else (0, 0)
        if b or b2:
            out.append(f'- {n:17}: {b:5} blocs / {d:4} distinctes' + (f' -> apres {b2:5} blocs / {d2:4} distinctes' if a is not None else ''))
    return out


def _rewrite_lines(ctx, after):
    acts = Counter((c.action, c.reason) for c in after)
    n = Counter(c.action for c in after)
    noop = {r: acts[('noop', r)] for r in _NOOPS if acts[('noop', r)]}
    out = ['', '## Reecritures (une par bloc de commande, minecart ou clic de panneau)',
           f'- modifiees : {n["reecrit"] + n["noop"]} (reecrites {n["reecrit"]}, remplacees par NOOP {n["noop"]}) ; laissees {n["laisse"]} ; '
           f'sans changement {n["inchange"]}',
           f'- fichiers reconstruits : {ctx["files_rebuilt"]} ; VERSION 2 (source-sha256 {ctx["source_sha"]})']
    out += [f'- {label} : {ctx["effects"][k]}' for k, label in _FX if ctx['effects'][k]]
    out += [f'- NOOP ({r}) : {k}' for r, k in noop.items()]
    out += [f'- cibles schedule distinctes : {len(ctx["sched"])} ; sans trampoline dans le depot : {len(ctx["sched_missing"])} '
            '(lancer gen_floaty.py puis relancer le build)' if ctx['sched_missing'] else f'- cibles schedule distinctes : {len(ctx["sched"])} ; '
            'toutes ont leur trampoline dans le depot']
    out += [f'  sans trampoline : {t}' for t in ctx['sched_missing']]
    return out


def _left_lines(after):
    left = sorted((c for c in after if c.action == 'laisse' or c.reason in ('selecteur_residuel', 'eclate')),     # eclate : un NOOP, listé aussi
                  key=lambda c: (_LEFT.index(c.reason) if c.reason in _LEFT else len(_LEFT), c.found.file, c.found.pos, c.found.kind))
    out = ['', f'## Non reecrits : {len(left)} (raison, x y z, type, commande)']
    out += [f'- {r} : {k}' for r, k in sorted(Counter(c.reason for c in left).items())]
    return out + [f'{c.reason}\t{c.found.pos[0]} {c.found.pos[1]} {c.found.pos[2]}\t{c.found.kind}\t{" ".join(c.found.command.split())}' for c in left]


def report_text(ctx, finds, stats, pending, after=None):
    """Texte du rapport des commandes du terrain (blocs, minecarts, panneaux ; `ctx` : carte, dim, sha, notes...). after : voir l'en-tête."""
    rows = risky_commands(finds)
    kinds = Counter(f.kind.split('[')[0] for f in finds)
    per_risk = {n: [r for r in rows if n in r[1]] for n in fl_terrain.RISK_NAMES}
    risky_blocks = sum(len(r[2]) for r in rows)
    out = ["# Blocs de commande du terrain Floaty (" + ("commandes reecrites au build : voir avant / apres)" if after is not None else
           "le terrain n'est pas reecrit : ces commandes tournent telles quelles)"),
           f'carte      : {ctx["map"]}', f'dimension  : {ctx["dim"]}', f'zip        : sha256 {ctx["zip_sha"]} ({ctx["zip_size"]} octets)',
           f'contenu    : sha256 {ctx["sha"]} ({ctx["files"]} fichiers, {ctx["regions"]} regions)'] + ctx['notes']
    out += ['', f'## Resume : {len(finds)} commandes du terrain (blocs, minecarts, panneaux) : {", ".join(f"{n} {k}" for k, n in sorted(kinds.items())) or "aucun"}',
            f'- commandes distinctes : {len(set(f.command for f in finds))} ; vides : {sum(1 for f in finds if not f.command.strip())}',
            f'- a risque{" (avant reecriture)" if after is not None else ""} : {risky_blocks} blocs, {len(rows)} commandes distinctes',
            f'- chunks a enregistrement complet : {stats["chunks"]} (lisibles ou non) ; {totals_line(*chunk_totals(stats, pending))}',
            f'- selecteurs en chaine non examines : {stats["sel_chaine"]} (@a @e... dans une chaine autre que "selector" / Command)'
            + (f', apres reecriture {sum(_sel_str(c.new) for c in after)}' if after is not None else '')]
    out += _chunk_sections(stats, pending) + _unread_cmd_lines(ctx.get('unread_cmd', ()))
    out += _risk_lines({n: (sum(len(r[2]) for r in rs), len(rs)) for n, rs in per_risk.items() if rs}, after)
    verbs = Counter(verb(r[0]) for r in per_risk['selecteur_global'] for _ in r[2])
    if verbs:
        out += ['', '## selecteur_global par commande finale (blocs, avant reecriture) : playsound = portee limitee au volume ; les autres (tellraw, title, tp, give, tag, spawnpoint...) visent TOUT le serveur']
        out += [f'- {v:16}: {n:5}' for v, n in verbs.most_common(VERBS)]
    out += ['', f'## {min(EXAMPLES, len(rows))} commandes les plus preoccupantes (distinctes ; 1er bloc ; nombre de blocs)']
    for c, risks, fs in rows[:EXAMPLES]:
        out.append(f'- [{",".join(risks)}] x{len(fs)} {_line(fs[0], risks)}')
    if after is None:
        out += ['', '## Liste complete (x y z, type, auto, risques, commande), triee par position']
        out += [_line(f, _risks(f.command)) for f in sorted(finds, key=lambda f: (f.file, f.pos, f.kind))]
        return '\n'.join(out) + '\n'
    out += _rewrite_lines(ctx, after) + _left_lines(after)
    out += ['', '## Liste complete APRES reecriture (x y z, type, auto, risques, commande ; <= avant : commande d\'origine), triee par position']
    for c in sorted(after, key=lambda c: (c.found.file, c.found.pos, c.found.kind)):
        line = _line(c.found, _risks(c.new), c.new)
        out.append(line if c.new == c.found.command else f'{line}\t<= avant : {" ".join(c.found.command.split())}')
    return '\n'.join(out) + '\n'
