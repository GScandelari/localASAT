import PySimpleGUI as PySG
from utils import log_action


# Main screen window
def main_screen():
    PySG.theme('LightBlue')
    layout = [
        [PySG.Menu([['Settings', ['APIs', 'Keys']], ['Profile', ['Edit Profile', 'Close']]], key='-MENU-')],
        [PySG.Button("Journal", size=(20, 2))],
        [PySG.Button("Article", size=(20, 2))],
        [PySG.Button("Author", size=(20, 2))]
    ]
    log_action("Screen opened: Home - Admin Tool Author Service (ASAT)")
    return PySG.Window("Home - Admin Tool Author Service (ASAT)", layout, finalize=True)


# Settings window
def settings_screen(option):
    layout = [
        [PySG.Text(f"Settings for {option}", font=('Arial', 14))],
        [PySG.Button("Back Home", size=(10, 1))]
    ]
    log_action(f"Screen opened: Settings for {option}")
    return PySG.Window(f"Settings for {option}", layout, finalize=True)


# Profile window
def profile_screen():
    layout = [
        [PySG.Text("Edit Profile", font=('Arial', 14))],
        [PySG.Text("Username:"), PySG.InputText(key='-USERNAME-')],
        [PySG.Text("Email Address:"), PySG.InputText(key='-EMAIL-')],
        [PySG.Button("Save", size=(10, 1)), PySG.Button("Cancel", size=(10, 1))]
    ]
    log_action("Screen opened: Edit Profile")
    return PySG.Window("Edit Profile", layout, finalize=True)


# Content management screen (Journal, Article, Author)
def content_screen(content_type):
    if content_type == "Author":
        search_layout = [
            [PySG.Text("Search by:"),
             PySG.Combo(["First Name", "Last Name", "E-mail", "User ID"], default_value="First Name",
                        key="-SEARCH_BY-")],
            [PySG.InputText(key='-SEARCH_TEXT-'), PySG.Button("Search")]
        ]
    else:
        search_layout = [
            [PySG.Text("Search:"), PySG.InputText(key='-SEARCH_TEXT-'), PySG.Button("Search")]
        ]

    layout = [
        [PySG.Text(f"{content_type} Management", font=('Arial', 14))],
        *search_layout,
        [PySG.Button("Back Home", size=(10, 1))]
    ]
    log_action(f"Screen opened: {content_type} Management")
    return PySG.Window(f"{content_type} Management", layout, finalize=True)


# Close confirmation window
def confirm_close():
    layout = [
        [PySG.Text("Do you really want to close the application?")],
        [PySG.Button("Yes"), PySG.Button("No")]
    ]
    log_action("Screen opened: Close Confirmation")
    return PySG.Window("Confirmation", layout, finalize=True)
