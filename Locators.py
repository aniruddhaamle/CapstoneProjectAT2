class WebLocators:

    def __init__(self):
        self.userNameLocator = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input"
        self.passwordLocator = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input"
        self.loginButtonLocator = "//*[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']"
        self.profileIconLocator = "//*[@class='oxd-userdropdown-name']"
        self.logoutLocator = "//a[@class='oxd-userdropdown-link'][@href = '/web/index.php/auth/logout' ]"

        self.forgotPasswordLocator = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p"
        self.ForgotPwdUserNameLocator = "//*[@id='app']/div[1]/div[1]/div/form/div[1]/div/div[2]/input"
        self.ReesetPwdButtonLocator = "//*[@id='app']/div[1]/div[1]/div/form/div[2]/button[2]"
        self.passwordResetSuccessfullMessage = "//*[@id='app']/div[1]/div[1]/div/h6"


        self.userManagementLocator = "/html[1]/body[1]/div[1]/div[1]/div[1]/header[1]/div[2]/nav[1]/ul[1]/li[1]/span[1]"
        self.jobLocator =            "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span"
        self.organizationLocator =   "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[3]/span"
        self.QualificationsLocator = "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[4]/span"
        self.nationalitiesLocator =  "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[5]/a"
        self.corporateBrandingLocator ="//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[6]/a"
        self.configurationLocator =    "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[7]/span"

        self.adminLocator = "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span"
        self.PIMLocator = "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span"
        self.LeaveLocator = "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a/span"
        self.TimeLocator ="//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a/span"
        self.RecruitmentLocator ="//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a/span"
        self.MyInfoLocator ="//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a/span"
        self.PerformanceLocator ="//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a/span"
        self.DashboardLocator ="//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a/span"
        self.DirectoryLocator ="//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[9]/a/span"
        self.MaintenanceLocator ="//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[10]/a/span"
        self.ClaimLocator ="//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[11]/a/span"
        self.BuzzLocator = "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[12]/a/span"


