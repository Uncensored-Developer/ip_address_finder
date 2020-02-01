class GetIPDetailsInteractor:

    def __init__(self, http_client=None):
        self.http_client = http_client

    def set_params(self, ip):
        self.ip = ip
        return self

    def execute(self):
        return self.http_client(self.ip)
