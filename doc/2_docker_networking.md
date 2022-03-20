# Docker Networking

### SSH certificate

---
An SSH key is an access credential for the SSH (secure shell) network protocol. This authenticated and encrypted secure 
network protocol is used for remote communication between machines on an unsecured open network. SSH is used for remote 
file transfer, network management, and remote operating system access.

### Symmetric encryption

---
Symmetric encryption aka symmetric key cryptography uses one single key to encrypt and decrypt data. You have to share 
this key with the recipient. Let’s say you want to say I love you Mom, you would write your email, then set a secret key 
to encrypt it. When mom receives the message she would enter the secret key to decrypt the email.

### Asymmetric encryption

---
Asymmetric encryption is a type of encryption that uses two separates yet mathematically related keys to encrypt and 
decrypt data. The public key encrypts data while its corresponding private key decrypts it. 

### Deploy new instance

---
After deploying a new instance connect it using ssh.

Run the following command:

    sudo apt update

    # For docker install
    sudo apt install docker.io

### Docker:

---

**Docker**
> Docker is an OS-level virtualization software platform that enables developers and IT administrators to creat, deploy 
> and run applications in a docker container with all their dependencies.

**Docker image:** 
>A Docker image is a read-only template that contains a set of instructions for creating a container 
that can run on the Docker platform. It provides a convenient way to package up applications and preconfigured server 
environments, which you can use for your own private use or share publicly with other Docker users.

**Docker container:** 
> A Docker container is an open source software development platform. Its main benefit is to package applications in 
containers, allowing them to be portable to any system running a Linux or Windows operating system (OS). A Windows 
machine can run Linux containers by using a virtual machine (VM) (`Isolation environment`).

Running nginx container:

    sudo docker run nginx       # command
    
    telnet 13.126.157.69 22     # for checking public access.
    
**Port mapping:**

Port forwarding, sometimes called port mapping, allows computers or services in private networks to connect 
over the internet with other public or private computers or services.

**Install net tools:**

    sudo apt install net-tools      # install network tools

**Show instance network interface:**

    sudo ip addr        # ip addr or ifconfig       # command
    
    # output
    .....
    3: docker0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default 
        link/ether 02:42:45:f4:3a:31 brd ff:ff:ff:ff:ff:ff
        inet 172.17.0.1/16 brd 172.17.255.255 scope global docker0
           valid_lft forever preferred_lft forever
        inet6 fe80::42:45ff:fef4:3a31/64 scope link 
           valid_lft forever preferred_lft forever

we can see new network bridge is created `docker0`. Bridge also a switch. 
Docker containers are attached with the `docker0` switch / bridge to sending and receiving packets.
Docker container connect `docker0` bridge using virtual ethernet `veth`.

Docker container ip address range: `172.17.0.1/16`. Docker container ip address prefix start with `172.17`

**Docker networks:**
    
    sudo docker network ls      # command

    # output
    NETWORK ID     NAME      DRIVER    SCOPE
    6ca8451a6311   bridge    bridge    local
    e32220144736   host      host      local
    5ac4f8cd3d3d   none      null      local

