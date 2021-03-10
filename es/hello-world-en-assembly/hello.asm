; este programa es un hello world creado en assembly, más específico en 
; x86 asm por Pablo Corbalán para su canal de YouTube. Por favor lee el 
; archivo README.md de esta carpeta para más información, y si vas a 
; copiar el código deja créditos o por lo menos un like en el canal de yt :)
section        .text                   ; declare the .text section
global         _start                  ; has to be declared for the linker (ld)
_start:                                ; entry point for _start
    mov edx, len                       ; "invoke" the len of the message
    mov ecx, msg                       ; "invoke" the message itself

    mov ebx, 1                         ; set the file descriptor (fd) to stdout

    mov eax, 4                         ; system call for "write"   
    int 0x80                           ; call the kernel

    mov eax, 1                         ; system call for "exit"
    int 0x80                           ; call the kernel

section        .data                   ; here you declare the data
    msg        db "Hello world!"       ; the actual message to use
    len        equ $ -msg              ; get the size of the message
