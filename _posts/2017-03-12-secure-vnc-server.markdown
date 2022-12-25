---
title: Secure VNC server
layout: post
date: '2017-03-12 11:05:00 +0800'
categories: platform
excerpt: Secure VNC server with SSH and VPN
---

VNC is a powerful remote administrative tool that provides Remote Desktop access to headless servers. It is particularly useful when certain applications on the server require a GUI environment (including [Interactive Brokers softwares](https://www.interactivebrokers.com.hk/en/index.php?f=1325)). However VNC is known for its lack of security for remote access. Attackers scan for common ports looking for weak passwords.

Taking a commonly used free VNC server [TightVNC](http://www.tightvnc.com/) as example, it authenticates connection against its passphrase in ```~/.vnc/passwd```, and when the number of unauthenticated connection attempts exceeds the threshold, the server may complain "too many authentication failures". When this happens, it may also block normal user from logging in. See discussion on this on [this thread](https://superuser.com/questions/437354/vncserver-too-many-security-failures) and [this thread](https://superuser.com/questions/438024/vnc-authentication-failure).

## Securing via SSH Tunneling ##

A common suggestion is to use SSH tunneling, i.e. to have VNC server to listen only to localhost thus not opening its port to the public. Instead, SSH will bind to a local port and pass all the data received from the port to the server's SSH port and then forwarded onwards to server's VNC port.

In order the do this, use the following command on Unix-like systems (you may use PuTTY on Windows for this):

```console
ssh [username]@[VNC-server-address] -L [local-port]:localhost:[VNC-server-port] -N
```

__-L__ here specifies the forwarding option. __-N__ is used as we do not need to execute any command but only to forward ports.

After SSH forwarding has been established, launch your preferred VNC client application and this time connects to __localhost:[local-port]__. Note you will still need to enter the VNC password as the forwarding merely forwards the connection.

If you often work on mobile you may also use SSH apps like Termius in iOS for forwarding.

## Securing via VPN ##

An alternative to SSH is to set up VPN connection to your server and to allow only connection to VNC from the virtual local network over VPN.

An easy way to set up an IPSec VPN server is to use [these scripts](https://github.com/hwdsl2/setup-ipsec-vpn). You may then customize the VPN login and password in ```/etc/ppp/chap-secrets``` and the PPTP IP address range in ```/etc/pptpd.conf```.

Once the above is done, try connecting via VPN and see if an IP has been assigned properly over ppp0. By default you may be assigned with an IP in a range of 192.168.1.1 - 10. With this done, you may then go ahead and create rules to lock down external connections to VNC. You may also want to log the activity.

To do this, execute first to create a new chain named __LOG_DROP__ for logging and dropping:

```console
iptables -N LOG_DROP
iptables -A LOG_DROP -j LOG --log-prefix "[your log message]"
iptables -A LOG_DROP -j DROP
```

Then explicitly allow local connection to port 5901 (change depending on the actual VNC port) and drop the rest:

```console
iptables -A INPUT -s 127.0.0.0/8 -p tcp -m tcp --dport 5901 -j ACCEPT
iptables -A INPUT -s 192.168.0.0/16 -p tcp -m tcp --dport 5901 -j ACCEPT
iptables -A INPUT -p tcp -m tcp --dport 5901 -j LOG_AND_DROP
```

You will then be able to find the log entries in `/var/log/syslog`.
