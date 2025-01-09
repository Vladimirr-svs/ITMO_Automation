class SidebarButton:
    def __init__(self, text, button_type="Кнопка", locator=""):

        self.text = text
        self.button_type = button_type
        self.locator = locator

    def click(self):
        return f"Клик по кнопке {self.text}"


text_box_button = SidebarButton("Text Box")
check_box_button = SidebarButton("Check Box")
radio_button = SidebarButton("Radio Button")
web_tables_button = SidebarButton("Web Tables")
buttons_button = SidebarButton("Buttons")
links_button = SidebarButton("Links")
broken_links_button = SidebarButton("Broken Links - Images")
upload_download_button = SidebarButton("Upload and Download")
dynamic_properties_button = SidebarButton("Dynamic Properties")


buttons = [
    text_box_button, check_box_button, radio_button, web_tables_button,
    buttons_button, links_button, broken_links_button, upload_download_button,
    dynamic_properties_button
]


print("Text Buttons:")
for button in buttons:
    print(button.text)

print("Click Results:")
for button in buttons:
    print(button.click())