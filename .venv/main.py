from datetime import datetime

def analyze_logs(log_file, report_file):
   risks = []
   failed_attempts = {}

   with open(log_file, "r") as f:
       for line in f:
           parts = line.strip().split("|")
           timestamp = datetime.strptime(parts[0].strip(), "%Y-%m-%d %H:%M:%S")
           user = parts[1].split("=")[1].strip()
           status = parts[2].split("=")[1].strip()

           if status == "FAILURE":
               failed_attempts[user] = failed_attempts.get(user, 0) + 1
               if failed_attempts[user] >= 2:
                   risks.append(f"Suspicious login: {user} had {failed_attempts[user]} failed attempts")
               else:
                   failed_attempts[user] = 0
           if status == "SUCCESS":
               if timestamp.hour < 7 or timestamp.hour > 22:
                   risks.append(f"Out-of-hours login: {user} logged in at {timestamp.strftime('%H:%M')}.")

   with open(report_file, "w") as out:
       out.write("=== Risk Analysis Report ===\n\n")
       if risks:
           for i, risk in enumerate(risks, 1):
               out.write(f"{i}. {risk}\n")
       else:
           out.write("No risks detected.\n")
analyze_logs("system_logs.txt", "report.txt")
print("Analysis complete. Check report.txt")


