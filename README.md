# K2P ImmortalWrt 24.10.4 + HTTP/TLS sing-box builder

This repository builds a Phicomm K2P (`ramips/mt7621`, `phicomm_k2p`)
ImmortalWrt 24.10.4 sysupgrade image using the official ImageBuilder.

It injects a custom, stripped Linux/mipsle sing-box 1.12.25 binary with only:
- TUN inbound
- HTTP outbound (TLS remains available)
- direct outbound
- block outbound

The firmware also includes:
- kmod-tun
- kmod-inet-diag
- kmod-netlink-diag
- ca-bundle

## Important

The subscription/config is intentionally NOT embedded in this repository or
firmware. Do not publish subscription tokens in a public GitHub repository.

After flashing, upload a compatible config to:

    /etc/sing-box/config.json

Then validate:

    /usr/bin/sing-box version
    /usr/bin/sing-box check -c /etc/sing-box/config.json
    ls -l /dev/net/tun

Only after `check` succeeds:

    /etc/init.d/sing-box enable
    /etc/init.d/sing-box start

## Build with GitHub Actions

1. Create a GitHub repository.
2. Upload all files/folders from this bundle, preserving `.github/workflows/`.
3. Open **Actions**.
4. Select **Build K2P ImmortalWrt 24.10.4 + sing-box**.
5. Click **Run workflow**.
6. When the job finishes, download the artifact
   `k2p-immortalwrt-24.10.4-singbox`.

The workflow performs an explicit size check against `0xF60000` (the K2P
firmware partition). If the image is too large, the job fails instead of
publishing it.

## Flashing

Use the generated `*phicomm_k2p*squashfs-sysupgrade.bin`.
For a major/custom image change, backing up settings and flashing without
keeping old configuration is safer.

Do not flash an image if the workflow failed its size check.
