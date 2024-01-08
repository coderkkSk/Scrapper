class Translation(object):
    START_TEXT = """<b>This Bot was created to help you retrieve APP ID and API Hash easily and SAFELY!
━━━━━━━━━━━━━━━━━━━━━━━━
Please enter your Telegram telephone number in country code format.
Example: +628xxxxxxx</b>
"""
    AFTER_RECVD_CODE_TEXT = """<b>Number Received!
Please send the code you received from Telegram!</b>

This code is only used for the purpose of getting the APP ID from my.telegram.org
If you don't trust this dev bot, just get the manual.
"""
    BEFORE_SUCC_LOGIN = "<code>Scrapping Web Page. . .</code>"
    ERRED_PAGE = """Error Occurred. Try the manual method

How to Retrieve APP ID and API HASH Manually:
1. Go to my.telegram.org/auth
2. Login to your Telegram account
3. Click the API Development menu
4. Fill in the data as below:
• App Title : tgbot
• Short Name : tgbot
• URL: (blank)
• Platform : desktop
5. Done

If successful, take the manual, please try again on this bot"""
    CANCELLED_MESG = "<b>Bye! Please /start again to repeat</b>"
    IN_VALID_CODE_PVDED = "<b>The OTP code you entered is WRONG</b>"
    IN_VALID_PHNO_PVDED = "<b><The cellphone number you entered is WRONG, please enter your Telegram telephone number in country code format.\nExample: +628xxxxxxx/b>"
