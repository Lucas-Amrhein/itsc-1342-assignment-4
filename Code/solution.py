# Lucas Amrhein - Assignment 4

def check_session(idle_minutes, max_idle=20):
    if idle_minutes >= (max_idle):
        return 'SESSION_EXPIRED'
    else:
        return 'SESSION_ACTIVE'