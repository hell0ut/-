%include "io.inc"

section .text
global CMAIN
CMAIN:
    mov ebp, esp; for correct debugging
    rdtsc                       ; get current timestamp (saved in a 64 bit value: EDX [first half], EAX [second half])
    xor ecx,ecx                 ; sets ECX to zero
    add ecx,eax                 ; save timestamp to ECX
    rdtsc                       ; get another timestamp
    sub eax,ecx                 ; compute elapsed ticks
    PRINT_DEC 4, eax
    ret