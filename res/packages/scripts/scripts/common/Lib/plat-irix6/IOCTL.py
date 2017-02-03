# 2017.02.03 22:00:13 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/plat-irix6/IOCTL.py
from warnings import warnpy3k
warnpy3k('the IOCTL module has been removed in Python 3.0', stacklevel=2)
del warnpy3k
IOCTYPE = 65280
LIOC = ord('l') << 8
LIOCGETP = LIOC | 1
LIOCSETP = LIOC | 2
LIOCGETS = LIOC | 5
LIOCSETS = LIOC | 6
DIOC = ord('d') << 8
DIOCGETC = DIOC | 1
DIOCGETB = DIOC | 2
DIOCSETE = DIOC | 3
IOCPARM_MASK = 127
IOC_VOID = 536870912
IOC_OUT = 1073741824
IOC_IN = 2147483648L
IOC_INOUT = IOC_IN | IOC_OUT
int = 'i'
short = 'h'
long = 'l'

def sizeof(t):
    import struct
    return struct.calcsize(t)


def _IO(x, y):
    return IOC_VOID | x << 8 | y


def _IOR(x, y, t):
    return IOC_OUT | (sizeof(t) & IOCPARM_MASK) << 16 | x << 8 | y


def _IOW(x, y, t):
    return IOC_IN | (sizeof(t) & IOCPARM_MASK) << 16 | x << 8 | y


def _IOWR(x, y, t):
    return IOC_INOUT | (sizeof(t) & IOCPARM_MASK) << 16 | x << 8 | y


FIONREAD = _IOR(ord('f'), 127, int)
FIONBIO = _IOW(ord('f'), 126, int)
FIOASYNC = _IOW(ord('f'), 125, int)
FIOSETOWN = _IOW(ord('f'), 124, int)
FIOGETOWN = _IOR(ord('f'), 123, int)
NCC = 8
NCC_PAD = 7
NCC_EXT = 16
NCCS = NCC + NCC_PAD + NCC_EXT
VINTR = 0
VQUIT = 1
VERASE = 2
VKILL = 3
VEOF = 4
VEOL = 5
VEOL2 = 6
VMIN = VEOF
VTIME = VEOL
VSWTCH = 7
VLNEXT = NCC + NCC_PAD + 0
VWERASE = NCC + NCC_PAD + 1
VRPRNT = NCC + NCC_PAD + 2
VFLUSHO = NCC + NCC_PAD + 3
VSTOP = NCC + NCC_PAD + 4
VSTART = NCC + NCC_PAD + 5
CNUL = '\x00'
CDEL = '\xff'
CESC = '\\'
CINTR = '\x7f'
CQUIT = '\x1c'
CBRK = '\xff'

def CTRL(c):
    return ord(c) & 15


