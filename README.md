The purpose of this list is to track and compare tunneling solutions. This is
primarily targeting toward developers and self-hosters who want to do things
like exposing a local webserver via a public address.


# Things to look out for when comparing solutions

* Underlying multiplexing technology. In particular, if a solution uses
  TCP-over-TCP (ie any of them that are built on SSH), it'll be subject to
  rather severe [issues](http://sites.inka.de/bigred/devel/tcp-tcp.html).
* Source code availability. Some of the best options are closed source only.
* Does it require root to run the client? For example, anything built on
  WireGuard will likely have great performance (on systems where it's built
  into the kernel at least), but typically requires elevated permissions to
  create the tun devices.


# The tools

* [ngrok 2.0](https://ngrok.com/) - Probably the gold standard and most popular. Closed source. Lots of features, including TLS and TCP tunnels. Doesn't require root to run client.
* [localtunnel](https://github.com/localtunnel) - Written in node. Popular suggestion.
* [PageKite](https://pagekite.net/) - Comprehensive open source solution with hosted options. 
* [ngrok 1.0](https://github.com/inconshreveable/ngrok) - Original version of ngrok. No longer developed in favor of the commercial 2.0 version.
* [frp](https://github.com/fatedier/frp) - Seems to be a pretty comprehensive open alternative to ngrok.
* [holepunch.io](https://holepunch.io) - Has nice hosted solution. Uses SSH for muxing. ([code](https://github.com/CypherpunkArmory/punch/)).
* [CloudFlare Argo Tunnel](https://www.cloudflare.com/products/argo-tunnel/) - $5/mo + $0.1/GB. Integrates with Argo smart routing. Client source code is [available](https://github.com/cloudflare/cloudflared).
* [Telebit](https://telebit.cloud/) - Written in JS. [Open source](https://git.coolaj86.com/coolaj86/telebit.js).
* [slt](https://github.com/inconshreveable/slt) - Open source TLS proxy from the creator of ngrok. Supports SNI.
* [serveo](https://serveo.net) - Mentioned quite a bit the last couple years, but appears to be down currently. Simply uses SSH for tunneling.
* [Tailscale](https://www.tailscale.com/) - Built on WireGuard. Closed source. Easy to use. Doesn't include an HTTPS proxy on the public side, but could be combined with nginx/Caddy/etc.
* [sshuttle](https://github.com/sshuttle/sshuttle) - Open source project originally from one of the founders of Tailscale. Server doesn't require root; client does. Explicitly designed to avoid TCP-over-TCP issues.
* [expose](https://github.com/beyondcode/expose) - ngrok alternative written in PHP.
* [chisel](https://github.com/jpillora/chisel) - Another HTTPS+SSH option.
* [tunneller](https://github.com/skx/tunneller) - Open source. Written in Go.


# Discussions of different solutions and tradeoffs

* [HN comment about needing Namecheap + CloudFlare + ngrok](https://news.ycombinator.com/item?id=24475946).
