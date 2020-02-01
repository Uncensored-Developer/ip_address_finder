import time
from factories import create_cli_view


if __name__ == '__main__':
    print('*********** IP ADDRESS FINDER **********')
    cli_view = create_cli_view()
    start = time.time()
    result = cli_view.get()
    end = time.time()
    msg = ('IP ADDRESS: {ip} \n'
           'CONTINENT: {continent} \n'
           'COUNTRY: {country} \n'
           'STATE: {state} \n'
           'LONGITUDE: {long} \n'
           'LATITUDE: {lat} \n'
           'RESPONSE TIME: {time}s').format(ip=result.ip, continent=result.continent,
                                            country=result.country, state=result.state,
                                            long=result.longitude, lat=result.latitude,
                                            time=end - start)
    print(msg)
