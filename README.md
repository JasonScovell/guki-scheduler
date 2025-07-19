# Call Schedule Generator

A GUI-based application for generating call schedules that can run on both Mac and Windows. The application helps manage personnel, groups, and create optimal call schedules based on specific rules.

## Features

- **Group Management**: Add, remove, and manage personnel groups
- **Personnel Management**: Add, remove, and reassign personnel to different groups
- **Excluded Weeks**: Mark specific weeks where no one should be on call
- **Smart Scheduling**: Generate schedules that follow these rules:
  - No two people from the same group can take call in consecutive weeks
  - Ideally, people from the same group should be spaced by 2+ weeks
  - Nobody can take call more than once
  - Call periods start Friday at 7 AM and last 7 full days
- **Multiple Options**: Generate up to 10 different schedule options
- **Excel Export**: Export schedules to Excel files with highlighted blank weeks

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Setup
1. Clone or download this repository
2. Navigate to the project directory
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Application
```bash
python call_scheduler.py
```

### Step-by-Step Guide

1. **Add Groups**
   - Go to the "Groups" tab
   - Enter a group name and click "Add Group"
   - Repeat for all your groups

2. **Add Personnel**
   - Go to the "Personnel" tab
   - Enter a name and select a group
   - Click "Add Personnel"
   - Repeat for all your personnel

3. **Set Excluded Weeks (Optional)**
   - Go to the "Excluded Weeks" tab
   - Select a Friday date and click "Add Excluded Week"
   - These weeks will be skipped in schedule generation

4. **Generate Schedules**
   - Go to the "Schedule" tab
   - Select a start date (must be a Friday)
   - Select an end date
   - Click "Generate Schedules"
   - Review the generated options in the text area

5. **Export to Excel**
   - After generating schedules, click "Export to Excel"
   - Choose a location and filename
   - The Excel file will contain all schedule options with highlighted blank weeks

## Database

The application uses SQLite for data storage. The database file (`call_schedule.db`) is created automatically in the same directory as the application. This ensures all data is stored locally and persists between sessions.

## Schedule Rules

The application enforces the following rules when generating schedules:

1. **Group Spacing**: No two people from the same group can take call in consecutive weeks
2. **Optimal Spacing**: People from the same group should ideally be spaced by 2+ weeks
3. **Single Assignment**: Nobody can take call more than once in the same period
4. **Week Structure**: Each call period starts Friday at 7 AM and lasts 7 full days
5. **Blank Weeks**: If no personnel are available for a week, it's marked as "BLANK" and highlighted in yellow

## File Structure

```
call schedule app/
├── call_scheduler.py      # Main application file
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── call_schedule.db      # SQLite database (created automatically)
```

## Troubleshooting

### Common Issues

1. **"No valid schedules found"**
   - Ensure you have enough personnel for the time period
   - Check that groups are properly assigned
   - Try reducing the time period or adding more personnel

2. **"Start date must be a Friday"**
   - The application requires the start date to be a Friday
   - Use the date picker to select a Friday

3. **Import errors**
   - Make sure all dependencies are installed: `pip install -r requirements.txt`
   - Ensure you're using Python 3.7 or higher

### Platform-Specific Notes

- **Mac**: The application should work out of the box with tkinter
- **Windows**: May need to install tkinter separately if not included with Python
- **Linux**: May need to install tkinter: `sudo apt-get install python3-tk` (Ubuntu/Debian)

## License

This project is open source and available under the MIT License.

## Support

For issues or questions, please check the troubleshooting section above or create an issue in the repository. 