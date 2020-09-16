The purpose of this list is to track and compare tunneling solutions. This is
primarily targeting toward developers who want to do things like exposing a
local webserver via a public address.


# Tools

* [ngrok 2.0](https://ngrok.com/) - Probably the gold standard and most popular. Closed source. Lots of features, including TLS and TCP tunnels.
* [localtunnel](https://github.com/localtunnel) - Written in node. Popular suggestion.
* [ngrok 1.0](https://github.com/inconshreveable/ngrok) - Original version of ngrok. No longer developed in favor of the commercial version.
* [frp](https://github.com/fatedier/frp) - Seems to be a pretty comprehensive open alternative to ngrok.
* [holepunch.io](https://holepunch.io) - Has nice hosted solution. Uses SSH for muxing. ([code](https://github.com/CypherpunkArmory/punch/)).
* [CloudFlare Argo Tunnel](https://www.cloudflare.com/products/argo-tunnel/) - $5/mo + $0.1/GB. Integrates with Argo smart routing. Client source code is [available](https://github.com/cloudflare/cloudflared).
* [Telebit](https://telebit.cloud/) - Written in JS. [Open source](https://git.coolaj86.com/coolaj86/telebit.js).
* [slt](https://github.com/inconshreveable/slt) - TLS proxy from the same person who made ngrok. Supports SNI.
* [serveo](https://serveo.net) - Mentioned quite a bit the last couple years, but appears to be down currently. Simply uses SSH for tunneling.


# Discussions of different solutions and tradeoffs

* [HN comment about needing Namecheap + CloudFlare + ngrok](https://news.ycombinator.com/item?id=24475946).
