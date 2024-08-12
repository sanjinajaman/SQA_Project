class LoginPage():
     #this is constructor
    def __init__(self,driver):
        self.driver=driver

        self.username_textbox_id=(By.ID,"email")
        self.password_textbox_id=(By.ID,"pass")
        self.login_id =(By.NAME,"login")

    def enter_username(self,email):
        self.driver.find_element(self.username_textbox_id).clear()
        self.driver.find_element(*self.username_textbox_id).send_keys(email)

    def enter_password(self,password):
        self.driver.find_element(self.password_textbox_id).clear()
        self.driver.find_element(*self.password_textbox_id).send_keys(password)


    def enter_login_btn(self,login):
        self.driver.find_element(*self.login_id).click()

