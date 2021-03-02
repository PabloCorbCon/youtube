### Video: link
![video-banner](../../img/es/hello-world-en-assembly.png "video banner")
En este pequeño video explico como puedes programar un **Hello world en assembly**, concretamente en la
arquitectura x86 para Linux.

Solo encontrarás un archivo llamado `hello.asm`, con todo el código comentado.

### Como compilar el código
Compilar assembly puede ser complicado, para compilar este programa vamos a usar nasm (el compilador para x86) y
ld (el linker). En tu terminal escribe lo siguiente:
```shell
nasm -f elf32 -o hello.o hello.asm
ld -m i_386 -o hello hello.o
./hello
```
O en una sola linea: 
```shell
nasm -f elf32 -o hello.o hello.asm && ld -m i_386 -o hello hello.o && ./hello
```
###### Este video ha sido dirigido y producido por [Pablo Corbalán](https://gitub.com/pblcc) para su canal de YouTube
