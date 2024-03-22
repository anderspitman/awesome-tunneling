The purpose of this list is to track and compare tunneling solutions. This is
primarily targeted toward self-hosters and developers who want to do things
like exposing a local webserver via a public domain name, with automatic HTTPS,
even if behind a NAT or other restricted network.

**NOTE:** We're building a community around self-hosting, data ownership, and decentralization in general.
Join us over at [IndieBits.io](https://forum.indiebits.io).

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
of them can do automatic certs through Let's Encrypt, none of them integrate
the domain registration and DNS management.

**UPDATE 2022-09-23:**

A lot of new tools have been developed since the list started, and many tools have been submitted for addition to the list. It's great to see so much interest in tunneling. That said, I want to make sure this remains a useful resource for not just listing all the possible options, but helping people pick one that will solve their problem. With that goal in mind, I've moved some of the items to a separate section at the bottom. This is dedicated to more complicated tools like overlay networks which can support tunneling and similar use cases, but aren't focused exclusively on tunneling. Please let me know if you think something is in the wrong section.

# Recommendations

* For most people, I currently recommend [CloudFlare Tunnel](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/). Although it's closed source, this is the production-quality service that gets the closest to achieving the dream. It's also a loss-leader for CloudFlare's other products which means they can offer it for free.
* If you want to self-host, there are many options. For something production ready [frp](https://github.com/fatedier/frp) is probably what you want. If you're a developer, I'd recommend starting with my own [SirTunnel](https://github.com/anderspitman/SirTunnel) project and modifying it for your needs. For non-developers and those wanting more of a GUI experience, I created [boringproxy](https://boringproxy.io/). It's my take on a comprehensive tunnel proxy solution. It's in beta but currently solves almost everything I want. Once the server is running this is a very easy tool to use and has some nice features.

# Open source (at least with a reasonably permissive license)
* [Telebit](https://telebit.cloud/) - Written in JS. [Code](https://git.coolaj86.com/coolaj86/telebit.js). 
* [tunnel.pyjam.as](https://tunnel.pyjam.as/) - No custom client; uses WireGuard directly instead. Written in Python. [source code](https://gitlab.com/pyjam.as/tunnel)
* [SSH-J.com](https://bitbucket.org/ValdikSS/dropbear-sshj/) -  Public SSH Jump & Port Forwarding server. No software, no registration, just an anonymous SSH server for forwarding. Users are encouraged to use it for SSH exposure only, to preserve end-to-end encryption. No public ports, only in-SSH connectivity. Run `ssh ssh-j.com` and it will display usage information.
* [frp](https://github.com/fatedier/frp) [![frp github stars badge](https://img.shields.io/github/stars/fatedier/frp?style=flat)](https://github.com/fatedier/frp/stargazers) - Comprehensive open alternative to ngrok. Supports UDP, and has a P2P mode. Supports multiplexing over TCP (single connection or pool), QUIC, and KCP.
* [ngrok 1.0](https://github.com/inconshreveable/ngrok) [![ngrok 1.0 github stars badge](https://img.shields.io/github/stars/inconshreveable/ngrok?style=flat)](https://github.com/inconshreveable/ngrok/stargazers) - Original version of ngrok. No longer developed in favor of the commercial 2.0 version.
* [localtunnel](https://github.com/localtunnel) [![localtunnel github stars badge](https://img.shields.io/github/stars/localtunnel/localtunnel?style=flat)](https://github.com/localtunnel/localtunnel/stargazers) - Written in node. Popular suggestion.
* [sshuttle](https://github.com/sshuttle/sshuttle) [![sshuttle github stars badge](https://img.shields.io/github/stars/sshuttle/sshuttle?style=flat)](https://github.com/sshuttle/sshuttle/stargazers) - Open source project originally from one of the founders of Tailscale. Server doesn't require root; client does. Explicitly designed to avoid TCP-over-TCP issues.
* [chisel](https://github.com/jpillora/chisel) [![chisel github stars badge](https://img.shields.io/github/stars/jpillora/chisel?style=flat)](https://github.com/jpillora/chisel/stargazers) - SSH under the hood, but still uses a custom client binary. Supports auto certs from LetsEncrypt. Written in Go.
* [bore](https://github.com/ekzhang/bore) [![bore github stars badge](https://img.shields.io/github/stars/ekzhang/bore?style=flat)](https://github.com/ekzhang/bore/stargazers) - Minimal tunneling solution. MIT Licensed. Written in Rust.
* [rathole](https://github.com/rapiz1/rathole) [![rathole github stars badge](https://img.shields.io/github/stars/rapiz1/rathole?style=flat)](https://github.com/rapiz1/rathole/stargazers) - Similar to frp, including the config format, but with improved performance. Low resource consumption. Hot reload. Written in Rust.
* [expose](https://github.com/beyondcode/expose) [![expose github stars badge](https://img.shields.io/github/stars/beyondcode/expose?style=flat)](https://github.com/beyondcode/expose/stargazers) - ngrok alternative written in PHP.
* [sish](https://github.com/antoniomika/sish) [![sish github stars badge](https://img.shields.io/github/stars/antoniomika/sish?style=flat)](https://github.com/antoniomika/sish/stargazers) - Open source ngrok/serveo alternative. SSH-based but uses a custom server written in Go. Supports WebSocket tunneling.
* [gost](https://latest.gost.run/en/) [![gost github stars badge](https://img.shields.io/github/stars/go-gost/gost?style=flat)](https://github.com/go-gost/gost/stargazers) - Looks like a comprehensive options. TCP and UDP tunneling. TAP/TUN devices. Load balancing. Web API. Written in Go.
* [go-http-tunnel](https://github.com/mmatczuk/go-http-tunnel) [![go-http-tunnel github stars badge](https://img.shields.io/github/stars/mmatczuk/go-http-tunnel?style=flat)](https://github.com/mmatczuk/go-http-tunnel/stargazers) - Uses a single HTTP/2 connection for muxing. Need to manually generate certs for server and clients.
* [pgrok/pgrok](https://github.com/pgrok/pgrok) [![pgrok github stars badge](https://img.shields.io/github/stars/pgrok/pgrok?style=flat)](https://github.com/pgrok/pgrok/stargazers) - A multi-tenant HTTP reverse tunnel solution through SSH remote port forwarding.
* [wstunnel](https://github.com/erebe/wstunnel) [![wstunnel github stars badge](https://img.shields.io/github/stars/erebe/wstunnel?style=flat)](https://github.com/erebe/wstunnel/stargazers) - Proxies over WebSockets. Focus on proxying from behind networks that block certain protocols. Written in Rust with executables provided.
* [tunnelto](https://tunnelto.dev/) [![tunnelto github stars badge](https://img.shields.io/github/stars/agrinman/tunnelto?style=flat)](https://github.com/agrinman/tunnelto/stargazers) - Open source (MIT). Written in Rust.
* [zrok](https://zrok.io/) [![zrok github stars badge](https://img.shields.io/github/stars/openziti/zrok?style=flat)](https://github.com/openziti/zrok/stargazers) - Aims for effortless sharing both publicly and privately. Supports multiple types of resources, including HTTP endpoints and files. Built on OpenZiti (see overlay section below). Apache 2 License. Written in Go.
* [SirTunnel](https://github.com/anderspitman/SirTunnel) [![SirTunnel github stars badge](https://img.shields.io/github/stars/anderspitman/SirTunnel?style=flat)](https://github.com/anderspitman/SirTunnel/stargazers) - Minimal, self-hosted, 0-config alternative to ngrok. Similar to sish but leverages Caddy+OpenSSH rather than custom server code.
* [boringproxy](https://boringproxy.io/) [![boringproxy github stars badge](https://img.shields.io/github/stars/boringproxy/boringproxy?style=flat)](https://github.com/boringproxy/boringproxy/stargazers) - Designed to be very easy to use. No config files. Clients can be remote-controlled through a simple WebUI and/or REST API on the server.
* [jprq](https://github.com/azimjohn/jprq) [![jprq github stars badge](https://img.shields.io/github/stars/azimjohn/jprq?style=flat)](https://github.com/azimjohn/jprq/stargazers) - Proxies over WebSockets. Written in Go.
* [Tunnelmole](https://github.com/robbie-cahill/tunnelmole-client/) [![tunnelmole github stars badge](https://img.shields.io/github/stars/robbie-cahill/tunnelmole-client?style=flat)](https://github.com/robbie-cahill/tunnelmole-client/stargazers) - Open source and optionally self hostable. The client and server are both written in TypeScript.
* [Wiretap](https://github.com/sandialabs/wiretap) [![wiretap github stars badge](https://img.shields.io/github/stars/sandialabs/wiretap?style=flat)](https://github.com/sandialabs/wiretap/stargazers) - Transparent tunneling over WireGuard (UDP) using userspace network stack. Root not required on server. Supports multiple clients and servers. Written in Go.
* [PageKite](https://pagekite.net/) [![pagekite github stars badge](https://img.shields.io/github/stars/pagekite/PyPagekite?style=flat)](https://github.com/pagekite/PyPagekite/stargazers) - Comprehensive open source solution with hosted options.
* [Crowbar](https://github.com/q3k/crowbar) [![crowbar github stars badge](https://img.shields.io/github/stars/q3k/crowbar?style=flat)](https://github.com/q3k/crowbar/stargazers) - Tunnels TCP connections over HTTP GET and POST requests.
* [tunneller](https://github.com/skx/tunneller) [![tunneller github stars badge](https://img.shields.io/github/stars/skx/tunneller?style=flat)](https://github.com/skx/tunneller/stargazers) - Open source. Written in Go.
* [onionpipe](https://github.com/cmars/onionpipe) [![onionpipe github stars badge](https://img.shields.io/github/stars/cmars/onionpipe?style=flat)](https://github.com/cmars/onionpipe/stargazers) - Onion addresses for anything. `onionpipe` forwards ports on the local host to remote Onion addresses as Tor hidden services and vice-versa. Written in Go.
* [tunnel](https://github.com/koding/tunnel) [![tunnel github stars badge](https://img.shields.io/github/stars/koding/tunnel?style=flat)](https://github.com/koding/tunnel/stargazers) - This one is a Golang library, not a program you can just run. However, it looks easy to use for creating custom solutions. Uses a single TCP socket, and [yamux](https://github.com/hashicorp/yamux) for multiplexing.
* [jerson/pgrok](https://www.proxy.jetzt/) [![pgrok github stars badge](https://img.shields.io/github/stars/jerson/pgrok?style=flat)](https://github.com/jerson/pgrok/stargazers) - Fork of ngrok 1.0, with more recent commits. Archived.
* [remotemoe](https://github.com/fasmide/remotemoe) [![remotemoe github stars badge](https://img.shields.io/github/stars/fasmide/remotemoe?style=flat)](https://github.com/fasmide/remotemoe/stargazers) - SSH-based, with custom golang server. Does some cool unique things. Instead of just plain tunnels, it drops you into a basic CLI UI that offers several useful commands interactively, such as adding a custom hostname. Also allows end-to-end encryption for both HTTPS and upstream SSH. Doesn't appear to offer non-e2e HTTPS, ie no auto Let's Encrypt support.
* [docker-tunnel](https://github.com/vitobotta/docker-tunnel) [![docker-tunnel github stars badge](https://img.shields.io/github/stars/vitobotta/docker-tunnel?style=flat)](https://github.com/vitobotta/docker-tunnel/stargazers) - Simple Docker-based nginx+SSH solution.
* [hypertunnel](https://github.com/berstend/hypertunnel) [![frp github stars badge](https://img.shields.io/github/stars/berstend/hypertunnel?style=flat)](https://github.com//berstend/hypertunnel/stargazers) - Public server appears to be down. MIT Licensed. Written in JavaScript.
* [tunwg](https://github.com/ntnj/tunwg) [![tunwg github stars badge](https://img.shields.io/github/stars/ntnj/tunwg?style=flat)](https://github.com/ntnj/tunwg/stargazers) - Wireguard in userspace based. Offers end to end encrypted TLS with LetsEncrypt certificates generated automatically by clients, with support for custom domains. Server can be self-hosted and doesn't require storing any data.
* [gt](https://github.com/ao-space/gt)[![gt github stars badge](https://img.shields.io/github/stars/ao-space/gt?style=flat)](https://github.com/ao-space/gt/stargazers) - Supports peer-to-peer direct connection (P2P) and Internet relay. Focus on performance. Written in Go.
* [holepunch](https://github.com/CypherpunkArmory/holepunch) [![holepunch github stars badge](https://img.shields.io/github/stars/CypherpunkArmory/holepunch?style=flat)](https://github.com/CypherpunkArmory/holepunch/stargazers) - Has nice hosted solution. Uses SSH for muxing.
* [cactus-tunnel](https://github.com/jeffreytse/cactus-tunnel) [![cactus tunnel github stars badge](https://img.shields.io/github/stars/jeffreytse/cactus-tunnel?style=flat)](https://github.com/jeffreytse/cactus-tunnel/stargazers) - 🌵 A charming TCP tunnel over WebSocket and Browser. Written in TypeScript.
* [docker-wireguard-tunnel](https://github.com/DigitallyRefined/docker-wireguard-tunnel) [![ngtor github stars badge](https://img.shields.io/github/stars/DigitallyRefined/docker-wireguard-tunnel?style=flat)](https://github.com/DigitallyRefined/docker-wireguard-tunnel/stargazers) - Connect two or more Docker servers together sharing container ports between them via a WireGuard tunnel.
* [StaqLab Tunnel](https://tunnel.staqlab.com/) [![staqlab github stars badge](https://img.shields.io/github/stars/abhishekq61/tunnel-client?style=flat)](https://github.com/abhishekq61/tunnel-client/stargazers) - SSH-based. Client is open source. Server doesn't appear to be.
* [docker-wireguard-tunnel](https://github.com/DigitallyRefined/docker-wireguard-tunnel) [![ngtor github stars badge](https://img.shields.io/github/stars/DigitallyRefined/docker-wireguard-tunnel?style=flat)](https://github.com/DigitallyRefined/docker-wireguard-tunnel/stargazers) - Connect two or more Docker servers together sharing container ports between them via a WireGuard tunnel.
* [frp-operator](https://github.com/zufardhiyaulhaq/frp-operator) [![frp-operator github stars badge](https://img.shields.io/github/stars/zufardhiyaulhaq/frp-operator?style=flat)](https://github.com/zufardhiyaulhaq/frp-operator/stargazers) - Kubernetes integration for [FRP](https://github.com/fatedier/frp). MIT License. Written in Go.
* [tnnlink](https://github.com/LiljebergXYZ/tnnlink) [![tnnlink github stars badge](https://img.shields.io/github/stars/LiljebergXYZ/tnnlink?style=flat)](https://github.com/LiljebergXYZ/tnnlink/stargazers) - SSH-based. Golang. Not maintained.
* [ngtor](https://github.com/theborakompanioni/ngtor) [![ngtor github stars badge](https://img.shields.io/github/stars/theborakompanioni/ngtor?style=flat)](https://github.com/theborakompanioni/ngtor/stargazers) - Easily expose local services via Tor. Written in Java.
* [Punchmole](https://github.com/Degola/punchmole/) [![punchmole github stars badge](https://img.shields.io/github/stars/Degola/punchmole?style=flat)](https://github.com/Degola/punchmole/stargazers) - Can be integrated directly into an existing Node.js project. Written in JavaScript.
* [ephemeral-hidden-service](https://github.com/aurelg/ephemeral-hidden-service) [![ephemeral-hidden-service github stars badge](https://img.shields.io/github/stars/aurelg/ephemeral-hidden-service?style=flat)](https://github.com/aurelg/ephemeral-hidden-service/stargazers) - Create ephemeral Tor hidden services from the command line. Written in Python.

# Commercial/Closed source

* [ngrok 2.0](https://ngrok.com/) - Probably the gold standard and most popular. Closed source. Lots of features, including TLS and TCP tunnels. Doesn't require root to run client.
* [CloudFlare Tunnel](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup) - Excellent free option. Nicely integrates tunneling with the rest of Cloudflare's products, which include DNS and auto HTTPS. Client [source code](https://github.com/cloudflare/cloudflared) is Apache 2.0 licensed and written in Golang.
* [Livecycle Docker Extension](https://hub.docker.com/extensions/livecycle/docker-extension) - Offer much more than just tunneling. Have a collaboration layer (Dashboard) that allows you to bring collaborations, debug, and gather feedback from the people you are working with. Share HTTPS URLs.
* [Beeceptor](https://beeceptor.com/) - Goes beyond tunneling. Rest API mocking and intercepting tool. You can view the live requests and send mocked response. Written in JavaScript.
* [Pinggy](https://pinggy.io/) - SSH based single command HTTPS / TCP / TLS tunnels, no downloads required. Rich terminal interface and a web debugger. Free tier - 60 min timeout. Paid tier allows custom domains with built-in Let's Encrypt certificates.
* [Loophole](https://loophole.cloud/) - Offers end-to-end TLS encryption with the client automatically getting certs from Let's Encrypt. QR codes for URL sharing. Client is open source. Can serve a local directory over WebDAV. MIT License. Written in Go.
* [localhost.run](https://localhost.run/) - Simple hosted SSH option. Supports custom domains for a cost.
* [Packetriot](https://packetriot.com) - Comprehensive alternative to ngrok.  HTTP Inspector, Let's Encrypt integration, doesn't require root and Linux repos for apt, yum and dnf.  Enterprise licenses and self-hosted option.
* [Horizon Tunnel](https://hrzn.run/) - Easy to use HTTP(S) and websocket tunneling aimed at development. Free tier available. Fixed URL is part of paid plans.
* [Hoppy](https://hoppy.network/) - WireGuard-based. Provides static IPv4 and IPv6 addresses for your machines, which is a simple and useful level of abstraction. Targeted towards self-hosters and people behind NATs.
* [gw.run](https://gw.run/) - Specifically focusing on securely exposing internal web apps to a group of people; not for publicly facing apps. Share access via email address then allow users to log in with common login providers like Google.
* [SSHReach.me](https://sshreach.me/) - Paid SSH-based option. Uses a simple python script.
* [KubeSail](https://kubesail.com/) - Company offering tunneling, dynamic DNS, and other services for self-hosting with Kubernetes.
* [inlets](https://inlets.dev/) - Used to be [open source](https://github.com/inlets/inlets-archived); now focused on a polished commercial offering. Designed to work well with Kubernetes.
* [LocalToNet](https://localtonet.com/) - Supports UDP. Free for a single tunnel. Paid supports custom domains.
* [LocalXpose](https://localxpose.io) - Looks like a solid paid option, with a limited free tier.
* [Tabserve.dev](https://tabserve.dev) - Web UI that runs entirely in the browser and uses a Cloudflare Worker for https.
* [Serveo](https://serveo.net) - SSH-based, signup optional, offering HTTP(S) and TCP tunneling and SSH jump host forwarding capabilities.
* [Homeway](https://homeway.io) - Secure and private remote access for Home Assistant. The free tier has a monthly data limit cap, but unlimited data is only $2.49/month.
* [btunnel](https://www.btunnel.in) - Expose localhost and local tcp server to the internet. Free plan includes file server, custom http request and response headers, basic auth protection and 1 hour tunnel timeout.
* [remote.it](https://www.remote.it/) - Tunnels SSH, HTTP/S, TCP, Docker, popular database etc. allows mapping local port to a remote port.

# Overlay networks and other advanced tools

* [headscale](https://github.com/juanfont/headscale) [![headscale github stars badge](https://img.shields.io/github/stars/juanfont/headscale?style=flat)](https://github.com/juanfont/headscale/stargazers) - Open source implementation of Tailscale control server. Can be used with Tailscale's official open source client. Written in Go.
* [Tailscale](https://www.tailscale.com/) [![tailscale github stars badge](https://img.shields.io/github/stars/tailscale/tailscale?style=flat)](https://github.com/tailscale/tailscale/stargazers) - Built on WireGuard. Easy to use. Control server is closed source. Client [code](https://github.com/tailscale) available with a BSD3 license + separate patents file.
* [Teleport](https://goteleport.com/) [![teleport github stars badge](https://img.shields.io/github/stars/gravitational/teleport?style=flat)](https://github.com/gravitational/teleport) - Comprehensive control plane tool, but also supports [accessing apps](https://goteleport.com/docs/application-access/introduction/) behind NATs. Written in Go.
* [Nebula](https://github.com/slackhq/nebula) - [![nebula github stars badge](https://img.shields.io/github/stars/slackhq/nebula?style=flat)](https://github.com/zerotier/slackhq/nebula) Peer-to-peer overlay network. Developed and used internally by Slack. Similar to Tailscale but completely open source. Doesn't use WireGuard. Written in Go.
* [ZeroTier](https://www.zerotier.com/) - [![zerotier github stars badge](https://img.shields.io/github/stars/zerotier/ZeroTierOne?style=flat)](https://github.com/zerotier/ZeroTierOne/stargazers) Layer 2 overlay network. They take decentralization seriously, and like to say "decentralize until it hurts, then centralize until it works." Written in C++.
* [Netmaker](https://github.com/gravitl/netmaker) [![netmaker github stars badge](https://img.shields.io/github/stars/gravitl/netmaker?style=flat)](https://github.com/gravitl/netmaker/stargazers) - Layer 3 peer-to-peer overlay network and private DNS. Similar to Tailscale, but with a self-hosted server/admin UI. Runs kernel WireGuard so very fast. Not FOSS, but source is available. Written in Go.
* [NetBird](https://github.com/netbirdio/netbird) [![netbird github stars badge](https://img.shields.io/github/stars/netbirdio/netbird?style=flat)](https://github.com/netbirdio/netbird/stargazers) - NetBird is an open-source VPN management platform built on top of WireGuard® making it easy to create secure private networks for your organization or home.
* [Firezone](https://www.firezone.dev/) [![firezone github stars badge](https://img.shields.io/github/stars/firezone/firezone?style=flat)](https://github.com/firezone/firezone) - Layer 3/4 overlay network. Runs on kernel WireGuard® and supports SSO using generic OIDC/SAML connectors. Distributed under apache 2.0 license and written in Elixir/Rust.
* [innernet](https://github.com/tonarino/innernet) [![innernet github stars badge](https://img.shields.io/github/stars/tonarino/innernet?style=flat)](https://github.com/tonarino/innernet/stargazers) - Similar to Netmaker, nebula, and Tailscale. Takes advantage of existing networking concepts like CIDRs and the security properties of WireGuard to turn your computer's basic IP networking into more powerful ACL primitives. Written in Rust.
* [Pritunl](https://pritunl.com/) [![pritunl github stars badge](https://img.shields.io/github/stars/pritunl/pritunl?style=flat)](https://github.com/pritunl/pritunl/stargazers) - Seems quite comprehensive and complicated. OpenVPN, WireGuard, and IPSec support.
* [Tinc](https://github.com/gsliepen/tinc) [![tinc github stars badge](https://img.shields.io/github/stars/gsliepen/tinc?style=flat)](https://github.com/gsliepen/tinc/stargazers) - Tinc is a peer-to-peer VPN daemon that supports VPNs with an arbitrary number of nodes. Instead of configuring tunnels, you give tinc the location and public key of a few nodes in the VPN. After making the initial connections to those nodes, tinc will learn about all other nodes on the VPN, and will make connections automatically. When direct connections are not possible, data will be forwarded by intermediate nodes. Written in C.
* [OpenZiti](https://openziti.github.io) - [![OpenZiti github stars badge](https://img.shields.io/github/stars/openziti/ziti?style=flat)](https://github.com/openziti/ziti/stargazers) - Overlay network. The goal of OpenZiti is to extend zero trust all the way into your application, not just to your network. Apache 2.0 license. Written in Go.
* [Ngrok-operator](https://github.com/zufardhiyaulhaq/ngrok-operator) [![ngrok operator github stars badge](https://img.shields.io/github/stars/zufardhiyaulhaq/ngrok-operator?style=flat)](https://github.com/zufardhiyaulhaq/ngrok-operator/stargazers) - Ngrok but integrated with Kubernetes, allows developers on private kubernetes to easily access their services via Ngrok.
* [chisel-operator](https://github.com/FyraLabs/chisel-operator/) [![chisel operator github stars badge](https://img.shields.io/github/stars/FyraLabs/chisel-operator?style=flat)](https://github.com/FyraLabs/chisel-operator/stargazers) - Kubernetes integration for Chisel. Similar functionality to inlets. MIT License. Written in Rust.


# Reference

* [Roll your own Ngrok with Nginx, Letsencrypt, and SSH reverse tunnelling](https://jerrington.me/posts/2019-01-29-self-hosted-ngrok.html)
* [Poor man's ngrok with tcp proxy and ssh reverse tunnel](https://dev.to/k4ml/poor-man-ngrok-with-tcp-proxy-and-ssh-reverse-tunnel-1fm)
* [How I built Ngrok Alternative (jprq)](https://dev.to/azimjohn/how-i-built-ngrok-alternative-3n0g)
* [Great SO answer by AJ ONeal about how these things work](https://stackoverflow.com/a/52614266/943814)
* [Talk by AJ ONeal about tunneling tech](https://youtu.be/E1Q2MWGCADo)
* [ngrok alternative: localtunnel + Caddy + Lets Encrypt](https://morph027.gitlab.io/blog/localtunnel-ngrok/)


# Discussions

* [HN comment about needing Namecheap + CloudFlare + ngrok](https://news.ycombinator.com/item?id=24475946).
