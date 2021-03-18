The purpose of this list is to track and compare tunneling solutions. This is
primarily targeted toward self-hosters and developers who want to do things
like exposing a local webserver via a public domain name, with automatic HTTPS,
even if behind a NAT or other restricted network.

# The dream

I started this list because I'm looking for a simple tool/service that does the
following:

* Allows me to register a domain name and automatically points the records at
  the server running the tunnels.
* Automatically sets up and manages HTTPS certificates (apex and subdomains)
  for the domain.
* Provides a client tool that tunnels HTTP/TCP connections through the server
  without requiring root on the client.
* Provides a simple GUI interface to allow me to map X domain/subdomain to Y port
  on Z client, and proxy all connections to that domain.

So far I haven't found a tool that does all of this. In particular, while some
of them can do automatic certs through Lets's Encrypt, none of them integrate
the domain registration and DNS management.

**UPDATE:** Since starting this list I found most of the other solutions to be
either too complicated or making different tradeoffs than I would want. I have
two of my own projects in this space:

1. [SirTunnel](https://github.com/anderspitman/SirTunnel) is I believe the
minimal way of getting auto-HTTPS tunneled through to a private network.
It's just a 50-line Python script that leverages Caddy and OpenSSH, but you
need to understand how it works to use it. This one is good for developers.

2. [boringproxy](https://boringproxy.io/) is my take on a comprehensive tunnel
proxy solution. It's in beta but currently solves almost everything I want except
auto DNS management, and that's planned. Once the server is running this is a very
easy tool to use, and is targeted at non-developers.


# Open source (at least with a reasonably permissive license)

* [frp](https://github.com/fatedier/frp) [![frp github stars badge](https://img.shields.io/github/stars/fatedier/frp?style=flat)](https://github.com/fatedier/frp/stargazers) - Seems to be a pretty comprehensive open alternative to ngrok.
* [ngrok 1.0](https://github.com/inconshreveable/ngrok) [![ngrok 1.0 github stars badge](https://img.shields.io/github/stars/inconshreveable/ngrok?style=flat)](https://github.com/inconshreveable/ngrok/stargazers) - Original version of ngrok. No longer developed in favor of the commercial 2.0 version.
* [localtunnel](https://github.com/localtunnel) [![localtunnel github stars badge](https://img.shields.io/github/stars/localtunnel/localtunnel?style=flat)](https://github.com/localtunnel/localtunnel/stargazers) - Written in node. Popular suggestion.
* [inlets](https://github.com/inlets) [![inlets github stars badge](https://img.shields.io/github/stars/inlets/inlets?style=flat)](https://github.com/inlets/inlets/stargazers) - Open source ngrok alternative. Has pro option.
* [sshuttle](https://github.com/sshuttle/sshuttle) [![sshuttle github stars badge](https://img.shields.io/github/stars/sshuttle/sshuttle?style=flat)](https://github.com/sshuttle/sshuttle/stargazers) - Open source project originally from one of the founders of Tailscale. Server doesn't require root; client does. Explicitly designed to avoid TCP-over-TCP issues.
* [ZeroTier](https://www.zerotier.com/) - [![zerotier github stars badge](https://img.shields.io/github/stars/zerotier/ZeroTierOne?style=flat)](https://github.com/zerotier/ZeroTierOne/stargazers) Layer 2 overlay network.
* [chisel](https://github.com/jpillora/chisel) [![chisel github stars badge](https://img.shields.io/github/stars/jpillora/chisel?style=flat)](https://github.com/jpillora/chisel/stargazers) - SSH under the hood, but still uses a custom client binary. Supports auto certs from LetsEncrypt.
* [expose](https://github.com/beyondcode/expose) [![expose github stars badge](https://img.shields.io/github/stars/beyondcode/expose?style=flat)](https://github.com/beyondcode/expose/stargazers) - ngrok alternative written in PHP.
* [Pritunl](https://pritunl.com/) [![pritunl github stars badge](https://img.shields.io/github/stars/pritunl/pritunl?style=flat)](https://github.com/pritunl/pritunl/stargazers) - Seems quite comprehensive and complicated. OpenVPN, WireGuard, and IPSec support.
* [teleconsole](https://www.teleconsole.com/) [![teleconsole github stars badge](https://img.shields.io/github/stars/gravitational/teleconsole?style=flat)](https://github.com/gravitational/teleconsole/stargazers) - SSH-based, but uses special client script. Focused on forwarding SSH console sessions, but can also forward ports.
* [go-http-tunnel](https://github.com/mmatczuk/go-http-tunnel) [![go-http-tunnel github stars badge](https://img.shields.io/github/stars/mmatczuk/go-http-tunnel?style=flat)](https://github.com/mmatczuk/go-http-tunnel/stargazers) - Uses a single HTTP/2 connection for muxing. Need to manually generate certs for server and clients.
* [sish](https://github.com/antoniomika/sish) [![sish github stars badge](https://img.shields.io/github/stars/antoniomika/sish?style=flat)](https://github.com/antoniomika/sish/stargazers) - Open source ngrok/serveo alternative. SSH-based but uses a custom server written in Go. Supports WebSocket tunneling.
* [tunnelto](https://tunnelto.dev/) [![tunnelto github stars badge](https://img.shields.io/github/stars/agrinman/tunnelto?style=flat)](https://github.com/agrinman/tunnelto/stargazers) - Open core (MIT). Written in Rust.
* [wstunnel](https://github.com/erebe/wstunnel) [![wstunnel github stars badge](https://img.shields.io/github/stars/erebe/wstunnel?style=flat)](https://github.com/erebe/wstunnel/stargazers) - Proxies over WebSockets. Focus on proxying from behind networks that block certain protocols. Written in Haskell with executables provided.
* [PageKite](https://pagekite.net/) [![pagekite github stars badge](https://img.shields.io/github/stars/pagekite/PyPagekite?style=flat)](https://github.com/pagekite/PyPagekite/stargazers) - Comprehensive open source solution with hosted options. 
* [Crowbar](https://github.com/q3k/crowbar) [![crowbar github stars badge](https://img.shields.io/github/stars/q3k/crowbar?style=flat)](https://github.com/q3k/crowbar/stargazers) - Tunnels TCP connections over HTTP GET and POST requests. 
* [tunneller](https://github.com/skx/tunneller) [![tunneller github stars badge](https://img.shields.io/github/stars/skx/tunneller?style=flat)](https://github.com/skx/tunneller/stargazers) - Open source. Written in Go.
* [jprq](https://github.com/azimjohn/jprq) [![jprq github stars badge](https://img.shields.io/github/stars/azimjohn/jprq?style=flat)](https://github.com/azimjohn/jprq/stargazers) - Proxies over WebSockets. Written in Python.
* [boringproxy](https://boringproxy.io/) [![boringproxy github stars badge](https://img.shields.io/github/stars/boringproxy/boringproxy?style=flat)](https://github.com/boringproxy/boringproxy/stargazers) - Designed to be very easy to use. No config files. Clients can be remote-controlled through a simple WebUI and/or REST API on the server.
* [docker-tunnel](https://github.com/vitobotta/docker-tunnel) [![docker-tunnel github stars badge](https://img.shields.io/github/stars/vitobotta/docker-tunnel?style=flat)](https://github.com/vitobotta/docker-tunnel/stargazers) - Simple Docker-based nginx+SSH solution.
* [pgrok](https://www.proxy.jetzt/) [![pgrok github stars badge](https://img.shields.io/github/stars/jerson/pgrok?style=flat)](https://github.com/jerson/pgrok/stargazers) - Fork of ngrok 1.0, with more recent commits.
* [remotemoe](https://github.com/fasmide/remotemoe) [![remotemoe github stars badge](https://img.shields.io/github/stars/fasmide/remotemoe?style=flat)](https://github.com/fasmide/remotemoe/stargazers) - SSH-based, with custom golang server. Does some cool unique things. Instead of just plain tunnels, it drops you into a basic CLI UI that offers several useful commands interactively, such as adding a custom hostname. Also allows end-to-end encryption for both HTTPS and upstream SSH. Doesn't appear to offer non-e2e HTTPS, ie no auto Let's Encrypt support.
* [SirTunnel](https://github.com/anderspitman/SirTunnel) [![SirTunnel github stars badge](https://img.shields.io/github/stars/anderspitman/SirTunnel?style=flat)](https://github.com/anderspitman/SirTunnel/stargazers) - Minimal, self-hosted, 0-config alternative to ngrok. Similar to sish but leverages Caddy+OpenSSH rather than custom server code.
* [holepunch.io](https://holepunch.io) [![holepunch github stars badge](https://img.shields.io/github/stars/CypherpunkArmory/holepunch?style=flat)](https://github.com/CypherpunkArmory/holepunch/stargazers) - Has nice hosted solution. Uses SSH for muxing.
* [StaqLab Tunnel](https://tunnel.staqlab.com/) [![staqlab github stars badge](https://img.shields.io/github/stars/abhishekq61/tunnel-client?style=flat)](https://github.com/abhishekq61/tunnel-client/stargazers) - SSH-based. Client is open source. Server doesn't appear to be.
* [tnnlink](https://github.com/LiljebergXYZ/tnnlink) [![tnnlink github stars badge](https://img.shields.io/github/stars/LiljebergXYZ/tnnlink?style=flat)](https://github.com/LiljebergXYZ/tnnlink/stargazers) - SSH-based. Golang. Not maintained.
* [Telebit](https://telebit.cloud/) - Written in JS. [Code](https://git.coolaj86.com/coolaj86/telebit.js).
* SSH-J.com (no website, `ssh ssh-j.com`) - Public SSH Jump & Port Forwarding server. No software, no registration, just an anonymous SSH server for forwarding. Users are encouraged to use it for SSH exposure only, to preserve end-to-end encryption. No public ports, only in-SSH connectivity.

# Commercial/Closed source

* [ngrok 2.0](https://ngrok.com/) - Probably the gold standard and most popular. Closed source. Lots of features, including TLS and TCP tunnels. Doesn't require root to run client.
* [Tailscale](https://www.tailscale.com/) [![tailscale github stars badge](https://img.shields.io/github/stars/tailscale/tailscale?style=flat)](https://github.com/tailscale/tailscale/stargazers) - Built on WireGuard. Easy to use. Doesn't include an HTTPS proxy on the public side, but could be combined with nginx/Caddy/etc. Client [code](https://github.com/tailscale) available with a BSD3 license + separate patents file.
* [Loophole](https://loophole.cloud/) - Offers end-to-end TLS encryption with the client automatically getting certs from Let's Encrypt. QR codes for URL sharing.
* [CloudFlare Argo Tunnel](https://www.cloudflare.com/products/argo-tunnel/) - [Free usage](https://blog.cloudflare.com/a-free-argo-tunnel-for-your-next-project/#how-can-i-use-the-free-version) available. $5/mo + $0.1/GB. Integrates with Argo smart routing. Client source code is [available](https://github.com/cloudflare/cloudflared).
* [localhost.run](https://localhost.run/) - Simple hosted SSH option. Supports custom domains for a cost.
* [Packetriot](https://packetriot.com) - Comprehensive alternative to ngrok.  HTTP Inspector, Let's Encrypt integration, doesn't require root and Linux repos for apt, yum and dnf.  Enterprise licenses and self-hosted option.
* [Lynk](https://lynk.sh/) - Advertises itself as a cheaper, faster, self-hostable (but not open source) alternative to ngrok. [Blog post](https://medium.com/@shivanshvij/building-a-better-ngrok-dbc104754822).
* [Hoppy](https://hoppy.network/) - WireGuard-based. Provides static IPv4 and IPv6 addresses for your machines, which is a simple and useful level of abstraction. Targeted towards self-hosters and people behind NATs.
* [gw.run](https://gw.run/) - Specifically focusing on securely exposing internal web apps to a group of people; not for publicly facing apps. Share access via email address then allow users to log in with common login providers like Google.
* [KubeSail](https://kubesail.com/) - Company offering tunneling, dynamic DNS, and other services for self-hosting with Kubernetes.
* [serveo](https://serveo.net) - Mentioned quite a bit the last couple years, but appears to be down currently. Simply uses SSH for tunneling.


# Reference

* [Roll your own Ngrok with Nginx, Letsencrypt, and SSH reverse tunnelling](https://jerrington.me/posts/2019-01-29-self-hosted-ngrok.html)
* [Poor man's ngrok with tcp proxy and ssh reverse tunnel](https://dev.to/k4ml/poor-man-ngrok-with-tcp-proxy-and-ssh-reverse-tunnel-1fm)
* [How I built Ngrok Alternative (jprq)](https://dev.to/azimjohn/how-i-built-ngrok-alternative-3n0g)
* [Great SO answer by AJ ONeal about how these things work](https://stackoverflow.com/a/52614266/943814)
* [Talk by AJ ONeal about tunneling tech](https://youtu.be/E1Q2MWGCADo)


# Discussions

* [HN comment about needing Namecheap + CloudFlare + ngrok](https://news.ycombinator.com/item?id=24475946).
