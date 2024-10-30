import PySimpleGUI as PySG
from windows import main_screen, settings_screen, profile_screen, content_screen, confirm_close
from utils import log_action

# Initialize the main screen
main_window = main_screen()
settings_window, profile_window, confirm_window, content_window = None, None, None, None
current_content_type = None

# Event loop
while True:
    window, event, values = PySG.read_all_windows()

    # Close the window
    if event == PySG.WINDOW_CLOSED:
        if window == confirm_window:
            confirm_window.close()
            confirm_window = None
        elif window == main_window:
            break
        else:
            window.close()

    # Settings menu events
    elif event in ['APIs', 'Keys']:
        if settings_window is None:
            settings_window = settings_screen(event)

    # Profile menu events
    elif event == 'Edit Profile' and profile_window is None:
        profile_window = profile_screen()
    elif event == 'Close':
        if confirm_window is None:
            confirm_window = confirm_close()

    # Journal, Article, and Author button events
    elif event == "Journal":
        if content_window is None:
            current_content_type = "Journal"
            content_window = content_screen(current_content_type)
    elif event == "Article":
        if content_window is None:
            current_content_type = "Article"
            content_window = content_screen(current_content_type)
    elif event == "Author":
        if content_window is None:
            current_content_type = "Author"
            content_window = content_screen(current_content_type)

    # Confirmation to close the application
    elif event == "Yes" and window == confirm_window:
        log_action("Action taken: Close Application")
        confirm_window.close()
        main_window.close()
        break
    elif event == "No" and window == confirm_window:
        log_action("Action taken: Cancel Close")
        confirm_window.close()

    # Profile save and cancel actions
    elif event == "Save" and window == profile_window:
        log_action("Action taken: Save Profile")
        print("Profile saved successfully.")
        profile_window.close()
        profile_window = None
    elif event == "Cancel" and window == profile_window:
        log_action("Action taken: Cancel Profile Edit")
        profile_window.close()
        profile_window = None

    # Back Home button to close the current screen and return to main
    elif event == "Back Home":
        log_action("Action taken: Back to Home")
        window.close()
        if window == content_window:
            content_window = None
        elif window == settings_window:
            settings_window = None
        elif window == profile_window:
            profile_window = None
        current_content_type = None

    # Search action in Journal, Article, or Author screens
    elif event == "Search":
        search_text = values['-SEARCH_TEXT-']
        if current_content_type == "Author":
            search_by = values["-SEARCH_BY-"]
            log_action(f"Search action in Author Management by {search_by} with term: {search_text}")
            print(f"Searching Author by {search_by}: {search_text}")
        else:
            log_action(f"Search action in {current_content_type} Management with term: {search_text}")
            print(f"Searching {current_content_type}: {search_text}")

# Close any remaining windows at the end
main_window.close()
