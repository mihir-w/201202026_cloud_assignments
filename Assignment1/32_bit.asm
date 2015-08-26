section .data
a1: dd 4
b1: dd 6
c1: dd 0

section .text

global _start       

_start:
    mov ecx, [a1]
    mov edx, [b1]

    add edx, ecx
    
    pop edx
    mov [c1], edx    

    mov eax, 1
    mov ebx, 0
    int 80h
