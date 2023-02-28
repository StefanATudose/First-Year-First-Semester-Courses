.data
	chardelim: .asciz " "
	sirfixe: .space 1000
	formatScanF: .asciz "%[^\n]s"
	n: .space 4
	m: .space 4
	formatPrintVar: .asciz "%d "
	formattestvar: .asciz "%d %d fix\n"
	formattestvar2: .asciz "%d %d nufix\n"
	formatPrintnewline: .asciz "\n"
	indicator: .long 0
	unu: .long 0
	nrap: .space 1000
	sol: .space 1000
	fixe: .space 1000
	numar: .space 5
	rusinica: .asciz "-1"
	l: .long 0
	k: .space 5
	zece: .byte 10
.text

.global main

atoibun:
	push %ebp
	movl %esp, %ebp
	
	xor %ecx, %ecx
	movl 8(%ebp), %edx
	movb 1(%edx), %bl
	cmp $0, %bl
	je olit
	jmp doilit
	
olit:
	xor %eax, %eax
	movb (%edx), %al
	subb $48, %al
	popl %ebp
	ret
	
doilit:
	subb $48, %bl
	xor %eax, %eax
	movb (%edx), %al
	subb $48, %al
	mulb zece
	addb %bl, %al
	popl %ebp
	ret

afisare:
	pushl %ebp
	movl %esp, %ebp
	pushl %eax
	pushl %ecx
	
	movl 8(%ebp), %esi		;// de data asta sol[] e in esi
	movl 12(%ebp), %eax
	movl $3, %ebx
	mull %ebx
	movl $0, %ecx

forafis:
	cmp %eax, %ecx
	je continuareafis
	
	movl (%esi, %ecx, 4), %ebx
	movl %ebx, numar
	
	pushl %eax
	pushl %ecx
	pushl %edx
	
	pushl numar
	pushl $formatPrintVar
	call printf
	popl %ebx
	popl %ebx
	
	pushl $0
	call fflush
	popl %ebx
	
	popl %edx
	popl %ecx
	popl %eax
	
	incl %ecx
	jmp forafis
	
		
continuareafis:	
	popl %ecx
	popl %eax
	popl %ebp
	ret

OK:
	pushl %ebp
	movl %esp, %ebp
	movl $0, l
	
	pushl %ecx
	pushl %ebx
	xor %ecx, %ecx
	movl 16(%ebp), %edx
	mov 20(%ebp), %esi
	movl 8(%ebp), %ecx   ;// i curent
	movl (%edx, %ecx, 4), %ebx	;// sol[i]
	subl $1, %ecx
	
for1ok:
	cmp $-1, %ecx
	je cont1ok
	cmp (%edx, %ecx, 4), %ebx
	je cont1ok
	incl l
	
	
	subl $1, %ecx
	jmp for1ok
	
cont1ok:	
	xor %ecx, %ecx
	movl 24(%ebp), %eax
	cmp l, %eax
	jg verifoksupl

cont2ok:
	xor %ecx, %ecx
	movl 12(%ebp), %eax
	incl %eax
	incl %ecx
	movl $3, %ebx
	jmp for2ok


for2ok:
	cmp %eax, %ecx
	je okadv
	
	
	
	cmp (%esi, %ecx, 4), %ebx
	jl okfals
	
	incl %ecx
	jmp for2ok


okadv:
	mov $1, %eax
	popl %ebx
	popl %ecx
	popl %ebp
	ret

okfals:
	mov $0, %eax
	popl %ebx
	popl %ecx
	popl %ebp
	ret

verifoksupl:
	movl (%esi, %ebx, 4), %eax
	cmp $1, %eax
	jne okfals
	jmp cont2ok

backu:
	pushl %ebp
	movl %esp, %ebp
	xor %ecx, %ecx
	movl 20(%ebp), %edi
	movl 24(%ebp), %edx
	movl 28(%ebp), %esi
	movl 32(%ebp), %ebx
	movl %ebx, indicator
	movl 8(%ebp), %ebx
	movl %ebx, unu
	movl 12(%ebp), %ebx
	movl %ebx, n
	movl 16(%ebp), %ebx
	movl %ebx, m
	movl 8(%ebp), %eax   ;//i curent
	movl (%edi, %eax, 4), %ebx	;// fixe[i] curent
	cmp $0, %ebx
	je nu_fix
	jmp fixul
	

nu_fix:
	movl $1, %ecx
	movl n, %ebx
	incl %ebx
	
fornufix:				
	cmp %ebx, %ecx
	je gatabackunufix
	
	

	movl %ecx, (%edx, %eax, 4)
	addl $1, (%esi, %ecx, 4)
	
	pushl %ecx
	pushl %ebx
	pushl %eax
	
	;//cadru apel OK
	pushl m
	pushl %esi
	pushl %edx
	pushl n
	push %eax
	call OK
	popl %ebx
	popl %ebx
	popl %ebx
	popl %ebx
	popl %ebx
	
	cmp $1, %eax
	je nufixok
	popl %eax			;//luam eax la loc (i)(caz nuiok)
	
	
	
