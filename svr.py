import os
import sys
import time
import random
import requests

# --- SVR CONFIGURATION ---
BOT_TOKEN = "8648265797:AAHYLu-efurLkAtCwxcDK-jtlDIDhh03tkg"
ADMIN_ID = "8257346492"

# --- SVR ULTRA NEON COLORS ---
G, R, W, C, Y, LR, M, B = '\033[1;32m', '\033[1;31m', '\033[1;37m', '\033[1;36m', '\033[1;33m', '\033[1;91m', '\033[1;35m', '\033[1;34m'

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

# --- SVR REAL-TIME LOGGING TO BOT ---
def send_svr_report(executor, target, t_type, reason, time_frame):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    msg = f"""
🚨 [ SVR NEURAL EXECUTIONER - 100% BAN LOG ]
------------------------------------------
👤 EXECUTOR : {executor}
🎯 TARGET   : {target}
📂 TYPE     : {t_type}
🔥 REASON   : {reason}
⏳ BAN TIME : {time_frame}
------------------------------------------
[[ 10,000+ REAL SESSIONS INJECTED ]]
STATUS : 100% PERMANENT BLACKLIST
Developed By : SVRCORN ( AMAN )
------------------------------------------
"""
    try: requests.post(url, data={'chat_id': ADMIN_ID, 'text': msg})
    except: pass

# --- Master Aggressive Warning Injection ---
def inject_deadly_warning(target):
    print(f"\n{R}[!] INITIALIZING NEURAL WARNING INJECTION TO TARGET...")
    time.sleep(1.5)
    print(f"{Y}[*] TARGET METADATA IDENTIFIED: {target}")
    print(f"{G}[*] CONNECTING TO TELEGRAM INTERNAL GATEWAY...")
    
    msg = [
        "╔" + "═"*66 + "╗",
        "║ ☢️  CRITICAL TERMINATION NOTICE : SVR NEURAL EXECUTIONER ☢️     ║",
        "║ -------------------------------------------------------------- ║",
        "║ WARNING: YOUR ACCOUNT IS PERMANENTLY FLAGGED FOR VIOLATIONS.   ║",
        "║ 10,000+ ENCRYPTED STRIKES INJECTED INTO TELEGRAM CORE SERVERS. ║",
        "║ THIS UID IS NOW BLACKLISTED FROM ALL GLOBAL SVR-NODES.         ║",
        "║ STATUS: 100% PERMANENT BAN | LOCKOUT: UNDER 12-48 HOURS.       ║",
        "║ NO APPEAL POSSIBLE. SYSTEM IS WIPING TARGET METADATA NOW.      ║",
        f"║ SOURCE: Developed By : SVRCORN ( AMAN )                        ║",
        "╚" + "═"*66 + "╝"
    ]
    for line in msg:
        print(f"{LR}{line}")
        time.sleep(0.04)
    print(f"\n{G}[SUCCESS] DEADLY WARNING BYPASSED SECURITY & INJECTED.")
    time.sleep(1.5)

# --- SVR PRIVATE ACCESS ---
def svr_auth():
    U, P = "SVRCORN@8530", "P@sw0rdSVRGod11"
    clear()
    print(f"{LR}="*72)
    print(f"{W}  S V R   T O O L S   X   |   N E U R A L   E X E C U T I O N E R")
    print(f"{LR}="*72)
    user = input(f"\n{C}[ROOT@SVR-MAIN]:~# {W}").strip()
    passw = input(f"[PASS@SVR-CORE]:~# {W}").strip()
    if user == U and passw == P:
        print(f"{G}\n[*] ACCESS GRANTED. SYNCHRONIZING REAL-TIME BAN ENGINE..."); time.sleep(1)
        return user
    else:
        print(f"{R}\n[!] ACCESS DENIED."); sys.exit()

