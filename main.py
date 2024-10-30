import PySimpleGUI as PySG
from datetime import datetime


# Function to log actions with date and time
def log_action(action):
    with open("logs/log.txt", "a") as log_file:
        log_file.write(f"{datetime.now()} - {action}\n")


# Function to create the main screen
def main_screen():
    PySG.theme('LightBlue')

    # Layout of the main screen with updated menu
    layout = [
        [PySG.Menu([['Settings', ['APIs', 'Keys']], ['Profile', ['Edit Profile', 'Close']]], key='-MENU-')],
        [PySG.Button("Journal", size=(20, 2))],
        [PySG.Button("Article", size=(20, 2))],
        [PySG.Button("Author", size=(20, 2))]
    ]

    # Creating the main window
    log_action("Screen opened: Home - Admin Tool Author Service (ASAT)")
    return PySG.Window("Home - Admin Tool Author Service (ASAT)", layout, finalize=True)


# Function to create the Settings screen
def settings_screen(option):
    layout = [
        [PySG.Text(f"Settings for {option}", font=('Arial', 14))],
        [PySG.Button("Back Home", size=(10, 1))]
    ]
    log_action(f"Screen opened: Settings for {option}")
    return PySG.Window(f"Settings for {option}", layout, finalize=True)


# Function to create the Profile screen
def profile_screen():
    layout = [
        [PySG.Text("Edit Profile", font=('Arial', 14))],
        [PySG.Text("Username:"), PySG.InputText(key='-USERNAME-')],
        [PySG.Text("Email Address:"), PySG.InputText(key='-EMAIL-')],
        [PySG.Button("Save", size=(10, 1)), PySG.Button("Cancel", size=(10, 1))]
    ]
    log_action("Screen opened: Edit Profile")
    return PySG.Window("Edit Profile", layout, finalize=True)


# Function to create the Journal, Article, and Author screens
def content_screen(content_type):
    layout = [
        [PySG.Text(f"{content_type} Management", font=('Arial', 14))],
        [PySG.Button("Back Home", size=(10, 1))]
    ]
    log_action(f"Screen opened: {content_type} Management")
    return PySG.Window(f"{content_type} Management", layout, finalize=True)


# Function to confirm the closing of the application
def confirm_close():
    layout = [
        [PySG.Text("Do you really want to close the application?")],
        [PySG.Button("Yes"), PySG.Button("No")]
    ]
    log_action("Screen opened: Close Confirmation")
    return PySG.Window("Confirmation", layout, finalize=True)


# Initialize the main screen
main_window = main_screen()
settings_window, profile_window, confirm_window, content_window = None, None, None, None

# Event loop
while True:
    window, event, values = PySG.read_all_windows()

    # Closing the window
    if event == PySG.WINDOW_CLOSED:
        if window == confirm_window:
            confirm_window.close()
            confirm_window = None
        elif window == main_window:
            break
        else:
            window.close()

    # Handling Settings menu events
    elif event in ['APIs', 'Keys']:
        if settings_window is None:
            settings_window = settings_screen(event)

    # Handling Profile menu events
    elif event == 'Edit Profile' and profile_window is None:
        profile_window = profile_screen()
    elif event == 'Close':
        if confirm_window is None:
            confirm_window = confirm_close()

    # Journal, Article, and Author button events
    elif event == "Journal":
        if content_window is None:
            content_window = content_screen("Journal")
    elif event == "Article":
        if content_window is None:
            content_window = content_screen("Article")
    elif event == "Author":
        if content_window is None:
            content_window = content_screen("Author")

    # Handling confirmation to close application
    elif event == "Yes" and window == confirm_window:
        log_action("Action taken: Close Application")
        confirm_window.close()
        main_window.close()
        break
    elif event == "No" and window == confirm_window:
        log_action("Action taken: Cancel Close")
        confirm_window.close()

    # Handling profile save and cancel buttons
    elif event == "Save" and window == profile_window:
        log_action("Action taken: Save Profile")
        # Logic to save profile information (username and email)
        print("Profile saved successfully.")
        profile_window.close()
        profile_window = None
    elif event == "Cancel" and window == profile_window:
        log_action("Action taken: Cancel Profile Edit")
        profile_window.close()
        profile_window = None

    # Handling Back Home button to return to main screen and close the current screen
    elif event == "Back Home":
        log_action("Action taken: Back to Home")
        window.close()
        if window == content_window:
            content_window = None
        elif window == settings_window:
            settings_window = None
        elif window == profile_window:
            profile_window = None

# Close any remaining windows at the end
main_window.close()
