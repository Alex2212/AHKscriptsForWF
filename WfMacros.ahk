
#maxThreadsPerHotkey, 2
setKeyDelay, 50, 50
setMouseDelay, 50

toggle := 0

F11::
    toggle := !toggle
    if (toggle){
        SetTimer, Key4, 19000
        ; SetTimer, key2, 15000
        Gosub, Key4
        ; Gosub, key2
    } else {
        SetTimer, Key4, Off
        ; SetTimer, key2, Off
    }
return

$~lbutton::
    while (getKeyState("lbutton", "P"))
    { 
        Gosub, nataruk

    }
return
; skill slot keys
Key4:
    Send 4
return

key3:
    Send 3
return

key2:
    Send 2
return

key1:
    Send 1
return

; firemode slots
nataruk:
    sleep, 200
    Send, {LButton Down}
    Sleep, 1550
    Send, {LButton Up}
return

fullAuto:
    Send {LButton}
return

$*End::
    Suspend, permit
    if (A_IsSuspended = "0")
    { 
        SoundPlay, C:\Users\Alex\Desktop\Warframe\deactivated.wav
        TrayTip, Suspended, %A_ScriptName%, , 1
    }
    Else
    {
        TrayTip, UnSuspended, %A_ScriptName%, , 1
        SoundPlay, C:\Users\Alex\Desktop\Warframe\activated.wav
    }
    Suspend, Toggle
return