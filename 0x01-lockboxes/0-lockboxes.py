#!/usr/bin/python3
"""Adetunji Afolabi"""


def look_next_opened_box(opened_boxes):
    """Adetunji Afolabi
    """
    for index, box in opened_boxes.items():
        if box.get('status') == 'opened':
            box['status'] = 'opened/checked'
            return box.get('keys')
    return None


def canUnlockAll(boxes):
    """
    """
    if len(boxes) <= 1 or boxes == [[]]:
        return True

    eth = {}
    while True:
        if len(eth) == 0:
            eth[0] = {
                'status': 'opened',
                'keys': boxes[0],
            }
        keys = look_next_opened_box(eth)
        if keys:
            for key in keys:
                try:
                    if eth.get(key) and eth.get(key).get('status') \
                       == 'opened/checked':
                        continue
                    eth[key] = {
                        'status': 'opened',
                        'keys': boxes[key]
                    }
                except (KeyError, IndexError):
                    continue
        elif 'opened' in [box.get('status') for box in eth.values()]:
            continue
        elif len(eth) == len(boxes):
            break
        else:
            return False

    return len(eth) == len(boxes)


def main():
    """Entry point"""
    canUnlockAll([[]])


if __name__ == '__main__':
    main()
