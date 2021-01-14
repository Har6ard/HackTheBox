$enc = [system.Text.Encoding]::UTF8
$attackstring = "Obfuscated bxor to base64 string"
$attackbytes = $enc.GetBytes($attackstring)
$xored = $attackbytes | % { [char] ($_ -bxor 0x33)}
$base64 = [System.Convert]::ToBase64String($xored)
Write-Output $base64
$message = "Switching to decoding"
Write-Output $message
$bytes = [convert]::FromBase64String($base64)
$string = -join ($bytes | % { [char] ($_ -bxor 0x33)})
Write-Output $string
