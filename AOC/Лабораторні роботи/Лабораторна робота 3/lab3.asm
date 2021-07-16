%include "io.inc"
section .data
A: DD 13.432
B: DD 18.12

section .text
global CMAIN
CMAIN:
    mov ebp, esp; for correct debugging
    ;write your code here
    FINIT
    FLD DWORD [A]
    FLD DWORD [B]
    FADD
    FLD DWORD [A]
    FLD DWORD [B]
    FMUL
    FLD DWORD [A]
    FLD DWORD [B]
    FDIV
    xor eax, eax
    ret