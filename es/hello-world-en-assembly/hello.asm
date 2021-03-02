; este programa es un hello world creado en assembly, más específico en 
; x86 asm por Pablo Corbalán para su canal de YouTube. Por favor lee el 
; archivo README.md de esta carpeta para más información, y si vas a 
; copiar el código deja créditos o por lo menos un like en el canal de yt :)

section       .text 

global        _start                    ; tenemos que declararla para ld

_start:
  mov         edx, len                  ; llamamos a la longitud, almacenada en len
  mov         ecx, msg                  ; llamamos al mensaje, almacenado en msg
  mov         ebx, 1                    ; "creamos" (set) el descriptor (stdout)

  mov         eax, 4                    ; llamamos al sistema para escribir
  int         0x80                      ; llamamos al kernel

  mov         eax, 1                    ; llamamos al sistema para salir
  int         0x80                      ; volvemos a llamar al kernel

section       .data                     ; aqui declaramos datos y variables
  msg         db "Hello world", 0xa     ; el mensaje que vamos a imprimir
  len         equ $ -msg                ; la longitud del mensaje

