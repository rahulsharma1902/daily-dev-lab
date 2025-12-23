# Setting Up Windows Task Scheduler for Daily Automation

## Quick Setup (Recommended)

### Option 1: Using PowerShell (One-time command)

Run this in PowerShell **as Administrator**:

```powershell
$action = New-ScheduledTaskAction -Execute "python" -Argument "C:\Users\Public\Downloads\rahul-office\personal\git-activity\daily-dev-lab\scripts\auto_daily.py" -WorkingDirectory "C:\Users\Public\Downloads\rahul-office\personal\git-activity\daily-dev-lab"

$trigger = New-ScheduledTaskTrigger -Daily -At 9:00AM

$settings = New-ScheduledTaskSettingsSet -StartWhenAvailable -DontStopIfGoingOnBatteries

Register-ScheduledTask -TaskName "DailyDevLab" -Action $action -Trigger $trigger -Settings $settings -Description "Daily Dev Lab auto commit"
```

### Option 2: Manual Setup via Task Scheduler GUI

1. **Open Task Scheduler**
   - Press `Win + R`, type `taskschd.msc`, press Enter

2. **Create New Task**
   - Click "Create Basic Task" in the right panel
   - Name: `DailyDevLab`
   - Description: `Daily Dev Lab - Auto learning commit`

3. **Set Trigger**
   - Select "Daily"
   - Set time: `9:00 AM` (or your preferred time)
   - Recur every: 1 day

4. **Set Action**
   - Select "Start a program"
   - Program: `python`
   - Arguments: `C:\Users\Public\Downloads\rahul-office\personal\git-activity\daily-dev-lab\scripts\auto_daily.py`
   - Start in: `C:\Users\Public\Downloads\rahul-office\personal\git-activity\daily-dev-lab`

5. **Finish**
   - Check "Open Properties dialog" before finishing
   - In Properties > Settings, check "Run task as soon as possible after a scheduled start is missed"

---

## How It Works

| Time | What Happens |
|------|--------------|
| **9:00 AM** | Script creates today's TIL file with a template |
| **During day** | You edit the file with actual learnings |
| **Anytime** | Run `python scripts/push.py` to push updates |

## Important Notes

⚠️ **The script creates a TEMPLATE file** - you must update it with real content!

✅ **Ethical**: Creates a genuine file for you to fill with today's learnings
✅ **No fake commits**: The template reminds you to add real content
✅ **One commit per day**: Won't create duplicates if run multiple times

---

## Testing Your Setup

```bash
# Test the script manually first
python scripts/auto_daily.py

# Check if file was created
dir notes\til\2024-*
```

## Disable/Remove Automation

```powershell
# Remove the scheduled task
Unregister-ScheduledTask -TaskName "DailyDevLab" -Confirm:$false
```

---

## Alternative: Multiple Commits Per Day

If you want 2-7 commits per day (as mentioned in requirements), you can:

1. **Morning**: Auto-create TIL (via scheduler)
2. **Afternoon**: Manually add a challenge solution
3. **Evening**: Add a snippet or experiment

Use these commands throughout the day:
```bash
python scripts/daily_commit.py --type challenge --name "problem-name" --push
python scripts/daily_commit.py --type snippet --topic "helper-name" --push
python scripts/daily_commit.py --type experiment --topic "new-library" --push
```
