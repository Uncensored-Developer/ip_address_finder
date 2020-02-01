# ip-address-finder
Displays the continent, country, state, longitude and latitude of an ip address

To run this program you need to have memcached installed, you can check out the installation process for your OS
[here](https://realpython.com/python-memcache-efficient-caching/) .
Before running this program make sure memcache service is running and installing pymemcache.
Do this by running
```
$ memcached
$ pip install pymemcache
```
To run the program:
```
$ python find_ip_address.py <ip_address>
```
For example:
```
$ python find_ip_address.py 196.378.23.675
```
