param(
    [switch]$WaitPhoneVerification,
    [switch]$ResumeAfterPhone,
    [switch]$AcceptTerms,
    [string]$Prefix = ""
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
Set-Location $Root

$argsList = @()
if ($WaitPhoneVerification) { $argsList += "--wait-phone-verification" }
if ($ResumeAfterPhone) { $argsList += "--resume-after-phone" }
if ($AcceptTerms) { $argsList += "--accept-terms" }
if ($Prefix) {
    $argsList += "--prefix"
    $argsList += $Prefix
}

python .\gmail_register_local.py @argsList
