from selenium.webdriver.common.by import By


class CreateChannel:

    def __init__(self, driver):
        self.driver = driver

    createChanelLink = (By.XPATH, "//*[contains(text(),'New Channel')]")
    channelName = (By.ID, "RecipientName")
    companyName = (By.ID, "CompanyName")
    emailAddress = (By.ID, "Emailaddress")
    tagLine = (By.ID, "TagLine")
    createButtonPopUpScreen = (By.XPATH, "//button[@class='btn btn-secondary']")
    linkAddedSuccessfullyMSG = (By.XPATH, "//span[text()='martina hingis']")

    def createLink(self):
        return self.driver.find_element(*CreateChannel.createChanelLink)

    def enterChannelName(self):
        return self.driver.find_element(*CreateChannel.channelName)

    def enterCompanyName(self):
        return self.driver.find_element(*CreateChannel.companyName)

    def enterEmailAddress(self):
        return self.driver.find_element(*CreateChannel.emailAddress)

    def enterTagLine(self):
        return self.driver.find_element(*CreateChannel.tagLine)

    def clickOnCreateButton(self):
        return self.driver.find_element(*CreateChannel.createButtonPopUpScreen)

    def verifyMsg(self):
        return self.driver.find_element(*CreateChannel.linkAddedSuccessfullyMSG)


