# Find-your-Timetable
University-specific project: prototype in a single day, improvements in the following months. **NUCES-FAST** folks should enjoy this one.

# The idea
Having to scour for your timetable through a Google Spreadsheet provided to you by the administration team is a task of its own, managing all of the timetable according to your needs. It gets worse when electives and repeat courses are thrown in the mix and you also have to manage them.

The Spreadsheet access is public, so with that in mind, the basic premise for this project is to read all of the data presently noted online and format it in such a manner that, through a few clicks, all of the subjects that you're registered for in a semester will be presented to you for you to either note down, or simply look up on without having to keep checking for your classes, the timings, and in what rooms they're being held in.

# How to run
S run the main file in a Python environment. All dependencies will be installed automatically if not present in your system.
You'll be presented with a UI where you can select your degree, batch year, and your section.
Entering your information, you'll get a list of classes and labs you have to take on what day, in which room, and at what time.

# What the project provides as benefits
- Input your degree, batch year, and section, and get a list of courses you have registered for.
- The data is always up to date with the changes made on the original spreadsheet, so you can track any changes in timings or rooms of your classes.

# What the project _bluntly_ sucks in
- The UI is minimal, so it could be unpleasant for a few eyes.
- A few timing issues here and there, and not properly labelling the time durations for a few classes.
- The process, for now, is internet-dependent. Don't expect it to work if you don't have an internet connection.
- The spreadsheet ID, along with a few other attributes, are hardcoded into the script... _whoops._
- Messy code and little commenting (this is a sin in and of itself).

# What I intend to work on
- Repeat/Elective courses are not handled (the program assumes you have a normal workload for a semester).
- Handle MS/PhD courses and their electives as well.
- Handle different timings for the classes.
- Polish up the UI, so it's pleasant just enough for students to keep on using.
- Make the code a **LOT** more tidier and a **LOT** more generic.
- An option to enter the URL which will be used for getting the timetable data.
- Offer an offline mode on the off-chance there's no internet, so a local excel file will be used to view the schedule.

Any more improvements I get suggested along the way, I'll gladly consider. If you're interested in contributing to this little scripture, do let me know on my email. That's really all I have to say...

_Why didn't anyone think of making something like this before?_
