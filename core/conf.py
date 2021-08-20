MX = MY = 10  # внешний отступ
PX = PY = 8  # внутренний отступ
CW = CH = 24
COLS = 50  # число клеток по горизонтали
ROWS = 35  # число клеток по вертикали
SNAKE = [(0, 0), (0, 0), (0, 0), (0, 0)]
H_PANEL = CH * 3
W = COLS*CW + 2*MX+2*PX
H = ROWS*CH + 2*MY+2*PY + H_PANEL
INI_SNAKE_LEN = 2
