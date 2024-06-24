from kivy.metrics import dp
from kivymd.uix.dialog import (
    MDDialog,
    MDDialogIcon,
    MDDialogHeadlineText,
    MDDialogSupportingText,
    MDDialogButtonContainer,
    MDDialogContentContainer,
)



def alert(title,msg):
    dialog = MDDialog(
        # -----------------------Headline text-------------------------
        MDDialogHeadlineText(
            text=title,
            font_style="Title",
            role="medium"
        ),
        # -----------------------Supporting text-----------------------
        MDDialogSupportingText(
            text=msg,
            font_style="Body",
            role="medium",
        ))
    dialog.open()
    dialog.update_width()


