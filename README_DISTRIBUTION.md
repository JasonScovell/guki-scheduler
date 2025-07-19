# Call Schedule Generator - Distribution Package

## 📦 What's Included

This package contains a **standalone executable** that includes all dependencies. No Python installation required!

### Files:
- `CallScheduleGenerator` (macOS) or `CallScheduleGenerator.exe` (Windows) - The main application
- `launch_mac.sh` (macOS) or `launch_windows.bat` (Windows) - Easy launcher script
- `README_DISTRIBUTION.md` - This file

## 🚀 Quick Start

### For macOS Users:
1. **Double-click** `CallScheduleGenerator` to run directly
   - OR -
2. **Right-click** `launch_mac.sh` → "Open" → "Open" (to bypass security)
   - OR -
3. **Terminal**: `./launch_mac.sh`

### For Windows Users:
1. **Double-click** `CallScheduleGenerator.exe` to run directly
   - OR -
2. **Double-click** `launch_windows.bat` for a launcher with pause

## 🔧 System Requirements

### macOS:
- macOS 10.14 (Mojave) or later
- Intel or Apple Silicon (M1/M2) Macs supported
- No additional software required

### Windows:
- Windows 10 or later
- No additional software required

## 📋 Features

### ✅ What the App Does:
- **Manage Personnel**: Add, edit, remove personnel with their groups
- **Manage Groups**: Create and organize personnel into groups
- **Generate Schedules**: Create weekly call schedules starting Fridays at 7 AM
- **Exclude Weeks**: Set specific weeks when personnel are unavailable
- **Export to Excel**: Save schedules as Excel files
- **Local Database**: All data stored locally in SQLite database

### 🎯 Key Features:
- **Friday-Only Scheduling**: All schedules start on Fridays
- **Multiple Options**: Generate up to 10 different schedule options
- **Smart Assignment**: Automatically assigns personnel based on availability
- **Excel Export**: Professional Excel output with formatting
- **Data Persistence**: All data saved automatically

## 📖 How to Use

### 1. First Time Setup:
1. **Launch the application**
2. **Add Groups**: Go to "Groups" tab → Add your groups (e.g., "Cardiology", "Emergency")
3. **Add Personnel**: Go to "Personnel" tab → Add people with their groups

### 2. Generate a Schedule:
1. **Go to "Generate Schedule" tab**
2. **Set Start Date**: Click 📅 to select a Friday start date
3. **Set End Date**: Click 📅 to select when the schedule should end
4. **Click "Generate Schedule"**
5. **Review Options**: The app will show up to 10 different schedule options
6. **Export**: Click "Export to Excel" to save your preferred option

### 3. Manage Excluded Weeks:
1. **Go to "Personnel Excluded Weeks" tab**
2. **Select Personnel**: Choose who can't work certain weeks
3. **Add Excluded Weeks**: Click 📅 to select weeks they're unavailable
4. **Save**: Click "Save Excluded Weeks"

## 🗂️ Data Storage

- **Database**: `call_schedule.db` (created automatically in the same folder)
- **Excel Files**: Saved wherever you choose when exporting
- **No Internet Required**: Everything works offline

## 🔒 Security & Privacy

- **100% Local**: No data sent anywhere
- **No Internet**: Works completely offline
- **Your Data**: All data stored on your computer only

## 🆘 Troubleshooting

### macOS Issues:
- **"Unidentified Developer"**: Right-click → "Open" → "Open"
- **Permission Denied**: `chmod +x CallScheduleGenerator` in Terminal
- **App Won't Open**: Check System Preferences → Security & Privacy

### Windows Issues:
- **"Windows protected your PC"**: Click "More info" → "Run anyway"
- **Antivirus Warning**: Add to exceptions or temporarily disable
- **Missing DLL**: Usually means Windows needs updates

### General Issues:
- **App Freezes**: Close and restart (data is auto-saved)
- **Can't Save Excel**: Check folder permissions
- **Database Issues**: Delete `call_schedule.db` to reset (loses all data)

## 📞 Support

If you encounter issues:
1. **Check this README** for troubleshooting steps
2. **Restart the application** (data is auto-saved)
3. **Check file permissions** in the folder
4. **Contact your IT department** if needed

## 🔄 Updates

To update the application:
1. **Download the new version**
2. **Replace the old executable**
3. **Your data will be preserved** (database stays the same)

## 📝 Version Information

- **Version**: 1.0
- **Build Date**: July 2025
- **Compatibility**: macOS 10.14+, Windows 10+
- **Dependencies**: None (all included)

---

**Note**: This is a standalone application. No Python, libraries, or additional software installation required! 