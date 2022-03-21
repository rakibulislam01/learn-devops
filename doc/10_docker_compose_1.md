## **Question:**
### Why two containers  can't communicate using container names in the docker default network?
[Docker networking](https://docs.docker.com/network/network-tutorial-standalone/#use-user-defined-bridge-networks)
> There is a term called `automatic service discovery` that isn't present in the docker default network. That's why it's not working.

## **Solution:** 
**You need to create custom network.** 

### Run two container webapp using docker.

    sudo apt install docker.io
    sudo docker ps
    sudo docker image ls
    sudo docker run -d --name=wbs1 nginx
    sudo docker run -d --name=wbs2 nginx
    sudo docker ps
    docker inspect wbs1     # checking container ip
                            # ip 172.17.0.2
    docker inspect wbs2     # checking container ip
                            # ip 172.17.0.3


### Container 1 sh access (wbs1):

    docker exec -it wbs1 sh
    apt update
    apt install net-tools
    ifconfig
    curl 172.17.0.3     # Working
    curl wbs2       # not working
                    # curl: (6) Could not resolve host: wbs2

### Create docker network:

    docker network ls
    docker network create wbs

### Connect container with new network:

    docker network connect wbs wbs1
    docker network connect wbs wbs2

### Inspect wbs network:
    
    
    docker network inspect wbs

    # Output:

    [
        {
            "Name": "wbs",
            "Id": "717b2e5fe7b976db324ca97dcbb45363c9c42c9d08767ddcc1ba001e72268c49",
            "Created": "2022-03-18T19:38:48.739777378Z",
            "Scope": "local",
            "Driver": "bridge",
            "EnableIPv6": false,
            "IPAM": {
                "Driver": "default",
                "Options": {},
                "Config": [
                    {
                        "Subnet": "172.18.0.0/16",
                        "Gateway": "172.18.0.1"
                    }
                ]
            },
            "Internal": false,
            "Attachable": false,
            "Ingress": false,
            "ConfigFrom": {
                "Network": ""
            },
            "ConfigOnly": false,
            "Containers": {
                "694f8dc05181107f07265f2de5db97f742aed229130afbdd176ba447159140a3": {
                    "Name": "wbs1",
                    "EndpointID": "ce52b9d4695c32d646cbd194e31384fd35c9ff91c91d2dae296a4de6f8ee6966",
                    "MacAddress": "02:42:ac:12:00:02",
                    "IPv4Address": "172.18.0.2/16",
                    "IPv6Address": ""
                },
                "f9f53ca4c20811ea1ae1c25d661c406e15e98ae3cee1e2e209acd8cffe69ae6f": {
                    "Name": "wbs2",
                    "EndpointID": "f0526b4fa493fec07d9d4cb8d32f6f173cb16b1d6cacb9441c1a6f1ea98141c5",
                    "MacAddress": "02:42:ac:12:00:03",
                    "IPv4Address": "172.18.0.3/16",
                    "IPv6Address": ""
                }
            },
            "Options": {},
            "Labels": {}
        }
    ]

### inspect web app:

    docker inspect wbs1

### Curl webserver 1: [docker dns](https://docs.docker.com/config/containers/container-networking/#dns-services)

    curl wbs2       # from wbs1

Now it's working.

### Nslookup:
`nslookup` is a network administration command-line tool for querying the Domain Name System to obtain the mapping between 
domain name and IP address, or other DNS records.

    apt install dnsutils        # install nslookup
    
    nslookup wbs1       # command
    Server:		127.0.0.11
    Address:	127.0.0.11#53
    
    Non-authoritative answer:
    Name:	webserver1
    Address: 172.19.0.2
