%include "io.inc"
section .data
    arr_len equ 5
    arr1 dd 2, 4, 1, 3, 5
    arr2 dd 5, 1, 8, 2, 0
    
    new_line dd "", 0dh, 0ah, 0
section .bss
    result resd 10
section .text
global CMAIN
CMAIN:
    mov ebp, esp; for correct debugging
    
    PRINT_STRING 'Array 1: '
    
    
    lea esi, [arr1]              
    
    
    mov ecx, arr_len
    

     
    
    
    PRINT_STRING new_line
    
    PRINT_STRING "Array 2: "
    lea esi, [arr2]
    mov ecx, arr_len
    call print_array
    
    xor ecx, ecx
    xor edx, edx
    
    call main_loop
    
    
    call print_array
    
    xor eax, eax
    
    PRINT_STRING new_line
    
    PRINT_STRING "Result: "
    lea esi, [result]
    mov ecx, 10
    call print_array
    ret

main_loop:

merdge_arrays    mov eax, [arr1 + ecx * 4]
    mov [result + edx * 4], eax
    inc edx
    mov eax, [arr2 + ecx * 4]
    mov [result + edx * 4], eax
    inc edx
    rdtsc
    xor ebx,ebx                 
    add ebx,eax  
    inc ecx
        rdtsc                       
    sub eax,ebx                 
    PRINT_DEC 4, eax
    cmp ecx, arr_len
    jl merdge_arrays
ret
print_array_digit:
    PRINT_DEC 4, eax
    PRINT_CHAR ' ' 
ret
 
print_array:
loop1 lodsd
    call print_array_digit
loop loop1
ret