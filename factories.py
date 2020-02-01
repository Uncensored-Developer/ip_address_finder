from repositories.memcache_db import MemcacheRepo
from interactors.memcache_db_interactor import SaveToMemcacheInteracor, FetchFromMemcacheInteractor
from interactors.http_requests_interactors import GetIPDetailsInteractor
from http_req.request_layer import get_ip_detials
from views.cli import CLIView


def create_memcache_repo():
    return MemcacheRepo()


def create_save_to_memcache_interactor():
    return SaveToMemcacheInteracor(memcache_repo=create_memcache_repo())


def create_fetch_from_memcache_interactor():
    return FetchFromMemcacheInteractor(memcache_repo=create_memcache_repo())


def create_get_ip_detail_interactor():
    return GetIPDetailsInteractor(http_client=get_ip_detials)


def create_cli_view():
    return CLIView(
        save_to_repo_interactor=create_save_to_memcache_interactor(),
        fetch_from_repo_interactor=create_fetch_from_memcache_interactor(),
        get_ip_details_interactor=create_get_ip_detail_interactor()
    )
