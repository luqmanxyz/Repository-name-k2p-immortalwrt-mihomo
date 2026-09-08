# K2P ImmortalWrt 24.10.4 + sing-box auto URLTest

This builder keeps only:
- TUN inbound
- HTTP outbound with TLS
- direct/block outbound
- selector + urltest outbound groups

It intentionally omits heavy proxy protocols, remote rule sets, Clash API,
and subscription secrets.

The generated router config is separate:
`k2p-singbox-ipv4-auto-urltest.json`

Recommended runtime design:
- IPv6 disabled on router/LAN
- TCP -> URLTest group
- UDP -> direct
- private IP -> direct
- DNS -> upstream gateway 192.168.1.1
- proxy sockets bound to WAN

Selected concrete nodes in the generated config: 14

Do not commit your subscription or config with credentials to a public repo.