**Inspect docker network:**

    sudo docker inspect network 6ca8451a6311        # command

    Output:
    [
        {
            "Name": "bridge",
            "Id": "6ca8451a63110e38e0ba38e227eab4f163b5f2deafad5351c51c4de19f4edb79",
            "Created": "2022-02-06T10:20:16.335247498Z",
            "Scope": "local",
            "Driver": "bridge",
            "EnableIPv6": false,
            "IPAM": {
                "Driver": "default",
                "Options": null,
                "Config": [
                    {
                        "Subnet": "172.17.0.0/16"
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
                "8c489333419183e74483397453c3676ac5c41354692880298f4b834cacc60a12": {
                    "Name": "funny_babbage",
                    "EndpointID": "faf80bd75abba7c6f4a1d5aae4c8d5480f9d23a44e2c4400b1d1461c7b36e4bf",
                    "MacAddress": "02:42:ac:11:00:02",
                    "IPv4Address": "172.17.0.2/16",
                    "IPv6Address": ""
                }
            },
            "Options": {
                "com.docker.network.bridge.default_bridge": "true",
                "com.docker.network.bridge.enable_icc": "true",
                "com.docker.network.bridge.enable_ip_masquerade": "true",
                "com.docker.network.bridge.host_binding_ipv4": "0.0.0.0",
                "com.docker.network.bridge.name": "docker0",
                "com.docker.network.driver.mtu": "1500"
            },
            "Labels": {}
        }
    ]

Now we can see our containers IP address.

    ping 172.17.0.2     # ping nginx server.
    
    PING 172.17.0.2 (172.17.0.2) 56(84) bytes of data.
    64 bytes from 172.17.0.2: icmp_seq=1 ttl=64 time=0.039 ms
    64 bytes from 172.17.0.2: icmp_seq=2 ttl=64 time=0.050 ms

Instance routing table:

    route       # command
    
    Kernel IP routing table
    Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
    default         ip-172-31-0-1.a 0.0.0.0         UG    100    0        0 eth0
    172.17.0.0      0.0.0.0         255.255.0.0     U     0      0        0 docker0
    172.31.0.0      0.0.0.0         255.255.240.0   U     0      0        0 eth0
    ip-172-31-0-1.a 0.0.0.0         255.255.255.255 UH    100    0        0 eth0

If any requests ip destination address prefix start with `172.17` it's connect to `docker0` bridge. Then `docker0` read 
the IP address and send the destination container.

**All running container:**

    sudo docker ps      # command

    # output
    CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS     NAMES
    8c4893334191   nginx     "/docker-entrypoint.…"   52 minutes ago   Up 52 minutes   80/tcp    funny_babbage

**Connect docker container terminal:**

    sudo docker exec -it 8c489 sh       # command

    # Container sh command
    apt update
    apt install net-tools
    route
    apt install telnet
    ifconfig
    apt install tcpdump
    apt install iputils-ping
    arp     # show arp table
    apt install traceroute

Using `ifconfig` we can see the container interfaces.

    # ifconfig
    eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
            inet 172.17.0.2  netmask 255.255.0.0  broadcast 172.17.255.255
            ether 02:42:ac:11:00:02  txqueuelen 0  (Ethernet)
            RX packets 685  bytes 8904702 (8.4 MiB)
            RX errors 0  dropped 0  overruns 0  frame 0
            TX packets 488  bytes 35511 (34.6 KiB)
            TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
    
    lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
            inet 127.0.0.1  netmask 255.0.0.0
            loop  txqueuelen 1000  (Local Loopback)
            RX packets 0  bytes 0 (0.0 B)
            RX errors 0  dropped 0  overruns 0  frame 0
            TX packets 0  bytes 0 (0.0 B)
            TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

The `nginx` container use eth0. `eth0` ip address `172.17.0.2`

### Ingress Packet flow

Now we check our incoming packets using `tcpdump`. First `ping` nginx server.

    ping 172.17.0.2     # command

    tcpdump -i eth0     # command
    
    # output
    tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
    listening on eth0, link-type EN10MB (Ethernet), snapshot length 262144 bytes
    11:32:25.644366 IP ip-172-17-0-1.ap-south-1.compute.internal > 8c4893334191: ICMP echo request, id 3, seq 19, length 64
    11:32:25.644384 IP 8c4893334191 > ip-172-17-0-1.ap-south-1.compute.internal: ICMP echo reply, id 3, seq 19, length 64
    11:32:25.724811 IP 8c4893334191.40017 > ip-172-31-0-2.ap-south-1.compute.internal.domain: 26897+ PTR? 1.0.17.172.in-addr.arpa. (41)
    11:32:25.726469 IP ip-172-31-0-2.ap-south-1.compute.internal.domain > 8c4893334191.40017: 26897 1/0/0 PTR ip-172-17-0-1.ap-south-1.compute.internal. (96)

> Instance sending packets using default gateway (ip-172-17-0-1.ap-south-1.compute.internal). 

### Egress Packet Flow

**Ping outside from docker container:**

    # ping 8.8.8.8
    PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
    64 bytes from 8.8.8.8: icmp_seq=1 ttl=109 time=1.81 ms
    64 bytes from 8.8.8.8: icmp_seq=2 ttl=109 time=1.86 ms

**Flow:**

    container network interface -> docker0 -> host network interface eth0(default gateway | host root namespace) -> outside world

Now we see the packet travel route using `taraceroute` (trace the path's data packets take from 
their source to their destinations)

    traceroute 8.8.8.8      # command

    # output
    traceroute to 8.8.8.8 (8.8.8.8), 30 hops max, 60 byte packets
     1  ip-172-17-0-1.ap-south-1.compute.internal (172.17.0.1)  0.040 ms  0.024 ms  0.008 ms
     2  ec2-52-66-0-243.ap-south-1.compute.amazonaws.com (52.66.0.243)  7.333 ms ec2-52-66-0-239.ap-south-1.compute.amazonaws.com (52.66.0.239)  3.180 ms ec2-52-66-0-247.ap-south-1.compute.amazonaws.com (52.66.0.247)  7.492 ms
     3  100.65.19.176 (100.65.19.176)  2.990 ms *  2.940 ms
     4  * * 100.66.8.150 (100.66.8.150)  3.380 ms
     5  100.66.10.198 (100.66.10.198)  4.679 ms 100.66.11.196 (100.66.11.196)  4.429 ms 100.66.11.132 (100.66.11.132)  0.627 ms
     6  100.66.6.5 (100.66.6.5)  6.714 ms 100.66.7.227 (100.66.7.227)  7.668 ms *
     7  100.66.4.85 (100.66.4.85)  5.850 ms 100.66.4.113 (100.66.4.113)  6.813 ms 100.66.4.41 (100.66.4.41)  5.880 ms
     8  100.65.10.65 (100.65.10.65)  0.387 ms 100.65.8.65 (100.65.8.65)  0.365 ms 100.65.10.33 (100.65.10.33)  1.397 ms
     9  99.83.76.141 (99.83.76.141)  1.657 ms 52.95.65.144 (52.95.65.144)  1.564 ms 99.83.76.115 (99.83.76.115)  2.361 ms
    10  99.83.76.100 (99.83.76.100)  2.481 ms 52.95.66.108 (52.95.66.108)  1.782 ms 99.83.76.132 (99.83.76.132)  2.859 ms
    11  52.95.66.71 (52.95.66.71)  1.519 ms 52.95.66.183 (52.95.66.183)  1.597 ms 52.95.66.139 (52.95.66.139)  1.649 ms
    12  99.82.180.91 (99.82.180.91)  1.790 ms 99.82.178.53 (99.82.178.53)  1.830 ms  1.814 ms
    13  * * *
    14  dns.google (8.8.8.8)  1.720 ms  2.132 ms  1.687 ms
    # 

### Why ip address changed for outside request from container.

---
.....

###  Veth pair:

---
The VETH (virtual Ethernet) device is a local Ethernet tunnel. Devices are created in pairs, as shown in the diagram 
below. Packets transmitted on one device in the pair are immediately received on the other device. When either device is
down, the link state of the pair is down.

<img alt="" src="images/veth.png">

### Nginx:

---
Nginx uses.
1. Reverse proxy.
2. Load balancer.
3. Web server.

### Load balancer:

---
1. **Layer 4**: 
Layer 4 load balancing, operating at the transport level, manages traffic based on network information such as 
application ports and protocols without visibility into the actual content of messages. This is an effective approach 
for simple packet-level load balancing.

2. **Layer 7**: 
Layer 7 load balancing operates at the application level, using protocols such as HTTP and SMTP to make decisions based 
on the actual content of each message. Instead of merely forwarding traffic unread, a layer 7 load balancer terminates 
network traffic, performs decryption as needed, inspects messages, makes content-based routing decisions, initiates a 
new TCP connection to the appropriate upstream server, and writes the request to the server.

### MTU (Maximum transmission unit):

---
The maximum transmission unit (MTU) setting determines the largest packet size that can be transmitted through your 
network. MTU is configured on the veth attached to each workload, and tunnel devices (if you enable IP in IP, VXLAN, 
or WireGuard).