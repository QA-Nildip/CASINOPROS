"""author = AK"""

'''
This file contains constants
'''

# parameters
Device_IP = '192.168.2.100'
user_name = 'neel@gmail.com'
pwd = 'neel123'

main_hud = 'http://' + Device_IP + ':8342/q/scene/Canvas/GameEnterHUD/Buttons/'
# login page object
login_hud = main_hud + 'LoginButton.Button.onClick.Invoke()'
login_uname = 'http://' + Device_IP + ':8342/q/scene/Canvas/GameEnterHUD/LoginHUD/Contents/Main/' \
                                      'Email.InputField.text=' + user_name + ''
login_pwd = 'http://' + Device_IP + ':8342/q/scene/Canvas/GameEnterHUD/LoginHUD/Contents/Main/' \
                                    'Password.InputField.text=' + pwd + ''
login_submit = 'http://' + Device_IP + ':8342/q/scene/Canvas/GameEnterHUD/LoginHUD/Contents/Main/' \
                                       'LoginButton.Button.onClick.Invoke()'
login_screenshot = 'http://' + Device_IP + ':8342/utils/screenshot'
registration_page = main_hud + 'RegistrationButton.Button.onClick.Invoke()'

# registration object
registration_btn = main_hud + 'RegistrationButton.Button.onClick.Invoke()'
registration_hud = 'http://' + Device_IP + ':8342/q/scene/Canvas/GameEnterHUD/RegistrationHUD/'
reg_uname = registration_hud + 'UserNameInput.InputField.text=' + user_name + ''
reg_email = registration_hud + 'EmailInput.InputField.text=' + user_name + ''
reg_pwd = registration_hud + 'PasswordInput.InputField.text=' + pwd + ''
reg_confirmpwd = registration_hud + 'PasswordConfirmInput.InputField.text=' + pwd + ''
reg_submit_btn = registration_hud + 'RegisterButton.Button.onClick.Invoke()'
reg_cancel_btn = registration_hud + 'CancelButton.Button.onClick.Invoke()'
reg_err_msg = registration_hud + 'ErrorText.Text.text'
