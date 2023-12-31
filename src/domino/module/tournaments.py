from .players import MonteCarlo, get_hand
from .domino import DominoManager


def runner(data, rep, output, game_config, hand='hand_out'):
    [(p0, *args0), (p1, *args1)] = data
    p0name = p0.__name__
    p1name = p1.__name__
    key = f'{p0name}_vs_{p1name}'
    d = output[key] = output.get(key, {-1:0, 0:0, 1:0})
    for _ in range(rep):
        manager = DominoManager()
        winner = manager.run([
                p0(f'{p0name}0', *args0),
                p1(f'{p0name}1', *args1),
                p0(f'{p0name}2', *args0),
                p1(f'{p0name}3', *args1),
            ], 
            get_hand(hand),
            *game_config,
        )
        d[winner] += 1

__all__ = []
