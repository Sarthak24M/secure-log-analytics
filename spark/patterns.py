# ---------- Username ----------

USERNAME_USER = r"user\s+'?([A-Za-z0-9._-]+)'?"
USERNAME_USER_EQUALS = r"user=([A-Za-z0-9._-]+)"
USERNAME_PASSWORD = r"password for '([A-Za-z0-9._-]+)'"
USERNAME_EXEC = r"USER=([A-Za-z0-9._-]+)"

# ---------- Target User ----------

# ---------- Target User ----------

TARGET_USER = r"\(to\s+([A-Za-z0-9._-]+)\)"
TARGET_USER_EQUALS = r"\buser=([A-Za-z0-9._-]+)"
TARGET_USER_EXEC = r"USER=([A-Za-z0-9._-]+)"

# ---------- Command ----------

COMMAND = r"COMMAND=(.*?)\]"

# ---------- Working Directory ----------

CWD = r"CWD=([^\]]+)"

# ---------- TTY ----------

TTY = r"TTY=([^\]]+)"

# ---------- UID ----------

UID = r"uid=(\d+)"

# ---------- Session ----------

SESSION_ID = r"session\s+'([^']+)'"

# ---------- IP ----------

IP = r"from\s+((?:\d{1,3}\.){3}\d{1,3})"

# ==========================================================
# Event Classification Patterns
# ==========================================================

# ---------- Authentication ----------

AUTH_FAILURE = (
    r"(?i)"
    r"Failed password|"
    r"authentication failure|"
    r"Invalid user|"
    r"Failed publickey"
)

AUTH_SUCCESS = (
    r"(?i)"
    r"Accepted password|"
    r"Accepted publickey"
)

# ---------- Password ----------

PASSWORD_CHANGE = (
    r"(?i)"
    r"password.*changed|"
    r"changed by"
)

# ---------- Privileged Commands ----------

PRIVILEGED_COMMAND = (
    r"(?i)"
    r"executing command"
)

# ---------- Sessions ----------

SESSION_OPEN = (
    r"(?i)"
    r"session opened"
)

SESSION_CLOSE = (
    r"(?i)"
    r"session closed"
)

# ---------- CRON ----------

CRON_JOB = (
    r"(?i)^cron"
)

# ---------- Shutdown ----------

SYSTEM_SHUTDOWN = (
    r"(?i)"
    r"powering down|"
    r"power off|"
    r"shutdown"
)

# ---------- Startup ----------

SYSTEM_STARTUP = (
    r"(?i)"
    r"startup|"
    r"system boot|"
    r"boot completed"
)