contfornufix:
	popl %ebx
	popl %ecx
	subl $1, (%esi, %ecx, 4)
	incl %ecx
	jmp fornufix

nufixok:
	popl %eax			;//luam eax la loc  (i)(cazok)
	xor %ecx, %ecx
	movl 12(%ebp), %ecx
	addl %ecx, %ecx
	addl 12(%ebp), %ecx
	subl $1, %ecx
	
	cmp %eax, %ecx
	je solutie
	jmp apelbackutertiar

gatabackunufix:
	popl %ebp
	ret

fixul:
	movl %ebx, (%edx, %eax, 4)
	addl $1, (%esi, %ebx, 4)
	pushl %eax			;// pastram eax pentru dupa ret ok
	pushl %ebx            		;//pastram ebx pentru dupa popuri
	
	;// cadru apel OK
	pushl m
	pushl %esi
	pushl %edx
	pushl n
	push %eax
	call OK
	popl %ebx
	popl %ebx
	popl %ebx
	popl %ebx
	popl %ebx
	
	popl %ebx    			;//luam ebx la loc (fixe[i])
	cmp $1, %eax
	je fixok
	popl %eax			;// luam eax la loc (i)(caz nuok)
	
cont1backu:
	subl $1, (%esi, %ebx, 4)
	popl %ebp
	ret

fixok:
	popl %eax			;//luam eax la loc  (i)(cazok)
	xor %ecx, %ecx
	movl 12(%ebp), %ecx
	addl %ecx, %ecx
	addl 12(%ebp), %ecx
	subl $1, %ecx
	
	cmp %eax, %ecx
	je solutie
	jmp apelbackusecundar
	
solutie:

	pushl n
	pushl %edx
	call afisare
	popl %ebx
	popl %ebx

	movl $1, indicator
	
	jmp end



main:
	;//citire
	push $sirfixe
	push $formatScanF
	call scanf
	popl %ebx
	popl %ebx
	
	
	;// parsare n si m
	
	pushl $chardelim
	pushl $sirfixe
	call strtok
	popl %ebx
	popl %ebx
	
	movl %eax, n
	
	pushl n
	call atoibun
	popl %ebx
	movl %eax, n

	pushl $chardelim
	pushl $0
	call strtok
	popl %ebx
	popl %ebx	
	
	movl %eax, m
	
	pushl m
	call atoibun
	popl %ebx
	movl %eax, m
	
	;//parsare sir de elemente fixe
	xor %ecx, %ecx
	movl $fixe, %edi
	
for_citirefixe:
	pushl %ecx
	
	pushl $chardelim
	pushl $0
	call strtok
	popl %ebx
	popl %ebx
	
	cmp $0, %eax
	je preludiuapelbacku
	
	movl %eax, numar
	pushl numar
	call atoibun
	popl %ebx
	
	popl %ecx
	movl %eax, (%edi, %ecx, 4)
	incl %ecx
	
	jmp for_citirefixe
	
	
preludiuapelbacku:
	movl $sol, %edx
	movl $nrap, %esi
	
apelbackuoriginal:
	
	
	push indicator
	pushl %esi
	pushl %edx
	pushl %edi
	push m
	push n
	push unu
	call backu
	pop %ebx
	pop %ebx
	pop %ebx
	popl %ebx
	popl %ebx
	popl %ebx
	pop %ebx
	jmp end

apelbackusecundar:
	
	push indicator
	pushl %esi
	pushl %edx
	pushl %edi
	push m
	push n
	incl unu
	push unu
	call backu
	pop %ebx
	pop %ebx
	pop %ebx
	popl %ebx
	popl %ebx
	popl %ebx
	pop %ebx
	
	subl $1, unu
	movl 8(%ebp), %eax   ;//i curent
	movl (%edi, %eax, 4), %ebx
	
	jmp cont1backu
	
apelbackutertiar:
	
	push indicator
	pushl %esi
	pushl %edx
	pushl %edi
	push m
	push n
	incl unu
	push unu
	call backu
	pop %ebx
	pop %ebx
	pop %ebx
	popl %ebx
	popl %ebx
	popl %ebx
	pop %ebx
	
	subl $1, unu
	movl 8(%ebp), %eax   ;//i curent
	jmp contfornufix


afisrusine:
	pushl $rusinica
	call printf
	popl %ebx
	jmp endend


	
end:
	movl indicator, %eax
	cmp $0, %eax
	je afisrusine
	
endend:
	pushl $formatPrintnewline
	call printf
	popl %ebx
	mov $1, %eax
	xor %ebx, %ebx
	int $0x80
	
	
	
	
