## Usage

```
cd bundle
sh \(re\)load_bundle.sh
sh script.sh
```

## EXP2

Compare `rust-perf-100000-4k_nowarmup.svg` and `rust-perf-100000-512k_nowarmup` (both for anonymous). Time consumption increased because the lowest level syscalls are getting slower.

## EXP1
Compare `rust-perf-shared-25000-4k.svg` and `rust-perf-shared-10000-4k.svg` (both for shared). FindAvilableLoced (findHighestAvailableLocked) is getting slower with increasing iterations.
