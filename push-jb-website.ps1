# Push JB Software Solutions site → GitHub Pages (jbsoftwaresolutions.com)
# Same SEO gate as Easy Peeze / Kharch Log: seo-build → llms → then push.
param(
    [string]$Message = "Update JB Software Solutions site (SEO refresh)",
    [switch]$SkipPagesBuild,
    [switch]$NoPush
)
$ErrorActionPreference = "Stop"
$Root = $PSScriptRoot

Write-Host "=== JB Software Solutions push ===" -ForegroundColor Cyan

if (-not $SkipPagesBuild -and (Test-Path (Join-Path $Root "_build_pages.py"))) {
    Write-Host "Regenerating HTML pages from _build_pages.py..."
    py -3 (Join-Path $Root "_build_pages.py")
    if ($LASTEXITCODE -ne 0) { throw "_build_pages.py failed" }
}

Write-Host "Running SEO build (meta + schema + sitemap + robots)..."
Push-Location $Root
try {
    node (Join-Path $Root "seo-build.js")
    if ($LASTEXITCODE -ne 0) { throw "seo-build.js failed" }
} finally {
    Pop-Location
}

Write-Host "Generating llms.txt / llms-full.txt / LLM.txt..."
py -3 (Join-Path $Root "generate-llms-txt.py")
if ($LASTEXITCODE -ne 0) {
    Write-Warning "llms.txt generation failed - continuing with existing files if any"
}

# Ensure crawl aliases exist even if an older seo-build ran
$sm = Join-Path $Root "sitemap.xml"
$rb = Join-Path $Root "robots.txt"
$ll = Join-Path $Root "llms.txt"
if (Test-Path $sm) { Copy-Item -Force $sm (Join-Path $Root "sitemaps.xml") }
if (Test-Path $rb) { Copy-Item -Force $rb (Join-Path $Root "robot.txt") }
if (Test-Path $ll) { Copy-Item -Force $ll (Join-Path $Root "LLM.txt") }

if ($NoPush) {
    Write-Host "SEO artifacts updated. Skipping git push (-NoPush)."
    return
}

Push-Location $Root
try {
    if (-not (Test-Path (Join-Path $Root ".git"))) {
        throw "Not a git repo: $Root"
    }
    git add -A
    $status = git status --porcelain
    if (-not $status) {
        Write-Host "No JB site changes to push."
        return
    }
    git -c user.name="Ahmedhussainpvtt" -c user.email="ahmedhussainpvtt@users.noreply.github.com" commit -m $Message
    git push origin HEAD:main
    Write-Host "Pushed jbsoftwaresolutions.com site." -ForegroundColor Green
} finally {
    Pop-Location
}
