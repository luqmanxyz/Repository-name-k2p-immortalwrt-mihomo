#!/usr/bin/env python3
from pathlib import Path
import sys

p = Path(sys.argv[1])
s = p.read_text()

# Ultra-small registry for this K2P use case:
# inbound: tun
# outbound: direct, block, http
drop_imports = [
    "protocol/anytls",
    "protocol/dns",
    "protocol/hysteria",
    "protocol/hysteria2",
    "protocol/mixed",
    "protocol/naive",
    "protocol/redirect",
    "protocol/shadowsocks",
    "protocol/shadowtls",
    "protocol/socks",
    "protocol/ssh",
    "protocol/tor",
    "protocol/trojan",
    "protocol/tuic",
    "protocol/vless",
    "protocol/vmess",
    "protocol/wireguard",
]

lines = s.splitlines()
lines = [line for line in lines if not any(x in line for x in drop_imports)]
s = "\n".join(lines) + "\n"

drop_calls = [
    "redirect.RegisterRedirect(registry)",
    "redirect.RegisterTProxy(registry)",
    "direct.RegisterInbound(registry)",
    "socks.RegisterInbound(registry)",
    "http.RegisterInbound(registry)",
    "mixed.RegisterInbound(registry)",
    "shadowsocks.RegisterInbound(registry)",
    "vmess.RegisterInbound(registry)",
    "trojan.RegisterInbound(registry)",
    "naive.RegisterInbound(registry)",
    "shadowtls.RegisterInbound(registry)",
    "vless.RegisterInbound(registry)",
    "anytls.RegisterInbound(registry)",
    "hysteria.RegisterInbound(registry)",
    "tuic.RegisterInbound(registry)",
    "hysteria2.RegisterInbound(registry)",
    "protocolDNS.RegisterOutbound(registry)",
    "socks.RegisterOutbound(registry)",
    "shadowsocks.RegisterOutbound(registry)",
    "vmess.RegisterOutbound(registry)",
    "trojan.RegisterOutbound(registry)",
    "tor.RegisterOutbound(registry)",
    "ssh.RegisterOutbound(registry)",
    "shadowtls.RegisterOutbound(registry)",
    "vless.RegisterOutbound(registry)",
    "anytls.RegisterOutbound(registry)",
    "hysteria.RegisterOutbound(registry)",
    "tuic.RegisterOutbound(registry)",
    "hysteria2.RegisterOutbound(registry)",
    "wireguard.RegisterOutbound(registry)",
    "naive.RegisterOutbound(registry)",
    "group.RegisterSelector(registry)",
    "group.RegisterURLTest(registry)",
]
lines = s.splitlines()
lines = [line for line in lines if not any(call in line for call in drop_calls)]
s = "\n".join(lines) + "\n"

# group import is unused after selector/urltest removal.
s = "\n".join(line for line in s.splitlines() if "protocol/group" not in line) + "\n"

p.write_text(s)
