; Refernce code to compare results

BITS 64

section .data
a1: dd 4
b1: dd 6
c1: dd 0

section .text

global _start

_start:
    mov rcx, [a1]
    mov rdx, [b1]

    add rdx, rcx
    
    pop rdx
    mov [c1], rdx
    
    mov rax, 60
    mov rdi, 0
    syscall
