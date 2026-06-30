# ---------- Username ----------

USERNAME_USER = r"user\s+'?([A-Za-z0-9._-]+)'?"
USERNAME_PASSWORD = r"password for '([A-Za-z0-9._-]+)'"
USERNAME_EXEC = r"USER=([A-Za-z0-9._-]+)"

# ---------- Target User ----------

TARGET_USER = r"\(to\s+([A-Za-z0-9._-]+)\)"
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