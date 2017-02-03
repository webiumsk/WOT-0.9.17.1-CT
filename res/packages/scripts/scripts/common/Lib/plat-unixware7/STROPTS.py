# 2017.02.03 22:00:50 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/plat-unixware7/STROPTS.py


def quad_low(x):
    return x.val[0]


ADT_EMASKSIZE = 8
SHRT_MIN = -32768
SHRT_MAX = 32767
INT_MIN = -0x80000000
INT_MAX = 2147483647
LONG_MIN = -0x80000000
LONG_MAX = 2147483647
OFF32_MAX = LONG_MAX
ISTAT_ASSERTED = 0
ISTAT_ASSUMED = 1
ISTAT_NONE = 2
OFF_MAX = OFF32_MAX
CLOCK_MAX = LONG_MAX
P_MYID = -1
P_MYHOSTID = -1
FD_SETSIZE = 4096
NBBY = 8
NULL = 0
D_NEW = 0
D_OLD = 1
D_DMA = 2
D_BLKOFF = 1024
D_LFS = 32768
D_STR = 2048
D_MOD = 4096
D_PSEUDO = 8192
D_RANDOM = 16384
D_HOT = 65536
D_SEEKNEG = 4
D_TAPE = 8
D_NOBRKUP = 16
D_INITPUB = 32
D_NOSPECMACDATA = 64
D_RDWEQ = 128
SECMASK = D_INITPUB | D_NOSPECMACDATA | D_RDWEQ
DAF_REQDMA = 1
DAF_PHYSREQ = 2
DAF_PRE8 = 4
DAF_STATIC = 8
DAF_STR = 16
D_MP = 256
D_UPF = 512
ROOTFS_NAMESZ = 7
FMNAMESZ = 8
MCD_VERSION = 1
DI_BCBP = 0
DI_MEDIA = 1
ES_MACOPENLID = 1
ES_MACSYSLID = 2
ES_MACROOTLID = 3
ES_PRVINFO = 4
ES_PRVSETCNT = 5
ES_PRVSETS = 6
ES_MACADTLID = 7
ES_PRVID = 8
ES_TPGETMAJOR = 9
SA_EXEC = 1
SA_WRITE = 2
SA_READ = 4
SA_SUBSIZE = 8
X_STR = ord('S') << 8
X_I_BASE = X_STR | 128
X_I_NREAD = X_STR | 129
X_I_PUSH = X_STR | 130
X_I_POP = X_STR | 131
X_I_LOOK = X_STR | 132
X_I_FLUSH = X_STR | 133
X_I_SRDOPT = X_STR | 134
X_I_GRDOPT = X_STR | 135
X_I_STR = X_STR | 136
X_I_SETSIG = X_STR | 137
X_I_GETSIG = X_STR | 138
X_I_FIND = X_STR | 139
X_I_LINK = X_STR | 140
X_I_UNLINK = X_STR | 141
X_I_PEEK = X_STR | 143
X_I_FDINSERT = X_STR | 144
X_I_SENDFD = X_STR | 145
X_I_RECVFD = X_STR | 146
R_OK = 4
W_OK = 2
X_OK = 1
F_OK = 0
EFF_ONLY_OK = 8
EX_OK = 16
SEEK_SET = 0
SEEK_CUR = 1
SEEK_END = 2
_SC_ARG_MAX = 1
_SC_CHILD_MAX = 2
_SC_CLK_TCK = 3
_SC_NGROUPS_MAX = 4
_SC_OPEN_MAX = 5
_SC_JOB_CONTROL = 6
_SC_SAVED_IDS = 7
_SC_VERSION = 8
_SC_PASS_MAX = 9
_SC_LOGNAME_MAX = 10
_SC_PAGESIZE = 11
_SC_PAGE_SIZE = _SC_PAGESIZE
_SC_XOPEN_VERSION = 12
_SC_NACLS_MAX = 13
_SC_NPROCESSORS_CONF = 14
_SC_NPROCESSORS_ONLN = 15
_SC_NPROCESSES = 39
_SC_TOTAL_MEMORY = 40
_SC_USEABLE_MEMORY = 41
_SC_GENERAL_MEMORY = 42
_SC_DEDICATED_MEMORY = 43
_SC_NCGS_CONF = 44
_SC_NCGS_ONLN = 45
_SC_MAX_CPUS_PER_CG = 46
_SC_CG_SIMPLE_IMPL = 47
_SC_CACHE_LINE = 48
_SC_SYSTEM_ID = 49
_SC_THREADS = 51
_SC_THREAD_ATTR_STACKADDR = 52
_SC_THREAD_ATTR_STACKSIZE = 53
_SC_THREAD_DESTRUCTOR_ITERATIONS = 54
_SC_THREAD_KEYS_MAX = 55
_SC_THREAD_PRIORITY_SCHEDULING = 56
_SC_THREAD_PRIO_INHERIT = 57
_SC_THREAD_PRIO_PROTECT = 58
_SC_THREAD_STACK_MIN = 59
_SC_THREAD_PROCESS_SHARED = 60
_SC_THREAD_SAFE_FUNCTIONS = 61
_SC_THREAD_THREADS_MAX = 62
_SC_KERNEL_VM = 63
_SC_TZNAME_MAX = 320
_SC_STREAM_MAX = 321
_SC_XOPEN_CRYPT = 323
_SC_XOPEN_ENH_I18N = 324
_SC_XOPEN_SHM = 325
_SC_XOPEN_XCU_VERSION = 327
_SC_AES_OS_VERSION = 330
_SC_ATEXIT_MAX = 331
_SC_2_C_BIND = 350
_SC_2_C_DEV = 351
_SC_2_C_VERSION = 352
_SC_2_CHAR_TERM = 353
_SC_2_FORT_DEV = 354
_SC_2_FORT_RUN = 355
_SC_2_LOCALEDEF = 356
_SC_2_SW_DEV = 357
_SC_2_UPE = 358
_SC_2_VERSION = 359
_SC_BC_BASE_MAX = 370
_SC_BC_DIM_MAX = 371
_SC_BC_SCALE_MAX = 372
_SC_BC_STRING_MAX = 373
_SC_COLL_WEIGHTS_MAX = 380
_SC_EXPR_NEST_MAX = 381
_SC_LINE_MAX = 382
_SC_RE_DUP_MAX = 383
_SC_IOV_MAX = 390
_SC_NPROC_CONF = 391
_SC_NPROC_ONLN = 392
_SC_XOPEN_UNIX = 400
_SC_SEMAPHORES = 440
_CS_PATH = 1
__O_CS_HOSTNAME = 2
_CS_RELEASE = 3
_CS_VERSION = 4
__O_CS_MACHINE = 5
__O_CS_ARCHITECTURE = 6
_CS_HW_SERIAL = 7
__O_CS_HW_PROVIDER = 8
_CS_SRPC_DOMAIN = 9
_CS_INITTAB_NAME = 10
__O_CS_SYSNAME = 11
_CS_LFS_CFLAGS = 20
_CS_LFS_LDFLAGS = 21
_CS_LFS_LIBS = 22
_CS_LFS_LINTFLAGS = 23
_CS_LFS64_CFLAGS = 24
_CS_LFS64_LDFLAGS = 25
_CS_LFS64_LIBS = 26
_CS_LFS64_LINTFLAGS = 27
_CS_ARCHITECTURE = 100
_CS_BUSTYPES = 101
_CS_HOSTNAME = 102
_CS_HW_PROVIDER = 103
_CS_KERNEL_STAMP = 104
_CS_MACHINE = 105
_CS_OS_BASE = 106
_CS_OS_PROVIDER = 107
_CS_SYSNAME = 108
_CS_USER_LIMIT = 109
_PC_LINK_MAX = 1
_PC_MAX_CANON = 2
_PC_MAX_INPUT = 3
_PC_NAME_MAX = 4
_PC_PATH_MAX = 5
_PC_PIPE_BUF = 6
_PC_NO_TRUNC = 7
_PC_VDISABLE = 8
_PC_CHOWN_RESTRICTED = 9
_PC_FILESIZEBITS = 10
_POSIX_VERSION = 199009L
_XOPEN_VERSION = 4
GF_PATH = '/etc/group'
PF_PATH = '/etc/passwd'
F_ULOCK = 0
F_LOCK = 1
F_TLOCK = 2
F_TEST = 3
_POSIX_JOB_CONTROL = 1
_POSIX_SAVED_IDS = 1
_POSIX_VDISABLE = 0
NULL = 0
STDIN_FILENO = 0
STDOUT_FILENO = 1
STDERR_FILENO = 2
_XOPEN_UNIX = 1
_XOPEN_ENH_I18N = 1
_XOPEN_XPG4 = 1
_POSIX2_C_VERSION = 199209L
_POSIX2_VERSION = 199209L
_XOPEN_XCU_VERSION = 4
_POSIX_SEMAPHORES = 1
_POSIX_THREADS = 1
_POSIX_THREAD_ATTR_STACKADDR = 1
_POSIX_THREAD_ATTR_STACKSIZE = 1
_POSIX_THREAD_PRIORITY_SCHEDULING = 1
_POSIX_THREAD_PROCESS_SHARED = 1
_POSIX_THREAD_SAFE_FUNCTIONS = 1
_POSIX2_C_BIND = 1
_POSIX2_CHAR_TERM = 1
_POSIX2_FORT_RUN = 1
_POSIX2_LOCALEDEF = 1
_POSIX2_UPE = 1
_LFS_ASYNCHRONOUS_IO = 1
_LFS_LARGEFILE = 1
_LFS64_ASYNCHRONOUS_IO = 1
_LFS64_LARGEFILE = 1
_LFS64_STDIO = 1
FMNAMESZ = 8
SNDZERO = 1
SNDPIPE = 2
RNORM = 0
RMSGD = 1
RMSGN = 2
RMODEMASK = 3
RPROTDAT = 4
RPROTDIS = 8
RPROTNORM = 16
RPROTMASK = 28
FLUSHR = 1
FLUSHW = 2
FLUSHRW = 3
FLUSHBAND = 4
S_INPUT = 1
S_HIPRI = 2
S_OUTPUT = 4
S_MSG = 8
S_ERROR = 16
S_HANGUP = 32
S_RDNORM = 64
S_WRNORM = S_OUTPUT
S_RDBAND = 128
S_WRBAND = 256
S_BANDURG = 512
RS_HIPRI = 1
MSG_HIPRI = 1
MSG_ANY = 2
MSG_BAND = 4
MSG_DISCARD = 8
MSG_PEEKIOCTL = 16
MORECTL = 1
MOREDATA = 2
MUXID_ALL = -1
ANYMARK = 1
LASTMARK = 2
STR = ord('S') << 8
I_NREAD = STR | 1
I_PUSH = STR | 2
I_POP = STR | 3
I_LOOK = STR | 4
I_FLUSH = STR | 5
I_SRDOPT = STR | 6
I_GRDOPT = STR | 7
I_STR = STR | 8
I_SETSIG = STR | 9
I_GETSIG = STR | 10
I_FIND = STR | 11
I_LINK = STR | 12
I_UNLINK = STR | 13
I_PEEK = STR | 15
I_FDINSERT = STR | 16
I_SENDFD = STR | 17
I_RECVFD = STR | 18
I_E_RECVFD = STR | 14
I_RECVFD = STR | 14
I_RECVFD = STR | 18
I_SWROPT = STR | 19
I_GWROPT = STR | 20
I_LIST = STR | 21
I_PLINK = STR | 22
I_PUNLINK = STR | 23
I_FLUSHBAND = STR | 28
I_CKBAND = STR | 29
I_GETBAND = STR | 30
I_ATMARK = STR | 31
I_SETCLTIME = STR | 32
I_GETCLTIME = STR | 33
I_CANPUT = STR | 34
I_S_RECVFD = STR | 35
I_STATS = STR | 36
I_BIGPIPE = STR | 37
I_GETTP = STR | 38
INFTIM = -1
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\common\Lib\plat-unixware7\STROPTS.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 22:00:51 St�edn� Evropa (b�n� �as)