CERASE = CTRL('H')
CKILL = CTRL('U')
CEOF = CTRL('d')
CEOT = CEOF
CSTART = CTRL('q')
CSTOP = CTRL('s')
CSWTCH = CTRL('z')
CSUSP = CSWTCH
CNSWTCH = 0
CLNEXT = CTRL('v')
CWERASE = CTRL('w')
CFLUSHO = CTRL('o')
CFLUSH = CFLUSHO
CRPRNT = CTRL('r')
CDSUSP = CTRL('y')
IGNBRK = 1
BRKINT = 2
IGNPAR = 4
PARMRK = 8
INPCK = 16
ISTRIP = 32
INLCR = 64
IGNCR = 128
ICRNL = 256
IUCLC = 512
IXON = 1024
IXANY = 2048
IXOFF = 4096
IBLKMD = 8192
OPOST = 1
OLCUC = 2
ONLCR = 4
OCRNL = 8
ONOCR = 16
ONLRET = 32
OFILL = 64
OFDEL = 128
NLDLY = 256
NL0 = 0
NL1 = 256
CRDLY = 1536
CR0 = 0
CR1 = 512
CR2 = 1024
CR3 = 1536
TABDLY = 6144
TAB0 = 0
TAB1 = 2048
TAB2 = 4096
TAB3 = 6144
BSDLY = 8192
BS0 = 0
BS1 = 8192
VTDLY = 16384
VT0 = 0
VT1 = 16384
FFDLY = 32768
FF0 = 0
FF1 = 32768
CBAUD = 15
B0 = 0
B50 = 1
B75 = 2
B110 = 3
B134 = 4
B150 = 5
B200 = 6
B300 = 7
B600 = 8
B1200 = 9
B1800 = 10
B2400 = 11
B4800 = 12
B9600 = 13
B19200 = 14
EXTA = 14
B38400 = 15
EXTB = 15
CSIZE = 48
CS5 = 0
CS6 = 16
CS7 = 32
CS8 = 48
CSTOPB = 64
CREAD = 128
PARENB = 256
PARODD = 512
HUPCL = 1024
CLOCAL = 2048
LOBLK = 16384
ISIG = 1
ICANON = 2
XCASE = 4
ECHO = 8
ECHOE = 16
ECHOK = 32
ECHONL = 64
NOFLSH = 128
IIEXTEN = 256
ITOSTOP = 512
SSPEED = B9600
IOCTYPE = 65280
TIOC = ord('T') << 8
oTCGETA = TIOC | 1
oTCSETA = TIOC | 2
oTCSETAW = TIOC | 3
oTCSETAF = TIOC | 4
TCSBRK = TIOC | 5
TCXONC = TIOC | 6
TCFLSH = TIOC | 7
TCGETA = TIOC | 8
TCSETA = TIOC | 9
TCSETAW = TIOC | 10
TCSETAF = TIOC | 11
TIOCFLUSH = TIOC | 12
TCDSET = TIOC | 32
TCBLKMD = TIOC | 33
TIOCPKT = TIOC | 112
TIOCPKT_DATA = 0
TIOCPKT_FLUSHREAD = 1
TIOCPKT_FLUSHWRITE = 2
TIOCPKT_NOSTOP = 16
TIOCPKT_DOSTOP = 32
TIOCNOTTY = TIOC | 113
TIOCSTI = TIOC | 114
TIOCSPGRP = _IOW(ord('t'), 118, int)
TIOCGPGRP = _IOR(ord('t'), 119, int)
TIOCCONS = _IOW(ord('t'), 120, int)
struct_winsize = 'hhhh'
TIOCGWINSZ = _IOR(ord('t'), 104, struct_winsize)
TIOCSWINSZ = _IOW(ord('t'), 103, struct_winsize)
TFIOC = ord('F') << 8
oFIONREAD = TFIOC | 127
LDIOC = ord('D') << 8
LDOPEN = LDIOC | 0
LDCLOSE = LDIOC | 1
LDCHG = LDIOC | 2
LDGETT = LDIOC | 8
LDSETT = LDIOC | 9
TERM_NONE = 0
TERM_TEC = 1
TERM_V61 = 2
TERM_V10 = 3
TERM_TEX = 4
TERM_D40 = 5
TERM_H45 = 6
TERM_D42 = 7
TM_NONE = 0
TM_SNL = 1
TM_ANL = 2
TM_LCF = 4
TM_CECHO = 8
TM_CINVIS = 16
TM_SET = 128
LDISC0 = 0
LDISC1 = 1
NTTYDISC = LDISC1
VSUSP = VSWTCH
TCSANOW = 0
TCSADRAIN = 1
TCSAFLUSH = 2
TCIFLUSH = 0
TCOFLUSH = 1
TCIOFLUSH = 2
TCOOFF = 0
TCOON = 1
TCIOFF = 2
TCION = 3
TO_STOP = LOBLK
IEXTEN = IIEXTEN
TOSTOP = ITOSTOP
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\common\Lib\plat-irix6\IOCTL.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 22:00:14 St�edn� Evropa (b�n� �as)