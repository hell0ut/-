%include "io.inc"
A EQU 14.312
B EQU -39
section .text
global CMAIN
CMAIN:
    mov ebp, esp; for correct debugging
    ;write your code here
    MOV AX, A
    MOV BL, B
    IDIV BL ; A/B
    MOV CH, AL  
    MOV AL, AH
    MUL AH ;(A%A)^2
    MOV BH, 3
    DIV BH ; (A%A)^2/3
    MOV CL, AL
    MOV AL, A
    MOV BL, 39
    MUL BL
    ADD CH, CL
    ADD AL, CH
    SHL AX, 2
    xor eax, eax
    ret