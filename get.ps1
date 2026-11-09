# Windows bootstrap for Zyvor Pharma QMS (pilot / not Part 11).
#   & ([scriptblock]::Create((irm https://github.com/zyvorai/zyvor-pharma-qms-site/releases/latest/download/get.ps1))) up
$ErrorActionPreference = "Stop"
$Base = if ($env:PHARMA_QMS_RELEASE_BASE) { $env:PHARMA_QMS_RELEASE_BASE } else { "https://github.com/zyvorai/zyvor-pharma-qms-site/releases/latest/download" }
$App = if ($env:PHARMA_QMS_APP_DIR) { $env:PHARMA_QMS_APP_DIR } else { Join-Path $env:USERPROFILE ".zyvor-pharma-qms\app" }
$tmp = Join-Path $env:TEMP ("pharma-qms-" + [guid]::NewGuid().ToString())
New-Item -ItemType Directory -Path $tmp | Out-Null
try {
  Write-Host "Downloading Zyvor Pharma QMS install bundle…"
  Invoke-WebRequest "$Base/pharma-qms-install.tar.gz" -OutFile (Join-Path $tmp "pharma-qms-install.tar.gz")
  Invoke-WebRequest "$Base/SHA256SUMS" -OutFile (Join-Path $tmp "SHA256SUMS")
  $want = (Get-Content (Join-Path $tmp "SHA256SUMS") | Where-Object { $_ -match "pharma-qms-install.tar.gz$" } | ForEach-Object { ($_ -split "\s+")[0] })
  $got = (Get-FileHash (Join-Path $tmp "pharma-qms-install.tar.gz") -Algorithm SHA256).Hash.ToLower()
  if (-not $want -or $want.ToLower() -ne $got) { throw "checksum mismatch: refusing to run" }
  if (Test-Path $App) { Remove-Item -Recurse -Force $App }
  New-Item -ItemType Directory -Force -Path $App | Out-Null
  tar -xzf (Join-Path $tmp "pharma-qms-install.tar.gz") -C $App
  & (Join-Path $App "deploy\install\install.ps1") @args
} finally {
  Remove-Item -Recurse -Force $tmp -ErrorAction SilentlyContinue
}
