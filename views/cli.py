import argparse


class CLIView:

    def __init__(
            self, save_to_repo_interactor=None, fetch_from_repo_interactor=None,
            get_ip_details_interactor=None
    ):
        self.save_to_repo_interactor = save_to_repo_interactor
        self.fetch_from_repo_interactor = fetch_from_repo_interactor
        self.get_ip_details_interactor = get_ip_details_interactor
        parser = argparse.ArgumentParser()
        parser.add_argument("ip", help="The ip address you want to find.")
        self.__args = parser.parse_args()

    def get(self, *args, **kwargs):
        # check if ip details is already in db
        result = self.fetch_from_repo_interactor.set_params(self.__args.ip).execute()
        if not result:
            # fetch ip details via http_req request
            return self.get_ip_details_interactor.set_params(self.__args.ip).execute()
        return result
