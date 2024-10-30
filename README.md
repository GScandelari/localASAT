# Admin Tool Author Service (ASAT)

## Overview

This application is a graphical user interface (GUI) developed using Python and PySimpleGUI. It includes a main screen with options to manage "Journal," "Article," and "Author" entities, as well as configuration and profile settings.

### Key Features

1. **Main Screen**: The main screen has buttons for managing journals, articles, and authors, along with a menu for "Settings" and "Profile."
2. **Settings**: Provides access to "APIs" and "Keys" settings, each of which opens a dedicated screen.
3. **Profile**: Allows users to edit their profile (username and email) and to close the application with confirmation.
4. **Journal, Article, and Author Management**: Each button on the main screen opens a specific screen for managing Journals, Articles, or Authors.
5. **Logging**: All actions, including screen navigation and button clicks, are logged with date and time in a `log.txt` file.

### Screens and Components

1. **Main Screen**: Contains buttons for "Journal," "Article," and "Author" management, and a menu with "Settings" and "Profile" options.
2. **Settings Screen**: Opens upon selecting "APIs" or "Keys" from the "Settings" menu, showing a dedicated screen for each option.
3. **Profile Screen**: Opens upon selecting "Edit Profile," displaying fields for editing the username and email.
4. **Confirmation Screen**: Prompts the user to confirm closing the application when "Close" is selected from the "Profile" menu.
5. **Journal, Article, and Author Screens**: Each button (Journal, Article, Author) opens a specific screen with management options and a "Back Home" button.

### Usage of "Back Home" Button

Each management or settings screen includes a "Back Home" button that closes the current screen and returns to the main screen. This button also resets the window state, allowing users to reopen the same screen multiple times without issues.

### Log File

The application maintains a `log.txt` file that records each user action, including the time, screen navigated, or action taken.

## Requirements

- Python 3.x
- PySimpleGUI

Install dependencies with:

> pip install PySimpleGUI

## How to Use
1. Run the program.
2. Use the main buttons or menu options to navigate between different screens.
3. Click "Back Home" to return to the main screen and allow for reopening any management or settings screen.
4. Choose "Close" from the Profile menu to exit the application, with a confirmation prompt.

### Example Log Entry

The log entries are saved in a log.txt file with a timestamp and a description of the action taken. 
Example:


- 2023-10-28 12:35:22 - Screen opened: Home - Admin Tool Author Service (ASAT)
- 2023-10-28 12:36:05 - Screen opened: Settings for APIs
- 2023-10-28 12:37:01 - Action taken: Back to Home
- 2023-10-28 12:40:10 - Screen opened: Journal Management


### Running the Program
1. Save this README.md file and the Python script in the same directory.
2. Run the Python script to start the GUI application.#   l o c a l A S A T  
 