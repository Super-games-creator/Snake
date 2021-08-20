from .conf import CW, CH, MX, MY, PX, PY, H_PANEL


def get_x(cx):
    return cx * CW + MX + PX


def get_y(cy):
    return cy * CH + MY + PY + H_PANEL
