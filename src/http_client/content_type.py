class ContentTypeHelper:
    # Helper class providing content type configuration methods

    def use_json(self):
        self.content_type = "application/json"

    def use_text(self):
        self.content_type = "text/plain"

    def use_xml(self):
        self.content_type = "application/xml"

    def use_urlencoded(self):
        self.content_type = "application/x-www-form-urlencoded"
