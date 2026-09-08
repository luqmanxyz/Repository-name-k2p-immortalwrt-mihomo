#!/usr/bin/env python3
import sys
from pathlib import Path

p = Path(sys.argv[1])
s = p.read_text()

# K2P minimal target:
# inbound: tun
# outbound: direct, block, http, selector, urltest
# Keep protocol/group because selector/urltest live there.
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
lines = [ln for ln in lines if not any(x in ln for x in drop_imports)]
s = "\n".join(lines) + "\n"

drop_calls = [
    # inbound: only tun
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

    # outbound: keep direct/block/http + selector/urltest
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
]
lines = s.splitlines()
lines = [ln for ln in lines if not any(call in ln for call in drop_calls)]
p.write_text("\n".join(lines) + "\n")
