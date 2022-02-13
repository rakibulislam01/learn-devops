# [Tcpdump](https://danielmiessler.com/study/tcpdump/)
## Question and Answer 

---

### 1. Draw the IP Header with detailed bits.
IP Header is meta information at the beginning of an IP packet. It displays information such as the IP version, 
the packet’s length, the source, and the destination.

IPV4 header format is 20 to 60 bytes in length. It contains information need for routing and delivery. It consists of 
13 fields such as Version, Header length, total distance, identification, flags, checksum, source IP address, 
destination IP address. It provides essential data need to transmit the data. [For more information](https://www.guru99.com/ip-header.html)


![ip header](images/ip_header.png)

---

### 2. What is [tcpdump](https://www.tcpdump.org/manpages/tcpdump.1.html)?
`tcpdump` is the world’s premier network analysis tool—combining both power and simplicity into a single command-line interface.

---
### 3. How to get the HTTPS traffic? Share the command!

    tcpdump -nnSX port 443

This showed some HTTPS traffic, with a hex display visible on the right portion of the output (alas, it’s encrypted). 
Just remember—when in doubt, run the command above with the port you’re interested in, and you should be on your way.

---
### 4. For everything on an interface, what is the command?
    tcpdump -i eth0
---
### 5. Write the command to find Traffic by IP.
One of the most common queries, using host, you can see traffic that’s going to or from 1.1.1.1     

    tcpdump host 1.1.1.1
---

### 6. Share the filtering by Source and/or Destination?
If you only want to see traffic in one direction or the other, you can use src and dst.

    tcpdump src 1.1.1.1
    tcpdump dst 1.0.0.1
---
### 7. How to find Packets by Network, write the line.
To find packets going to or from a particular network or subnet, use the net option.

    tcpdump net 1.2.3.0/24

---
### 8. Using packet contents with Hex Output, write the command.
Hex output is useful when you want to see the content of the packets in question, and it’s often best used when you’re 
isolating a few candidates for closer scrutiny.

    tcpdump -c 1 -X icmp        # icmp (Internet Control Message Protocol)
---
### 9. To find a specific port traffic, write the command.
You can find specific port traffic by using the port option followed by the port number.

    tcpdump port 3389
    tcpdump src port 1025
---
### 10. Show Traffic of One Protocol command.
If you’re looking for one particular kind of traffic, you can use tcp, udp, icmp, and many others as well.

    tcpdump icmp
---
### 11. Write the command showing only IP6 Traffic.
You can also find all IP6 traffic using the protocol option.

    tcpdump ip6
---
### 12. Write the command for finding Traffic Using Port Ranges.
You can also use a range of ports to find traffic.

    tcpdump portrange 21-23

---
### 13. [What are PCAP (PEE-cap) files?](https://www.comparitech.com/net-admin/pcap-guide/)
PCAP files are data files created using a program. These files contain packet data of a network and are used to analyze 
the network characteristics. They also contribute to controlling the network traffic and determining network status. 
Using PCAP files, teams can attend to detect network problems and resolve data communications using various programs.
PCAP comes in a range of formats including `Libpcap`, `WinPcap`, and `PCAPng`.

---
### 14. How are PCAP files processed and why is it so?
 PCAP files can be processed by hundreds of different applications, including network analyzers, intrusion detection systems, and of course by tcpdump itself.
> [PCAP file process using python.](https://vnetman.github.io/pcap/python/pyshark/scapy/libpcap/2018/10/25/analyzing-packet-captures-with-python-part-1.html)
---

### 15. Which switch is used to write the PCAP file called capture_file?
Here we’re writing to a file called capture_file using the `-w switch`.

---

### 16. What is the command for reading / writing to capture a File?
    tcpdump port 80 -w capture_file     # PCAP writing command

    tcpdump -r capture_file     # PCAP reading command
---

### 17. Which switch is needed to read the PCAP files?

You can read PCAP files by using the `-r switch`. Note that you can use all the regular commands within tcpdump while 
reading in a file; you’re only limited by the fact that you can’t capture and process what doesn't exist in the file already.

---

### 18. What is the tcpdump command while reading in a file?

    tcpdump -r capture_file     # PCAP reading command
---
### 19. Which switch is used for the ethernet header?

    -XX     # Same as -X, but also shows the ethernet header.

---

### 20. What is Line-readable output? How is it notified?

    -l      # Line-readable output (for viewing as you save, or sending to other commands)
---

### 21. What does -q implify?

    -q      # Be less verbose (more quiet) with your output.

example:

    sudo tcpdump -q     # command
    
    # output
    tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
    listening on wlo1, link-type EN10MB (Ethernet), capture size 262144 bytes
    16:45:52.208958 IP cn-142-83.circlenetworkbd.com.443 > rakibul.38894: UDP, length 1250
    16:45:52.209232 IP cn-142-83.circlenetworkbd.com.443 > rakibul.38894: UDP, length 1250
    16:45:52.209505 IP cn-142-83.circlenetworkbd.com.443 > rakibul.38894: UDP, length 1250
    16:45:52.209780 IP cn-142-83.circlenetworkbd.com.443 > rakibul.38894: UDP, length 1250
    16:45:52.210056 IP cn-142-83.circlenetworkbd.com.443 > rakibul.38894: UDP, length 1250

---

### 22. What does this tweak: -t work?

    -t      # Give human-readable timestamp output.

---
### 23. What does -tttt show?

    -tttt       # Give maximally human-readable timestamp output.

---
### 24. To listen on the eth0 interface, which one is used?

    -i eth0     # Listen on the eth0 interface.

---
### 25. Purpose for -vv ?

    -vv     # Verbose output (more v’s gives more output).
---

### 26. Purpose for -c?

    -c      # Only get x number of packets and then stop.
    
example:

    sudo tcpdump -c 5       # command

    # output
    tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
    listening on wlo1, link-type EN10MB (Ethernet), capture size 262144 bytes
    16:59:07.492937 IP se-in-f136.1e100.net.443 > rakibul.53647: UDP, length 29
    16:59:07.493391 IP se-in-f136.1e100.net.443 > rakibul.53647: UDP, length 70
    16:59:07.493414 IP se-in-f136.1e100.net.443 > rakibul.53647: UDP, length 26
    16:59:07.493658 IP rakibul.53647 > se-in-f136.1e100.net.443: UDP, length 36
    16:59:07.495143 IP rakibul.44646 > ns1.dotinternetbd.com.domain: 7717+ [1au] PTR? 14.0.168.192.in-addr.arpa. (54)
    5 packets captured
    19 packets received by filter
    0 packets dropped by kernel

---
### 27. Why -s is used?

    -s      # Define the snaplength (size) of the capture in bytes. Use -s0 to get everything, 
            # unless you are intentionally capturing less. Maximu 65k+

    sudo tcpdump port 53 -s0        # command
    tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
    listening on wlo1, link-type EN10MB (Ethernet), capture size 262144 bytes
    17:19:19.185112 IP rakibul.33948 > 172.16.172.10.domain: 62184+ [1au] A? beacons.gcp.gvt2.com. (49)
    17:19:19.186418 IP rakibul.45396 > 172.16.172.10.domain: 29577+ [1au] PTR? 10.172.16.172.in-addr.arpa. (55)

---
### 28. What does -S, -e, -q, [-E](https://lists.freebsd.org/pipermail/freebsd-questions/2014-March/256538.html) implify?

    -S      # Print absolute sequence numbers.
    -e      # Get the ethernet header as well.
    -q      # Show less protocol information.
    -E      # Decrypt IPSEC traffic by providing an encryption key.

---
### 29. How to show the raw output view?

Use this combination to see verbose output, with no resolution of hostnames or port numbers, using absolute sequence 
numbers, and showing human-readable timestamps.

    tcpdump -ttnnvvS

---
### 30. If a specific IP and destined course are given then which tweak is used for?

Let’s find all traffic from 140.82.112.26 going to any host on port 53688.

    sudo tcpdump -nnvvS src 140.82.112.26 and dst port 53688

---

### 31. To pass from One Network to Another, the command?

Let’s look for all traffic coming from `192.168.x.x` and going to the `10.x or 172.16.x.x `networks, and we’re showing hex 
output with no hostname resolution and one level of extra verbosity.

    tcpdump -nvX src net 192.168.0.0/16 and dst net 10.0.0.0/8 or 172.16.0.0/16

---
### 32. If a Non ICMP Traffic Goes to a Specific IP, what should be the query?

This will show us all traffic going to 192.168.0.2 that is `not ICMP`.

    tcpdump dst 192.168.0.2 and src net and not icmp

---
### 33. If a host isn't on a specific port, what will be tweaked and commanded?

This will show us all traffic from a host that isn’t SSH traffic (assuming default port usage).
    
    tcpdump -vv src mars and not dst port 22

---
### 34. Why single quotes used?

when you’re building complex queries you might have to group your options using single quotes. Single quotes are used in 
order to tell tcpdump to ignore certain special characters—in this case below the “( )” brackets. This same technique 
can be used to group using other expressions such as host, port, net, etc.

    tcpdump 'src 10.0.2.4 and (dst port 3389 or 22)'

---
> The filters below find these various packets because `tcp[13]` looks at offset 13 in the TCP header, the number 
> represents the location within the byte, and the `!=0` means that the flag in question is set to 1, i.e. it’s on.

> Only the `PSH, RST, SYN, and FIN` flags are displayed in tcpdump‘s flag field output. `URGs and ACKs` are displayed, but 
> they are shown elsewhere in the output rather than in the flags field. 
### 35. How to isolate TCP [RST](https://ipwithease.com/tcp-rst-flag/) flags?
 
    tcpdump 'tcp[13] & 4!=0'
    tcpdump 'tcp[tcpflags] == tcp-rst'

---
### 36. To Isolate TCP SYN flags, which query is used?

    tcpdump 'tcp[13] & 2!=0'
    tcpdump 'tcp[tcpflags] == tcp-syn'

---
### 37. To Isolate packets that have both the SYN and ACK flags set, what shouldbe the command?

    tcpdump 'tcp[13]=18'

---
### 38. How to Isolate TCP [URG](https://packetlife.net/blog/2011/mar/2/tcp-flags-psh-and-urg/) flags?

    tcpdump 'tcp[13] & 32!=0'
    tcpdump 'tcp[tcpflags] == tcp-urg'

---
### 39. How to Isolate TCP ACK flags?

    tcpdump 'tcp[13] & 16!=0'
    tcpdump 'tcp[tcpflags] == tcp-ack'

---
### 40. Isolate TCP [PSH](https://packetlife.net/blog/2011/mar/2/tcp-flags-psh-and-urg/) flags?

    tcpdump 'tcp[13] & 8!=0'
    tcpdump 'tcp[tcpflags] == tcp-push'

---
### 41. Isolate TCP FIN flags.

    tcpdump 'tcp[13] & 1!=0'
    tcpdump 'tcp[tcpflags] == tcp-fin'

---
### 42. How is [grep](https://www.geeksforgeeks.org/grep-command-in-unixlinux/) used?

> tcpdump can output content in ASCII, you can use it to search for cleartext content using other command-line tools like `grep`.

> The -l switch lets you see the traffic as you’re capturing it, and helps when sending to commands like grep.
    
    tcpdump -vvAls0 | grep 'User-Agent:'

---
### 43. Command for Both SYN and RST?

    tcpdump 'tcp[13] = 6'

---
### 44. What to do for Cleartext GET Requests?

    tcpdump -vvAls0 | grep 'GET'

---
### 45. What to do to Find HTTP Host Headers?

    tcpdump -vvAls0 | grep 'Host:'

---
### 46. How to Find HTTP Cookies?

    tcpdump -vvAls0 | grep 'Set-Cookie|Host:|Cookie:'

---
### 47. The command line for Find SSH Connections?

This one works regardless of what port the connection comes in on, because it’s getting the banner response.

    tcpdump 'tcp[(tcp[12]>>2):4] = 0x5353482D'

---
### 48. How to Find DNS Traffic?

    tcpdump -vvAs0 port 53

---
### 49. Command for Find FTP Traffic.

    tcpdump -vvAs0 port ftp or ftp-data

---
### 50. Find [NTP](https://www.imperva.com/learn/ddos/ntp-amplification/) Traffic, what is the command?

    tcpdump -vvAs0 port 123

---
### 51. Command to Find Cleartext Passwords?

    tcpdump port http or port ftp or port smtp or port imap or port pop3 or port telnet -lA | egrep -i -B5 'pass=|pwd=|log=|login=|user=|username=|pw=|passw=|passwd= |password=|pass:|user:|username:|password:|login:|pass |user '

---
### 53. Describe Evil bit.

There’s a bit in the IP header that never gets set by legitimate applications, which we call the “Evil Bit”. Here’s a 
fun filter to find packets where it’s been toggled.

---
### 54. Write the fun filter to find packets where it’s been toggled.

Here’s a fun filter to find packets where it’s been toggled.
    
        tcpdump 'ip[6] & 128 != 0'

---


### References:

1. https://nanxiao.github.io/tcpdump-little-book/
2. https://www.youtube.com/watch?v=hWc-ddF5g1I
3. https://www.geeksforgeeks.org/grep-command-in-unixlinux/
4. https://www.youtube.com/watch?v=3uhA8bdz8gI