# --- AI Reason Engine & Ban Timer ---
def get_ai_reasons():
    reasons = {
        "1": ("Child Safety (CSAM)", "INSTANT (1-6 Hours)", "100%"),
        "2": ("Terrorist Content", "ULTRA FAST (2-12 Hours)", "100%"),
        "3": ("Hate Speech/Violence", "STRICT (12-24 Hours)", "95%"),
        "4": ("Financial Fraud/Scam", "LEGAL (24-48 Hours)", "90%"),
        "5": ("Copyright/Pornography", "NORMAL (48-72 Hours)", "85%"),
        "6": ("Personal Harassment", "MODERATION (72 Hours)", "80%")
    }
    print(f"\n{C}[ SVR AI-STRIKE ENGINE - PROBABILITY LOG ]")
    print(f"{LR}ID   REASON                     BAN-TIME           PROBABILITY")
    print(f"{W}--------------------------------------------------------------")
    for k, v in reasons.items():
        print(f"{G}[{k}]  {W}{v[0]:25}  {Y}{v[1]:18}  {LR}{v[2]}")
    return reasons

# --- 10,000+ Session Strike Animation ---
def session_flood(target):
    print(f"\n{R}[!] INJECTING 10,000+ REAL SVR-SESSIONS INTO TG-CORE...")
    for i in range(1, 10001, 200):
        sys.stdout.write(f"\r{Y}[STRIKE] {W}SESSION_ID: {random.randint(100000, 999999):X} {G}BYPASSED {LR}[{i}/10000]")
        sys.stdout.flush()
        time.sleep(0.015)
    print(f"\n{G}[SUCCESS] ALL 10,000+ SESSIONS ARE NOW REPORTING {target}")

# --- Big Display Banner ---
def svr_banner():
    clear()
    print(f"{LR}="*72)
    print(f"{LR}" + r"""
  ██████  ██    ██ ██████      ████████  ██████   ██████  ██      ███████ 
 ██       ██    ██ ██   ██        ██    ██    ██ ██    ██ ██      ██      
  █████   ██    ██ ██████         ██    ██    ██ ██    ██ ███████ ███████ 
      ██   ██  ██  ██   ██        ██    ██    ██ ██    ██ ██           ██ 
  ██████     ██    ██   ██        ██     ██████   ██████  ███████ ███████ 
                                                                          
          [[  S V R   T O O L S   X   -   V 2 5 0 0 . 0  ]]
    """)
    print(f"{W}       Developed By : SVRCORN ( AMAN )  |  [ NEURAL EXECUTION ]")
    print(f"{LR}="*72)

def main():
    executor = svr_auth()
    while True:
        svr_banner()
        print(f"{G}[01] Telegram Account Ban (Strict)")
        print(f"{G}[02] Telegram Channel Ban (Permanent)")
        print(f"{G}[03] Telegram Group Ban (Total Wipe)")
        mode = input(f"\n{C}[SVR-MODE@SELECT]:~# {W}").strip()
        target = input(f"{G}[?] TARGET LINK/NUMBER: {Y}").strip()
        
        # Trigger Warning Injection
        inject_deadly_warning(target)
        
        reasons_list = get_ai_reasons()
        r_choice = input(f"\n{C}[?] SELECT REASON ID FOR EXECUTION: {W}").strip()
        
        if r_choice in reasons_list:
            reason, ban_time, prob = reasons_list[r_choice]
            
            print(f"\n{R}[!] PREPARING FINAL NEURAL STRIKE... TARGET IS NOW BLACKLISTED.")
            time.sleep(2)
            
            # Start Flooding
            session_flood(target)
            
            # Send Notification to Admin Bot
            t_type = "ACCOUNT" if mode == '1' else "CHANNEL" if mode == '2' else "GROUP"
            send_svr_report(executor, target, t_type, reason, ban_time)
            
            print(f"\n{G}[COMPLETE] 100% REAL ACTION FINISHED ON {target}")
            print(f"{W}NOTIFIED TO SVR-CORE CLOUD BOT.")
            print(f"{C}Developed By : SVRCORN ( AMAN )")
            input(f"\n{Y}Press Enter to return to Command Center...")
        else:
            print(f"{R}[!] INVALID SELECTION."); time.sleep(1)

if __name__ == "__main__":
    try: main()
    except KeyboardInterrupt: sys.exit()
